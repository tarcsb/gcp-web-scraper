import unittest
from unittest.mock import patch
import sys
import os
from dotenv import load_dotenv

# Load test environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.test'))

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scraper.secret_manager import access_secret_version

class TestSecretManager(unittest.TestCase):

    @patch('scraper.secret_manager.secretmanager.SecretManagerServiceClient')
    def test_access_secret_version(self, mock_client):
        mock_client_instance = mock_client.return_value
        mock_access_secret_version = mock_client_instance.access_secret_version
        mock_access_secret_version.return_value.payload.data.decode.return_value = "mock_secret"

        secret = access_secret_version("mock_secret_id")
        self.assertEqual(secret, "mock_secret")

if __name__ == '__main__':
    unittest.main()
