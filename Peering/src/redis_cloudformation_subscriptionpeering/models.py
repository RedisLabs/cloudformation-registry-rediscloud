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
    PeeringID: Optional[str]
    BaseUrl: Optional[str]
    SubscriptionID: Optional[str]
    Provider: Optional[str]
    Region: Optional[str]
    AwsAccountId: Optional[str]
    VpcId: Optional[str]
    VpcCidr: Optional[str]
    VpcCidrs: Optional[Sequence[str]]
    VpcProjectUid: Optional[str]
    VpcNetworkName: Optional[str]

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
            PeeringID=json_data.get("PeeringID"),
            BaseUrl=json_data.get("BaseUrl"),
            SubscriptionID=json_data.get("SubscriptionID"),
            Provider=json_data.get("Provider"),
            Region=json_data.get("Region"),
            AwsAccountId=json_data.get("AwsAccountId"),
            VpcId=json_data.get("VpcId"),
            VpcCidr=json_data.get("VpcCidr"),
            VpcCidrs=json_data.get("VpcCidrs"),
            VpcProjectUid=json_data.get("VpcProjectUid"),
            VpcNetworkName=json_data.get("VpcNetworkName"),
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


