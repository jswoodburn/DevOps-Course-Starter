from calendar import c
from datetime import datetime
from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items
from todo_app.data.trello_items import create_item_on_todo_list, get_lists_on_board, update_item_list_id

from todo_app.flask_config import Config
from todo_app.item import Item
from todo_app.view_model import ViewModel

app = Flask(__name__)
app.config.from_object(Config())

list_ids_in_progression_order = []

@app.route('/')
def index():
    lists_on_board = get_lists_on_board()
    list_names = []
    items_on_board = []

    for list in lists_on_board:
        list_names.append(list['name'])
        list_ids_in_progression_order.append(list['id'])
        for card in list['cards']:
            if not wasCardCompletedBeforeToday(list, card):
                items_on_board.append(Item.from_trello_card(card, list))

    return render_template('index.html', view_model=ViewModel(items_on_board, list_names))

def getDateTimeFromString(dateAsString):
    return datetime.strptime(dateAsString, "%Y-%m-%dT%H:%M:%S.%fZ").date()

def wasCardCompletedBeforeToday(list, card):
    return list['name'] == 'Done' and getDateTimeFromString(card['dateLastActivity']) != datetime.today().date()

@app.route('/add-todo', methods=[ 'POST'])
def add_todo_item():
    new_item = request.form.get('todo')
    # TODO exercise-2: hard coding this to add to start of flow (To Do) for now
    create_item_on_todo_list(new_item)
    return redirect('/')

@app.route('/update-item-status/<item_id>/<current_list_id>', methods=[ 'POST'])
def update_item_status(item_id, current_list_id):
    new_list_id = _get_next_list_id(current_list_id)
    print(current_list_id, new_list_id)
    update_item_list_id(item_id, new_list_id)
    return redirect('/')

def _get_next_list_id(current_list_id):
    current_index = list_ids_in_progression_order.index(current_list_id)
    next_index = current_index + 1
    if next_index > (len(list_ids_in_progression_order) - 1):
        # TODO exercise-2: Should probably throw an error here, they shouldn't be able to click next on a Done item
        return current_list_id
    return list_ids_in_progression_order[next_index]
