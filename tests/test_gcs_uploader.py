import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from dotenv import load_dotenv

# Load test environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.test'))

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
print("Current sys.path:")
print("\n".join(sys.path))

from scraper.gcs_uploader import upload_to_gcs

class TestGCSUploader(unittest.TestCase):

    @patch('scraper.gcs_uploader.storage.Client')
    def test_upload_to_gcs(self, mock_storage_client):
        mock_bucket = MagicMock()
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob
        mock_storage_client.return_value.bucket.return_value = mock_bucket

        data = ['Test data']
        upload_to_gcs(data, 'test_blob.txt')

        mock_blob.upload_from_string.assert_called_once_with('Test data')

if __name__ == '__main__':
    unittest.main()
