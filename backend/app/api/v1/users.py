# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.database import get_db_session
from ..schemas.user import UserCreate, UserRead, UserUpdate, UserResponse
from ..models import User, Organization
from ..core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def create_user(
    user_data: UserCreate,
    db = Depends(get_db_session)
):
    """Create a new user."""
    # Check email uniqueness
    from sqlalchemy import select
    stmt = select(User).where(User.email == user_data.email)
    existing = db.scalar(stmt)
    if existing:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists",
            error_code="email_already_exists",
        )
    # Check username uniqueness
    stmt = select(User).where(User.username == user_data.username)
    existing = db.scalar(stmt)
    if existing:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this username already exists",
            error_code="conflicting_operation",
        )
    # Verify organization exists
    organization = db.get(Organization, user_data.organization_id)
    if not organization:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
            error_code="organization_not_found",
        )
    # Create user
    from ..core.security import hash_password
    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        phone=user_data.phone,
        organization_id=user_data.organization_id,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user