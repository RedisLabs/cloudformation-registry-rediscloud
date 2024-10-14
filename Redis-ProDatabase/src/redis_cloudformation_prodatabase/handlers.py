import logging
import urllib3
import json
import time
from typing import Any, MutableMapping, Optional
from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
)

from .models import ResourceHandlerRequest, ResourceModel, TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Redis::CloudFormation::ProDatabase"

resource = Resource(TYPE_NAME, ResourceModel, TypeConfigurationModel)
test_entrypoint = resource.test_entrypoint

LOG.setLevel("INFO")

def HttpRequests(method, url, headers, body = None):
    response = urllib3.request(method = method, url = url, body = body, headers = headers)
    response = response.json()
    return response

#Makes the POST API call for Database    
def PostDatabase (base_url, event, subscription_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases"
    
    response = HttpRequests(method = "POST", url = url, body = event, headers = http_headers)
    LOG.info(f"The POST call response is: {response}")
    return response

#Returns the status of the Database: active/pending/deleting
def GetDatabaseStatus (base_url, subscription_id, database_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases/" + str(database_id)
    
    response = HttpRequests(method = "GET", url = url, headers = http_headers)
    LOG.info(f'Database status is: {response["status"]}')
    return response["status"]

#Returns the ID and the Description of the Database    
def GetDatabaseId (href_value, http_headers):
    response = HttpRequests(method = "GET", url = href_value, headers = http_headers)
    count = 0
    
    while "databaseId" not in str(response) and count < 50:
        time.sleep(1)
        count += 1
        response = HttpRequests(method = "GET", url = href_value, headers = http_headers)

    db_id = response["databaseId"]
    LOG.info(f"Database with ID {db_id} has the response for the GET call: {response}")
    return db_id

#Makes the Update API call
def PutDatabase (base_url, subscription_id, database_id, event, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases/" + str(database_id)
    
    response = HttpRequests(method = "PUT", url = url, body = event, headers = http_headers)
    LOG.info(f"The PUT call response is: {response}")
    return response

#Makes the Delete API call    
def DeleteDatabase (base_url, subscription_id, database_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases/" + str(database_id)
    
    response = HttpRequests(method = "DELETE", url = url, headers = http_headers)
    LOG.info("Database was deleted with response:" + str(response))

@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    typeConfiguration = request.typeConfiguration
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    http_headers = {"accept":"application/json", "x-api-key":typeConfiguration.RedisAccess.xapikey, "x-api-secret-key":typeConfiguration.RedisAccess.xapisecretkey, "Content-Type":"application/json"}
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID

    #Check if we're retrying (if db_id and db_status are in callback_context)
    if "db_id" in callback_context and "db_status" in callback_context:
        db_id = callback_context["db_id"]
        db_status = callback_context["db_status"]

        # If the database status is complete return success
        if db_status == "active":
            return ProgressEvent(
                status=OperationStatus.SUCCESS,
                resourceModel=model
            )
        elif db_status in ["failed", "error"]:
            return ProgressEvent.failed(
                HandlerErrorCode.InternalFailure,
                f"Database creation failed with status: {db_status}"
            )
        else:
            db_status = GetDatabaseStatus(base_url, sub_id, db_id, http_headers)
            callback_context["db_status"] = db_status
            return ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
                resourceModel=model,
                callbackDelaySeconds=60,
                callbackContext=callback_context
            )

    event = {}
    if model.DatabaseName != '':
        event["name"] = model.DatabaseName
    if model.DatasetSizeInGb != '':
        event["datasetSizeInGb"] = int(model.DatasetSizeInGb)

    # replica = {}
    # syncSourcesList = []
    # syncSourcesDict = {}
    # if model.Endpoint != '':
    #     throughputMeasurement["by"] = model.By
    # if model.Value != '':
    #     throughputMeasurement["value"] = int(model.Value)
    # if model.Value != '':
    #     throughputMeasurement["value"] = int(model.Value)

    # throughputMeasurement = {}
    # if model.By != '':
    #     throughputMeasurement["by"] = model.By
    # if model.Value != '':
    #     throughputMeasurement["value"] = int(model.Value)


    event = json.dumps(event)
    LOG.info(f"The actual event sent for POST call is: {event}")

    #Sending a POST API call to create a database
    response = PostDatabase(base_url, event, sub_id, http_headers)

    #Retrieving the detailed link for Database after POST call
    LOG.info(f'This is the link after POST call {response["links"][0]["href"]}')
    href_value = response["links"][0]["href"]

    #Retrieving Database ID and it's Description
    db_id = GetDatabaseId (href_value, http_headers)
    db_id = str(db_id)
    model.DatabaseID = db_id

    LOG.info(f"The Database ID is: {db_id}")

    # Initial status check and storing both in callback_context
    db_status = GetDatabaseStatus(base_url, sub_id, db_id, http_headers)
    callback_context["db_id"] = db_id
    callback_context["db_status"] = db_status

    return ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
        callbackDelaySeconds=60,
        callbackContext=callback_context
    )


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    typeConfiguration = request.typeConfiguration
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    # TODO: put code here
    return read_handler(session, request, callback_context)


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    typeConfiguration = request.typeConfiguration
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    http_headers = {"accept":"application/json", "x-api-key":typeConfiguration.RedisAccess.xapikey, "x-api-secret-key":typeConfiguration.RedisAccess.xapisecretkey, "Content-Type":"application/json"}
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID
    db_id = model.DatabaseID

    DeleteDatabase (base_url, sub_id, db_id, http_headers)

    return ProgressEvent(status=OperationStatus.SUCCESS)


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    typeConfiguration = request.typeConfiguration
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


@resource.handler(Action.LIST)
def list_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    typeConfiguration = request.typeConfiguration
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )
