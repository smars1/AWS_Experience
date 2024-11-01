# AWS EXPERIENCE

## Module de awscli just in global env
```powershell
python.exe -m pip install awscli
```

## AWS SETTINGS COMMAND
```powershell
aws configure

# [OUTPUT]: 
#### Terminal-Console

AWS ACCES KEY ID [************EDIT]:
AWS SECRET ACCES KEY [************EDIT]:
DEFAULT REGION NAME [AWS REGION - EDIT]:
DEFAULT OUTPUT FORMAT [JSON-EDIT]:
```

Is possible to alternate between diferents user, or rols, but to do this is necesary to settings the users crendentials y your machine in the path user/.aws in the file crendentials and file configure, see the following example:

#### config:
```powershell
[default]
region = us-west-1
output = json

[admin]
region = us-west-1
output = json
```


#### credentials:
```powershell
[default]
aws_access_key_id = AKIAQSWVF2P2W3LBCPWX
aws_secret_access_key = G256x6gcZfm2o9SP9uYth9ixNL6jRyR1Fn3N+DkL
region = us-west-1


[admin]
# This key identifies your AWS account.
aws_access_key_id = ******************
# Treat this secret key like a password. Never share it or store it in source
# control. If your secret key is ever disclosed, immediately use IAM to delete
# the key pair and create a new one.
aws_secret_access_key = **********************************
```

## Install boto3 (Recommended - made to install in virtual env)

```powershell
pip install boto3
```

[Tip]: Use pip freeze to save the versions of all module to be installed in the virtual env

```powershell
pip freeze > requirements.txt
```
### Example

```py
import boto3

# Initialize client
def read_s3_file_content(bucket_name, object_name, file_name=None):
    s3 = boto3.client("s3")

    # Name of the s3 bucket
    bucket_name = "test-bucket"

    file_key = "files/objects/s3_file.txt"

    # Download_file
    s3.download_file(bucket_name, file_key, "my_file.txt")

    # Read and print the file contents
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
 
```


# AWS CLI Commands-Sheet 

## IAM
### Show your dataUser
```
aws sts get-caller-identity
```

## AWS S3
### Create a S3 bucket
```powershell
aws s3 mb s3://<NameBucket>
```
### show a list existing buckets
```powershell
aws s3 ls
```

# Initialize CDK
The first step well be to install node.js and aws-cdk packages:

```powershell
npm install -g aws-cdk
```

them go to an empty directory and  execute the folling command:

```powershell
cdk init app --language python
```