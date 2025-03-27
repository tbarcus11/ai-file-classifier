📁 SortForm AI File Classifier – MVP Phase 1
This project is the backend for SortForm, an AI-powered file classification system. Right now, it handles:

A Flask API to upload files to an S3 bucket

An Apache Airflow pipeline to:

Detect the file’s MIME type and size

Log that metadata for future classification steps

✅ What’s Working
Flask File Uploader API
Simple REST endpoint that takes a file and uploads it to S3.

Airflow DAG: detect_mime_metadata_dag
Triggered manually (for now), it:

Downloads a file from S3

Uses python-magic to get its MIME type

Logs metadata like filename, size, and type

🛠️ Stack
Flask (file uploader)

Apache Airflow (DAGs running via Docker)

AWS S3 (storage)

EC2 (host for Docker/Airflow)

Boto3 + python-magic (file detection)

🚧 Next Steps
Hook up S3 events to auto-trigger Airflow

Add file classification

Organize files into customer folders
