#!/bin/bash

# $1 is the first parameter passed into this script when called 
folderName=$1

# Configure AWS CLI with environment variables
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set default.region $AWS_REGION

# Generate & Submit project
cd $folderName

echo 'Generate Project:'
echo $folderName
cfn generate

echo 'Submit Project'
cfn submit

# Concatenate the name of the of the extension as it is supposed to be uploaded
typeNamePrefix='Redis::CloudFormation::'
typeName="${typeNamePrefix}${folderName}"
echo 'Name of Extension'
echo $typeName

# Find the newest extension id and set to local variable
VERSION_ID=$(aws cloudformation list-type-versions --type RESOURCE --type-name $typeName | jq -r '.TypeVersionSummaries | sort_by(.TimeCreated) | reverse | .[0].VersionId')
echo 'Newest VERSION_ID'
echo $VERSION_ID

# If VERSION_ID is unset or empty, set it to '00000001'
if [ -z "$VERSION_ID" ]; then
    VERSION_ID="00000001"
fi

# Set the newest version as the default version
aws cloudformation set-type-default-version --type RESOURCE --type-name $typeName --version-id $VERSION_ID
