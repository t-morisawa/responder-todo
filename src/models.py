# yourapp.models.py

from tortoise.models import Model
from tortoise import fields


class Todolist(Model):
    id = fields.IntField(pk=True)
    checked = fields.BooleanField()
    task = fields.TextField()
