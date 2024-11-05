from pydantic import BaseModel
from typing import Optional
from app.src.schemas import WasteType


class WasteTransferRequest(BaseModel):
    organization_name: str
    waste_type: WasteType
    quantity: int


class WasteGenerationRequest(BaseModel):
    organization_name: str
    waste_type: Optional[WasteType] = None


class WasteRecycleRequest(BaseModel):
    wsa_name: str
    waste_type: Optional[WasteType] = None
