from functools import lru_cache

from pydantic import BaseSettings


class Config(BaseSettings):
    db_url: str = "sqlite:///"



@lru_cache
def get_config():
    return Config()


@lru_cache
def get_tortoise_config():
    config = get_config()
    return {
        "connections": {"default": config.db_url},
        "apps": {
            "models": {
                "models": ["src.models", "aerich.models"],
                "default_connection": "default",
            },
        },
    }
