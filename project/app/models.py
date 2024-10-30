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

    storages = relationship("Storage", secondary="organization_storages", back_populates="organizations")

class WSA(Base):
    __tablename__ = "wsas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    storages = relationship("Storage", secondary="wsa_storages", back_populates="wsas")

class Storage(Base):
    __tablename__ = "storages"
    id = Column(Integer, primary_key=True, index=True)
    waste_type = Column(Enum(WasteType), index=True)
    size = Column(Float)
    capacity = Column(Float)

    organizations = relationship("Organization", secondary="organization_storages", back_populates="storages")
    wsas = relationship("WSA", secondary="wsa_storages", back_populates="storages")

class Path(Base):
    __tablename__ = "paths"
    id = Column(Integer, primary_key=True, index=True)
    length = Column(Float)
    bidirectional = Column(Boolean, default=False)

    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    wsa_start_id = Column(Integer, ForeignKey("wsas.id"), nullable=True)
    wsa_end_id = Column(Integer, ForeignKey("wsas.id"), nullable=True)
