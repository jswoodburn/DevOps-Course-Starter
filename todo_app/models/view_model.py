from todo_app.data.to_do_state import ToDoState
from todo_app.models.item import Item
from typing import List

class ViewModel:
    def __init__(self, items):
        self._items: List[Item] = items
        self._column_names = ToDoState.get_lists_to_display()

    @property
    def items(self) -> List[Item]:
        return self._items
    
    @property
    def column_names(self) -> List[ToDoState]:
        return self._column_names

    @property
    def todo_items(self) -> List[Item]:
        todo_items = list(filter(lambda item: item.status == ToDoState.TO_DO, self._items))
        todo_items.sort(key=lambda item: item.last_edited)
        return todo_items

    @property
    def doing_items(self) -> List[Item]:
        doing_items = list(filter(lambda item: item.status == ToDoState.DOING, self._items))
        doing_items.sort(key=lambda item: item.last_edited)
        return doing_items

    @property
    def done_items(self) -> List[Item]:
        done_items = list(filter(lambda item: item.status == ToDoState.DONE, self._items))
        done_items.sort(key=lambda item: item.last_edited)
        return done_items
