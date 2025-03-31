# here to create the VPC via cli we will perform the following steps

# we will create the vpc

# 1. we will create and IGW
# 2. the we will attach the IGW 

# 3. we will create the subnets 
# 4. then we wil attach the subnets 

# 5. we will add a route for the route table for the Internet gateway

# creating the vpc via bash and shell scripting

VPC_ID=$(aws ec2 create-vpc --cidr-block "171.1.0.0/16" \
--tag-specifications 'ResourceType=vpc,Tags=[{Key=Name, Value=my-vpc-3}]' \
--region ap-south-1 \
--output text
)

echo $VPC_ID