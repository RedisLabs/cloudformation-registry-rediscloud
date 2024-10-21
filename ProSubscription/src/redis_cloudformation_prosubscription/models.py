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
    SubscriptionID: Optional[str]
    BaseUrl: Optional[str]
    SubscriptionName: Optional[str]
    DryRun: Optional[str]
    DeploymentType: Optional[str]
    PaymentMethod: Optional[str]
    PaymentMethodId: Optional[str]
    MemoryStorage: Optional[str]
    Provider: Optional[str]
    CloudAccountId: Optional[str]
    Region: Optional[str]
    MultipleAvailabilityZones: Optional[str]
    PreferredAvailabilityZones: Optional[str]
    DeploymentCIDR: Optional[str]
    VpcId: Optional[str]
    RedisVersion: Optional[str]

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
            SubscriptionID=json_data.get("SubscriptionID"),
            BaseUrl=json_data.get("BaseUrl"),
            SubscriptionName=json_data.get("SubscriptionName"),
            DryRun=json_data.get("DryRun"),
            DeploymentType=json_data.get("DeploymentType"),
            PaymentMethod=json_data.get("PaymentMethod"),
            PaymentMethodId=json_data.get("PaymentMethodId"),
            MemoryStorage=json_data.get("MemoryStorage"),
            Provider=json_data.get("Provider"),
            CloudAccountId=json_data.get("CloudAccountId"),
            Region=json_data.get("Region"),
            MultipleAvailabilityZones=json_data.get("MultipleAvailabilityZones"),
            PreferredAvailabilityZones=json_data.get("PreferredAvailabilityZones"),
            DeploymentCIDR=json_data.get("DeploymentCIDR"),
            VpcId=json_data.get("VpcId"),
            RedisVersion=json_data.get("RedisVersion"),
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


