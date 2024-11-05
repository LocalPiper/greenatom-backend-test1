from typing import Optional
from pydantic import BaseModel
from app.src.schemas import WasteType


class StorageBase(BaseModel):
    waste_type: WasteType
    size: int
    capacity: int


class StorageCreate(StorageBase):
    organization_id: Optional[int] = None
    wsa_id: Optional[int] = None


class Storage(StorageBase):
    id: int

    class Config:
        from_attributes = True
