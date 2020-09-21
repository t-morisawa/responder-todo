import responder
import random
import os
import time
from todo import Todo, Todolist
from tortoise import Tortoise
from models import Todolist
from repository import TodolistRepository


api = responder.API()

if os.environ.get("ENV") == "local":
    db_url="mysql://root:password@db/todolist"
else:
    PROJECT_NAME = os.environ.get("PROJECT_NAME")
    db_url=f"mysql://root:password@localhost/todolist?unix_socket=/cloudsql/{PROJECT_NAME}:asia-northeast1:todolist"

@api.on_event("startup")
async def setup():
    # ローカルでMySQLサーバより先にアプリが起動してしまう可能性があるのでリトライ制御する
    while True:
        try:
            await Tortoise.init(
                db_url=db_url, modules={"models": ["models"]}
            )
            break
        except Exception:
            time.sleep(1)

@api.route("/")
def hello_world(req, resp):
    print(os.environ.get("ENV"))
    resp.text = "hello, world!"

@api.route("/test")
async def get_html(req, resp):
    todolist = await TodolistRepository().get_all()
    resp.html = api.template('test.html', todolist_presenter=todolist)

@api.route("/todo")
async def add_todo(req, resp):
    media = await req.media()

    if not media.get('task') is None:
        await TodolistRepository().create_item(task=media.get('task'))

    api.redirect(resp, '/test')

@api.route("/todolist")
async def update_todolist(req, resp):
    media = await req.media()
    checklist = media.get_list('riyu')

    await TodolistRepository().update_checked_from_checklist(checklist)

    api.redirect(resp, '/test')

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
