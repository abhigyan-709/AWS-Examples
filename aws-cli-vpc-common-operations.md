# here we will see the command aws cli operations over AWS VPC

# below is the command to create the vpc via AWS CLI

```bash 
aws ec2 create-vpc --cidr-block "172.1.0.0/16" \
--tag-specifications 'ResourceType=vpc,Tags=[{Key=Name, Value=my-vpc-3}]' \
--region ap-south-1 \
--output text
```


# below is the command to delete the VPC 
```bash
aws ec2 delete-vpc --vpc-id <your-vpc-id>
aws ec2 delete-vpc --vpc-id vpc-010d96e68e89ec4e9
```
