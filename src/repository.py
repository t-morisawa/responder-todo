from db import Todolist as TodolistModel
from entity import Todo, Todolist, TodolistRepository


class TodolistRepositoryImpl(TodolistRepository):
    def __init__(self):
        self.db = TodolistModel

    async def get_all(self):
        data = await self.db.all()
        list_todo = []

        for datum in data:
            list_todo.append(Todo(datum.checked, datum.task))

        return Todolist(list_todo).todolist

    async def add_item(self, task):
        await self.db.create(checked=False, task=task)

    async def update_checked_from_checklist(self, checklist):
        data = await self.db.all()

        for index, item in enumerate(data):
            if index in checklist.checklist:
                item.checked = True
            else:
                item.checked = False

            #セーブの処理を待つ必要がある
            await item.save()
