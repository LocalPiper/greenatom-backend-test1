from typing import Optional
from pydantic import BaseModel, Field, field_validator, model_validator
from app.src.schemas import WasteType


class StorageBase(BaseModel):
    waste_type: WasteType
    size: int = Field(..., ge=0, description="Size must be greater or equal to 0")
    capacity: int = Field(
        ..., ge=0, description="Capacity must be greater or equal to 0"
    )


class StorageCreate(StorageBase):
    organization_id: Optional[int] = None
    wsa_id: Optional[int] = None

    @field_validator("organization_id", "wsa_id", mode="before")
    def ids_must_be_positive(cls, value, field):
        if value is not None and value <= 0:
            raise ValueError(f"{field.field_name} must be greater than 0")
        return value

    @model_validator(mode="before")
    def validate_storage(cls, values):
        size = values.get("size")
        capacity = values.get("capacity")

        if size > capacity:
            raise ValueError("Size can't be greater than Capacity")
        organization_id = values.get("organization_id")
        wsa_id = values.get("wsa_id")
        if (organization_id is None and wsa_id is None) or (
            organization_id is not None and wsa_id is not None
        ):
            raise ValueError(
                "Either organization_id or wsa_id must be provided, but not both"
            )
        return values


class Storage(StorageBase):
    id: int

    class Config:
        from_attributes = True
