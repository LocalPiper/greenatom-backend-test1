from enum import Enum
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
    pass

class Storage(StorageBase):
    id: int

    class Config:
        orm_mode = True
