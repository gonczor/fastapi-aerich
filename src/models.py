from tortoise.models import Model
from tortoise import fields

from src.schemas import ItemStatus


class Item(Model):
    id = fields.BigIntField(pk=True)
    name = fields.TextField()
    current_status = fields.CharEnumField(ItemStatus)
    read_counter = fields.IntField(default=0)

    def expire(self):
        self.current_status = ItemStatus.OLD
        self.name = "[expired]"

    class Meta:
        table = "items"