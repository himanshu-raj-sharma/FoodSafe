# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.database import get_db_session
from ..schemas.notification import NotificationCreate, NotificationRead
from ..models import Notification, User
from ..core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=NotificationRead)
async def create_notification(
    notification_data: NotificationCreate,
    db = Depends(get_db_session)
):
    """Create a new notification."""
    # Verify user exists
    user = db.get(User, notification_data.user_id)
    if not user:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
            error_code="resource_not_found",
        )
    # Create notification
    notification = Notification(
        user_id=notification_data.user_id,
        organization_id=notification_data.organization_id,
        type=notification_data.type,
        title=notification_data.title,
        message=notification_data.message,
        is_read=False,
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification