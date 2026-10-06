# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...core.database import get_db_session
from ...schemas.sync import SyncRequest, SyncResponse
from ...models import SyncRecord, Organization
from ...core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/sync", tags=["sync"])

@router.post("/", response_model=SyncResponse)
async def sync_data(
    sync_data: SyncRequest,
    db = Depends(get_db_session)
):
    """Sync data from client to server."""
    # Verify organization exists
    organization = db.get(Organization, sync_data.organization_id)
    if not organization:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
            error_code="organization_not_found",
        )
    # Process sync request
    sync_record = SyncRecord(
        organization_id=sync_data.organization_id,
        last_synced_at=sync_data.last_synced_at,
        pending_changes=sync_data.pending_changes,
        status="SYNCING",
    )
    db.add(sync_record)
    db.commit()
    db.refresh(sync_record)
    # Return sync response
    return SyncResponse(
        sync_id=sync_record.id,
        status="SYNCED",
        synced_at=sync_record.created_at,
        conflicts=[],
    )