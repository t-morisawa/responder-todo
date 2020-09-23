import responder
from db import init as init_db, Todolist as TodolistDriver
from repository import TodolistRepositoryImpl
from form import checklist_from_form
from usecase import UsecaseImpl

api = responder.API()

@api.on_event("startup")
async def setup():
    await init_db()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

class TodoController:
    async def on_get(self, req, resp):
        usecase = UsecaseImpl(TodolistRepositoryImpl(TodolistDriver))
        todolist = await usecase.get_all()
        resp.html = api.template('test.html', todolist_presenter=todolist.data)

    async def on_post(self, req, resp):
        media = await req.media()
        if media.get('action') == 'add_todo':
            if media.get('task') is None:
                api.redirect(resp, '/test')
            usecase = UsecaseImpl(TodolistRepositoryImpl(TodolistDriver))
            await usecase.add_item(task=media.get('task'))
            todolist = await usecase.get_all()
            resp.html = api.template('test.html', todolist_presenter=todolist.data)
        elif media.get('action') == 'update_checklist':
            media = await req.media()
            checklist = checklist_from_form(media)
            usecase = UsecaseImpl(TodolistRepositoryImpl(TodolistDriver))
            await usecase.update_all_from_checklist(checklist)
            todolist = await usecase.get_all()
            resp.html = api.template('test.html', todolist_presenter=todolist.data)

api.add_route('/todo', TodoController)

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
