## IMPORTANT:
Before this code is shared with anyone else we need to clear the commit history since older commits contain secrets!

## Setting up credentials to Redis API
Simply run this command in the CloudShell or similar. Change the region and key value information first tho.

aws cloudformation set-type-configuration \
    --region eu-west-1 \
    --type-name "Redis::CloudFormation::ProSubscription" \
    --type RESOURCE \
    --configuration-alias default \
    --configuration '{"RedisAccess": {"xapikey": "{{resolve:secretsmanager:"Secret Name":SecretString:"Secret Key for x_api_key"}}", "xapisecretkey": "{{resolve:secretsmanager:"Secret Name":SecretString:"Secret Key for x_api_secret_key"}}"}}'

## USEFULL COMMANDS:
After updating the files, in order to use the latest version, please follow the steps bellow:
1. cfn generate - validate schema and generates files for resource type
2. cfn submit - publish the latest version of your code to private registry
3. set the default value for the resource type, the latest one:
aws cloudformation set-type-default-version \
    --type RESOURCE \
    --type-name Redis::CloudFormation::ProSubscription \
    --version-id 00000071
4. Use the CreateProSubscription.yml file to create a new stack

! In order to see all the versions for the resource type use this command:
aws cloudformation list-type-versions --type RESOURCE --type-name "Redis::CloudFormation::ProSubscription"

!! If the maximum number of versions has been reached (50), use the following command to deregister the old ones, one by one:
aws cloudformation deregister-type --type RESOURCE --type-name "Redis::CloudFormation::ProSubscription" --version-id 00000011

!!! If by any means, someone wants to delete the entire private registry, first deregister all the versions not default, then deregister the default one by running:
aws cloudformation deregister-type --type RESOURCE --type-name "Redis::CloudFormation::ProSubscription"

# Redis::CloudFormation::ProSubscription

Congratulations on starting development! Next steps:


1. Write the JSON schema describing your resource, `redis-cloudformation-prosubscription.json`
2. Implement your resource handlers in `redis_cloudformation_prosubscription/handlers.py`

> Don't modify `models.py` by hand, any modifications will be overwritten when the `generate` or `package` commands are run.

Implement CloudFormation resource here. Each function must always return a ProgressEvent.

```python
ProgressEvent(
    # Required
    # Must be one of OperationStatus.IN_PROGRESS, OperationStatus.FAILED, OperationStatus.SUCCESS
    status=OperationStatus.IN_PROGRESS,
    # Required on SUCCESS (except for LIST where resourceModels is required)
    # The current resource model after the operation; instance of ResourceModel class
    resourceModel=model,
    resourceModels=None,
    # Required on FAILED
    # Customer-facing message, displayed in e.g. CloudFormation stack events
    message="",
    # Required on FAILED: a HandlerErrorCode
    errorCode=HandlerErrorCode.InternalFailure,
    # Optional
    # Use to store any state between re-invocation via IN_PROGRESS
    callbackContext={},
    # Required on IN_PROGRESS
    # The number of seconds to delay before re-invocation
    callbackDelaySeconds=0,
)
```

Failures can be passed back to CloudFormation by either raising an exception from `cloudformation_cli_python_lib.exceptions`, or setting the ProgressEvent's `status` to `OperationStatus.FAILED` and `errorCode` to one of `cloudformation_cli_python_lib.HandlerErrorCode`. There is a static helper function, `ProgressEvent.failed`, for this common case.

## What's with the type hints?

We hope they'll be useful for getting started quicker with an IDE that support type hints. Type hints are optional - if your code doesn't use them, it will still work.

## References for the future

1. Deploy across regions with StackSets: https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension-stacksets.html
2. How to run contract tests
- https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html
Basically:
- Start Docker
- sam local start-lambda
- cfn test
