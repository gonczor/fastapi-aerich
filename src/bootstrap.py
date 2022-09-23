import asyncio

from tortoise import Tortoise

from src.config import get_tortoise_config


def init():
    config = get_tortoise_config()
    event_loop = asyncio.ensure_future(Tortoise.init(config=config))
