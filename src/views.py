from fastapi import Depends
from fastapi.routing import APIRouter

from src.schemas import ItemCreate, ItemRead
from src.models import Item
from src.repository import ItemRepository


router = APIRouter(prefix="/api")


@router.get("/items", response_model=list[ItemRead])
async def list_items(item_repository: ItemRepository=Depends(ItemRepository)):
    return await item_repository.list_items()


@router.post("/items", response_model=ItemRead, status_code=201)
async def create_item(data: ItemCreate):
    item = Item(
        name=data.name,
        current_status=data.current_status
    )
    await item.save()
    return item


@router.patch("/items/{item_id}/expire", response_model=ItemRead)
async def expire_item(item_id: int, item_repository: ItemRepository=Depends(ItemRepository)):
    item: Item = await item_repository.get_item(item_id)
    item.expire()
    await item_repository.save_item(item)
    return item
