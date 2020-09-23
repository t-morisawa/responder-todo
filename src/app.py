import responder
from db import init as init_db, Todolist as TodolistDriver
from repository import TodolistRepositoryImpl
from usecase import UsecaseImpl
from controller import TodoController
from entity import Checklist

api = responder.API()

@api.on_event("startup")
async def setup():
    await init_db()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

class TodoRoute:
    async def on_get(self, req, resp):
        controller = TodoController(UsecaseImpl(TodolistRepositoryImpl(TodolistDriver)))
        todolist = await controller.get_all()
        resp.html = api.template('todo.html', todolist_presenter=todolist.data)

    async def on_post(self, req, resp):
        media = await req.media()
        if media.get('action') == 'add_todo':
            controller = TodoController(UsecaseImpl(TodolistRepositoryImpl(TodolistDriver)))
            todolist = await controller.add_item(media)
            resp.html = api.template('todo.html', todolist_presenter=todolist.data)
        elif media.get('action') == 'update_checklist':
            querydict = media.get_list('riyu')
            checklist = Checklist(list(map(lambda i: int(i)-1, querydict)))
            controller = TodoController(UsecaseImpl(TodolistRepositoryImpl(TodolistDriver)))
            todolist = await controller.update_all_from_checklist(checklist)
            resp.html = api.template('todo.html', todolist_presenter=todolist.data)

api.add_route('/todo', TodoRoute)

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
