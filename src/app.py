import responder
import random

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

@api.route("/random")
def test_random(req, resp):
    resp.text = str(random.random())

@api.route("/test")
async def get_html(req, resp):
    media = {}
    resp.html = api.template('test.html', params=media)

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
    # 追加処理をここに実装する
    api.redirect(resp, '/test')

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
