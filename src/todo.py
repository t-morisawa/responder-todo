class Todo:
  def __init__(self, checked, task):
    self.checked = checked
    self.task = task


class TodolistManager:
  def __init__(self, todolist=[]):
    self.todolist = todolist

  def add_todo(self, task):
    todo = Todo(False, task)
    self.todolist.append(todo)

  def update_todo(self):
    pass  # あとで実装する
