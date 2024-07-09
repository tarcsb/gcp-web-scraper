import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Ensure the src directory is in the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import scraper.monday_client as monday_client

class TestMondayClient(unittest.TestCase):

    @patch('scraper.monday_client.MondayClient')
    @patch('scraper.monday_client.access_secret_version')
    def test_create_monday_task(self, mock_access_secret_version, mock_monday_client):
        mock_access_secret_version.return_value = 'mock_api_key'
        mock_monday_client_instance = mock_monday_client.return_value
        mock_monday_client_instance.items.create_item.return_value = {'id': '12345'}
        
        task_name = 'Test Task'
        task_description = 'This is a test task.'
        item = monday_client.create_monday_task(task_name, task_description)
        
        self.assertEqual(item['id'], '12345')

if __name__ == '__main__':
    unittest.main()
