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


# Function using urllib3 that creates and sends the API call
def HttpRequests(method, url, headers, body=None):
    response = urllib3.request(method=method, url=url, body=body, headers=headers)
    response = response.json()
    return response


# Function to Create a new Subscription
def PostSubscription(base_url, event, http_headers):
    url = base_url + "/v1/subscriptions/"

    response = HttpRequests(method="POST", url=url, body=event, headers=http_headers)
    LOG.info(f"The POST call response is: {response}")
    return response


# Returns the details about all the existing Subscriptions
def GetSubscriptions(base_url, http_headers):
    url = base_url + "/v1/subscriptions"

    response = HttpRequests(method="GET", url=url, headers=http_headers)

    LOG.info(f"The response after GET all Subscriptions is: {response}")
    return response


# Function which returns the response of GET Subscription
def BasicGetSubscription(base_url, subscription_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id)

    response = HttpRequests(method="GET", url=url, headers=http_headers)

    LOG.info(f"The response after basic GET Subscription is: {response}")
    return response


# Function that runs a GET call based on a href link took from another response
def GetHrefLink(href_value, http_headers):
    response = HttpRequests(method="GET", url=href_value, headers=http_headers)

    LOG.info(f"This is the response for the href_link given: {response}")
    return response


# Function to retrieve Subscription ID and it's Description
def GetSubscriptionId(href_value, http_headers):
    response = HttpRequests(method="GET", url=href_value, headers=http_headers)
    count = 0

    while "resourceId" not in str(response) and count < 50:
        time.sleep(1)
        count += 1
        response = HttpRequests(method="GET", url=href_value, headers=http_headers)

    sub_id = response["response"]["resourceId"]
    sub_description = response["description"]
    LOG.info(
        f"Subscription with ID {sub_id} has the response for the GET call: {response}"
    )
    return sub_id, sub_description


# Function to retrieve subscription status to then call the callback_context
def GetSubscriptionStatus(base_url, subscription_id, http_headers):
    sub_url = base_url + "/v1/subscriptions/" + str(subscription_id)

    response = HttpRequests(method="GET", url=sub_url, headers=http_headers)
    sub_status = response["status"]
    LOG.info("Subscription status is: " + sub_status)
    return sub_status


# Function which returns the Database ID
def GetDatabaseId(base_url, subscription_id, http_headers, offset=0, limit=100):
    db_url = (
        base_url
        + "/v1/subscriptions/"
        + str(subscription_id)
        + "/databases?offset="
        + str(offset)
        + "&limit="
        + str(limit)
    )

    response = HttpRequests(method="GET", url=db_url, headers=http_headers)
    default_db_id = response["subscription"][0]["databases"][0]["databaseId"]
    return default_db_id


# Makes the Update API call
def PutSubscription(base_url, subscription_id, event, http_headers):
    url = base_url + "/v1/subscriptions/" + subscription_id

    response = HttpRequests(method="PUT", url=url, body=event, headers=http_headers)
    LOG.info(f"The PUT call response is: {response}")
    return response


# Makes the Delete API call
def DeleteDatabase(base_url, subscription_id, database_id, http_headers):
    url = (
        base_url
        + "/v1/subscriptions/"
        + str(subscription_id)
        + "/databases/"
        + str(database_id)
    )

    response = HttpRequests(method="DELETE", url=url, headers=http_headers)
    LOG.info("Default database was deleted with response:" + str(response))


# Functions which returns the total number of databases assigned to a subscription
def GetNumberOfDatabases(base_url, subscription_id, http_headers):
    sub_url = base_url + "/v1/subscriptions/" + str(subscription_id)

    response = HttpRequests(method="GET", url=sub_url, headers=http_headers)
    db_number = response["numberOfDatabases"]
    LOG.info(
        "The Number of Databases assigned to Subscription with ID "
        + str(subscription_id)
        + " is "
        + str(db_number)
    )
    return str(db_number)


# Function to delete a subscription
def DeleteSubscription(base_url, subscription_id, http_headers):
    subs_url = base_url + "/v1/subscriptions/" + subscription_id

    response = HttpRequests(method="DELETE", url=subs_url, headers=http_headers)
    time.sleep(
        10
    )  # hardcoded 10 seconds of sleep because the delete call takes longer to be processed.
    LOG.info(
        f"Subscription with ID {subscription_id} was deleted with response: {response}"
    )
    return response


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

    http_headers = {
        "accept": "application/json",
        "x-api-key": typeConfiguration.RedisAccess.xapikey,
        "x-api-secret-key": typeConfiguration.RedisAccess.xapisecretkey,
        "Content-Type": "application/json",
    }
    base_url = model.BaseUrl

    # Check if we're retrying (if sub_id and sub_status are in callback_context)
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
                        f"The deletion for the Dummy Database with ID: {default_db_id} has failed. Please delete it manually.",
                    )
            if GetNumberOfDatabases(base_url, sub_id, http_headers) == "0":
                return ProgressEvent(
                    status=OperationStatus.SUCCESS, resourceModel=model
                )
            else:
                return ProgressEvent(
                    status=OperationStatus.IN_PROGRESS,
                    resourceModel=model,
                    callbackDelaySeconds=60,
                    callbackContext=callback_context,
                )
        elif sub_status in ["failed", "error"]:
            return ProgressEvent.failed(
                HandlerErrorCode.InternalFailure,
                f"Subscription creation failed with status: {sub_status}. Please manually check that all resources have been deleted from Redis Cloud console.",
            )
        else:
            sub_status = GetSubscriptionStatus(base_url, sub_id, http_headers)
            callback_context["sub_status"] = sub_status
            return ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
                resourceModel=model,
                callbackDelaySeconds=60,
                callbackContext=callback_context,
            )

    # If we're here, it means this is the first call (no sub_id in callback_context)
    # Creating the event dictionary that will be identical with a Swagger API call
    else:
        databasesList = []
        databasesDict = {}
        databasesDict["name"] = "DummyDatabase"
        databasesDict["datasetSizeInGb"] = 1
        databasesList.append(databasesDict)

        event = {}
        if model.SubscriptionName != "":
            event["name"] = model.SubscriptionName
        if model.DryRun != "":
            if model.DryRun.lower() == "true":
                event["dryRun"] = True
            elif model.DryRun.lower() == "false":
                event["dryRun"] = False
        if model.DeploymentType != "":
            event["deploymentType"] = model.DeploymentType
        if model.PaymentMethod != "":
            event["paymentMethod"] = model.PaymentMethod
        if model.PaymentMethodId != "":
            event["paymentMethodId"] = int(model.PaymentMethodId)
        if model.MemoryStorage != "":
            event["memoryStorage"] = model.MemoryStorage
        event["cloudProviders"] = json.loads(model.CloudProviders)
        event["databases"] = databasesList
        if model.RedisVersion != "":
            event["redisVersion"] = model.RedisVersion

        event = json.dumps(event)
        LOG.info(f"The actual event sent for POST call is: {event}")

        # Sending a POST API call to create a subscription and a dummy database
        response = PostSubscription(base_url, event, http_headers)

        # Retrieving the detailed link for Subscription after POST call
        href_value = response["links"][0]["href"]

        # Retrieving Subscription ID and it's Description
        sub_id, sub_description = GetSubscriptionId(href_value, http_headers)
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
            callbackContext=callback_context,
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
    http_headers = {
        "accept": "application/json",
        "x-api-key": typeConfiguration.RedisAccess.xapikey,
        "x-api-secret-key": typeConfiguration.RedisAccess.xapisecretkey,
        "Content-Type": "application/json",
    }
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID

    # Decided that only the Subscription Name is an updatable field
    event = {}
    if model.SubscriptionName != "":
        event["name"] = model.SubscriptionName
        event = json.dumps(event)
        LOG.info(f"The event sent for PUT call is: {event}")
        PutSubscription(base_url, sub_id, event, http_headers)
    else:
        LOG.info(f"No Updates required.")
        return read_handler(session, request, callback_context)

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

    http_headers = {
        "accept": "application/json",
        "x-api-key": typeConfiguration.RedisAccess.xapikey,
        "x-api-secret-key": typeConfiguration.RedisAccess.xapisecretkey,
        "Content-Type": "application/json",
    }
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID

    # Check if we're in the retry phase by checking if deletion was attempted already
    if callback_context.get("delete_in_progress"):
        try:
            # Poll the subscription status
            response_check = BasicGetSubscription(base_url, sub_id, http_headers)
            LOG.info(f"Polling deletion status: {response_check}")

            if response_check["status"] == "deleting":
                return ProgressEvent(
                    status=OperationStatus.IN_PROGRESS,
                    resourceModel=model,
                    callbackDelaySeconds=60,  # Poll every 60 seconds
                    callbackContext={"delete_in_progress": True},
                )

            if "Not Found" in str(response_check):
                return ProgressEvent(status=OperationStatus.SUCCESS)

        except Exception as e:
            return ProgressEvent.failed(HandlerErrorCode.InternalFailure, str(e))

    # If this is the first attempt to delete
    try:
        # Attempt to delete the subscription
        delete_response = DeleteSubscription(base_url, sub_id, http_headers)
        href_value = delete_response["links"][0]["href"]
        LOG.info(f"Deletion initiated: {delete_response}")

        delete_response = GetHrefLink(href_value, http_headers)

        # Handle the case where the subscription is already not found
        if "response" in str(delete_response) and "error" in str(
            delete_response["response"]
        ):
            error_code = str(delete_response["response"]["error"]["type"])
            if error_code == "SUBSCRIPTION_NOT_FOUND":
                return ProgressEvent.failed(
                    HandlerErrorCode.NotFound,
                    f"Subscription with ID {sub_id} was not found.",
                )
        else:
            response_check = BasicGetSubscription(base_url, sub_id, http_headers)
            if (
                "id" in str(response_check)
                and response_check["id"] == int(sub_id)
                and response_check["status"] == "deleting"
            ):
                LOG.info(f"Subscription has the status: deleting.")
                return ProgressEvent(
                    status=OperationStatus.IN_PROGRESS,
                    resourceModel=model,
                    callbackDelaySeconds=60,  # Poll every 60 seconds
                    callbackContext={"delete_in_progress": True},
                )
            else:
                LOG.info(f"Subscription has the status: {response_check['status']}")
                return ProgressEvent.failed(
                    HandlerErrorCode.InternalFailure,
                    f"Subscription {sub_id} still exists and is not in a deleting state.",
                )

    except Exception as e:
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, str(e))


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    typeConfiguration = request.typeConfiguration

    http_headers = {
        "accept": "application/json",
        "x-api-key": typeConfiguration.RedisAccess.xapikey,
        "x-api-secret-key": typeConfiguration.RedisAccess.xapisecretkey,
        "Content-Type": "application/json",
    }
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID
    LOG.info(f"This is the model sent in read handler: {model}")

    # Try to retrieve the resource
    response = BasicGetSubscription(base_url, sub_id, http_headers)
    LOG.info(f"This is the response after BasicGetSubscription: {response}")

    # If the resource does not exist anymore, return NotFound
    if "id" not in str(response) or response["id"] != int(sub_id):
        LOG.info(f"Subscription with ID {sub_id} not found. Returning NotFound error.")
        return ProgressEvent.failed(
            HandlerErrorCode.NotFound, f"Subscription {sub_id} does not exist."
        )
    elif response["status"] == "deleting":
        return ProgressEvent.failed(
            HandlerErrorCode.NotFound, f"Subscription {sub_id} is in delete state"
        )
    else:
        # If the resource still exists, return it
        LOG.info(f"Subscription with ID {sub_id} exists. Returning the resource.")
        LOG.info(f"Model before ending read_handler is: {model}")
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

    http_headers = {
        "accept": "application/json",
        "x-api-key": typeConfiguration.RedisAccess.xapikey,
        "x-api-secret-key": typeConfiguration.RedisAccess.xapisecretkey,
        "Content-Type": "application/json",
    }
    base_url = model.BaseUrl

    # Fetch all subscriptions from the external service
    response = GetSubscriptions(base_url, http_headers)
    subscriptions = response.get("subscriptions", [])
    models = []

    # Loop through each subscription and build models based on criteria
    LOG.info(f"Retrieved subscriptions: {subscriptions}")
    for sub in subscriptions:
        # Only include subscriptions that are not in 'deleting' state
        if sub["status"] != "deleting":
            models.append(
                ResourceModel(
                    SubscriptionID=str(sub.get("id")),
                    BaseUrl=base_url,
                    SubscriptionName=sub.get("name"),
                    DryRun="false",
                    DeploymentType=sub.get("deploymentType"),
                    PaymentMethod=sub.get("paymentMethodType"),
                    PaymentMethodId=sub.get("paymentMethodId"),
                    MemoryStorage=sub.get("memoryStorage"),
                    CloudProviders=sub.get("cloudDetails"),
                    RedisVersion=model.RedisVersion,
                )
            )

    # If no subscriptions are found, return an empty model array
    LOG.info(f"Final list of models: {models}")
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=models,
    )
