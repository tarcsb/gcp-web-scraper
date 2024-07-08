import requests
from bs4 import BeautifulSoup
from monday import MondayClient

# Monday.com setup
api_key = 'your_monday_api_key'  # Replace with actual API key
monday = MondayClient(api_key)

def create_monday_task(task_name, task_description):
    board_id = 'your_board_id'  # Replace with your board ID
    group_id = 'your_group_id'  # Replace with your group ID

    item = monday.items.create_item(
        board_id=board_id,
        group_id=group_id,
        item_name=task_name,
        column_values={
            'description': task_description
        }
    )
    return item

# Web scraping logic
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Example: Extract the title
    title = soup.title.string
    return title

# Example usage
website_url = 'https://example.com'
task_name = 'Scrape website title'
task_description = scrape_website(website_url)
create_monday_task(task_name, task_description)

