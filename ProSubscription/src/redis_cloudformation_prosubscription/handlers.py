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

# Use this logger to forward log messages to CloudWatch Logs. CHANGE TO TRIGGER PIPELINE
LOG = logging.getLogger(__name__)
TYPE_NAME = "Redis::CloudFormation::ProSubscription"

resource = Resource(TYPE_NAME, ResourceModel, TypeConfigurationModel)
test_entrypoint = resource.test_entrypoint

LOG.setLevel("INFO")

def HttpRequests(method, url, headers, body = None):
    response = urllib3.request(method = method, url = url, body = body, headers = headers)
    response = response.json()
    return response

#Function to Create a new Subscription
def PostSubscription (base_url, event, http_headers):
    url = base_url + "/v1/subscriptions/"
    
    response = HttpRequests(method = "POST", url = url, body = event, headers = http_headers)
    LOG.info(f"The POST call response is: {response}")
    return response

#Function to retrieve Subscription ID and it's Description
def GetSubscriptionId (href_value, http_headers):
    response = HttpRequests(method = "GET", url = href_value, headers = http_headers)
    count = 0
    
    while "resourceId" not in str(response) and count < 50:
        time.sleep(1)
        count += 1
        response = HttpRequests(method = "GET", url = href_value, headers = http_headers)

    sub_id = response["response"]["resourceId"]
    sub_description = response["description"]
    LOG.info(f"Subscription with ID {sub_id} has the response for the GET call: {response}")
    return sub_id, sub_description

#Function to retrieve subscription status to then call the callback_context
def GetSubscriptionStatus (base_url, subscription_id, http_headers):
    sub_url = base_url + "/v1/subscriptions/" + str(subscription_id)
    
    # A GET request to the API
    response = HttpRequests(method = "GET", url = sub_url, headers = http_headers)
    sub_status = response["status"]
    LOG.info("Subscription status is: " + sub_status)
    return sub_status

def GetDatabaseId (base_url, subscription_id, http_headers, offset = 0, limit = 100):
    db_url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases?offset=" + str(offset) + "&limit=" + str(limit)
    
    response = HttpRequests(method = "GET", url = db_url, headers = http_headers)
    default_db_id = response["subscription"][0]["databases"][0]["databaseId"]
    return default_db_id

#Makes the Update API call
def PutSubscription (base_url, subscription_id, event, http_headers):
    url = base_url + "/v1/subscriptions/" + subscription_id
    
    response = HttpRequests(method = "PUT", url = url, body = event, headers = http_headers)
    LOG.info(f"The PUT call response is: {response}")
    return response

#Makes the Delete API call    
def DeleteDatabase (base_url, subscription_id, database_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases/" + str(database_id)
    
    response = HttpRequests(method = "DELETE", url = url, headers = http_headers)
    LOG.info("Default database was deleted with response:" + str(response))

def GetNumberOfDatabases (base_url, subscription_id, http_headers):
    sub_url = base_url + "/v1/subscriptions/" + str(subscription_id)

    response = HttpRequests(method = "GET", url = sub_url, headers = http_headers)
    db_number = response["numberOfDatabases"]
    LOG.info("The Number of Databases assigned to Subscription with ID " + str(subscription_id) + " is " + str(db_number))
    return str(db_number)

def DeleteSubscription (base_url, subscription_id, http_headers):
    subs_url = base_url + "/v1/subscriptions/" + subscription_id
    
    response = HttpRequests(method = "DELETE", url = subs_url, headers = http_headers)
    LOG.info(f"Subscription with ID {subscription_id} was deleted with response: {response}")

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

    #Check if we're retrying (if sub_id and sub_status are in callback_context)
    if "sub_id" in callback_context and "sub_status" in callback_context:
        sub_id = callback_context["sub_id"]
        sub_status = callback_context["sub_status"]

        # If the subscription status is complete, delete the dummy database and return success
        if sub_status == "active":
            if callback_context.get("db_deletetion_api_call_executed") != True:
                try:
                    default_db_id = str(GetDatabaseId(base_url, sub_id, http_headers))
                    LOG.info("Default Database ID is: " + default_db_id)
                    DeleteDatabase(base_url, sub_id, default_db_id, http_headers)
                    callback_context["db_deletetion_api_call_executed"] = True
                except:
                    return ProgressEvent.failed(
                        HandlerErrorCode.InternalFailure,
                        f"The deletion for the Dummy Database with ID: {default_db_id} has failed. Please delete it manually."
            )
            if GetNumberOfDatabases(base_url, sub_id, http_headers) == "0":
                return ProgressEvent(
                    status=OperationStatus.SUCCESS,
                    resourceModel=model
                )
            else:
                return ProgressEvent(
                    status=OperationStatus.IN_PROGRESS,
                    resourceModel=model,
                    callbackDelaySeconds=60,
                    callbackContext=callback_context
                )
        elif sub_status in ["failed", "error"]:
            return ProgressEvent.failed(
                HandlerErrorCode.InternalFailure,
                f"Subscription creation failed with status: {sub_status}. Please manually check that all resources have been deleted from Redis Cloud console."
            )
        else:
            sub_status = GetSubscriptionStatus(base_url, sub_id, http_headers)
            callback_context["sub_status"] = sub_status
            return ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
                resourceModel=model,
                callbackDelaySeconds=60,
                callbackContext=callback_context
            )

    # If we're here, it means this is the first call (no sub_id in callback_context)
    # Creating the event dictionary that will be identical with a Swagger API call
    networking = {}
    if model.DeploymentCIDR != '':
        networking["deploymentCIDR"] = model.DeploymentCIDR
    if model.VpcId != '':
        networking["vpcId"] = model.VpcId
    
    regionsList = []
    regionsDict = {}
    regionsDict["region"] = model.Region
    if model.MultipleAvailabilityZones != '':
        regionsDict["multipleAvailabilityZones"] = model.MultipleAvailabilityZones
    if model.PreferredAvailabilityZones != '':
        regionsDict["preferredAvailabilityZones"] = model.PreferredAvailabilityZones
    regionsDict["networking"] = networking
    regionsList.append(regionsDict)
    
    cloudProvidersList = []
    cloudProvidersDict = {}
    if model.Provider != '':
        cloudProvidersDict["provider"] = model.Provider
    if model.CloudAccountId != '':
        cloudProvidersDict["cloudAccountId"] = int(model.CloudAccountId)
    cloudProvidersDict["regions"] = regionsList
    cloudProvidersList.append(cloudProvidersDict)
    
    databasesList = []
    databasesDict = {} 
    databasesDict["name"] = "DummyDatabase"
    databasesDict["datasetSizeInGb"] = 1
    databasesList.append(databasesDict)
    
    event = {}
    if model.SubscriptionName != '':
        event["name"] = model.SubscriptionName
    if model.DryRun != '':
        event["dryRun"] = model.DryRun
    if model.DeploymentType != '':
        event["deploymentType"] = model.DeploymentType
    if model.PaymentMethod != '':
        event["paymentMethod"] = model.PaymentMethod
    if model.PaymentMethodId != '':
        event["paymentMethodId"] = int(model.PaymentMethodId)
    if model.MemoryStorage != '':
        event["memoryStorage"] = model.MemoryStorage
    event["cloudProviders"] = cloudProvidersList
    event["databases"] = databasesList
    if model.RedisVersion != '':
        event["redisVersion"] = model.RedisVersion

    event = json.dumps(event)
    LOG.info(f"The actual event sent for POST call is: {event}")

    #Sending a POST API call to create a subscription and a dummy database
    response = PostSubscription(base_url, event, http_headers)

    #Retrieving the detailed link for Subscription after POST call
    href_value = response["links"][0]["href"]
    
    #Retrieving Subscription ID and it's Description
    sub_id, sub_description = GetSubscriptionId (href_value, http_headers)
    sub_id = str(sub_id)
    model.SubscriptionID = sub_id

    LOG.info(f"The Subscription ID is: {sub_id}")
    LOG.info(f"The Subscription description is: {sub_description}")
        
    # Initial status check and storing both in callback_context
    sub_status = GetSubscriptionStatus(base_url, sub_id, http_headers)
    callback_context["sub_id"] = sub_id
    callback_context["sub_status"] = sub_status

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
    http_headers = {"accept":"application/json", "x-api-key":typeConfiguration.RedisAccess.xapikey, "x-api-secret-key":typeConfiguration.RedisAccess.xapisecretkey, "Content-Type":"application/json"}
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID

    event = {}
    event["name"] = model.SubscriptionName
    event = json.dumps(event)
    LOG.info(f"The event sent for PUT call is: {event}")
    PutSubscription (base_url, sub_id, event, http_headers)

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
        resourceModel=model
    )

    http_headers = {"accept":"application/json", "x-api-key":typeConfiguration.RedisAccess.xapikey, "x-api-secret-key":typeConfiguration.RedisAccess.xapisecretkey, "Content-Type":"application/json"}
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID
    DeleteSubscription(base_url, sub_id, http_headers)

    return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModel=model,
        )

@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
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
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )
