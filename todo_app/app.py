import os
from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items
from todo_app.data.trello_items import get_lists_on_board

from todo_app.flask_config import Config
from todo_app.item import Item

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    lists_on_board = get_lists_on_board()
    list_names = []
    items_on_board = []

    for list in lists_on_board:
        list_names.append(list['name'])
        for card in list['cards']:
            items_on_board.append(Item.from_trello_card(card, list))

    return render_template('index.html', column_names=list_names, todos=items_on_board)

@app.route('/add-todo', methods=[ 'POST'])
def add_todo_item():
    new_item = request.form.get('todo')
    add_item(new_item)
    return redirect('/')
    