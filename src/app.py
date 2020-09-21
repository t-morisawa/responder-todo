import responder
from db import init as init_db
from repository import TodolistRepositoryImpl
from form import checklist_from_form


api = responder.API()

@api.on_event("startup")
async def setup():
    await init_db()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

@api.route("/test")
async def get_html(req, resp):
    todolist = await TodolistRepositoryImpl().get_all()
    resp.html = api.template('test.html', todolist_presenter=todolist)

@api.route("/todo")
async def add_todo(req, resp):
    media = await req.media()

    if not media.get('task') is None:
        await TodolistRepositoryImpl().add_item(task=media.get('task'))

    api.redirect(resp, '/test')

@api.route("/todolist")
async def update_todolist(req, resp):
    media = await req.media()
    checklist = checklist_from_form(media)

    await TodolistRepositoryImpl().update_checked_from_checklist(checklist)

    api.redirect(resp, '/test')

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
