# 📁 SortForm AI File Classifier

This project is the backend for **SortForm**, an AI-powered file classification system. Right now, it handles:

- A **Flask API** to upload files to an S3 bucket
- An **Apache Airflow pipeline** to:
  - Detect the file’s MIME type and size
  - Log that metadata for future classification steps

---

## ✅ What’s Working

### 🧪 Flask File Uploader API  
A simple REST endpoint that takes a file and uploads it to S3.

### 🔁 Airflow DAG: `detect_mime_metadata_dag`  
Triggered manually (for now), it:
- Downloads a file from S3
- Uses `python-magic` to get its MIME type
- Logs metadata like:
  - Filename  
  - File size  
  - MIME type  

---

## 🛠️ Stack

- Flask (file uploader)
- Apache Airflow (DAGs running via Docker)
- EC2 (host for Docker/Airflow)
- AWS S3 (storage)
- AWS Lambda (trigger)
- Boto3 + python-magic (MIME detection)

---

