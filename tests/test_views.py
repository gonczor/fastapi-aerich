import asyncio

from fastapi.testclient import TestClient
import pytest
import pytest_asyncio

from src.models import Item
from src.repository import ItemRepository
from src.schemas import ItemStatus


@pytest_asyncio.fixture()
async def item() -> Item:
    repository = ItemRepository()
    item = Item(name="test", current_status=ItemStatus.NEW)
    await repository.save_item(item)
    return item


def test_hello_world(test_client: TestClient):
    response = test_client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "world!"}


@pytest.mark.asyncio
async def test_list_items(item, test_client):
    response = test_client.get("/api/items")
    
    assert response.status_code == 200
    assert response.json() == [{
        "id": item.id,
        "name": item.name,
        "currentStatus": item.current_status.value
    }]


@pytest.mark.asyncio
async def test_create_item(test_client):
    repository = ItemRepository()
    data = {"name": "test_name", "currentStatus": "NEW"}

    response = test_client.post("/api/items", json=data)

    assert response.status_code == 201
    item = await repository.get_item(response.json()["id"])
    assert item.name == data["name"]
    assert item.current_status == data["currentStatus"]


@pytest.mark.asyncio
async def test_expire_item(item, test_client):
    repository = ItemRepository()

    response = test_client.patch(f"/api/items/{item.id}/expire")

    assert response.status_code == 200
    item = await repository.get_item(item.id)
    assert item.name == "[expired]"
    assert item.current_status == ItemStatus.OLD
