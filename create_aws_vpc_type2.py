from re import M
from tkinter import N, Image
import boto3
import time

# important: explain the difference between boto3.client and boto3.resource

# init aws clients
ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

# declare the cidr block range for the vpc
vpc_cidr = "10.0.0.0/16"

# create the vpc
vpc = ec2_resource.create_vpc(CidrBlock=vpc_cidr)
vpc.wait_until_available()
vpc.create_tags(Tags=[{"Key" : "Name", "Value" : "ProjectDevOpsDemoVPC"}])
print(f"VPC with the id {vpc.id} is created")

# now we will create the public and private subnets
public_subnet = ec2_resource.create_subnet(
    VpcId = vpc.id, 
    CidrBlock="10.0.1.0/24", 
    MapPublicIpOnLaunch=True
)
private_subnet = ec2_resource.create_subnet(
    VpcId = vpc.id,
    CidrBlock="10.0.2.0/24"
)

print(f"Public subnet with the id {public_subnet.id} is created")
print(f"Private subnet with the id {private_subnet.id} is created")

# now we will create and attch the internet gateway i.e IGW
igw = ec2_resource.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=igw.id)
print(f"Internet Gateway with the id {igw.id} is created and attached to the vpc {vpc.id}")

# now we will create the public route table and associate with the public subnet
public_rt = ec2_resource.create_route_table(VpcId=vpc.id)
public_rt.create_route(DestinationCidrBlock = "0.0.0.0/0", GatewayId=igw.id)
public_rt.associate_with_subnet(SubnetId=public_subnet.id)
print(f"Public Route table with the id {public_rt.id} is created and associated with the public subnet {public_subnet.id}")


# important: explain the differece between nat gateway and nat instance
# important: explain the difference between public and private subnets
# important: explain the difference between igw and nat gateway
# important: explain the difference between public and private route tables

# now we will allocate the elastic ip for the NAT gateway 

eip = ec2_client.allocate_address(Domain="vpc")
print(f"Elastic IP with the id {eip['AllocationId']} is created")

# now we will create the nat gateway for the private subnet
nat_gw = ec2_client.create_nat_gateway(
    SubneyId = private_subnet.id,
    AllocationId = eip["AllocationId"],
)

nat_gw_id = nat_gw['NatGateway']['NatGatewayId']
print(f"NAT Gateway with the id {nat_gw_id} is created and associated with the private subnet {private_subnet.id}")

# we will wait for the nat gateway to be available
time.sleep(20) # allow 20 seconds for the NAT Gatewat to initialize

# now we will create the private route table and associate with the private subnet
private_rt = ec2_resource.create_route_table(VpcId=vpc.id)
private_rt.create_route(DestinationCidrBlock = "0.0.0.0/0", NatGatewayId=nat_gw_id)
private_rt.associate_with_subnet(SubnetId=private_subnet.id)
print(f"Private Route table with the id {private_rt.id} is created and associated with the private subnet {private_subnet.id}")

# now we will create the security group and allow ssh and http access
security_group = ec2_resource.create_security_group(
    GroupName = "ProjectDevOpsDemoSG",
    Description = "Security group for the VPC, for SSH and HTTP access",
    VpcId = vpc.id
)

security_group.authorize_ingress(
    IpPermissions=[
        {"IpProtocol" : "tcp", "FromPort" : 22, "ToPort": 22, "IpRanges" : [{"CidrIp": "0.0.0.0/0"}]},
        {"IpProtocol" : "tcp", "FromPort" : 80, "ToPort": 80, "IpRanges" : [{"CidrIp": "0.0.0.0/0"}]},
    ]
)
print(f"Security group with the id {security_group.id} is created and SSH and HTTP access is allowed")

# now will launch the ec2 instance in the public subnet
ami_id = "ami-0c55b159cbfafe1f0" # amazon linux 2
public_instance = ec2_resource.create_instances(
    ImageId=ami_id,
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1,
    KeyName="ProjectDevOpsDemoKeyPair",
    NetworkInterfaces=[
        {
            "SubnetId": public_subnet.id,
            "DeviceIndex": 0,
            "AssociatePublicIpAddress": True, # true as this is the public subnet
            "Groups": [
                security_group.id
            ]
        }
    ],
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "ProjectDevOpsDemoPublicInstance"
                }
            ]
        }
    ]
)
print(f"Public EC2 instance with the id {public_instance[0].id} is created in the public subnet {public_subnet.id}")

# now will launch the ec2 instance in the private subnet, so we will not have any public ip
private_instance = ec2_resource.create_instances(
    ImageId=ami_id,
    InstanceType="t2.micro",
    MaxCount=1,
    MinCount=1,
    KeyName="ProjectDevOpsDemoKeyPair",
    NetworkInterfaces=[
        {
            "SubnetId": private_subnet.id,
            "DeviceIndex": 0,
            "AssociatePublicIpAddress": False, # false as this is the private subnet
            "Groups": [
                security_group.id
            ]
        }
    ],
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "ProjectDevOpsDemoPrivateInstance"
                }
            ]
        }
    ]
)

print(f"Private EC2 instance with the id {private_instance[0].id} is created in the private subnet {private_subnet.id}")

