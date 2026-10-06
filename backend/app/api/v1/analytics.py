# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...core.database import get_db_session
from ...schemas.risk import RiskResponse
from ...services.risk_service import RiskService

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/risk/{organization_id}", response_model=RiskResponse)
async def get_organization_risk(
    organization_id: int,
    db = Depends(get_db_session)
):
    """Get risk analysis for an organization."""
    risk_service = RiskService(db)
    risk_data = risk_service.calculate_organization_risk(organization_id)
    return risk_data