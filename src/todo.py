class Todo:
  def __init__(self, checked, task):
    self.checked = checked
    self.task = task


class Todolist:
  def __init__(self, todolist=[]):
    self.todolist = todolist

  def add_todo(self, todo):
    self.todolist.append(todo)

  def update_todo(self):
    pass  # あとで実装する
