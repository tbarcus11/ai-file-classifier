# ai-file-classifier

1. file-sorter-api:
This piece is a Flask-based API that allows users to upload files to an AWS S3 bucket, with future integration for AI-driven file classification and automated data pipelines. The API is designed with scalability in mind, featuring modular services for uploading, deleting, and managing files securely.

The project structure follows best practices, separating routes, services, and configurations, while sensitive credentials are managed through environment variables (.env). A frontend interface is included for direct file uploads, eliminating the need for Postman. Future enhancements will include AWS Lambda event triggers, Delta Lake storage, and automated file sorting. 
