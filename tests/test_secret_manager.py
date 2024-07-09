import unittest
from unittest.mock import patch
from scraper.secret_manager import access_secret_version

class TestSecretManager(unittest.TestCase):

    @patch('scraper.secret_manager.secretmanager.SecretManagerServiceClient')
    def test_access_secret_version(self, mock_client):
        mock_client_instance = mock_client.return_value
        mock_client_instance.access_secret_version.return_value.payload.data.decode.return_value = "mock_secret"

        secret = access_secret_version("mock_secret_id")
        self.assertEqual(secret, "mock_secret")

if __name__ == '__main__':
    unittest.main()
