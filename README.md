# Image Processor

A Django-based system to process image data from CSV files asynchronously.

## Features
- Upload CSV files with product and image data.
- Asynchronously compress images by 50%.
- Track processing status using a unique `request_id`.
- Notify external systems via webhooks.

## Documentation
- [Low-Level Design (LLD)](docs/LLD.md)
- [API Documentation](docs/API_Documentation.md)
- [Workers Documentation](docs/Workers_Documentation.md)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/prave15/Assignment-Backend.git

2. Create and Activate Virtual Environment:
   pipenv shell

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   py manage.py makemigrations
   py manage.py migrate

5. Start the Django development server:
   python manage.py runserver

6. Start the Celery worker:
   celery -A image_processor worker --loglevel=info


## Postman Collection
You can find the Postman collection for testing the APIs here:  
[Postman Collection JSON](https://gist.github.com/prave15/3cd002de804a596e69c47b810a5b96a1)