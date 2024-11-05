from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.src.database import Base


class WSA(Base):
    __tablename__ = "wsas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    storages = relationship("StorageModel", back_populates="wsa")
