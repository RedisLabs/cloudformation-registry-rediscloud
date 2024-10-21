# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]
    typeConfiguration: Optional["TypeConfigurationModel"]


@dataclass
class ResourceModel(BaseModel):
    DatabaseID: Optional[str]
    BaseUrl: Optional[str]
    SubscriptionID: Optional[str]
    DryRun: Optional[str]
    DatabaseName: Optional[str]
    Protocol: Optional[str]
    Port: Optional[str]
    DatasetSizeInGb: Optional[str]
    RespVersion: Optional[str]
    SupportOSSClusterApi: Optional[str]
    UseExternalEndpointForOSSClusterApi: Optional[str]
    DataPersistence: Optional[str]
    DataEvictionPolicy: Optional[str]
    Replication: Optional[str]
    Replica: Optional[str]
    ThroughputMeasurement: Optional[str]
    LocalThroughputMeasurement: Optional[str]
    AverageItemSizeInBytes: Optional[str]
    RemoteBackup: Optional[str]
    SourceIp: Optional[str]
    ClientTlsCertificates: Optional[str]
    EnableTls: Optional[str]
    Password: Optional[str]
    SaslUsername: Optional[str]
    SaslPassword: Optional[str]
    Alerts: Optional[str]
    Modules: Optional[str]
    QueryPerformanceFactor: Optional[str]
    RegexRules: Optional[str]
    EnableDefaultUser: Optional[str]
    OnDemandBackup: Optional[str]
    RegionName: Optional[str]
    OnDemandImport: Optional[str]
    SourceType: Optional[str]
    ImportFromUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DatabaseID=json_data.get("DatabaseID"),
            BaseUrl=json_data.get("BaseUrl"),
            SubscriptionID=json_data.get("SubscriptionID"),
            DryRun=json_data.get("DryRun"),
            DatabaseName=json_data.get("DatabaseName"),
            Protocol=json_data.get("Protocol"),
            Port=json_data.get("Port"),
            DatasetSizeInGb=json_data.get("DatasetSizeInGb"),
            RespVersion=json_data.get("RespVersion"),
            SupportOSSClusterApi=json_data.get("SupportOSSClusterApi"),
            UseExternalEndpointForOSSClusterApi=json_data.get("UseExternalEndpointForOSSClusterApi"),
            DataPersistence=json_data.get("DataPersistence"),
            DataEvictionPolicy=json_data.get("DataEvictionPolicy"),
            Replication=json_data.get("Replication"),
            Replica=json_data.get("Replica"),
            ThroughputMeasurement=json_data.get("ThroughputMeasurement"),
            LocalThroughputMeasurement=json_data.get("LocalThroughputMeasurement"),
            AverageItemSizeInBytes=json_data.get("AverageItemSizeInBytes"),
            RemoteBackup=json_data.get("RemoteBackup"),
            SourceIp=json_data.get("SourceIp"),
            ClientTlsCertificates=json_data.get("ClientTlsCertificates"),
            EnableTls=json_data.get("EnableTls"),
            Password=json_data.get("Password"),
            SaslUsername=json_data.get("SaslUsername"),
            SaslPassword=json_data.get("SaslPassword"),
            Alerts=json_data.get("Alerts"),
            Modules=json_data.get("Modules"),
            QueryPerformanceFactor=json_data.get("QueryPerformanceFactor"),
            RegexRules=json_data.get("RegexRules"),
            EnableDefaultUser=json_data.get("EnableDefaultUser"),
            OnDemandBackup=json_data.get("OnDemandBackup"),
            RegionName=json_data.get("RegionName"),
            OnDemandImport=json_data.get("OnDemandImport"),
            SourceType=json_data.get("SourceType"),
            ImportFromUri=json_data.get("ImportFromUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TypeConfigurationModel(BaseModel):
    RedisAccess: Optional["_RedisAccess"]

    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls(
            RedisAccess=RedisAccess._deserialize(json_data.get("RedisAccess")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TypeConfigurationModel = TypeConfigurationModel


@dataclass
class RedisAccess(BaseModel):
    xapikey: Optional[str]
    xapisecretkey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedisAccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedisAccess"]:
        if not json_data:
            return None
        return cls(
            xapikey=json_data.get("xapikey"),
            xapisecretkey=json_data.get("xapisecretkey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedisAccess = RedisAccess


