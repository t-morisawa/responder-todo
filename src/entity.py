from dataclasses import dataclass
from typing import List


@dataclass
class Todo:
  checked: bool
  task: str


@dataclass
class Todolist:
  todolist: List[Todo]


@dataclass
class Checklist:
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
    Todolistのチェック状態を更新する
    """
    pass
