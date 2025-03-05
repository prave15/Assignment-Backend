# Workers Documentation

- **Content**:
  - Description of Celery tasks.
  - Task parameters and workflow.


## Celery Task: `process_images`
- **Description**: Asynchronously processes images for a given `request_id`.
- **Parameters**:
  - `request_id`: Unique ID of the processing request.


- **Steps**:
  1. Fetch products associated with the `request_id`.
  2. Download input images.
  3. Compress images by 50%.
  4. Update the database with output image URLs.
  5. Trigger webhook notification (if provided).