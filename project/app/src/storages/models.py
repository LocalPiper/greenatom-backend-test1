from sqlalchemy import Column, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship
from app.src.database import Base
from app.src.schemas import WasteType


class StorageModel(Base):
    __tablename__ = "storages"
    id = Column(Integer, primary_key=True, index=True)
    waste_type = Column(Enum(WasteType), index=True)
    size = Column(Integer)
    capacity = Column(Integer)

    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    wsa_id = Column(Integer, ForeignKey("wsas.id"), nullable=True)

    organization = relationship("Organization", back_populates="storages")
    wsa = relationship("WSAModel", back_populates="storages")
