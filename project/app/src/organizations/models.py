from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.src.database import Base

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    storages = relationship("Storage", back_populates="organization")