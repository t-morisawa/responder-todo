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

  def update_todo(self, list):
    for index, item in enumerate(self.todolist):
      if str(index + 1) in list:
        item.checked = True
      else:
        item.checked = False