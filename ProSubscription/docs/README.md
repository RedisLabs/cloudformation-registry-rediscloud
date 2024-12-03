# Redis::Cloud::Subscription

CloudFormation template for Pro Subscription.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Redis::Cloud::Subscription",
    "Properties" : {
        "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
        "<a href="#subscriptionname" title="SubscriptionName">SubscriptionName</a>" : <i>String</i>,
        "<a href="#dryrun" title="DryRun">DryRun</a>" : <i>String</i>,
        "<a href="#deploymenttype" title="DeploymentType">DeploymentType</a>" : <i>String</i>,
        "<a href="#paymentmethod" title="PaymentMethod">PaymentMethod</a>" : <i>String</i>,
        "<a href="#paymentmethodid" title="PaymentMethodId">PaymentMethodId</a>" : <i>String</i>,
        "<a href="#memorystorage" title="MemoryStorage">MemoryStorage</a>" : <i>String</i>,
        "<a href="#cloudproviders" title="CloudProviders">CloudProviders</a>" : <i>String</i>,
        "<a href="#redisversion" title="RedisVersion">RedisVersion</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Redis::Cloud::Subscription
Properties:
    <a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
    <a href="#subscriptionname" title="SubscriptionName">SubscriptionName</a>: <i>String</i>
    <a href="#dryrun" title="DryRun">DryRun</a>: <i>String</i>
    <a href="#deploymenttype" title="DeploymentType">DeploymentType</a>: <i>String</i>
    <a href="#paymentmethod" title="PaymentMethod">PaymentMethod</a>: <i>String</i>
    <a href="#paymentmethodid" title="PaymentMethodId">PaymentMethodId</a>: <i>String</i>
    <a href="#memorystorage" title="MemoryStorage">MemoryStorage</a>: <i>String</i>
    <a href="#cloudproviders" title="CloudProviders">CloudProviders</a>: <i>String</i>
    <a href="#redisversion" title="RedisVersion">RedisVersion</a>: <i>String</i>
</pre>

## Properties

#### BaseUrl

[Required]. The Base URL where the API calls are sent.

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

#### CloudProviders

[Required as JSON]. Cloud hosting & networking details. Example: [{"regions": [{"region": "us-east-1", "networking": {}}]}]

_Required_: Yes

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

