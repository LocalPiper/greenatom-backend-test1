from enum import Enum
from typing import Optional
from pydantic import BaseModel


class WasteType(str, Enum):
    BIO = "bio"
    GLASS = "glass"
    PLASTIC = "plastic"

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
        orm_mode = True
