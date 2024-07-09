import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Ensure the src directory is in the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import scraper.gcs_uploader as gcs_uploader

class TestGCSUploader(unittest.TestCase):

    @patch('scraper.gcs_uploader.storage.Client')
    def test_upload_to_gcs(self, mock_storage_client):
        mock_bucket = MagicMock()
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob
        mock_storage_client.return_value.bucket.return_value = mock_bucket
        
        data = ['Test data']
        gcs_uploader.upload_to_gcs(data, 'test_blob.txt')
        
        mock_blob.upload_from_string.assert_called_once_with('Test data')

if __name__ == '__main__':
    unittest.main()
