# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.database import get_db_session
from ..schemas.incident import IncidentCreate, IncidentRead, IncidentUpdate
from ..models import Incident, Outlet
from ..core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=IncidentRead)
async def create_incident(
    incident_data: IncidentCreate,
    db = Depends(get_db_session)
):
    """Create a new incident."""
    # Verify outlet exists
    outlet = db.get(Outlet, incident_data.outlet_id)
    if not outlet:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Outlet not found",
            error_code="resource_not_found",
        )
    # Create incident
    incident = Incident(
        outlet_id=incident_data.outlet_id,
        organization_id=incident_data.organization_id,
        title=incident_data.title,
        description=incident_data.description,
        type=incident_data.type,
        severity=incident_data.severity,
        reported_by=incident_data.reported_by,
        reported_at=incident_data.reported_at,
        status="OPEN",
        supplier=incident_data.supplier,
        delivery=incident_data.delivery,
        batch=incident_data.batch,
        immediate_action=incident_data.immediate_action,
        root_cause=incident_data.root_cause,
        assigned_to=incident_data.assigned_to,
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident