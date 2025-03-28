# here we will learn how to create the s3 bucket through the aws CLI

## you can download the aws cli, by refering to the Readme.md file

> ## what is s3?
> ### s3 is the managed global service 
>
>  - it is used to store files like, images, pdfs or anything which is relevant to the use cases
>  - we define policies and other ACL(access control list) which is used to control and give access to the particular service
>  - we use it to store the object and you can refer it to the file storage from AWS
>  - here you can store the objects ranging from 0 bytes to the 5 TB and this is the single file
>  - s3 provides the facility to store the unlimited object

#### s3 have two major components
1. AWS S3 Object - key, value pair of the object
    - key: contians the key of the object i.e the ID of the object 
    - value: contains the data itself
    - version ID: when the versioning is enabled in the s3 object, it helps us to track the changes to the objects
    - metaData: any additional information that gets attached to the object

2. AWS S3 Bucket - the bucket where there objects are stored
    - s3 bucket will have the storage class, to what type of storage we could use for our data access
    - s3 bucket also consists of the the universal namespace and the name will be unique in the aws

### AWS S3 Cli commands

1. List the s3 buckets in the configured region
```bash
aws s3 ls
```

> note: the commands given here will only work, if you have configured the AWS CLI in your local system, you can look over to the Readme.md file to know how to configure the AWS CLI in your local system either its ad Mac or Windows or Linux

- you can always use the aws cli command reference from the AWS official documentation - [Command Line referecne](https://docs.aws.amazon.com/cli/latest/reference/)

2. one more thing you can configure in your system which will make your work more easier is to set the auto prompt, so that if you don't know the command, you can go ahead and see the commands in your cli as by pressing enter
```bash
# configure these commands in your terminal
AWS_CLI_AUTO_PROMPT = on-partial
export AWS_CLI_AUTO_PROMPT
env | grep AWS_CLI # check if it get configured or not

# now whenever you wil write some commands and hit enter it wil show you the suggested commands like and interactive IDEs
aws s3 <press-enter>
```

3. Now we will see how we can create the bucket in the AWS CLI
```bash
there is always a suggestion to create the aws s3 bucket through the AWS S3 Boto3 module of python or AWS CDK
```

4. Uploading the file from AWS CLI to the aws s3 bucket
```bash
aws s3 cp /path/of/local/file.ext s3://<your-bucket-name>/folder/<file-name>
```

5. In the same way you can use the other commands like rm (remove command, you can add -recursive, and it will remove all ojects inside the bucket recursively)
```bash
aws s3 rm s3://your-bucket/ --recursive
```

 6. Removing the bucket if its empty 
 ```bash 
 aws s3 rb s3://bucket-name # make sure the bucke is empty otherwise it will throw and error
 ```

7. You can also use the aws s3api for the further interaction with the AWS CLI S3 operations
```bash
aws s3api and press enter and you can see a lot more options by auto prompter

aws s3api create-bucket --bucket demo-project-devops-s3 --region us-east-1
# more options are there to create the aws s3 bucket from the aws cli
```

8. You can use the aws s3api also to perform more advance actions and it gives you the output in the json format


