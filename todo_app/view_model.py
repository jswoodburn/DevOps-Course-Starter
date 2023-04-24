from todo_app.data.to_do_state import ToDoState

class ViewModel:
    

    def __init__(self, items):
        self._items = items
        self._column_names = ToDoState().get_lists_to_display()

    @property
    def items(self):
        return self._items
    
    @property
    def column_names(self):
        return self._column_names

    @property
    def todo_items(self):
        todo_items = []
        for item in self._items:
            if item.status == ToDoState().TO_DO:
                todo_items.append(item)
        return todo_items

    @property
    def doing_items(self):
        doing_items = []
        for item in self._items:
            if item.status == ToDoState().DOING:
                doing_items.append(item)
        return doing_items

    @property
    def done_items(self):
        done_items = []
        for item in self._items:
            if item.status == ToDoState().DONE:
                done_items.append(item)
        return done_items
