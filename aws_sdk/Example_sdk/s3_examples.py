import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_to_s3(file_name, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket.

    :param file_name: File to upload
    :param bucket_name: Bucket to upload to
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    # Use file_name as object_name if not specified
    if object_name is None:
        object_name = file_name
    
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File '{file_name}' uploaded to '{bucket_name}/{object_name}'")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials")
        return False

# Example usage
#upload_to_s3('path/to/your/file.txt', 'your-bucket-name', 'optional/object/name/in/s3.txt')


def download_from_s3(bucket_name, object_name, file_name=None):
    """
    Download a file from an S3 bucket.

    :param bucket_name: Bucket to download from
    :param object_name: S3 object name
    :param file_name: Local path to save the file. If not specified, object_name is used
    :return: True if file was downloaded, else False
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    # Use object_name as file_name if not specified
    if file_name is None:
        file_name = object_name
    
    try:
        s3_client.download_file(bucket_name, object_name, file_name)
        print(f"File '{object_name}' downloaded from '{bucket_name}' to '{file_name}'")
        return True
    except FileNotFoundError:
        print("The specified file path was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    except PartialCredentialsError:
        print("Incomplete credentials")
        return False
    except s3_client.exceptions.NoSuchKey:
        print(f"The object '{object_name}' does not exist in the bucket '{bucket_name}'")
        return False

# Example usage
#download_from_s3('your-bucket-name', 'path/in/s3/object.txt', 'path/to/local/file.txt')
# Improve: if the local path spesificated not exist made a rule to create before download the file
#download_from_s3('test-bucket-atzin', 'files/objects/s3_file.txt',  '/file2.txt')

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