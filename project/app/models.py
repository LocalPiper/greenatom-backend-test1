from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base
import enum

class WasteType(str, enum.Enum):
    BIO = "bio"
    GLASS = "glass"
    PLASTIC = "plastic"

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    storages = relationship("Storage", back_populates="organization")

class WSA(Base):
    __tablename__ = "wsas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    storages = relationship("Storage", back_populates="wsa")

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

class Path(Base):
    __tablename__ = "paths"
    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    bidirectional = Column(Boolean, default=False)

    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    wsa_start_id = Column(Integer, ForeignKey("wsas.id"), nullable=True)
    wsa_end_id = Column(Integer, ForeignKey("wsas.id"), nullable=True)
