import boto3
from config import Config

s3 = boto3.client("s3",
                  aws_access_key_id=Config.AWS_ACCESS_KEY,
                  aws_secret_access_key=Config.AWS_SECRET_KEY)

try:
    response = s3.list_buckets()
    print("S3 Connection Successful! Buckets:", [bucket['Name'] for bucket in response['Buckets']])
except Exception as e:
    print("S3 Connection Failed:", str(e))
