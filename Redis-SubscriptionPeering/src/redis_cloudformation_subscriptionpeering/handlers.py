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
TYPE_NAME = "Redis::CloudFormation::SubscriptionPeering"

resource = Resource(TYPE_NAME, ResourceModel, TypeConfigurationModel)
test_entrypoint = resource.test_entrypoint

LOG.setLevel("INFO")

def HttpRequests(method, url, headers, body = None):
    response = urllib3.request(method = method, url = url, body = body, headers = headers)
    response = response.json()
    return response

#Makes the POST API call for Peering    
def PostPeering (base_url, event, subscription_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/peerings"
    

    response = HttpRequests(method = "POST", url = url, body = event, headers = http_headers)
    LOG.info(f"The POST call response is: {response}")
    return response

#Returns all the information about Peerings under the specified Subscription
def GetPeering (base_url, subscription_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/peerings"
    count = 0

    response = HttpRequests(method = "GET", url = url, headers = http_headers)
    count = 0
    
    while "vpcPeeringId" not in str(response) and count < 50:
        time.sleep(1)
        count += 1
        response = HttpRequests(method = "GET", url = response['links'][0]['href'], headers = http_headers)

    LOG.info(f"Get all Peerings for Subscription with ID {subscription_id} has the response: {response}")
    return response

#Returns the Peering ID used for other API calls
def GetPeeringId (url, http_headers):
    response = HttpRequests(method = "GET", url = url, headers = http_headers)
    count = 0
    
    while "resourceId" not in str(response) and count < 50:
        time.sleep(1)
        count += 1
        response = HttpRequests(method = "GET", url = url, headers = http_headers)

    peer_id = response["response"]["resourceId"]
    peer_description = response["description"]
    LOG.info(f"Peering with ID {peer_id} has the response for the GET call: {response}")
    return peer_id, peer_description

#Function to retrieve peering status to then call the callback_context
def GetPeeringStatus (base_url, subscription_id, vpcId, http_headers):
    peer_url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/peerings"
    
    response = HttpRequests(method = "GET", url = peer_url, headers = http_headers)
    href_value = response["links"][0]["href"]
    count = 0
    while "vpcPeeringId" not in str(response) and count < 50:
        time.sleep(1)
        count += 1
        response = HttpRequests(method = "GET", url = href_value, headers = http_headers)

    LOG.info(f"Peering response after GET call is: {response}") 
    peerings = response["response"]["resource"]["peerings"]
    for peering in peerings:
        if peering["vpcUid"] == vpcId:
            return peering["status"]
        else:
            return ProgressEvent.failed(
                HandlerErrorCode.InternalFailure,
                f"Peering status could not be retrieved."
            )

#Makes the PUT API call on Update stack    
def PutPeering (base_url, subscription_id, peering_id, event, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/peerings/" + str(peering_id)
    
    response = HttpRequests(method = "PUT", url = url, body = event, headers = http_headers)
    LOG.info(f"The PUT call response is: {response}")
    return response

#Deletes Peering
def DeletePeering (base_url, subscription_id, peering_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/peerings/" + str(peering_id)
    
    response = HttpRequests(method = "DELETE", url = url, headers = http_headers)
    LOG.info(f"Peering with ID {peering_id} was deleted with response: {response}")

#Returns the error message of a wrong peering    
def GetPeeringError (url, http_headers):
    response = HttpRequests(method = "GET", url = url, headers = http_headers)
    count = 0

    while "processing-error" not in str(response) and count < 50:
        time.sleep(1)
        count += 1
        response = HttpRequests(method = "GET", url = url, headers = http_headers)

    peer_error_description = response["response"]["error"]["description"]
    LOG.info(f"Peering Creation received the following response: {response}")
    return peer_error_description

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
    provider = model.Provider
    vpcId = model.VpcId

     #Check if we're retrying (if sub_id and sub_status are in callback_context)
    if "peer_id" in callback_context and "peer_status" in callback_context:
        peer_id = callback_context["peer_id"]
        peer_status = callback_context["peer_status"]

        # Check in loop if the Peering is active before existing program
        if peer_status == "active":
            LOG.info(f"The Peering status is: {peer_status}.")
            return ProgressEvent(
                status=OperationStatus.SUCCESS,
                resourceModel=model
            )
        elif peer_status == "initiating-request" or peer_status == "pending-acceptance":
            LOG.info(f"The Peering status is: {peer_status}. Please accept the request from AWS console -> Peering connections.")
            peer_status = GetPeeringStatus(base_url, sub_id, vpcId, http_headers)
            callback_context["peer_id"] = peer_id
            callback_context["peer_status"] = peer_status
            return ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
                resourceModel=model,
                callbackDelaySeconds=60,
                callbackContext=callback_context
                )
        else:
            return ProgressEvent.failed(
                HandlerErrorCode.InternalFailure,
                f"Peering creation failed with status: {peer_status}"
            )
    else:
        # TO DO: Added error handling for all the parameters (in case the customer don t know how to use them or assign a wrong value)
        if provider == "AWS" or provider == '':
            event = {}
            if model.Region != '':
                event["region"] = model.Region
            if model.AwsAccountId != '':
                event["awsAccountId"] = model.AwsAccountId
            if model.VpcId != '':
                event["vpcId"] = model.VpcId
            if model.VpcCidr != '':
                event["vpcCidr"] = model.VpcCidr
            if model.VpcCidrs != '':
                event["vpcCidrs"] = model.VpcCidrs

        elif provider == "GCP":
            event = {}
            if model.VpcProjectUid != '':
                event["vpcProjectUid"] = model.VpcProjectUid
            if model.VpcNetworkName != '':
                event["vpcNetworkName"] = model.VpcNetworkName
        else:
            return ProgressEvent.failed(
                HandlerErrorCode.InternalFailure,
                f"Incorrect value for 'Provider' field. Please choose one from 'AWS' or 'GCP'."
                )

        event = json.dumps(event)
        LOG.info(f"The actual event sent for POST call is: {event}")

        #Sending a POST API call to create a Subscription Peering
        response = PostPeering (base_url, event, sub_id, http_headers)

        #Retrieving the detailed link for Peering after POST call
        href_value = response["links"][0]["href"]

        #Retrieving Peering ID and it's Description
        peer_id, peer_description = GetPeeringId (href_value, http_headers)
        peer_id = str(peer_id)
        model.PeeringID = peer_id

        LOG.info(f"The Peering ID is: {peer_id}")
        LOG.info(f"The Peering description is: {peer_description}")
            
        # Initial status check and storing both in callback_context
        peer_status = GetPeeringStatus(base_url, sub_id, vpcId, http_headers)
        callback_context["peer_id"] = peer_id
        callback_context["peer_status"] = peer_status

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
        resourceModel=None,
    )

    http_headers = {"accept":"application/json", "x-api-key":typeConfiguration.RedisAccess.xapikey, "x-api-secret-key":typeConfiguration.RedisAccess.xapisecretkey, "Content-Type":"application/json"}
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID
    peer_id = model.PeeringID

    DeletePeering (base_url, sub_id, peer_id, http_headers)

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
