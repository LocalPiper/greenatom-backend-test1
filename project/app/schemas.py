from pydantic import BaseModel
from enum import Enum
from typing import Optional

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



class OrganizationBase(BaseModel):
    name: str

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int

    class Config:
        orm_mode = True

class WSABase(BaseModel):
    name: str

class WSACreate(WSABase):
    pass

class WSA(WSABase):
    id: int

    class Config:
        orm_mode = True

class PathBase(BaseModel):
    length: int
    bidirectional: Optional[bool] = False

class PathCreate(PathBase):
    organization_id: Optional[int] = None
    wsa_start_id: Optional[int] = None
    wsa_end_id: Optional[int] = None

class Path(PathBase):
    id: int

    class Config:
        orm_mode = True