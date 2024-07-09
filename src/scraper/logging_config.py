"""
Author: Jeff Plewak
Date: 2024-07-09
Description: Logging configuration for the GCP Web Scraper project.
"""

import logging
from google.cloud import logging as cloud_logging

def setup_logging():
    """
    Set up logging for the application.
    """
    client = cloud_logging.Client()
    client.setup_logging()
    logger = logging.getLogger("gcp_web_scraper")
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logging()
