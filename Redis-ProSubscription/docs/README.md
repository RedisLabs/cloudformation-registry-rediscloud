# Redis::CloudFormation::ProSubscription

CloudFormation template for Pro Subscription.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Redis::CloudFormation::ProSubscription",
    "Properties" : {
        "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
        "<a href="#subscriptionname" title="SubscriptionName">SubscriptionName</a>" : <i>String</i>,
        "<a href="#dryrun" title="DryRun">DryRun</a>" : <i>String</i>,
        "<a href="#deploymenttype" title="DeploymentType">DeploymentType</a>" : <i>String</i>,
        "<a href="#paymentmethod" title="PaymentMethod">PaymentMethod</a>" : <i>String</i>,
        "<a href="#paymentmethodid" title="PaymentMethodId">PaymentMethodId</a>" : <i>String</i>,
        "<a href="#memorystorage" title="MemoryStorage">MemoryStorage</a>" : <i>String</i>,
        "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>,
        "<a href="#cloudaccountid" title="CloudAccountId">CloudAccountId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#multipleavailabilityzones" title="MultipleAvailabilityZones">MultipleAvailabilityZones</a>" : <i>String</i>,
        "<a href="#preferredavailabilityzones" title="PreferredAvailabilityZones">PreferredAvailabilityZones</a>" : <i>String</i>,
        "<a href="#deploymentcidr" title="DeploymentCIDR">DeploymentCIDR</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#databasename" title="DatabaseName">DatabaseName</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#datasetsizeingb" title="DatasetSizeInGb">DatasetSizeInGb</a>" : <i>String</i>,
        "<a href="#supportossclusterapi" title="SupportOSSClusterApi">SupportOSSClusterApi</a>" : <i>String</i>,
        "<a href="#datapersistence" title="DataPersistence">DataPersistence</a>" : <i>String</i>,
        "<a href="#replication" title="Replication">Replication</a>" : <i>String</i>,
        "<a href="#by" title="By">By</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>String</i>,
        "<a href="#localthroughputmeasurementregion" title="LocalThroughputMeasurementRegion">LocalThroughputMeasurementRegion</a>" : <i>String</i>,
        "<a href="#writeoperationspersecond" title="WriteOperationsPerSecond">WriteOperationsPerSecond</a>" : <i>String</i>,
        "<a href="#readoperationspersecond" title="ReadOperationsPerSecond">ReadOperationsPerSecond</a>" : <i>String</i>,
        "<a href="#modulename" title="ModuleName">ModuleName</a>" : <i>String</i>,
        "<a href="#moduleparameters" title="ModuleParameters">ModuleParameters</a>" : <i>String</i>,
        "<a href="#quantity" title="Quantity">Quantity</a>" : <i>String</i>,
        "<a href="#averageitemsizeinbytes" title="AverageItemSizeInBytes">AverageItemSizeInBytes</a>" : <i>String</i>,
        "<a href="#respversion" title="RespVersion">RespVersion</a>" : <i>String</i>,
        "<a href="#queryperformancefactor" title="QueryPerformanceFactor">QueryPerformanceFactor</a>" : <i>String</i>,
        "<a href="#redisversion" title="RedisVersion">RedisVersion</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Redis::CloudFormation::ProSubscription
Properties:
    <a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
    <a href="#subscriptionname" title="SubscriptionName">SubscriptionName</a>: <i>String</i>
    <a href="#dryrun" title="DryRun">DryRun</a>: <i>String</i>
    <a href="#deploymenttype" title="DeploymentType">DeploymentType</a>: <i>String</i>
    <a href="#paymentmethod" title="PaymentMethod">PaymentMethod</a>: <i>String</i>
    <a href="#paymentmethodid" title="PaymentMethodId">PaymentMethodId</a>: <i>String</i>
    <a href="#memorystorage" title="MemoryStorage">MemoryStorage</a>: <i>String</i>
    <a href="#provider" title="Provider">Provider</a>: <i>String</i>
    <a href="#cloudaccountid" title="CloudAccountId">CloudAccountId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#multipleavailabilityzones" title="MultipleAvailabilityZones">MultipleAvailabilityZones</a>: <i>String</i>
    <a href="#preferredavailabilityzones" title="PreferredAvailabilityZones">PreferredAvailabilityZones</a>: <i>String</i>
    <a href="#deploymentcidr" title="DeploymentCIDR">DeploymentCIDR</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#databasename" title="DatabaseName">DatabaseName</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#datasetsizeingb" title="DatasetSizeInGb">DatasetSizeInGb</a>: <i>String</i>
    <a href="#supportossclusterapi" title="SupportOSSClusterApi">SupportOSSClusterApi</a>: <i>String</i>
    <a href="#datapersistence" title="DataPersistence">DataPersistence</a>: <i>String</i>
    <a href="#replication" title="Replication">Replication</a>: <i>String</i>
    <a href="#by" title="By">By</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>String</i>
    <a href="#localthroughputmeasurementregion" title="LocalThroughputMeasurementRegion">LocalThroughputMeasurementRegion</a>: <i>String</i>
    <a href="#writeoperationspersecond" title="WriteOperationsPerSecond">WriteOperationsPerSecond</a>: <i>String</i>
    <a href="#readoperationspersecond" title="ReadOperationsPerSecond">ReadOperationsPerSecond</a>: <i>String</i>
    <a href="#modulename" title="ModuleName">ModuleName</a>: <i>String</i>
    <a href="#moduleparameters" title="ModuleParameters">ModuleParameters</a>: <i>String</i>
    <a href="#quantity" title="Quantity">Quantity</a>: <i>String</i>
    <a href="#averageitemsizeinbytes" title="AverageItemSizeInBytes">AverageItemSizeInBytes</a>: <i>String</i>
    <a href="#respversion" title="RespVersion">RespVersion</a>: <i>String</i>
    <a href="#queryperformancefactor" title="QueryPerformanceFactor">QueryPerformanceFactor</a>: <i>String</i>
    <a href="#redisversion" title="RedisVersion">RedisVersion</a>: <i>String</i>
</pre>

## Properties

#### BaseUrl

The Base URL where the API calls are sent.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### SubscriptionName

[Optional]. Subscription name. Example: My new subscription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DryRun

[Optional]. When 'false': Creates a deployment plan and deploys it (creating any resources required by the plan). When 'true': creates a read-only deployment plan without any resource creation. Example: false. Default: 'false'.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### DeploymentType

[Optional]. Creates a single region subscription. Example: single-region

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### PaymentMethod

[Optional]. Payment method for the requested subscription. If credit card is specified, the payment method Id must be defined. Default: 'credit-card'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### PaymentMethodId

[Optional]. A valid payment method that was pre-defined in the current account. This value is Optional if 'paymentMethod' is 'marketplace', but Required for all other account types.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### MemoryStorage

[Optional]. Optional. Memory storage preference: either 'ram' or a combination of 'ram-and-flash'. Example: ram. Default: 'ram'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Provider

[Optional]. Cloud provider. Example: AWS. Default: 'AWS'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### CloudAccountId

[Optional]. Cloud account identifier. Default: Redis internal cloud account (using Cloud Account Id = 1 implies using Redis internal cloud account). Note that a GCP subscription can be created only with Redis internal cloud account.Example: 1. Default: 1

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Region

[Required]. Deployment region as defined by cloud provider. Example: us-east-1

_Required_: Yes

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### MultipleAvailabilityZones

[Optional]. Support deployment on multiple availability zones within the selected region. Example: false. Default: 'false'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### PreferredAvailabilityZones

[Optional]. Availability zones deployment preferences (for the selected provider & region). If 'multipleAvailabilityZones' is set to 'true', you must specify three availability zones. In AWS Redis internal cloud account, set the zone IDs (for example: ['use-az2', 'use-az3', 'use-az5'])

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### DeploymentCIDR

[Required]. Deployment CIDR mask. Example: 10.0.0.0/24. Default: If using Redis internal cloud account, 192.168.0.0/24

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### VpcId

[Optional]. Either an existing VPC Id (already exists in the specific region) or create a new VPC (if no VPC is specified). VPC Identifier must be in a valid format (for example: 'vpc-0125be68a4625884ad') and existing within the hosting account

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### DatabaseName

[Required]. Database name (Database name must be up to 40 characters long, include only letters, digits, or hyphen ('-'), start with a letter, and end with a letter or digit). Example: Redis-database-example

_Required_: Yes

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Protocol

[Optional]. Database protocol: either 'redis' or 'memcached'. Default: 'redis'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### DatasetSizeInGb

[Optional]. The maximum amount of data in the dataset for this specific database is in GB. You can not set both datasetSizeInGb and totalMemoryInGb. if 'replication' is true, the database's total memory will be twice as large as the datasetSizeInGb.if 'replication' is false, the database's total memory of the database will be the datasetSizeInGb value.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### SupportOSSClusterApi

[Optional]. Support Redis open-source (OSS) Cluster API. Default: 'false'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### DataPersistence

[Optional]. Rate of database data persistence (in persistent storage). Example: none. Default: 'none'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Replication

[Optional]. Databases replication. Default: 'true'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### By

[Required to enable throughputMeasurement]. Throughput measurement method. Either 'number-of-shards' or 'operations-per-second'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Value

[Required to enable throughputMeasurement]. Throughput value (as applies to selected measurement method). Example: 10000

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### LocalThroughputMeasurementRegion

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### WriteOperationsPerSecond

[Optional]. Example: 1000. Default: 1000 ops/sec

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ReadOperationsPerSecond

[Optional]. Example: 1000. Default: 1000 ops/sec

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ModuleName

[Required only to enable modules]. Redis module Id

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ModuleParameters

[Optional]. Redis database module parameters (name and value), as relevant to the specific module (see modules parameters specification). Example: OrderedMap {}

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Quantity

[Optional]. Number of databases (of this type) that will be created. Default: 1

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### AverageItemSizeInBytes

[Optional]. Relevant only to ram-and-flash clusters. Estimated average size (measured in bytes) of the items stored in the database. Default: 1000

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### RespVersion

[Optional]. RESP version must be compatible with Redis version. Example: resp3. Allowed values: resp2/resp3.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### QueryPerformanceFactor

[Optional]. Query performance factor. Example: 2x

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### RedisVersion

[Optional]. If specified, the redisVersion defines the Redis version of the databases in the subscription. If omitted, the Redis version will be the default (available in 'GET /subscriptions/redis-versions'). Example: 7.2. Default = 'default'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the SubscriptionID.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### SubscriptionID

Subscription ID. Populated with value within the handlers.py.

