from enum import Enum
from pydantic import BaseModel
from typing import Optional

class WasteType(str, Enum):
    BIO = "bio"
    GLASS = "glass"
    PLASTIC = "plastic"

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