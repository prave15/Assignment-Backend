import csv
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlparse
from .models import Product
from .tasks import process_images
from rest_framework.views import APIView
from rest_framework.response import Response


@csrf_exempt
def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        
        # Get webhook URL from request (optional)
        webhook_url = request.POST.get('webhook_url', None)

        # Validate CSV headers
        required_columns = {'S. No.', 'Product Name', 'Input Image Urls'}
        if not required_columns.issubset(reader.fieldnames):
            return JsonResponse({'error': 'CSV file is missing required columns'}, status=400)

        request_id = str(uuid.uuid4())
        errors = []

        for row_number, row in enumerate(reader, start=1):
            # Validate serial number
            if not row['S. No.'].strip():
                errors.append(f"Row {row_number}: Serial Number is missing")
                continue

            # Validate product name
            if not row['Product Name'].strip():
                errors.append(f"Row {row_number}: Product Name is missing")
                continue

            # Validate input image URLs
            input_urls = row['Input Image Urls'].strip().split(',')
            for url in input_urls:
                if not url.strip():
                    errors.append(f"Row {row_number}: Empty URL found")
                    continue
                parsed_url = urlparse(url.strip())
                if not all([parsed_url.scheme, parsed_url.netloc]):
                    errors.append(f"Row {row_number}: Invalid URL format: {url}")

            if errors:
                continue

            # Save valid data to the database
            Product.objects.create(
                serial_number=row['S. No.'],
                product_name=row['Product Name'],
                input_image_urls=row['Input Image Urls'],
                request_id=request_id,
                webhook_url=webhook_url  # Save webhook URL
            )

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        # Trigger Celery task for image processing
        process_images.delay(request_id)
        return JsonResponse({'request_id': request_id}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)


class StatusAPI(APIView):
    def get(self, request, request_id):
        products = Product.objects.filter(request_id=request_id)
        if products.exists():
            status = products.first().status
            return Response({'request_id': request_id, 'status': status})
        return Response({'error': 'Invalid request ID'}, status=404)
