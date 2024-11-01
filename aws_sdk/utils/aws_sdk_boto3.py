import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class AWS_S3_Service:
    def __init__(self):
        self.s3 = boto3.client("s3")

    def upload_to_s3(self, file_name, bucket_name, object_name=None):
        """
        Upload a file to an S3 bucket.

        :param file_name: File to upload
        :param bucket_name: Bucket to upload to
        :param object_name: S3 object name. If not specified, file_name is used
        :return: True if file was uploaded, else False
        """
        if object_name is None:
            object_name = file_name

        try:
            self.s3.upload_file(file_name, bucket_name, object_name)
            print(f"File '{file_name}' uploaded to '{bucket_name}/{object_name}'")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except (NoCredentialsError, PartialCredentialsError):
            print("Credentials not available or incomplete")
            return False

    def download_from_s3(self, bucket_name, object_name, file_name=None):
        """
        Download a file from an S3 bucket.

        :param bucket_name: Bucket to download from
        :param object_name: S3 object name
        :param file_name: Local path to save the file. If not specified, object_name is used
        :return: True if file was downloaded, else False
        """
        if file_name is None:
            file_name = object_name

        # Ensure the local directory exists
        os.makedirs(os.path.dirname(file_name), exist_ok=True)

        try:
            self.s3.download_file(bucket_name, object_name, file_name)
            print(f"File '{object_name}' downloaded from '{bucket_name}' to '{file_name}'")
            return True
        except FileNotFoundError:
            print("The specified file path was not found")
            return False
        except (NoCredentialsError, PartialCredentialsError):
            print("Credentials not available or incomplete")
            return False
        except self.s3.exceptions.NoSuchKey:
            print(f"The object '{object_name}' does not exist in the bucket '{bucket_name}'")
            return False

    def read_s3_file_content(self, bucket_name, object_name, local_path="temp_file.txt"):
        """
        Download a file from S3 and print its contents.

        :param bucket_name: Name of the S3 bucket
        :param object_name: S3 object key (path in bucket)
        :param local_path: Local path to save the downloaded file
        """
        # Download the file and read its contents if successful
        if self.download_from_s3(bucket_name, object_name, local_path):
            try:
                with open(local_path, "r") as file:
                    contents = file.read()
                    print(contents)
            except FileNotFoundError:
                print("The local file was not found after download.")



def path_exists(self, bucket_name, path):
        """
        Check if a file or directory exists at a specified S3 path.

        :param bucket_name: Name of the S3 bucket
        :param path: S3 object key (file path or directory prefix)
        :return: True if the path exists, else False
        """
        try:
            response = self.s3.list_objects_v2(Bucket=bucket_name, Prefix=path)
            if 'Contents' in response:
                print(f"Path '{path}' exists in bucket '{bucket_name}'")
                return True
            else:
                print(f"Path '{path}' does not exist in bucket '{bucket_name}'")
                return False
        except (NoCredentialsError, PartialCredentialsError):
            print("Credentials not available or incomplete")
            return False

def delete_path(self, bucket_name, path):
        """
        Delete a file or all objects within a specified directory in an S3 bucket if the path exists.

        :param bucket_name: Name of the S3 bucket
        :param path: S3 object key (file path or directory prefix)
        :return: True if deletion was successful, else False
        """
        if not self.path_exists(bucket_name, path):
            print(f"Cannot delete: Path '{path}' does not exist in bucket '{bucket_name}'")
            return False

        try:
            # Delete a single file or all files under a directory prefix
            response = self.s3.list_objects_v2(Bucket=bucket_name, Prefix=path)
            if 'Contents' in response:
                objects_to_delete = [{'Key': obj['Key']} for obj in response['Contents']]
                delete_response = self.s3.delete_objects(
                    Bucket=bucket_name,
                    Delete={'Objects': objects_to_delete}
                )
                print(f"Deleted {len(objects_to_delete)} objects from '{bucket_name}/{path}'")
                return True
            else:
                print(f"No objects found to delete in path '{path}'")
                return False
        except (NoCredentialsError, PartialCredentialsError):
            print("Credentials not available or incomplete")
            return False