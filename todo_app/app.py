from calendar import c
from datetime import date
from flask import Flask, redirect, render_template, request

from todo_app.data.database_repository import DatabaseRepository
from todo_app.item import Item
from todo_app.flask_config import FlaskConfig
from todo_app.view_model import ViewModel
from todo_app.data.to_do_state import ToDoState

def create_app():
    app = Flask(__name__)
    app.config.from_object(FlaskConfig())
    
    database = DatabaseRepository()

    list_ids_in_progression_order = []

    @app.route('/')
    def index():
        items_on_board = database.get_items_on_board()
        valid_items_to_display = list(filter(_was_item_completed_before_today, items_on_board))

        return render_template('index.html', view_model=ViewModel(valid_items_to_display))

    def _was_item_completed_before_today(item: Item) -> bool:
        return not (item.status == ToDoState.DONE and item.last_edited.date() < date.today())

    @app.route('/add-todo', methods=['POST'])
    def add_todo_item():
        new_item = request.form.get('todo')
        database.create_item_on_todo_list(new_item)
        return redirect('/')

    @app.route('/update-item-status/<item_id>/<current_status>', methods=['POST'])
    def update_item_status(item_id: str, current_status: ToDoState) -> None:
        updated_status = _get_next_status(current_status)
        database.update_item_list_id(item_id, updated_status)
        return redirect('/')

    def _get_next_status(current_status: ToDoState) -> ToDoState:
        if current_status == ToDoState.TO_DO:
            return ToDoState.DOING
        
        if current_status == ToDoState.DOING:
            return ToDoState.DONE
        
        raise Exception("Item state does not have a successor")

    return app
