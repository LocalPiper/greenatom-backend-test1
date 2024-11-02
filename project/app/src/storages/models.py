
import enum
from sqlalchemy import Column, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship
from app.src.database import Base

class WasteType(str, enum.Enum):
    BIO = "bio"
    GLASS = "glass"
    PLASTIC = "plastic"

class Storage(Base):
    __tablename__ = "storages"
    id = Column(Integer, primary_key=True, index=True)
    waste_type = Column(Enum(WasteType), index=True)
    size = Column(Integer)
    capacity = Column(Integer)

    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    wsa_id = Column(Integer, ForeignKey("wsas.id"), nullable=True)

    organization = relationship("Organization", back_populates="storages")
    wsa = relationship("WSA", back_populates="storages")