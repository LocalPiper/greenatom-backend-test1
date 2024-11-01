from typing import Optional
from pydantic import BaseModel


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