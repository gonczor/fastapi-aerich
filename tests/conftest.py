import asyncio

from aerich import Command
from fastapi.testclient import TestClient
import pytest
import pytest_asyncio
from tortoise import Tortoise

from src.main import app
from src.models import Item


@pytest.fixture()
def test_client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def clean_db():
    await Item.all().delete()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def disconnect_db():
    """
    Important fixture. Without it at the end of the tests the test framework would hang
    waiting for the connection termination.
    """
    yield
    await Tortoise.close_connections()
