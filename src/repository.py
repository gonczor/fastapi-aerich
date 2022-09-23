from typing import Iterable
from src.models import Item

class ItemRepository:
    async def list_items(self) -> Iterable[Item]:
        return await Item.all()

    async def save_item(self, item: Item):
        await item.save()

    async def get_item(self, item_id: int) -> Item:
        return await Item.get(id=item_id)
