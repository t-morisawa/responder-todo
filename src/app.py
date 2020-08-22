import responder
import random

api = responder.API()
todolist = [2,3,4,5,6]

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

@api.route("/random")
def test_random(req, resp):
    resp.text = str(random.random())

@api.route("/test")
async def get_html(req, resp):
    resp.html = api.template('test.html', todolist=todolist)

@api.route("/todo")
async def add_todo(req, resp):
    media = await req.media()
    print(media)
    # 追加処理をここに実装する
    api.redirect(resp, '/test')

@api.route("/todolist")
async def update_todolist(req, resp):
    media = await req.media()
    print(media)
    # todolistの更新処理を入れる
    api.redirect(resp, '/test')

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
