from dataclasses import dataclass
from typing import List


@dataclass
class Todo:
  """
  Todoリストの要素
  """
  checked: bool
  task: str


@dataclass
class Todolist:
  """
  Todoリスト本体
  """
  data: List[Todo]


class TodolistRepository:
  async def get_all(self):
    """
    Todolistの一覧を取得する
    """
    pass

  async def add_item(self, task):
    """
    Todolistのアイテムを一件追加する
    """
    pass

  async def update_all(self, todolist):
    """
    Todolistを一括更新する
    """
    pass
