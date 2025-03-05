from django.urls import path
from .views import upload_csv, StatusAPI

urlpatterns = [
    path('upload-csv/', upload_csv, name='upload_csv'),
    path('check-status/<str:request_id>/', StatusAPI.as_view(), name='status_api'),
]