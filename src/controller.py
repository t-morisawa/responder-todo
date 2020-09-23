from db import Todolist as TodolistDriver
from repository import TodolistRepositoryImpl
from usecase import Checklist

class TodoController:
    def __init__(self, usecase):
        self.usecase = usecase

    async def get_all(self):
        return await self.usecase.get_all()

    async def add_item(self, body):
        task = body.get('task')
        if task is not None:
            await self.usecase.add_item(task)
        return await self.usecase.get_all()

    async def update_all_from_checklist(self, checkbox_list):
        """
        :param list checkbox_list HTML form checkboxのデータ(チェックを入れたものだけ送信されるイメージ)
        """
        checklist = Checklist(list(map(lambda i: int(i)-1, checkbox_list)))
        await self.usecase.update_all_from_checklist(checklist)
        return await self.usecase.get_all()
