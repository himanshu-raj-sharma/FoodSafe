# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select, func
from typing import List, Optional
from ..models import Outlet
from .base_repository import BaseRepository

class OutletRepository(BaseRepository):
    """Repository for Outlet entity."""

    model = Outlet

    def get_by_organization(self, organization_id: int, skip: int = 0, limit: int = 100) -> List[Outlet]:
        """Get outlets for an organization."""
        query = select(Outlet).where(Outlet.organization_id == organization_id).offset(skip).limit(limit)
        results = self.db.execute(query).scalars().all()
        return list(results)