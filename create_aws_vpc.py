# to create the vpc throught the aws boto3 module make sure you have proper iam configurations or access to the aws resources

import boto3 

# initialize the aws clients
ec2_client = boto3.client('ec2')
ec2_resource = boto3.client('ec2')


# defind the vpc cidr block
vpc_cidr = "10.0.0.0/16"

# create the vpc
vpc = ec2_resource.create_vpc(CidrBlock = vpc_cidr)
vpc.wait_until_available()
vpc.create_tags(
    Tags = [
        {
            "Key" : "Name",
            "Value" : "DemoVPC"
        }
    ]
)
print(f"VPC with the id {vpc.id} is created")

# now we will create the public and private subnets
public_subnets = ""
private_subnets = ""

