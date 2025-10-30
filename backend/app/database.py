"""Database configuration and connection"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlmodel import SQLModel
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL from environment or use default
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/microservice_db"
)

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=os.getenv("DEBUG", "False") == "True",  # Log SQL queries in debug mode
    future=True,
    pool_pre_ping=True,  # Verify connections before using them
    pool_size=5,
    max_overflow=10,
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session,
)


def get_session():
    """Get database session dependency for FastAPI"""
    with SessionLocal() as session:
        yield session


def init_db():  # pragma: no cover
    """Initialize database tables - production only, not used in tests"""
    SQLModel.metadata.create_all(engine)
