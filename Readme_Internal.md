# Internal Readme:
This is a draft for the internal readme. It doesn't contain seneitive information but rather information about developing CloudFormation Public Extensions.

TODOs:
- Before this code is shared with anyone else we need to clear the commit history since older commits contain secrets!
- Work on a concept for using multiple profiles
- foldernames should follow a naming convention (lower case all e.g.)
- Write a proper gitignore

# Redis AWS CloudFormation Public Extensions 
Code Health -> Link to automated tests  
Contract Testing -> Link to automated tests

Use AWS CloudFormation to manage [Redis](https://redis.io/) Cloud Resources


## Credential Management

### 2. Configure your Profile
In the root of this project you will find the *CreateSecrets.yml*. This is a CloudFormation template that set up AWS SecretsManager in the region of your choice and creates two placeholders for secrets. </br>
Please run this CloudFormation template and replace the placeholders for secrets manually once the creation is done.


The secret will be set up following this format: (???)
```
SecretName: cfn/profile/{ProfileName}
SecretValue: {"PublicKey": "YourPublicKey", "PrivateKey": "YourPrivateKey"}
```

### 3. Activate the extension

xxx

### 4. Setting up credentials to Redis API
Change the region and key value information in the command below. Simply run this command in CloudShell or similar.

```
aws cloudformation set-type-configuration \
    --region eu-west-1 \
    --type-name "Redis::CloudFormation::ProSubscription" \
    --type RESOURCE \
    --configuration-alias default \
    --configuration '{"RedisAccess": {"xapikey": "{{resolve:secretsmanager:"Secret Name":SecretString:"Secret Key for x_api_key"}}", "xapisecretkey": "{{resolve:secretsmanager:"Secret Name":SecretString:"Secret Key for x_api_secret_key"}}"}}'
```
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
