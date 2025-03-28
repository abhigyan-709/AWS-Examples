# here we will learn how we can create the AWS s3 bucket via AWS boto3 module via python

import boto3

# initialize the s3 client 
s3_client = boto3.client('s3')

# Define the bucket name and region
# bucket name should be unique and they are in global namespaces
bucket_name = "project-devops-demo-s3-bucket"

# the region will be your default region i.e. we are using the ap-south-1
region = "ap-south-1"

# now we will define the bucket settings
bucket_config = {
    'locationConstraint' : region
}

# now we will create the s3 bucket 
response = s3_client.create_bucket(
    Bucket = bucket_name,
    CreateBucketConfoguration=bucket_config
)

print(f"Bucket {bucket_name} created successfully.")

# now we will set the ACL i.e. access control list, to keep our bucket secure
# here we are defining the bucket as the private bucket so no one other than authorised member will be able to acces the objects of the buckets

acl = "private"
s3_client.put_bucket_acl(Bucket=bucket_name, ACL=acl)

print(f"ACL '{acl}' is now set for the bucket {bucket_name}")

