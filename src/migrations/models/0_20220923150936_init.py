from typing import List

from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> List[str]:
    return [
        """CREATE TABLE IF NOT EXISTS "items" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "current_status" VARCHAR(3) NOT NULL  /* NEW: NEW\nOLD: OLD */
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""
    ]


async def downgrade(db: BaseDBAsyncClient) -> List[str]:
    return [
        
    ]
