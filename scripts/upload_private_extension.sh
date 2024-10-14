#!/bin/bash

# Bash script to list AWS S3 buckets
# Accepts AWS Access Key, Secret Key, and region as input arguments

# Ensure the script is run as root/sudo if awscli is not installed
if ! command -v aws &> /dev/null
then
    echo "AWS CLI not found. Installing..."
    sudo apt update
    sudo apt install -y awscli
fi

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <Name_Of_Subfolder>"
    exit 1
fi

# Assign command-line arguments to variables
Name_Of_Subfolder=$1

echo $1
echo $Name_Of_Subfolder

# Configure AWS CLI with environment variables
aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set default.region $AWS_REGION

# List S3 buckets
echo "Listing S3 buckets..."
aws s3 ls

# End of script
