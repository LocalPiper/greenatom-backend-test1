from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional


class PathBase(BaseModel):
    length: int = Field(..., gt=0, description="Length must be greater than 0")
    bidirectional: Optional[bool] = False


class PathCreate(PathBase):
    organization_id: Optional[int] = None
    wsa_start_id: int
    wsa_end_id: Optional[int] = None

    @field_validator("organization_id", "wsa_end_id", "wsa_start_id", mode="before")
    def ids_must_be_positive(cls, value, field):
        if value is not None and value <= 0:
            raise ValueError(f"{field.field_name} must be greater than 0")
        return value

    @model_validator(mode="before")
    def validate_organization_and_wsa(cls, values):
        organization_id = values.get("organization_id")
        wsa_end_id = values.get("wsa_end_id")

        if (organization_id is None and wsa_end_id is None) or (
            organization_id is not None and wsa_end_id is not None
        ):
            raise ValueError(
                "Either organization_id or wsa_end_id must be provided, but not both."
            )
        wsa_start_id = values.get("wsa_start_id")
        if wsa_start_id == wsa_end_id:
            raise ValueError("Path cannot point to the same WSA")

        return values


class Path(PathBase):
    id: int

    class Config:
        from_attributes = True
