class ViewModel:
    def __init__(self, items, column_names):
        self._items = items
        self._column_names = column_names

    @property
    def items(self):
        return self._items
    
    @property
    def column_names(self):
        return self._column_names