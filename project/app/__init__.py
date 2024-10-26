from .database import Base, engine
from .models import Organization, Storage

def init_db():
    Base.metadata.create_all(bind=engine)