import sys

sys.path.append("./")

from sqlmodel import Session, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10, 
    max_overflow=20, 
    pool_timeout=30,
    pool_recycle=1800,
)


Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """ensures the database connection is always closed
    to use this we have to use fastapi.Depends() as an argument in the routes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
