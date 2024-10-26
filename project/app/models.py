from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from .database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Storage(Base):
    __tablename__ = "storages"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    waste_type = Column(ENUM("bio", "glass", "plastic", name="waste_type"))
    capacity = Column(Integer)
    current_load = Column(Integer, default=0)