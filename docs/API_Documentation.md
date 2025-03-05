# API Documentation

## Upload API
- **Endpoint**: `/upload-csv/`
- **Method**: `POST`
- **Description**: Accepts a CSV file and returns a unique `request_id`.
- **Request**:
  ```json
  {
    "csv_file": "file.csv",
    "webhook_url": "https://client-server.com/webhook"  # Optional
  }

  ```
- **Response**: 
  ```json
  {
  "request_id": "123e4567-e89b-12d3-a456-426614174000"
   }
   
   ```


## Status API
- **Endpoint**: `check-status/<str:request_id>/`
- **Method**: `GET`
- **Description**: Returns the processing status and output image URLs.

- **Response**: 
  ```json
  {
  "request_id": "123e4567-e89b-12d3-a456-426614174000",
  "status": "completed",
  "output_image_urls": [
    "https://www.public-image-output-url1.jpg",
    "https://www.public-image-output-url2.jpg"
  ]
  }
   ```

## Testing the APIs
To test the APIs, use the following Postman collection:  
[Postman Collection JSON](## Testing the APIs
To test the APIs, use the following Postman collection:  
[Postman Collection JSON](https://gist.github.com/prave15/3cd002de804a596e69c47b810a5b96a1)
  