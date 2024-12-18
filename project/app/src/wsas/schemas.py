from pydantic import BaseModel


class WSABase(BaseModel):
    name: str


class WSACreate(WSABase):
    pass


class WSA(WSABase):
    id: int

    class Config:
        from_attributes = True
