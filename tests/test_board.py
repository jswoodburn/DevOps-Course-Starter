from turtle import done
from todo_app.view_model import ViewModel
from todo_app.item import Item

todo_list_name = 'To Do'
doing_list_name = 'Doing'
done_list_name = 'Done'

todo_card_name = 'This is a card that is still to do'
doing_card_name = 'This is a card that is in progress'
done_card_name = 'This is a card that was completed today'
done_yesterday_card_name = 'This is a card that was completed yesterday'

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
    assert items[0].name == done_card_name
    assert items[1].name == done_yesterday_card_name

def mock_board():
    item_1 = Item(1, todo_card_name, todo_list_name, 1)
    item_2 = Item(2, doing_card_name, doing_list_name, 2)
    item_3 = Item(3, done_card_name, done_list_name, 3)
    item_4 = Item(4, done_yesterday_card_name, done_list_name, 3)

    list_names = [todo_list_name, doing_list_name, done_list_name]

    return ViewModel([item_1, item_2, item_3, item_4], list_names)