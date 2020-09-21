from dataclasses import dataclass
from typing import List
from tortoise import Tortoise

@dataclass
class Todo:
  checked: bool
  task: str


@dataclass
class Todolist:
  todolist: List[Todo]


@dataclass
class Repository:
  async def get_all(self):
    """
    Todolistの一覧を取得する
    """
    pass

  async def create_item(self, task):
    """
    Todolistのアイテムを一件追加する
    """
    pass

  async def update_checked(self, index, checked):
    """
    Todolistのチェック状態を更新する
    """
    pass
