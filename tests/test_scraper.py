import unittest
from unittest.mock import patch
import sys
import os

# Ensure the src directory is in the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import scraper

class TestWebScraper(unittest.TestCase):

    @patch('scraper.requests.get')
    def test_scrape_website(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.content = '<html><head><title>Test Title</title></head><body><p>Test paragraph.</p></body></html>'
        
        title, paragraphs = scraper.scrape_website('http://example.com')
        
        self.assertEqual(title, 'Test Title')
        self.assertEqual(paragraphs, ['Test paragraph.'])
    
    @patch('scraper.MondayClient')
    def test_create_monday_task(self, mock_monday_client):
        mock_monday_client_instance = mock_monday_client.return_value
        mock_monday_client_instance.items.create_item.return_value = {'id': '12345'}
        
        task_name = 'Test Task'
        task_description = 'This is a test task.'
        item = scraper.create_monday_task(task_name, task_description)
        
        self.assertEqual(item['id'], '12345')

if __name__ == '__main__':
    unittest.main()
