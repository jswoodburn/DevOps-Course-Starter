import os
import pytest
from dotenv import load_dotenv, find_dotenv
import mongomock
import pymongo
from datetime import datetime

from todo_app import app
from todo_app.config.mongo_db_config import MongoDbConfig


@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page_loads(client):
    # Given
    config = MongoDbConfig()

    collection = pymongo.MongoClient(
        config.COSMOS_CONNECTION_STRING
    )[config.COSMOS_DB_NAME]["to_dos"]
    collection.insert_one(_get_db_document())

    # When
    response = client.get('/')

    # Then
    assert response.status_code == 200
    assert 'Just another to-do app.' in response.data.decode()

def test_index_page_displays_data(client):
    # Given
    config = MongoDbConfig()

    collection = pymongo.MongoClient(
        config.COSMOS_CONNECTION_STRING
    )[config.COSMOS_DB_NAME]["to_dos"]
    collection.insert_one(_get_db_document())
    
    # When
    response = client.get('/')

    # Then
    assert 'Test card' in response.data.decode()

def _get_db_document() -> dict:
    return {
        'name': 'Test card',
        'status': 'To Do',
        'last_edited': datetime.now()
    }