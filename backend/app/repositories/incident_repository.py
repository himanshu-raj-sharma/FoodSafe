# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select, func
from typing import List, Optional
from ..models import Incident
from .base_repository import BaseRepository

class IncidentRepository(BaseRepository):
    """Repository for Incident entity."""

    model = Incident

    def get_by_organization(self, organization_id: int, skip: int = 0, limit: int = 100) -> List[Incident]:
        """Get incidents for an organization."""
        query = select(Incident).where(Incident.organization_id == organization_id)
        results = self.db.execute(query).scalars().all()
        return list(results)

    def get_by_outlet(self, outlet_id: int, organization_id: int) -> List[Incident]:
        """Get incidents for an outlet."""
        query = select(Incident).where(
            Incident.outlet_id == outlet_id,
            Incident.organization_id == organization_id,
        )
        results = self.db.execute(query).scalars().all()
        return list(results)

    def get_open_incidents(self, organization_id: int) -> List[Incident]:
        """Get open incidents for an organization."""
        query = select(Incident).where(
            Incident.organization_id == organization_id,
            Incident.status.in_(["OPEN", "ACKNOWLEDGED", "INVESTIGATING"]),
        )
        results = self.db.execute(query).scalars().all()
        return list(results)

    def get_critical_incidents(self, organization_id: int) -> List[Incident]:
        """Get critical incidents for an organization."""
        query = select(Incident).where(
            Incident.organization_id == organization_id,
            Incident.severity == "CRITICAL",
            Incident.status.notin_(["CLOSED", "RESOLVED"]),
        )
        results = self.db.execute(query).scalars().all()
        return list(results)