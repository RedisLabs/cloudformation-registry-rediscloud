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

#Function using urllib3 that creates and sends the API call
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

#Returns the details about all the existing Databases
def GetDatabases (base_url, subscription_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases?offset=0&limit=100"
    LOG.info(f"URL for GetDatabases is: {url}")
    response = HttpRequests(method = "GET", url = url, headers = http_headers)

    LOG.info(f"The response after GET all Databases is: {response}")
    return response

#Function which returns the response of GET Database
def BasicGetDatabase (base_url, subscription_id, database_id, http_headers):
    url = base_url + "/v1/subscriptions/" + str(subscription_id) + "/databases/" + str(database_id)

    response = HttpRequests(method = "GET", url = url, headers = http_headers)

    LOG.info(f"The response after Basic GET Database is: {response}")
    return response

#Function that runs a GET call based on a href link took from another response
def GetHrefLink (href_value, http_headers):
    response = HttpRequests(method = "GET", url = href_value, headers = http_headers)

    LOG.info(f"This is the response for the href_link given: {response}")
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
   
    # Creating the event dictionary that will be identical with a Swagger API call
    else:
        event = {}
        if model.DryRun != '' and model.DryRun != None:
            if model.DryRun.lower() == 'true':
                event["dryRun"] = True
            elif model.DryRun.lower() == 'false':
                event["dryRun"] = False
        if model.DatabaseName != '':
            event["name"] = model.DatabaseName
        if model.Protocol != '':
            event["protocol"] = model.Protocol
        if model.Port != '':
            event["port"] = model.Port
        if model.DatasetSizeInGb != '' and model.DatasetSizeInGb != None:
            event["datasetSizeInGb"] = int(model.DatasetSizeInGb)
        if model.RespVersion != '':
            event["respVersion"] = model.RespVersion
        if model.SupportOSSClusterApi != '' and model.SupportOSSClusterApi != None:
            if model.SupportOSSClusterApi.lower() == 'true':
                event["supportOSSClusterApi"] = True
            elif model.SupportOSSClusterApi.lower() == 'false':
                event["supportOSSClusterApi"] = False
        if model.UseExternalEndpointForOSSClusterApi != '' and model.UseExternalEndpointForOSSClusterApi != None:
            if model.UseExternalEndpointForOSSClusterApi.lower() == 'true':
                event["useExternalEndpointForOSSClusterApi"] = True
            elif model.UseExternalEndpointForOSSClusterApi.lower() == 'false':
                event["useExternalEndpointForOSSClusterApi"] = False
        if model.DataPersistence != '':
            event["dataPersistence"] = model.DataPersistence
        if model.DataEvictionPolicy != '':
            event["dataEvictionPolicy"] = model.DataEvictionPolicy
        if model.Replication != '' and model.Replication != None:
            if model.Replication.lower() == 'true':
                event["replication"] = True
            elif model.Replication.lower() == 'false':
                event["replication"] = False
        if model.Replica != '' and model.Replica != None:
            event["replica"] = json.loads(model.Replica)
        if model.ThroughputMeasurement != '' and model.ThroughputMeasurement != None:
            event["throughputMeasurement"] = json.loads(model.ThroughputMeasurement)
        if model.LocalThroughputMeasurement != '' and model.LocalThroughputMeasurement != None:
            event["localThroughputMeasurement"] = json.loads(model.LocalThroughputMeasurement)
        if model.AverageItemSizeInBytes != '':
            event["averageItemSizeInBytes"] = model.AverageItemSizeInBytes
        if model.RemoteBackup != '' and model.RemoteBackup != None:
            event["remoteBackup"] = json.loads(model.RemoteBackup)
        if model.SourceIp != '':
            event["sourceIp"] = model.SourceIp
        if model.ClientTlsCertificates != '' and model.ClientTlsCertificates != None:
            event["clientTlsCertificates"] = json.loads(model.ClientTlsCertificates)
        if model.EnableTls != '' and model.EnableTls != None:
            if model.EnableTls.lower() == 'true':
                event["enableTls"] = True
            elif model.EnableTls.lower() == 'false':
                event["enableTls"] = False
        if model.Password != '':
            event["password"] = model.Password
        if model.SaslUsername != '':
            event["saslUsername"] = model.SaslUsername
        if model.SaslPassword != '':
            event["saslPassword"] = model.SaslPassword
        if model.Alerts != '' and model.Alerts != None:
            event["alerts"] = json.loads(model.Alerts)
        if model.Modules != '' and model.Modules != None:
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

    #Checking if the Update should create a new backup on demand
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
    
    #Checking if the Update should Import a previous created Backup
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

    #If neither Backup nor Import are desired upon Update call, then initiate a normal Put call for the current database
    else:
        if model.DryRun != '' and model.DryRun != None:
            if model.DryRun.lower() == 'true':
                event["dryRun"] = True
            elif model.DryRun.lower() == 'false':
                event["dryRun"] = False
        if model.DatabaseName != '':
            event["name"] = model.DatabaseName
        if model.DatasetSizeInGb != '' and model.DatasetSizeInGb != None:
            event["datasetSizeInGb"] = int(model.DatasetSizeInGb)
        if model.RespVersion != '':
            event["respVersion"] = model.RespVersion
        if model.ThroughputMeasurement != '' and model.ThroughputMeasurement != None:
            event["throughputMeasurement"] = json.loads(model.ThroughputMeasurement)    
        if model.DataPersistence != '':
            event["dataPersistence"] = model.DataPersistence
        if model.DataEvictionPolicy != '':
            event["dataEvictionPolicy"] = model.DataEvictionPolicy
        if model.Replication != '' and model.Replication != None:
            if model.Replication.lower() == 'true':
                event["replication"] = True
            elif model.Replication.lower() == 'false':
                event["replication"] = False
        if model.RegexRules != '':
            event["regexRules"] = model.RegexRules
        if model.Replica != '' and model.Replica != None:
            event["replica"] = json.loads(model.Replica)
        if model.SupportOSSClusterApi != '' and model.SupportOSSClusterApi != None:
            if model.SupportOSSClusterApi.lower() == 'true':
                event["supportOSSClusterApi"] = True
            elif model.SupportOSSClusterApi.lower() == 'false':
                event["supportOSSClusterApi"] = False
        if model.UseExternalEndpointForOSSClusterApi != '' and model.UseExternalEndpointForOSSClusterApi != None:
            if model.UseExternalEndpointForOSSClusterApi.lower() == 'true':
                event["useExternalEndpointForOSSClusterApi"] = True
            elif model.UseExternalEndpointForOSSClusterApi.lower() == 'false':
                event["useExternalEndpointForOSSClusterApi"] = False
        if model.Password != '':
            event["password"] = model.Password
        if model.SaslUsername != '':
            event["saslUsername"] = model.SaslUsername
        if model.SaslPassword != '':
            event["saslPassword"] = model.SaslPassword
        if model.SourceIp != '':
            event["sourceIp"] = model.SourceIp
        if model.ClientTlsCertificates != '' and model.ClientTlsCertificates != None:
            event["clientTlsCertificates"] = json.loads(model.ClientTlsCertificates)
        if model.EnableTls != '' and model.EnableTls != None:
            if model.EnableTls.lower() == 'true':
                event["enableTls"] = True
            elif model.EnableTls.lower() == 'false':
                event["enableTls"] = False
        if model.EnableDefaultUser != '':
            event["enableDefaultUser"] = model.EnableDefaultUser
        if model.RemoteBackup != '' and model.RemoteBackup != None:
            event["remoteBackup"] = json.loads(model.RemoteBackup)
        if model.Alerts != '' and model.Alerts != None:
            event["alerts"] = json.loads(model.Alerts)
        if model.QueryPerformanceFactor != '':
            event["queryPerformanceFactor"] = model.QueryPerformanceFactor

        event = json.dumps(event)
        LOG.info(f"The event sent for PUT call is: {event}")
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

    #This block runs only after callback is activated in order to check the database status
    if callback_context.get("delete_in_progress"):
        try:
            # Poll the Database status
            response_check = BasicGetDatabase(base_url, sub_id, db_id, http_headers)
            LOG.info(f"Polling deletion status: {response_check}")

            if 'delete-draft' in response_check:
                return ProgressEvent(
                    status=OperationStatus.IN_PROGRESS,
                    resourceModel=model,
                    callbackDelaySeconds=60,  # Poll every 60 seconds
                    callbackContext={"delete_in_progress": True}
                ) 
            elif "Not Found" in str(response_check):
                return ProgressEvent(
                    status=OperationStatus.SUCCESS
                )
            else:
                LOG.info(f"Database has the status: {response_check['status']}")
                return ProgressEvent.failed(
                    HandlerErrorCode.InternalFailure,
                    f"Database {db_id} still exists and is not in a deleting state."
                )

        except Exception as e:
            return ProgressEvent.failed(
                HandlerErrorCode.InternalFailure,
                str(e)
            )

    try:
        DeleteDatabase (base_url, sub_id, db_id, http_headers)
        response_check = BasicGetDatabase(base_url, sub_id, db_id, http_headers)

        # Handle the case where the database is already not found
        if "404" in str(response_check):
            return ProgressEvent.failed(
                HandlerErrorCode.NotFound,
                f"Database with ID {db_id} was not found."
                )
        else:
            return ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
                resourceModel=model,
                callbackDelaySeconds=60,  # Poll every 60 seconds
                callbackContext={"delete_in_progress": True}
            )

    except Exception as e:
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure,
            str(e)
        )

@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    typeConfiguration = request.typeConfiguration

    http_headers = {"accept":"application/json", "x-api-key":typeConfiguration.RedisAccess.xapikey, "x-api-secret-key":typeConfiguration.RedisAccess.xapisecretkey, "Content-Type":"application/json"}
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID
    db_id = model.DatabaseID
    LOG.info(f"the model in read handler: {model}")

    # Retrieve the resource
    response = BasicGetDatabase(base_url, sub_id, db_id, http_headers)
    LOG.info(f"This is the response after BasicGetDatabase: {response}")

    # If the resource does not exist anymore, return NotFound
    if 'databaseId' not in str(response) or response['databaseId'] != int(db_id):
        LOG.info(f"Database with ID {db_id} not found. Returning NotFound error.")
        return ProgressEvent.failed(
            HandlerErrorCode.NotFound,
            f"Database {db_id} does not exist."
        )
    elif response["status"] == "deleting":
        return ProgressEvent.failed(
            HandlerErrorCode.NotFound,
            f"Database {db_id} is in delete state"
        )
    else:
        # If the resource still exists, return it
        LOG.info(f"Database with ID {db_id} exists. Returning the resource.")
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

    http_headers = {"accept":"application/json", "x-api-key":typeConfiguration.RedisAccess.xapikey, "x-api-secret-key":typeConfiguration.RedisAccess.xapisecretkey, "Content-Type":"application/json"}
    base_url = model.BaseUrl
    sub_id = model.SubscriptionID

    # Fetch all subscriptions from the external service
    LOG.info(f"sub_id in list is: {sub_id}")
    response = GetDatabases(base_url, sub_id, http_headers)
    subscription = response.get("subscription", [])
    LOG.info(f"This is the Subscriptions list: {subscription}")
    # Check if subscriptions list is not empty before accessing the first item
    if subscription:
        databases = subscription[0].get("databases", [])
        LOG.info(f"This is the Database list: {subscription}")
    else:
        databases = []
    models = []

    # Loop through each subscription and build models based on criteria
    LOG.info(f"Retrieved databases: {databases}")
    for db in databases:
        # Only include databases that are not in 'deleting' state
        if 'delete-draft' not in str(db):
            models.append(ResourceModel(
                DatabaseID=str(db.get("databaseId")),
                BaseUrl=base_url,
                SubscriptionID=sub_id,
                DryRun="false",
                DatabaseName=db.get("name"),
                Protocol=db.get("protocol"),
                Port=db.get("port"),
                DatasetSizeInGb=db.get("datasetSizeInGb"),
                RespVersion=db.get("respVersion"),
                SupportOSSClusterApi=db.get("supportOSSClusterApi"),
                UseExternalEndpointForOSSClusterApi=db.get("useExternalEndpointForOSSClusterApi"),
                DataPersistence=db.get("dataPersistence"),
                DataEvictionPolicy=db.get("dataEvictionPolicy"),
                Replication=db.get("replication"),
                Replica=db.get("replica"),
                ThroughputMeasurement=db.get("throughputMeasurement"),
                LocalThroughputMeasurement=db.get("localThroughputMeasurement"),
                AverageItemSizeInBytes=db.get("averageItemSizeInBytes"),
                RemoteBackup=db.get("backup"),
                SourceIp=db.get("security", {}).get("sourceIps", []),
                ClientTlsCertificates=db.get("security", {}).get("tlsClientAuthentication", None),
                EnableTls=db.get("security", {}).get("enableTls", None),
                Password=db.get("password", None),
                SaslUsername=db.get("saslUsername", None),
                SaslPassword=db.get("saslPassword", None),
                Alerts=db.get("alerts"),
                Modules=db.get("modules"),
                QueryPerformanceFactor=db.get("queryPerformanceFactor", None),
                RegexRules=db.get("clustering", {}).get("regexRules", []),
                EnableDefaultUser=db.get("security", {}).get("enableDefaultUser", None),
                OnDemandBackup="",
                RegionName="",
                OnDemandImport="",
                SourceType="",
                ImportFromUri="",
            ))

    # If no subscriptions are found, return an empty model array
    LOG.info(f"Final list of models: {models}")
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=models,
    )
    