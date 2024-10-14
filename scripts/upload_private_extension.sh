#!/bin/bash

## Check if the correct number of arguments is provided
#if [ "$#" -ne 1 ]; then
#    echo "Usage: $0 <Name_Of_Subfolder>"
#    exit 1
#fi
#
#echo $1 #Is the name of the subfolder containing the exenstion's code 
folderName='ProSubscription'
echo 'SAY SOMETHING'

# Configure AWS CLI with environment variables
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set default.region $AWS_REGION

# List S3 buckets
cd $folderName
# cfn generate
# cfn submit

typeNamePrefix='Redis::CloudFormation::'
typeName="${typeNamePrefix}${folderName}"
echo $typeName

VERSION_ID=$(aws cloudformation list-type-versions --type RESOURCE --type-name $typeName | jq -r '.TypeVersionSummaries | sort_by(.TimeCreated) | reverse | .[0].VersionId')
echo $VERSION_ID
aws cloudformation set-type-default-version --type RESOURCE --type-name $typeName --version-id $VERSION_ID
