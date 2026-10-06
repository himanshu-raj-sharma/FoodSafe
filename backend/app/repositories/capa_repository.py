# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select, func
from typing import List, Optional
from datetime import datetime
from ..models import CorrectiveAction
from .base_repository import BaseRepository

class CorrectiveActionRepository(BaseRepository):
    """Repository for CorrectiveAction entity."""

    model = CorrectiveAction

    def get_overdue(self, organization_id: int, skip: int = 0, limit: int = 100) -> List[CorrectiveAction]:
        """Get overdue corrective actions."""
        query = select(CorrectiveAction).where(
            CorrectiveAction.organization_id == organization_id,
            CorrectiveAction.due_date < datetime.now(),
            CorrectiveAction.status.in_(["OPEN", "ASSIGNED", "IN_PROGRESS"]),
        ).offset(skip).limit(limit)
        results = self.db.execute(query).scalars().all()
        return list(results)