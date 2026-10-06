# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...core.database import get_db_session
from ...schemas.capa import CAPACreate, CAPARead, CAPAUpdate
from ...models import CorrectiveAction, Incident
from ...core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/capa", tags=["capa"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CAPARead)
async def create_capa(
    capa_data: CAPACreate,
    db = Depends(get_db_session)
):
    """Create a new corrective action."""
    # Verify incident exists
    incident = db.get(Incident, capa_data.incident_id)
    if not incident:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incident not found",
            error_code="resource_not_found",
        )
    # Create CAPA
    capa = CorrectiveAction(
        incident_id=capa_data.incident_id,
        organization_id=capa_data.organization_id,
        title=capa_data.title,
        description=capa_data.description,
        root_cause=capa_data.root_cause,
        corrective_action=capa_data.corrective_action,
        preventive_action=capa_data.preventive_action,
        assigned_to=capa_data.assigned_to,
        due_date=capa_data.due_date,
        priority=capa_data.priority,
        status="OPEN",
    )
    db.add(capa)
    db.commit()
    db.refresh(capa)
    return capa