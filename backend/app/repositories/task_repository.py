# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from ..models import Task
from .base_repository import BaseRepository

class TaskRepository(BaseRepository):
    """Repository for Task entity."""

    model = Task

    def get_by_outlet(self, outlet_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        """Get tasks for an outlet."""
        query = select(Task).where(Task.outlet_id == outlet_id).offset(skip).limit(limit)
        results = self.db.execute(query).scalars().all()
        return list(results)