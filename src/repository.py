from db import Todolist as TodolistModel
from entity import Todo, Todolist, Repository


class TodolistRepository(Repository):
    def __init__(self):
        self.db = TodolistModel

    async def get_all(self):
        data = await self.db.all()
        list_todo = []

        for datum in data:
            list_todo.append(Todo(datum.checked, datum.task))

        return Todolist(list_todo).todolist

    async def create_item(self, task):
        await self.db.create(checked=False, task=task)

    async def update_checked(self, index, checked):
        item = await self.db[index]
        item.checked = checked

    async def update_checked_from_checklist(self, checklist):
        """
        現状の実装はチェックの一括更新を行っているので効率よく登録できるような実装を用意する
        """
        data = await self.db.all()

        for index, item in enumerate(data):
            if str(index + 1) in checklist:
                item.checked = True
            else:
                item.checked = False

            #セーブの処理を待つ必要がある
            await item.save()
