from sqlalchemy import Boolean, Column, ForeignKey, Integer
from app.src.database import Base

class Path(Base):
    __tablename__ = "paths"
    id = Column(Integer, primary_key=True, index=True)
    length = Column(Integer)
    bidirectional = Column(Boolean, default=False)

    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=True)
    wsa_start_id = Column(Integer, ForeignKey("wsas.id"), nullable=True)
    wsa_end_id = Column(Integer, ForeignKey("wsas.id"), nullable=True)
