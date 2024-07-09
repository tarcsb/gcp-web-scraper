import unittest
from unittest.mock import patch
import sys
import os
from dotenv import load_dotenv

# Load test environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env.test'))

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scraper.pubsub_publisher import publish_message

class TestPubSubPublisher(unittest.TestCase):

    @patch('scraper.pubsub_publisher.pubsub_v1.PublisherClient')
    def test_publish_message(self, mock_publisher_client):
        mock_publisher = mock_publisher_client.return_value
        mock_publisher.topic_path.return_value = 'projects/mock_project/topics/mock_topic'
        future = mock_publisher.publish.return_value
        future.result.return_value = 'mock_message_id'

        publish_message('mock_topic', 'mock_message')

        mock_publisher.publish.assert_called_once_with(
            'projects/mock_project/topics/mock_topic', b'mock_message'
        )

if __name__ == '__main__':
    unittest.main()
