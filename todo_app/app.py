from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', todos=get_items())

@app.route('/add-todo', methods=[ 'POST'])
def add_todo_item():
    new_item = request.form.get('todo')
    add_item(new_item)
    return redirect('/')
    