from db import Todolist as TodolistModel
from entity import Todo, Todolist, TodolistRepository


class TodolistTortoiseRepository(TodolistRepository):
    def __init__(self, db):
        self.db = db

    async def get_all(self):
        data = await self.db.all()
        list_todo = []

        for datum in data:
            list_todo.append(Todo(datum.checked, datum.task))

        return Todolist(list_todo)

    async def add_item(self, todo):
        await self.db.create(checked=False, task=todo.task)

    async def update_all(self, todolist):
        data = await self.db.all()
        todolist_iter = iter(todolist.data)

        for item in data:
            request = todolist_iter.__next__()
            item.checked = request.checked
            item.task = request.task

            #セーブの処理を待つ必要がある
            await item.save()
