from google.cloud import storage
import os
from scraper.logging_config import logger
from scraper.retry_utils import retry_on_exception

@retry_on_exception
def upload_to_gcs(data, destination_blob_name):
    bucket_name = f"{os.getenv('GCP_PROJECT_ID')}-scraper-bucket"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string('\n'.join(data))
    logger.info(f"Data uploaded to {destination_blob_name} in bucket {bucket_name}")
