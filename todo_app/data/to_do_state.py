class ToDoState():
    TO_DO = "To Do"
    DOING = "Doing"
    DONE = "Done"

    @staticmethod
    def get_lists_to_display():
        return ToDoState.TO_DO, ToDoState.DOING, ToDoState.DONE
    
    def __call__(self, *args):
        return self.value(*args)
    