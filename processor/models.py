from django.db import models

class Product(models.Model):
    serial_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    input_image_urls = models.TextField()  # Comma-separated URLs
    output_image_urls = models.TextField(blank=True, null=True)  # Comma-separated URLs
    status = models.CharField(max_length=50, default='pending')  # pending, processing, completed
    request_id = models.CharField(max_length=100, unique=True)
    webhook_url = models.URLField(blank=True, null=True)  # Webhook URL field

    def __str__(self):
        return self.product_name
