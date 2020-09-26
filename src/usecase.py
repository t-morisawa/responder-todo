from entity import Todo, Todolist
from typing import List
from dataclasses import dataclass


@dataclass
class Checklist:
  """
  UseCase Input
  Todoリストの更新に利用. ユーザがチェックした要素の配列
  """
  data: List[int]


class Usecase:
  def __init__(self, todolist_repository):
      self.repository = todolist_repository

  async def get_all(self):
    """
    Todolistの一覧を取得する
    """
    return await self.repository.get_all()

  async def add_item(self, task):
    """
    Todolistのアイテムを一件追加する
    """
    todo = Todo(False, task)
    await self.repository.add_item(todo)

  async def update_all_from_checklist(self, checklist):
    """
    Todolistのチェック状態を一括更新する
    """
    todolist = await self.repository.get_all()
    new = []

    for index, item in enumerate(todolist.data):
        if index in checklist.data:
            checked = True
        else:
            checked = False
        new.append(Todo(checked, item.task))

    new_todolist = Todolist(new)
    await self.repository.update_all(new_todolist)
