# yourapp.models.py

import time
import os
from tortoise import Tortoise
from tortoise.models import Model
from tortoise import fields


if os.environ.get("ENV") == "local":
    db_url="mysql://root:password@db/todolist"
else:
    PROJECT_NAME = os.environ.get("PROJECT_NAME")
    db_url=f"mysql://root:password@localhost/todolist?unix_socket=/cloudsql/{PROJECT_NAME}:asia-northeast1:todolist"


class Todolist(Model):
    id = fields.IntField(pk=True)
    checked = fields.BooleanField()
    task = fields.TextField()


async def init():
    # ローカルでMySQLサーバより先にアプリが起動してしまう可能性があるのでリトライ制御する
    while True:
        try:
            await Tortoise.init(
                db_url=db_url, modules={"models": ["db"]}
            )
            break
        except Exception:
            time.sleep(1)
