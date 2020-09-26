import responder
from db import init as init_db
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
    async def on_get(self, req, resp):
        todolist = await TodoController().get_all()
        resp.html = api.template('todo.html', todolist_presenter=todolist.data)

    async def on_post(self, req, resp):
        media = await req.media()
        if media.get('action') == FORM_VALUE['ADD_TODO']:
            todolist = await TodoController().add_item(media)
        elif media.get('action') == FORM_VALUE['UPDATE_CHECKLIST']:
            todolist = await TodoController().update_all_from_checklist(media.get_list(FORM_VALUE['CHECKLIST']))
        resp.html = api.template('todo.html', todolist_presenter=todolist.data)

api.add_route('/', TodoRoute)
