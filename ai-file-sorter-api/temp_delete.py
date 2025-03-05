import boto3
import sys
from config import Config

# Initialize S3 client
s3 = boto3.client("s3",
                  region_name=Config.S3_REGION,
                  aws_access_key_id=Config.AWS_ACCESS_KEY,
                  aws_secret_access_key=Config.AWS_SECRET_KEY)

def delete_file_from_s3(file_key):
    """
    Deletes a single file from S3.
    :param file_key: The path/key of the file to delete in S3.
    """
    try:
        s3.delete_object(Bucket=Config.S3_BUCKET, Key=file_key)
        print(f"✅ Successfully deleted {file_key}")
    except Exception as e:
        print(f"❌ Error deleting file: {str(e)}")

# Allow running from the command line
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python scripts/delete_s3_file.py <file_name>")
    else:
        delete_file_from_s3(sys.argv[1])
