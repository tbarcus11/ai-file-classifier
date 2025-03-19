import json
import boto3
import requests

# Airflow API URL (Update this if running remotely)
AIRFLOW_TRIGGER_URL = "https://59bc-2001-49d0-8511-1-2548-a1e9-de08-eba8.ngrok-free.app/api/v1/dags/s3_file_processor/dagRuns"

# Airflow Admin Credentials
AIRFLOW_USERNAME = "admin"
AIRFLOW_PASSWORD = "admin"

# Trigger Airflow DAG
response = requests.post(
    AIRFLOW_TRIGGER_URL,
    json=payload,
    auth=(AIRFLOW_USERNAME, AIRFLOW_PASSWORD)  # ✅ Adding authentication
)


# AWS Lambda Handler
def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']

        print(f"📂 New file uploaded: {file_key} in bucket: {bucket_name}")

        # Prepare payload for Airflow
        payload = {
            "conf": {"file_key": file_key}
        }

        # Trigger Airflow DAG
        response = requests.post(
            AIRFLOW_TRIGGER_URL,
            json=payload,
            auth=(AIRFLOW_USERNAME, AIRFLOW_PASSWORD)  # ✅ Adding authentication
        )

        print("Airflow Response:", response.text)

    return {"statusCode": 200, "body": json.dumps("Lambda executed successfully!")}