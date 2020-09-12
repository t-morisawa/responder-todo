import responder
import random
from todo import Todo, TodolistManager
from tortoise import Tortoise
from models import Todolist


api = responder.API()
# todolist = ['2','3','4','5','6']
todolist_manager = TodolistManager([Todo(True, "買い物"), Todo(False, "洗濯"), Todo(True, "お風呂")])

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

@api.route("/db")
async def db_echo(req, resp):
    #接続
    await Tortoise.init(
        db_url="mysql://root:password@db/todolist", modules={"models": ["models"]}
    )
    #登録
    await Todolist.create(checked=False, task="cleaning")

    #取得
    todo = await Todolist.first()

    #表示
    resp.text = f"Hello, {todo.task}"

@api.route("/random")
def test_random(req, resp):
    resp.text = str(random.random())

@api.route("/test")
async def get_html(req, resp):
    #接続
    await Tortoise.init(
        db_url="mysql://root:password@db/todolist", modules={"models": ["models"]}
    )
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
