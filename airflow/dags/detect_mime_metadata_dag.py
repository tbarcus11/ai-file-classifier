from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3
import os
import magic
import tempfile

def detect_mime_and_metadata(**context):
    s3 = boto3.client('s3')

    bucket = context['dag_run'].conf.get('bucket')
    key = context['dag_run'].conf.get('file_key')

    if not bucket or not key:
        raise ValueError("Missing 'bucket' or 'file_key' in DAG trigger payload")

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        s3.download_fileobj(bucket, key, tmp_file)
        tmp_path = tmp_file.name

    # Detect MIME
    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(tmp_path)

    # Metadata
    metadata = {
        "file_name": os.path.basename(key),
        "file_size_bytes": os.path.getsize(tmp_path),
        "mime_type": mime_type,
    }

    print(f"[MIME DETECTED]: {metadata}")
    context['ti'].xcom_push(key='file_metadata', value=metadata)

    os.remove(tmp_path)

default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='detect_mime_metadata_dag',
    description='Detect MIME type and metadata of uploaded file',
    schedule_interval=None,
    default_args=default_args,
    tags=['sortform', 'metadata'],
) as dag:

    detect_task = PythonOperator(
        task_id='detect_mime_and_metadata',
        python_callable=detect_mime_and_metadata,
        provide_context=True
    )
