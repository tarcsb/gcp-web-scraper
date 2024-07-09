"""
Author: Jeff Plewak
Date: 2024-07-09
Description: Main script to initiate the web scraping, data upload, and task creation process.
"""

import logging
import os

from scraper.web_scraper import scrape_website
from scraper.gcs_uploader import upload_to_gcs
from scraper.monday_client import create_monday_task
from scraper.pubsub_publisher import publish_message
from scraper.logging_config import logger

def main():
    """
    Main function to run the web scraper and handle data processing.
    """
    logger.info("Starting the scraper...")
    try:
        title, data = scrape_website(os.getenv('WEBSITE_URL'))
        upload_to_gcs(data, 'scraped_data.txt')
        create_monday_task(title, ' '.join(data))
        publish_message('scraping-completed', f"Scraping completed for {os.getenv('WEBSITE_URL')}")
        logger.info("Scraper completed successfully.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        publish_message('scraping-failed', f"Scraping failed for {os.getenv('WEBSITE_URL')} due to {e}")

if __name__ == "__main__":
    main()
