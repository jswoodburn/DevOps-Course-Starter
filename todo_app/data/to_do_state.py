class ToDoState():
    TO_DO = "To Do"
    DOING = "Doing"
    DONE = "Done"

    def get_lists_to_display(self):
        return self.TO_DO, self.DOING, self.DONE
    
    def __call__(self, *args):
        return self.value(*args)
    