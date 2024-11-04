from enum import Enum
from pydantic import BaseModel

class WasteType(str, Enum):
    BIO = "bio"
    GLASS = "glass"
    PLASTIC = "plastic"

class WasteTransferRequest(BaseModel):
    organization_name: str
    waste_type: WasteType
    quantity: int