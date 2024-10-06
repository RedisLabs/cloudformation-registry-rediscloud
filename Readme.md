## External Readme:
This is a draft for the external readme.

# Redis AWS CloudFormation Public Extensions 
Code Health -> Link to automated tests  
Contract Testing -> Link to automated tests

Use AWS CloudFormation to manage [Redis](https://redis.io/) Cloud Resources


## Getting Started
## Redis Cloud API Key Management
Redis Cloud API keys are required for both CloudFormation Public Extensions. These API keys should be stored in AWS Secrets Manager and used by CloudFormation Public Extension Handlers as an input by the use of a type-configuration.

### 1. Configure your MongoDB Atlas API Keys 
This happens on the Redis cloud side 

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



