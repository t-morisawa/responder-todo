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
  todolist: List[Todo]


@dataclass
class Checklist:
  """
  Todoリストの更新に利用. ユーザがチェックした要素の配列
  """
  checklist: List[int]


@dataclass
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

  async def update_checked_from_checklist(self, checklist):
    """
    Todolistのチェック状態を一括更新する
    """
    pass
