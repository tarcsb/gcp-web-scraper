import requests
import json

# Replace with your Monday.com API key
api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjM4MTg4Njc2MiwiYWFpIjoxMSwidWlkIjo2MzIwNTQzNiwiaWFkIjoiMjAyNC0wNy0wOVQwNDoxNDo1Mi4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MjQzMzQxMTMsInJnbiI6InVzZTEifQ.5AY2oeqoEDBwjWqLJJaySMY2ekBBMup9EKizrdeMl0M'

headers = {
    'Authorization': api_key,
    'Content-Type': 'application/json'
}

# Function to get board ID
def get_board_id():
    query = '{ boards { id name } }'
    response = requests.post('https://api.monday.com/v2', json={'query': query}, headers=headers)
    if response.status_code != 200:
        print("Failed to authenticate. Please check your API key.")
        print("Response:", response.json())
        return None
    boards = response.json()['data']['boards']
    for board in boards:
        print(f"Board Name: {board['name']}, Board ID: {board['id']}")
    board_id = input("Enter the Board ID you want to use: ")
    return board_id

# Function to get group ID from a board
def get_group_id(board_id):
    query = f'{{ boards(ids: {board_id}) {{ groups {{ id title }} }} }}'
    response = requests.post('https://api.monday.com/v2', json={'query': query}, headers=headers)
    if response.status_code != 200:
        print("Failed to authenticate or fetch groups. Please check your API key and Board ID.")
        print("Response:", response.json())
        return None
    groups = response.json()['data']['boards'][0]['groups']
    for group in groups:
        print(f"Group Title: {group['title']}, Group ID: {group['id']}")
    group_id = input("Enter the Group ID you want to use: ")
    return group_id

if __name__ == '__main__':
    board_id = get_board_id()
    if board_id:
        group_id = get_group_id(board_id)
        if group_id:
            print(f"Selected Board ID: {board_id}")
            print(f"Selected Group ID: {group_id}")
