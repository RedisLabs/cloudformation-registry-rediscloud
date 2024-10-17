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
    Endpoint: Optional[str]
    Encryption: Optional[str]
    ServerCert: Optional[str]
    By: Optional[str]
    Value: Optional[str]
    LocalThroughputMeasurementRegion: Optional[str]
    WriteOperationsPerSecond: Optional[str]
    ReadOperationsPerSecond: Optional[str]
    AverageItemSizeInBytes: Optional[str]
    Active: Optional[str]
    Interval: Optional[str]
    TimeUTC: Optional[str]
    StorageType: Optional[str]
    StoragePath: Optional[str]
    SourceIp: Optional[str]
    PublicCertificatePEMString: Optional[str]
    EnableTls: Optional[str]
    Password: Optional[str]
    SaslUsername: Optional[str]
    SaslPassword: Optional[str]
    AlertName: Optional[str]
    AlertValue: Optional[str]
    ModuleName: Optional[str]
    ModuleParameters: Optional[str]
    QueryPerformanceFactor: Optional[str]
    RegexRules: Optional[str]
    EnableDefaultUser: Optional[str]
    OnDemandBackup: Optional[str]
    RegionName: Optional[str]

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
            Endpoint=json_data.get("Endpoint"),
            Encryption=json_data.get("Encryption"),
            ServerCert=json_data.get("ServerCert"),
            By=json_data.get("By"),
            Value=json_data.get("Value"),
            LocalThroughputMeasurementRegion=json_data.get("LocalThroughputMeasurementRegion"),
            WriteOperationsPerSecond=json_data.get("WriteOperationsPerSecond"),
            ReadOperationsPerSecond=json_data.get("ReadOperationsPerSecond"),
            AverageItemSizeInBytes=json_data.get("AverageItemSizeInBytes"),
            Active=json_data.get("Active"),
            Interval=json_data.get("Interval"),
            TimeUTC=json_data.get("TimeUTC"),
            StorageType=json_data.get("StorageType"),
            StoragePath=json_data.get("StoragePath"),
            SourceIp=json_data.get("SourceIp"),
            PublicCertificatePEMString=json_data.get("PublicCertificatePEMString"),
            EnableTls=json_data.get("EnableTls"),
            Password=json_data.get("Password"),
            SaslUsername=json_data.get("SaslUsername"),
            SaslPassword=json_data.get("SaslPassword"),
            AlertName=json_data.get("AlertName"),
            AlertValue=json_data.get("AlertValue"),
            ModuleName=json_data.get("ModuleName"),
            ModuleParameters=json_data.get("ModuleParameters"),
            QueryPerformanceFactor=json_data.get("QueryPerformanceFactor"),
            RegexRules=json_data.get("RegexRules"),
            EnableDefaultUser=json_data.get("EnableDefaultUser"),
            OnDemandBackup=json_data.get("OnDemandBackup"),
            RegionName=json_data.get("RegionName"),
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


