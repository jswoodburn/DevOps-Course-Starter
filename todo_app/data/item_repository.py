import os
from pymongo import MongoClient
from todo_app.item import Item
from todo_app.data.to_do_state import ToDoState
from datetime import datetime
from typing import List

client = MongoClient(os.getenv('COSMOS_CONNECTION_STRING'))
db = client.get_database(os.getenv('COSMOS_DB_NAME'))
to_dos = db.to_dos

def get_items_on_board() -> List[Item]:
    raw_items = to_dos.find({})
    return [Item.from_document(document) for document in raw_items]

def create_item_on_todo_list(item_name: str) -> None:
    create_item_on_list(item_name, ToDoState().TO_DO)

def create_item_on_list(item_name: str, status: ToDoState) -> None:
    item = {
        'name': item_name,
        'status': status,
        'last_edited': datetime.now()
    }

    to_dos.insert_one(item)

def update_item_list_id(item_id: str, updated_status: ToDoState) -> None:
    to_dos.update_one(
        {'_id': item_id}, 
        {'$set': {
            'status': updated_status,
            'last_edited': datetime.now()
            }
        }
    )