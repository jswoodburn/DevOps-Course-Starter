from todo_app.models.view_model import ViewModel
from todo_app.models.item import Item
from todo_app.data.to_do_state import ToDoState

from datetime import datetime, timedelta

todo_list_name = ToDoState.TO_DO
doing_list_name = ToDoState.DOING
done_list_name = ToDoState.DONE

todo_card_name = 'This is a card that is still to do'
doing_card_name = 'This is a card that is in progress'
done_card_name = 'This is a card that was completed today'
done_yesterday_card_name = 'This is a card that was completed yesterday'

now = datetime.now()
yesterday = now - timedelta(days=1)


def test_todo_cards_returned_from_board():
    # Given
    board = mock_board()

    # When 
    items = board.todo_items
    
    # Then
    assert len(items) == 1
    assert items[0].name == todo_card_name

def test_doing_cards_returned_from_board():
    # Given
    board = mock_board()

    # When 
    items = board.doing_items
    
    # Then
    assert len(items) == 1
    assert items[0].name == doing_card_name

def test_done_cards_returned_from_board():
    # Given
    board = mock_board()

    # When 
    items = board.done_items
    
    # Then
    assert len(items) == 2
    assert items[0].name == done_yesterday_card_name
    assert items[1].name == done_card_name

def mock_board():
    item_1 = Item(
        id=1, 
        name=todo_card_name, 
        status=todo_list_name, 
        last_edited=now
        )
    item_2 = Item(
        id=2, 
        name=doing_card_name, 
        status=doing_list_name, 
        last_edited=now
        )
    item_3 = Item(
        id=3, 
        name=done_card_name, 
        status=done_list_name,
        last_edited=now)
    item_4 = Item(
        id=4, 
        name=done_yesterday_card_name, 
        status=done_list_name, 
        last_edited=yesterday)

    return ViewModel([item_1, item_2, item_3, item_4])