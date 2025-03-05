from celery import shared_task
from .models import Product
import requests
from PIL import Image
from io import BytesIO

@shared_task
def process_images(request_id):
    products = Product.objects.filter(request_id=request_id)
    for product in products:
        input_urls = product.input_image_urls.split(',')
        output_urls = []
        for url in input_urls:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img = img.resize((img.width // 2, img.height // 2))  # Compress by 50%
            output_url = f"https://www.public-image-output-url{len(output_urls) + 1}.jpg"
            output_urls.append(output_url)
            img.save(output_url)  # Save the compressed image (mock implementation)
        product.output_image_urls = ','.join(output_urls)
        product.status = 'completed'
        product.save()
        
        # Trigger webhook if URL is provided
        if product.webhook_url:
            webhook_data = {
                'request_id': request_id,
                'status': 'completed',
                'output_image_urls': product.output_image_urls.split(',') if product.output_image_urls else []
            }
            try:
                response = requests.post(product.webhook_url, json=webhook_data)
                response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            except requests.exceptions.RequestException as e:
                # Log the error (you can use Django's logging or print for debugging)
                print(f"Webhook failed for request {request_id}: {e}")