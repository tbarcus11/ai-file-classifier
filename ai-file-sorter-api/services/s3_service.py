import boto3
import os
from config import Config

s3 = boto3.client("s3", region_name=Config.S3_REGION,
                  aws_access_key_id=Config.AWS_ACCESS_KEY,
                  aws_secret_access_key=Config.AWS_SECRET_KEY)

def upload_file_to_s3(file, filename):
    """
    Uploads a file to the universal S3 bucket.
    """
    s3.upload_fileobj(file, Config.S3_BUCKET, filename)
    return f"https://{Config.S3_BUCKET}.s3.{Config.S3_REGION}.amazonaws.com/{filename}"
