# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select, func
from typing import List, Optional
from ..models import Batch
from .base_repository import BaseRepository

class BatchRepository(BaseRepository):
    """Repository for Batch entity."""

    model = Batch

    def get_by_supplier(self, supplier_id: int, skip: int = 0, limit: int = 100) -> List[Batch]:
        """Get batches for a supplier."""
        query = select(Batch).where(Batch.supplier_id == supplier_id).offset(skip).limit(limit)
        results = self.db.execute(query).scalars().all()
        return list(results)