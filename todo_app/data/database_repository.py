import os
import pymongo 
from todo_app.models.item import Item
from todo_app.data.to_do_state import ToDoState
from datetime import datetime
from typing import List

from todo_app.config.mongo_db_config import MongoDbConfig


class DatabaseRepository:
    def __init__(self):
        self.config = MongoDbConfig()
        self.client = pymongo.MongoClient(self.config.COSMOS_CONNECTION_STRING)
        self.db = self.client[self.config.COSMOS_DB_NAME]
        self.to_dos = self.db.to_dos

    def get_items_on_board(self) -> List[Item]:
        raw_items = self.to_dos.find({})
        return [Item.from_document(document) for document in raw_items]

    def create_item_on_todo_list(self, item_name: str) -> None:
        self.create_item_on_list(item_name, ToDoState.TO_DO)

    def create_item_on_list(self, item_name: str, status: ToDoState) -> None:
        item = {
            'name': item_name,
            'status': status,
            'last_edited': datetime.now()
        }

        self.to_dos.insert_one(item)

    def update_item_list_id(self, item_id: str, updated_status: ToDoState) -> None:
        self.to_dos.update_one(
            {'_id': item_id}, 
            {'$set': {
                'status': updated_status,
                'last_edited': datetime.now()
                }
            }
        )