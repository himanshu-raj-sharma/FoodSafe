# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Author: Himanshu Raj

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
from sqlalchemy.pool import QueuePool
from contextlib import contextmanager
from typing import Generator
from .config import get_settings

Settings = get_settings()

engine = create_engine(
    Settings.DATABASE_URL,
    poolclass=QueuePool,
    pool_size=Settings.DATABASE_POOL_SIZE,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=3600,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    """Base class for all database models."""

    # Common fields that all models should have
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    """Database session context manager."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
def create_database_indexes():
    """Create any missing indexes."""
    # This can be implemented as needed
    pass