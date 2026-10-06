# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Type, TypeVar, Generic, Optional, List

T = TypeVar("T")

class BaseRepository(Generic[T]):
    """Base repository class."""

    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def get_by_id(self, id: int) -> Optional[T]:
        """Get entity by ID."""
        return self.db.get(self.model, id)

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Get all entities with pagination."""
        query = select(self.model).offset(skip).limit(limit)
        results = self.db.execute(query).scalars().all()
        return list(results)

    def create(self, obj_in: dict) -> T:
        """Create a new entity."""
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, id: int, obj_in: dict) -> Optional[T]:
        """Update an entity."""
        db_obj = self.get_by_id(id)
        if not db_obj:
            return None
        for key, value in obj_in.items():
            setattr(db_obj, key, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> bool:
        """Delete an entity."""
        db_obj = self.get_by_id(id)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def exists(self, id: int) -> bool:
        """Check if entity exists."""
        return self.get_by_id(id) is not None