import unittest
from unittest.mock import patch
import sys
import os

# Ensure the src directory is in the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

import scraper.web_scraper as web_scraper

class TestWebScraper(unittest.TestCase):

    @patch('scraper.web_scraper.requests.get')
    def test_scrape_website(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.content = '<html><head><title>Test Title</title></head><body><p>Test paragraph.</p></body></html>'
        
        title, paragraphs = web_scraper.scrape_website('http://example.com')
        
        self.assertEqual(title, 'Test Title')
        self.assertEqual(paragraphs, ['Test paragraph.'])

if __name__ == '__main__':
    unittest.main()
