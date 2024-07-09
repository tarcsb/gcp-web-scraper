import unittest
from unittest.mock import patch
import sys
import os
from dotenv import load_dotenv

# Load test environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.test'))

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scraper.web_scraper import scrape_website

class TestWebScraper(unittest.TestCase):

    @patch('scraper.web_scraper.requests.get')
    def test_scrape_website(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.content = '<html><head><title>Test Title</title></head><body><p>Test paragraph.</p></body></html>'

        title, paragraphs = scrape_website('http://example.com')

        self.assertEqual(title, 'Test Title')
        self.assertEqual(paragraphs, ['Test paragraph.'])

if __name__ == '__main__':
    unittest.main()
