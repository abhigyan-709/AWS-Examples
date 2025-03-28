# this is the code base for the examples of AWS and its related services for DevOps

## this is the open source repository and the keys & other secrets are used in this repository,
## has been already removed

# method to push the code

```bash
# command to check the configuration in the global namespace for the github
git config --global --list

# initialize the git repo with empty 
git init

touch Readme.MD
git add .

git commit -m "first commit"

git branch -M main
```

### now go to the github.com and from your profile create your new repo with your choice
### and now we will connect this git repo from the local computer and terminal
```bash 
# add it with the remote branch
git remote add origin git@github.com:abhigyan-709/AWS-Examples.git

# push the code to the main, or publish the repo
git push -u origin main
```

### now we will install aws cli for the seamless interaction with aws
### you can download it from AWS documentation and then you can set it up with IAM user, or with root user as well

```bash
# it will ask for the key, secret and default region that you have generated from your IAM user
# as for practice you can provide the admin access to the the IAM user that you have created.
aws configure
AWS Access Key ID: your-access-key-id 
AWS Secret Access Key: your-secret-acces-key 
Default region name: ap-south-1 i.e mumbai 
Default output format: hit enter as with no default output
```


## if you will follow the below table of contents, you will be able to understand the AWS concepts more easily 
Now you can visit the table of contents Mark down file for the best experience

