from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import logging

# Function to process the uploaded S3 file
def process_s3_file(**kwargs):
    file_name = kwargs['dag_run'].conf.get('file_key', 'No file received')
    logging.info(f"📂 Processing file: {file_name}")

# Airflow DAG configuration
default_args = {
    'owner': 'admin',
    'start_date': datetime(2024, 3, 10),
    'catchup': False
}

with DAG('s3_file_processor',
         default_args=default_args,
         schedule_interval=None) as dag:

    process_task = PythonOperator(
        task_id='process_s3_file',
        python_callable=process_s3_file,
        provide_context=True
    )
