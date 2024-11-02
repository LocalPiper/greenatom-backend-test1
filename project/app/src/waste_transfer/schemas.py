from enum import Enum
from typing import Dict, List
from pydantic import BaseModel

class WasteType(str, Enum):
    BIO = "bio"
    GLASS = "glass"
    PLASTIC = "plastic"

class WasteTransferRequest(BaseModel):
    organization_name: str
    waste_type: WasteType
    quantity: int

class VertexModel(BaseModel):
    sz: int = 0
    cap: int = 0

class EdgeModel(BaseModel):
    next: int
    length: int

class GraphModel(BaseModel):
    vertices: Dict[int, VertexModel]
    edges: Dict[int, List[EdgeModel]]