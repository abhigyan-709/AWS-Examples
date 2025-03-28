#!/bin/bash

# we will take the user input for the creating the bucket 
# check if at least one argument is provided or not
# here we will check for the bucket name

if [ -z "$1" ]; then
    echo "Please provide a bucket name, i.e ./bucket <my-unique-bucket-name>"
    exit 1
fi

# however this command will fail as we have not provided the region which is commented out
# aws s3api create-bucket --bucket $1

# now will will create the bucket in a specific region with the --region flag
aws s3api create-bucket --bucket $1 --region us-east-1

