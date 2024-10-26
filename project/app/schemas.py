from pydantic import BaseModel

class OrganizationCreate(BaseModel):
    name: str

class StorageCreate(BaseModel):
    location: str
    waste_type: str
    capacity: int