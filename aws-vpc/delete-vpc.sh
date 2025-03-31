# here we will delete the vpc in the same way as we are doing in the AWS CLI

DELETE_VPC=$(
    awdaws ec2 delete-vpc --vpc-id vpc-010d96e68e89ec4e9
)

echo "VPC is deleted"
echo $DELETE_VPC

# thers is another way in which we can assign the vpc id via cli as an argument when we are going to run it as the bash shel
