import os
import requests
from bs4 import BeautifulSoup
from monday import MondayClient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Monday.com setup using environment variables
api_key = os.getenv('MONDAY_API_KEY')  # Load from environment variable
if not api_key:
    raise ValueError("No MONDAY_API_KEY found in environment variables")

monday = MondayClient(api_key)

# Web scraping logic
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string
        paragraphs = [p.get_text() for p in soup.find_all('p')]

        logger.info(f'Scraped title: {title}')
        logger.info(f'Scraped paragraphs: {paragraphs}')
        return title, paragraphs
    except requests.RequestException as e:
        logger.error(f'Failed to fetch URL: {e}')
        raise
    except Exception as e:
        logger.error(f'Failed to scrape website: {e}')
        raise

def create_monday_task(task_name, task_description):
    try:
        board_id = os.getenv('BOARD_ID')  # Load from environment variable
        group_id = os.getenv('GROUP_ID')  # Load from environment variable

        item = monday.items.create_item(
            board_id=board_id,
            group_id=group_id,
            item_name=task_name,
            column_values={
                'description': task_description
            }
        )
        logger.info(f'Task created with ID: {item["id"]}')
        return item
    except Exception as e:
        logger.error(f'Failed to create task: {e}')
        raise

# Example usage
if __name__ == '__main__':
    try:
        website_url = os.getenv('SCRAPE_URL')  # Load from environment variable
        task_name = 'Scrape website title and paragraphs'
        title, paragraphs = scrape_website(website_url)
        task_description = f"Title: {title}\n\n" + "\n\n".join(paragraphs)
        create_monday_task(task_name, task_description)
    except Exception as e:
        logger.critical(f'Failed to run scraper: {e}')
