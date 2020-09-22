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

@api.route("/test")
async def get_html(req, resp):
    usecase = UsecaseImpl(TodolistRepositoryImpl(TodolistDriver))
    todolist = await usecase.get_all()
    resp.html = api.template('test.html', todolist_presenter=todolist.data)

@api.route("/todo")
async def add_todo(req, resp):
    media = await req.media()
    if media.get('task') is None:
        api.redirect(resp, '/test')
    usecase = UsecaseImpl(TodolistRepositoryImpl(TodolistDriver))
    await usecase.add_item(task=media.get('task'))

    api.redirect(resp, '/test')

@api.route("/todolist")
async def update_todolist(req, resp):
    media = await req.media()
    checklist = checklist_from_form(media)
    usecase = UsecaseImpl(TodolistRepositoryImpl(TodolistDriver))
    await usecase.update_all_from_checklist(checklist)

    api.redirect(resp, '/test')

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
