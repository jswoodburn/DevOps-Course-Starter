import os
import requests
import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client

def test_index_page_loads(monkeypatch, client):
    
    # Given
    monkeypatch.setattr(requests, 'get', get_lists_stub)

    # When
    response = client.get('/')

    # Then
    assert response.status_code == 200
    assert 'Just another to-do app.' in response.data.decode()

def test_index_page_displays_trello_data(monkeypatch, client):
    
    # Given
    monkeypatch.setattr(requests, 'get', get_lists_stub)

    # When
    response = client.get('/')

    # Then
    assert 'Test card' in response.data.decode()

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def get_lists_stub(url, params):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')

    print(url)
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [
            {
                'idBoard': '1234ABCD',
                'id': '890xyz',
                'name': 'To Do',
                'cards': [
                    {
                        'id': '456', 
                        'name': 'Test card', 
                        'dateLastActivity': '2022-09-06T15:45:55.959Z',
                        'idBoard': '1234ABCD',
                        'idList': '890xyz',
                    },
                ],
            }
        ]
    return StubResponse(fake_response_data)