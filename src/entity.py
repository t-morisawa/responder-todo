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


@dataclass
class Checklist:
  """
  Todoリストの更新に利用. ユーザがチェックした要素の配列
  """
  data: List[int]
