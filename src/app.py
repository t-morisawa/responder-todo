import responder
import random
import os
import time
from todo import Todo, TodolistManager
from tortoise import Tortoise
from models import Todolist


api = responder.API()
# todolist = ['2','3','4','5','6']
todolist_manager = TodolistManager([Todo(True, "買い物"), Todo(False, "洗濯"), Todo(True, "お風呂")])

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
    todolist = await Todolist.all()
    new_todolist = []

    for todo in todolist:
        new_todolist.append(Todo(todo.checked,todo.task))

    todolist_manager.set_todolist(new_todolist)
    resp.html = api.template('test.html', todolist_presenter=todolist_manager.todolist)

@api.route("/todo")
async def add_todo(req, resp):
    media = await req.media()
    print(media)
    # 追加処理
    #DBに以下を登録させる
    if not media.get('task') is None:
        await Todolist.create(checked=False, task=media.get('task'))

    # print(vars(todolist_manager))
    api.redirect(resp, '/test')

@api.route("/todolist")
async def update_todolist(req, resp):
    media = await req.media()
    print(media)
    # todolistの更新処理を入れる

    todolist = media.get_list('riyu')
    print(todolist)

    todolistAll = await Todolist.all()

    for index, item in enumerate(todolistAll):
        if str(index + 1) in todolist:
            item.checked = True
        else:
            item.checked = False

        #セーブの処理を待つ必要がある
        await item.save()

    api.redirect(resp, '/test')

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
