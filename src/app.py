import responder
from db import init as init_db, Todolist as TodolistDriver
from repository import TodolistRepositoryImpl
from usecase import UsecaseImpl
from controller import TodoController

api = responder.API()

FORM_VALUE = {
    'ADD_TODO': 'add_todo',
    'UPDATE_CHECKLIST': 'update_checklist',
    'CHECKLIST': 'checklist'
}

@api.on_event("startup")
async def setup():
    await init_db()

@api.route("/hello")
def hello_world(req, resp):
    resp.text = "hello, world!"

class TodoRoute:
    def __init__(self):
        self.controller = TodoController(UsecaseImpl(TodolistRepositoryImpl(TodolistDriver)))

    async def on_get(self, req, resp):
        todolist = await self.controller.get_all()
        resp.html = api.template('todo.html', todolist_presenter=todolist.data)

    async def on_post(self, req, resp):
        media = await req.media()
        if media.get('action') == FORM_VALUE['ADD_TODO']:
            todolist = await self.controller.add_item(media)
        elif media.get('action') == FORM_VALUE['UPDATE_CHECKLIST']:
            todolist = await self.controller.update_all_from_checklist(media.get_list(FORM_VALUE['CHECKLIST']))
        resp.html = api.template('todo.html', todolist_presenter=todolist.data)

api.add_route('/', TodoRoute)
