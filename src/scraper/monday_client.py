"""
Author: Jeff Plewak
Date: 2024-07-09
Description: Module for creating tasks in Monday.com.
"""

from monday import MondayClient
from scraper.logging_config import logger
from scraper.retry_utils import retry_on_exception
from scraper.secret_manager import access_secret_version

@retry_on_exception
def create_monday_task(task_name, task_description):
    """
    Create a task in Monday.com.
    
    :param task_name: Name of the task.
    :param task_description: Description of the task.
    :return: Created task item.
    """
    api_key = access_secret_version("MONDAY_API_KEY")
    client = MondayClient(api_key)
    item = client.items.create_item(os.getenv('BOARD_ID'), os.getenv('GROUP_ID'), task_name)
    logger.info(f"Monday task created with id {item['id']}")
    return item
