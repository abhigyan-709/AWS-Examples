#!/bin/bash

# we will list the buckets in the s3
aws s3api list-buckets --query "Buckets[].Name" --output json