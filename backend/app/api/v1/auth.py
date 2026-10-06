# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.core.database import get_db_session
from app.core.config import get_settings, Settings
from app.core.security import verify_token, create_access_token, create_refresh_token, hash_password, verify_password
from app.core.exceptions import FoodsafeHTTPException, FoodsafeErrorCode
from app.models import User, Organization, Role, OrganizationMembership
from app.schemas.auth import AuthResponse, CurrentUserResponse

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_data: dict,
    db: Session = Depends(get_db_session),
):
    """Register a new user."""
    from app.schemas.user import UserCreate
    # Validate and create user
    user_in = UserCreate(**user_data)
    user_password = user_in.password
    user_create = User(
        username=user_in.username,
        email=user_in.email,
        password_hash=hash_password(user_password),
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        phone=user_in.phone,
        organization_id=user_in.organization_id,
    )
    db.add(user_create)
    db.commit()
    db.refresh(user_create)
    return {"message": "User registered successfully"}

@router.post("/login", response_model=dict)
async def login(
    credentials: dict,
    db: Session = Depends(get_db_session),
):
    """Login and receive tokens."""
    email = credentials.get("email")
    password = credentials.get("password")
    # Find user
    stmt = select(User).where(User.email == email)
    user = db.scalar(stmt)
    if not user or not verify_password(password, user.password_hash):
        raise FoodsafeHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            error_code=FoodsafeErrorCode.INVALID_CREDENTIALS,
        )
    # Check user is active
    if not user.is_active or user.deleted_at is not None:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is disabled or deleted",
            error_code=FoodsafeErrorCode.USER_NOT_FOUND,
        )
    # Check organization is active
    if not user.organization.is_active:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Organization is disabled",
            error_code=FoodsafeErrorCode.ORGANIZATION_NOT_FOUND,
        )
    # Create tokens
    access_token = create_access_token({"sub": str(user.id), "org_id": user.organization_id})
    refresh_token = create_refresh_token({"sub": str(user.id), "org_id": user.organization_id})
    # Get user roles
    user_roles = user.roles if hasattr(user, 'roles') and user.roles else []
    user_permissions = []
    for role in user_roles:
        if hasattr(role, 'permissions'):
            for perm in role.permissions:
                if perm.is_active:
                    user_permissions.append(perm.name)
    # Build response
    auth_response = AuthResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        user_id=user.id,
        organization_id=user.organization_id,
        expires_in=Settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    )
    user_response = CurrentUserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        organization_id=user.organization_id,
        organization_name=user.organization.name if user.organization else "",
        is_active=user.is_active,
        is_verified=user.is_verified,
        roles=[role.name for role in user_roles],
        permissions=user_permissions,
        created_at=user.created_at,
    )
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": user_response.model_dump(),
        "expires_in": Settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    }
