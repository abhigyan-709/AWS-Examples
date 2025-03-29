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
            "Value" : "ProjectDevOpsDemoVPC"
        }
    ]
)
print(f"VPC with the id {vpc.id} is created")

# now we will create the public and private subnets
public_subnets = ec2_resource.create_subnet(VpcId = vpc.id, CidrBlock="10.0.1.0/24")
private_subnets = ec2_resource.create_subnet(VpcId = vpc.id, CidrBlock="10.0.2.0/24")

# create and attach the internet gatewat i.e IGW
igw = ec2_resource.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId = igw.id)
print(f"Internet Gateway with the id {igw.id} is created and attached to the vpc {vpc.id}")

# now we will create the route table
route_table = ec2_resource.create_route_table(VpcId = vpc.id)
route_table.create_route(DestinationCidrBlock="0.0.0.0/0", GatewayId=igw.id)
route_table.associate_with_subnet(SubnetId=public_subnets.id)
print(f"Route table with the id {route_table.id} is created and associated with the public subnet {public_subnets.id}")

# now we will create the security group and allow SSH and HTTP access
security_group = ec2_resource.create_security_group(
    GroupName = "ProjectDevOpsDemoSG",
    Description = "Security group for the VPC, for SSH and HTTP access",
    VpcId = vpc.id
)

security_group.authorize_ingress(
    IpPermissions=[
        {
            "IpProtocol" : "tcp",
            "FromPort" : 22,
            "ToPort" : 22,
            "IpRanges" : [
                {
                    "CidrIp" : "0.0.0.0/0"
                }
            ]
        },
        {
            "IpProtocol" : "tcp",
            "FromPort" : 80,
            "ToPort" : 80,
            "IpRanges" : [
                {
                    "CidrIp" : "0.0.0.0/0"
                }
            ]
        },
    ]
)

print(f"Security group with the id {security_group.id} is created and SSH and HTTP access is allowed")

# now we will launch the ec2 instance in the public subnet
ami_id = "ami-0c55b159cbfafe1f0" # this is the amazon linux 2 ami id
instance = ec2_resource.create_instances(
    ImageId = ami_id,
    InstanceType = "t2.micro",
    MaxCount = 1, 
    MinCount = 1, 
    KeyName = "ProjectDevOpsDemoKey",
    NetworkInterfaces = [
        {
            "SubnetId" : public_subnets.id,
            "DeviceIndex" : 0,
            "AssociatedPublicIpAddress" : True,
            "Groups" : [
                security_group.id
            ]
        }
    ],
    TagsSpecifications = [
        {
            "ResourceType" : "instance",
            "Tags" : [
                {
                    "Key" : "Name",
                    "Value" : "ProjectDevOpsDemoEC2Instance"
                }
            ]
        }
    ]
)

print(f"EC2 instance with the id {instance[0].id} is created and launched in the public subnet {public_subnets.id}")

"""
Explaination of the code: 
1. We started with the importing the boto3 module which is used for the interaction with the aws services.
2. Then we initialised the ec2_client and ec2_resource which are used for the further oprations for the vpc creation.
3. Then we defined our vpc_cidr block, which defines the range or under which IP range our VPC will be created
4. now we created the vpc using the create_vpc method and we wauted for the until the vpc is created or gets available
5. then we staretd defiining the private and public subnets using the create_subnet method
6. after that we created the internet gateway and attched to the above created VPC
7. then we created the route table and assoicated it with the public subnet
8. however the private subnet will be associated with the NAT Gateway
9. no we will create the security group and allowed the SSH and Http access for the ec2_instance, i.e. opend the port 22 and 80 
10. this is done by securitry_group.authorize_ingress method
11. and then we will create the ec2 instance in the public subnet using the create_instances method
12. we also need to consider the ami id which is the amazon linux 2 ami id, with the Instance type, minimum and maximum count, key name, network interfaces, and tags specifications 
13. and finally we printed the ec2 instance id, vpc id, igw id, route table id, security group id, and subnet ids
"""

