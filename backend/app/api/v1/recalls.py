# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...core.database import get_db_session
from ...schemas.recall import RecallCreate, RecallRead
from ...models import Recall, Batch
from ...core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/recalls", tags=["recalls"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=RecallRead)
async def create_recall(
    recall_data: RecallCreate,
    db = Depends(get_db_session)
):
    """Create a new recall."""
    # Verify batch exists
    batch = db.get(Batch, recall_data.batch_id)
    if not batch:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Batch not found",
            error_code="resource_not_found",
        )
    # Create recall
    recall = Recall(
        batch_id=recall_data.batch_id,
        organization_id=batch.supplier_id,
        recall_type=recall_data.recall_type,
        reason=recall_data.reason,
        status="INITIATED",
    )
    db.add(recall)
    db.commit()
    db.refresh(recall)
    return recall