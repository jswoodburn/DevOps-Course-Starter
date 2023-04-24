import os
import requests
from pymongo import MongoClient
from todo_app.item import Item

client = MongoClient(os.getenv('COSMOS_CONNECTION_STRING'))
db = client.get_database(os.getenv('COSMOS_DB_NAME'))
to_dos = db.to_dos

def get_items_on_board():
    raw_items = to_dos.find({})
    return [Item.from_document(document) for document in raw_items]

def create_item_on_todo_list(item_name):
    create_item_on_list(item_name, todo_list_id)

def create_item_on_list(item_name, list_id):
    api_key = os.getenv('TRELLO_API_KEY')
    api_token = os.getenv('TRELLO_API_TOKEN')
    board_id = os.getenv('TRELLO_BOARD_ID')

    create_item_endpoint = f'{trello_base_url}cards'
    params = {
        'key': api_key,
        'token': api_token,
        'name': item_name,
        'idList': list_id
    }

    requests.post(create_item_endpoint, params=params)

def update_item_list_id(item_id, updated_list_id):
    api_key = os.getenv('TRELLO_API_KEY')
    api_token = os.getenv('TRELLO_API_TOKEN')
    board_id = os.getenv('TRELLO_BOARD_ID')

    update_item_endpoint = f'{trello_base_url}cards/{item_id}'
    params = {
        'key': api_key,
        'token': api_token,
        'idList': updated_list_id
    }

    requests.put(update_item_endpoint, params=params)