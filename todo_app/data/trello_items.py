import os
import requests

trello_base_url = 'https://api.trello.com/1/'
api_key = os.getenv('TRELLO_API_KEY')
api_token = os.getenv('TRELLO_API_TOKEN')
board_id = os.getenv('TRELLO_BOARD_ID')

# TODO exercise-2: is there a nice way to not hard code
todo_list_id = '6305fd4bf77620537efc5cf5'
done_list_id = '6305fd4c6de4d31d4d1a97b3'

def get_lists_on_board():
    get_board_endpoint = f'{trello_base_url}boards/{board_id}/lists'
    params = {
        'key': api_key,
        'token': api_token,
        'cards': 'open'
    }
    return requests.get(get_board_endpoint, params=params).json()
