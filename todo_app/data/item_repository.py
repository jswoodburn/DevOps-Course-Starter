import os
import requests
from pymongo import MongoClient
from todo_app.item import Item
from todo_app.data.to_do_state import ToDoState
from datetime import datetime

client = MongoClient(os.getenv('COSMOS_CONNECTION_STRING'))
db = client.get_database(os.getenv('COSMOS_DB_NAME'))
to_dos = db.to_dos

def get_items_on_board():
    raw_items = to_dos.find({})
    return [Item.from_document(document) for document in raw_items]

def create_item_on_todo_list(item_name):
    create_item_on_list(item_name, ToDoState().TO_DO)

def create_item_on_list(item_name, status):
    item = {
        'name': item_name,
        'status': status,
        'last_edited': datetime.now()
    }

    to_dos.insert_one(item)

def update_item_list_id(item_id, updated_list_id):
    to_dos.update_one(
        {'_id': item_id}, 
        {'$set': {
            'status': updated_list_id,
            'last_edited': datetime.now()
            }
        }
    )