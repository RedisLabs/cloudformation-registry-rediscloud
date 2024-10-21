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

#Creates Backup for Database
def PostBackup (base_url, subscription_id, database_id, event, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases/" + str(database_id) + "/backup"
    
    response = HttpRequests(method = "POST", url = url, body = event, headers = http_headers)
    LOG.info(f"The POST call response for Create Backup is: {response}")
    return response

#Creates Import for Database
def PostImport (base_url, subscription_id, database_id, event, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases/" + str(database_id) + "/import"
    
    response = HttpRequests(method = "POST", url = url, body = event, headers = http_headers)
    LOG.info(f"The POST call response for Create Import is: {response}")
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
    if model.DryRun != '':
        event["dryRun"] = model.DryRun
    if model.DatabaseName != '':
        event["name"] = model.DatabaseName
    if model.Protocol != '':
        event["protocol"] = model.Protocol
    if model.Port != '':
        event["port"] = model.Port
    if model.DatasetSizeInGb != '':
        event["datasetSizeInGb"] = int(model.DatasetSizeInGb)
    if model.RespVersion != '':
        event["respVersion"] = model.RespVersion
    if model.SupportOSSClusterApi != '':
        event["supportOSSClusterApi"] = model.SupportOSSClusterApi
    if model.UseExternalEndpointForOSSClusterApi != '':
        event["useExternalEndpointForOSSClusterApi"] = model.UseExternalEndpointForOSSClusterApi
    if model.DataPersistence != '':
        event["dataPersistence"] = model.DataPersistence
    if model.DataEvictionPolicy != '':
        event["dataEvictionPolicy"] = model.DataEvictionPolicy
    if model.Replication != '':
        event["replication"] = model.Replication
    if model.Replica != '':
        event["replica"] = json.loads(model.Replica)
    if model.ThroughputMeasurement != '':
        event["throughputMeasurement"] = json.loads(model.ThroughputMeasurement)
    if model.LocalThroughputMeasurement != '':
        event["localThroughputMeasurement"] = json.loads(model.LocalThroughputMeasurement)
    if model.AverageItemSizeInBytes != '':
        event["averageItemSizeInBytes"] = model.AverageItemSizeInBytes
    if model.RemoteBackup != '':
        event["remoteBackup"] = json.loads(model.RemoteBackup)
    if model.SourceIp != '':
        event["sourceIp"] = model.SourceIp
    if model.ClientTlsCertificates != '':
        event["clientTlsCertificates"] = json.loads(model.ClientTlsCertificates)
    if model.EnableTls != '':
        event["enableTls"] = model.EnableTls
    if model.Password != '':
        event["password"] = model.Password
    if model.SaslUsername != '':
        event["saslUsername"] = model.SaslUsername
    if model.SaslPassword != '':
        event["saslPassword"] = model.SaslPassword
    if model.Alerts != '':
        event["alerts"] = json.loads(model.Alerts)
    if model.Modules != '':
        event["modules"] = json.loads(model.Modules)
    if model.QueryPerformanceFactor != '':
        event["queryPerformanceFactor"] = model.QueryPerformanceFactor

    event = json.dumps(event)
    LOG.info(f"The actual event sent for POST call is: {event}")

    #Sending a POST API call to create a database
    response = PostDatabase(base_url, event, sub_id, http_headers)

    while response["status"] != "processing-completed":
        response = HttpRequests("GET", response["links"][0]["href"], http_headers)

    #Retrieving the detailed link for Database after POST call
    LOG.info(f'This is the link after POST call {response["links"][0]["href"]}')

    #Retrieving Database ID and it's Description
    db_id = GetDatabaseId (response["links"][0]["href"], http_headers)
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

    http_headers = {"accept":"application/json", "x-api-key":typeConfiguration.RedisAccess.xapikey, "x-api-secret-key":typeConfiguration.RedisAccess.xapisecretkey, "Content-Type":"application/json"}
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID
    db_id = model.DatabaseID
    event = {}

    if model.OnDemandBackup == 'true' or model.OnDemandBackup == 'True':
        if model.RegionName == 'null' or model.RegionName == '':
            event['regionName'] = None
            event = json.dumps(event)
            LOG.info(f"The event when regionName is null is: {event}")
        else:
            event['regionName'] = model.RegionName
            event = json.dumps(event)
        response = PostBackup (base_url, sub_id, db_id, event, http_headers)
    
    elif model.OnDemandImport == 'true' or model.OnDemandImport == 'True':
        if model.SourceType != '':
            event["sourceType"] = model.SourceType
        if model.ImportFromUri != '':
            importFromUriList = []
            importFromUriList.append(model.ImportFromUri)
            event["importFromUri"] = importFromUriList
        event = json.dumps(event)    
        LOG.info(f"The event sent for Import is: {event}")
        response = PostImport (base_url, sub_id, db_id, event, http_headers)

    else:
        if model.DryRun != '':
            event["dryRun"] = model.DryRun
        if model.DatabaseName != '':
            event["name"] = model.DatabaseName
        if model.DatasetSizeInGb != '':
            event["datasetSizeInGb"] = int(model.DatasetSizeInGb)
        if model.RespVersion != '':
            event["respVersion"] = model.RespVersion
        if model.ThroughputMeasurement != '':
            event["throughputMeasurement"] = json.loads(model.ThroughputMeasurement)    
        if model.DataPersistence != '':
            event["dataPersistence"] = model.DataPersistence
        if model.DataEvictionPolicy != '':
            event["dataEvictionPolicy"] = model.DataEvictionPolicy
        if model.Replication != '':
            event["replication"] = model.Replication
        if model.RegexRules != '':
            event["regexRules"] = model.RegexRules
        if model.Replica != '':
            event["replica"] = json.loads(model.Replica)
        if model.SupportOSSClusterApi != '':
            event["supportOSSClusterApi"] = model.SupportOSSClusterApi
        if model.UseExternalEndpointForOSSClusterApi != '':
            event["useExternalEndpointForOSSClusterApi"] = model.UseExternalEndpointForOSSClusterApi
        if model.Password != '':
            event["password"] = model.Password
        if model.SaslUsername != '':
            event["saslUsername"] = model.SaslUsername
        if model.SaslPassword != '':
            event["saslPassword"] = model.SaslPassword
        if model.SourceIp != '':
            event["sourceIp"] = model.SourceIp
        if model.ClientTlsCertificates != '':
            event["clientTlsCertificates"] = json.loads(model.ClientTlsCertificates)
        if model.EnableTls != '':
            event["enableTls"] = model.EnableTls
        if model.EnableDefaultUser != '':
            event["enableDefaultUser"] = model.EnableDefaultUser
        if model.RemoteBackup != '':
            event["remoteBackup"] = json.loads(model.RemoteBackup)
        if model.Alerts != '':
            event["alerts"] = json.loads(model.Alerts)
        if model.QueryPerformanceFactor != '':
            event["queryPerformanceFactor"] = model.QueryPerformanceFactor

        event = json.dumps(event)
        LOG.info(f"The event sent for PUT call is: {event}")
        LOG.info(f"The model is: {model}")
        response = PutDatabase(base_url, sub_id, db_id, event, http_headers)
        LOG.info(f"Response for PUT call is: {response}")
    
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
