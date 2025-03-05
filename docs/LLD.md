# Low-Level Design (LLD)

## System Overview
The system processes image data from CSV files asynchronously. It accepts a CSV file, compresses images by 50%, and stores the processed image URLs in a database.

## Components
1. **Django Application**: Handles HTTP requests and database interactions.
2. **Celery**: Manages asynchronous tasks.
3. **Redis**: Acts as a message broker for Celery.
4. **Database**: Stores product information and processing status.
5. **Image Processing Service**: Compresses images and updates the database.
6. **Webhook**: Notifies external systems after processing.

## Workflow
1. Client uploads a CSV file.
2. System validates the CSV and saves data to the database.
3. Celery processes images asynchronously.
4. Client checks processing status using the `request_id`.
5. Webhook notifies the client after processing is complete.

