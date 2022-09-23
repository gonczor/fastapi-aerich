from typing import List

from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> List[str]:
    return [
        """ALTER TABLE "items" ADD "read_counter" INT NOT NULL  DEFAULT 0"""
    ]


async def downgrade(db: BaseDBAsyncClient) -> List[str]:
    return [
        """ALTER TABLE "items" DROP COLUMN "read_counter\""""
    ]
