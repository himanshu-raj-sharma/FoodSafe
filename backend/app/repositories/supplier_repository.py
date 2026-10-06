# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select, func
from typing import List, Optional
from ..models import Supplier
from .base_repository import BaseRepository

class SupplierRepository(BaseRepository):
    """Repository for Supplier entity."""

    model = Supplier

    def get_by_organization(self, organization_id: int, skip: int = 0, limit: int = 100) -> List[Supplier]:
        """Get suppliers for an organization."""
        query = select(Supplier).where(Supplier.organization_id == organization_id).offset(skip).limit(limit)
        results = self.db.execute(query).scalars().all()
        return list(results)

    def get_high_risk(self, organization_id: int, threshold: int = 70) -> List[Supplier]:
        """Get high-risk suppliers."""
        query = select(Supplier).where(
            Supplier.organization_id == organization_id,
            Supplier.risk_score >= threshold,
        )
        results = self.db.execute(query).scalars().all()
        return list(results)