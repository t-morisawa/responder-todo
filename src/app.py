import responder
import random

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

@api.route("/random")
def test_random(req, resp):
    resp.text = str(random.random())

if __name__ == '__main__':
    api.run(address='0.0.0.0', port=80)
