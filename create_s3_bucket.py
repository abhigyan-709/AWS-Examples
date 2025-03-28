# here we will learn how we can create the AWS s3 bucket via AWS boto3 module via python

import boto3
import os

s3_client = boto3.client('s3')

# here you can provide the bucket name of your defined s3 bucket
bucket_name = "project-devops-demo-s3-bucket"