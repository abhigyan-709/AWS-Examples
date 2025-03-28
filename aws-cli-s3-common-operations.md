# here we will learn how to create the s3 bucket through the aws CLI

## you can download the aws cli, by refering to the Readme.md file

## what is s3?
> s3 is the managed global service 
> it is used to store files like, images, pdfs or anything which is relevant to the use cases
> we define policies and other ACL(access control list) which is used to control and give access to the particular service
> we use it to store the object and you can refer it to the file storage from AWS
> here you can store the objects ranging from 0 bytes to the 5 TB and this is the single file
> s3 provides the facility to store the unlimited object
> s3 have two major component
1. AWS S3 Object - key, value pair of the object
    a. key - contians the key of the object i.e the ID of the object 
    b. value - contains the data itself
    c. version ID - when the versioning is enabled in the s3 object, it helps us to track the changes to the objects
    d. metaData - any additional information that gets attached to the object

2. AWS S3 Bucket - the bucket where there objects are stored