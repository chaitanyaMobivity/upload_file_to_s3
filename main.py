import boto3
import os

ACCESS_KEY = "AKIA33URC2IL74VJ3F62"
SECRET_KEY = "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"
BUCKET_NAME ="mobivitytest1"

def upload_file_to_s3(file_path):
    s3_client = boto3.client('s3', region_name = "us-west-1",
                               aws_access_key_id=ACCESS_KEY,
                               aws_secret_access_key=SECRET_KEY)
    try:
        with open(file_path, 'rb') as data:
            s3_client.upload_fileobj(data, BUCKET_NAME, Key = os.path.basename(file_path))
            print(" object uploaded successfully!")
    except Exception as error:
        print(" there is a error in the function")


if __name__ == "__main__":
        upload_file_to_s3("/Users/chaitanyapoluri/Desktop/AWSTest/I9 Mobivity.pdf")



