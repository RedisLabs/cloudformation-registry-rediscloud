# Redis Cloud AWS CloudFormation Public Extensions 

[![Deploy Private Extension for DB](https://github.com/FlorinManaila/Redis-CloudFormationResourceType/actions/workflows/submit_private_extension_database.yml/badge.svg?branch=master)](https://github.com/github/docs/actions/workflows/submit_private_extension_database.yml)

[![Deploy Private Extension for Peering](https://github.com/FlorinManaila/Redis-CloudFormationResourceType/actions/workflows/submit_private_extension_peering.yml/badge.svg?branch=master)](https://github.com/github/docs/actions/workflows/submit_private_extension_peering.yml)

[![Deploy Private Extension for Subscription](https://github.com/FlorinManaila/Redis-CloudFormationResourceType/actions/workflows/submit_private_extension_subscription.yml/badge.svg?branch=master)](https://github.com/github/docs/actions/workflows/submit_private_extension_subscription.yml)


## About this project
### What is a CloudFormation Public Extension?
A CloudFormation Public Extension is typically a CloudFormation resource type developed by a third-party publisher, like Redis. Such an extension can allow AWS customers to integrate Redis-specific resources, which are only available over the Redis API, in their CloudFormation templates. 

The AWS CloudFormation registry serves as a centralized hub to discover, manage, and provision these extensions.

### What are the capabilities of Redis' extensions?
There are currently three Redis resource types that can be provisioned via CloudFormation. The resource types act as a wrapper around our API [1]. How resource types relate to the API can be seen in the diagram below.

![Diagram](resource_architecture_diagram.png)

### Bugs and feature requests
[...]

### CloudFormation examples
[...]

## Getting Started
### 0. Prerequisites
- Redis Cloud API keys are required to use CloudFormation Public Extensions. Please have your API Keys ready

### 1. Store your API keys in Secrets Manager
#### Automated way
- Find the *CreateSecrets.yml* in the root of this project.
- Run this CloudFormation template and replace the placeholders for secrets manually once the creation is done.
- The secret will be set up following this format:
``` 
SecretName: cfn/profile/{ProfileName}
SecretValue: {"PublicKey": "YourPublicKey", "PrivateKey": "YourPrivateKey"}
```

#### Alternative way
- If you desire a different naming convention for your secrets, feel free to either change the CloudFormation Template or create the secret in any other way. Please keep in mind to change the secrets name in the type-configuration in step 4. 

### 2. Activate the extension
- Activate the extension from the Extension Registry. This can we done in the CloudFormation UI but also programatically.

### 4. Setting up credentials to Redis API

- In the command below
   - Change the region parameter to the AWS region you required
   - Change  the key value information if you used a different secret name from Step 1
- Run the command in CloudShell or similar.

```
aws cloudformation set-type-configuration \
    --region eu-west-1 \
    --type-name "Redis::CloudFormation::ProSubscription" \
    --type RESOURCE \
    --configuration-alias default \
    --configuration '{"RedisAccess": {"xapikey": "{{resolve:secretsmanager:"Secret Name":SecretString:"Secret Key for x_api_key"}}", "xapisecretkey": "{{resolve:secretsmanager:"Secret Name":SecretString:"Secret Key for x_api_secret_key"}}"}}'
```

[1] https://api.redislabs.com/v1/swagger-ui/index.html#/



