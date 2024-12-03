# Redis::Cloud::Peering

CloudFormation template for Subscription Peering.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Redis::Cloud::Peering",
    "Properties" : {
        "<a href="#baseurl" title="BaseUrl">BaseUrl</a>" : <i>String</i>,
        "<a href="#subscriptionid" title="SubscriptionID">SubscriptionID</a>" : <i>String</i>,
        "<a href="#provider" title="Provider">Provider</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpccidr" title="VpcCidr">VpcCidr</a>" : <i>String</i>,
        "<a href="#vpccidrs" title="VpcCidrs">VpcCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpcprojectuid" title="VpcProjectUid">VpcProjectUid</a>" : <i>String</i>,
        "<a href="#vpcnetworkname" title="VpcNetworkName">VpcNetworkName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Redis::Cloud::Peering
Properties:
    <a href="#baseurl" title="BaseUrl">BaseUrl</a>: <i>String</i>
    <a href="#subscriptionid" title="SubscriptionID">SubscriptionID</a>: <i>String</i>
    <a href="#provider" title="Provider">Provider</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpccidr" title="VpcCidr">VpcCidr</a>: <i>String</i>
    <a href="#vpccidrs" title="VpcCidrs">VpcCidrs</a>: <i>
      - String</i>
    <a href="#vpcprojectuid" title="VpcProjectUid">VpcProjectUid</a>: <i>String</i>
    <a href="#vpcnetworkname" title="VpcNetworkName">VpcNetworkName</a>: <i>String</i>
</pre>

## Properties

#### BaseUrl

[Required]. The Base URL where the API calls are sent.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### SubscriptionID

[Required]. The ID of the Pro Subscription that will make a peering connection. Example: 163199

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

[Optional]. Cloud provider. Example: AWS. Default: 'AWS'

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### Region

[Required for AWS]. Deployment region as defined by cloud provider. Example: us-east-1

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### AwsAccountId

[Required for AWS]. AWS Account uid. Example: 178919255286

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### VpcId

[Required for AWS]. VPC uid. Example: vpc-00e1a8cdca658ce8c

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### VpcCidr

[Optional]. VPC CIDR. Example:  '10.10.10.0/24'

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcCidrs

[Optional]. List of VPC CIDRs. Example: '[10.10.10.0/24,10.10.20.0/24]'

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcProjectUid

[Required for GCP]. VPC project uid.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### VpcNetworkName

[Required for GCP]. VPC network name.

_Required_: No

_Type_: String

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the PeeringID.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### PeeringID

The ID of the Subscription Peering.

