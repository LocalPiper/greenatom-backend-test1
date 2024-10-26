from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://fastapi:fastapi@db/project"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False)
base = declarative_base()