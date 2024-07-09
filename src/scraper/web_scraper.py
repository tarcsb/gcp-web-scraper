import requests
from bs4 import BeautifulSoup
from scraper.logging_config import logger
from scraper.retry_utils import retry_on_exception

@retry_on_exception
def scrape_website(url):
    logger.info(f"Scraping the website: {url}")
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    return title, paragraphs
