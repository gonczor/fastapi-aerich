from enum import Enum

from pydantic import BaseModel, Field


class ItemStatus(str, Enum):
    NEW = "NEW"
    OLD = "OLD"


class ItemCreate(BaseModel):
    name: str
    current_status: ItemStatus = Field(alias="currentStatus")


class ItemRead(BaseModel):
    id: int
    name: str
    current_status: ItemStatus = Field(alias="currentStatus")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
