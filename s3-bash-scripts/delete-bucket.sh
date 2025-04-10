#!/bin/bash
# here we will delete the bucket with the specified name

if [ -z "$1" ]; then
    echo "Please provide a bucket name, i.e ./bucket <my-unique-bucket-name>"
    exit 1
fi
# we will delete the bucket with the specified name
aws s3api delete-bucket --bucket $1 --region us-east-1

# the following command deletes an object from the bucket 
aws s3api delete-objects --bucket my-bucket --delete file://delete.json

