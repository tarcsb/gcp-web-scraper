"""
Author: Jeff Plewak
Date: 2024-07-09
Description: Module for web scraping functionality.
"""

import requests
from bs4 import BeautifulSoup
from scraper.logging_config import logger
from scraper.retry_utils import retry_on_exception

@retry_on_exception
def scrape_website(url):
    """
    Scrape the specified website and extract the title and paragraphs.
    
    :param url: URL of the website to scrape.
    :return: Tuple containing the title and list of paragraphs.
    """
    logger.info(f"Scraping the website: {url}")
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    return title, paragraphs
