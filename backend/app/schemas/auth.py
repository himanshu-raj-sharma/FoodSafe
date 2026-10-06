# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user_id: int
    organization_id: int
    expires_in: int

    class Config:
        from_attributes = True

class RefreshTokenRequest(BaseModel):
    refresh_token: str = Field(..., description="Refresh token from auth response")

class CurrentUserResponse(BaseModel):
    id: int
    email: str
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    organization_id: int
    organization_name: str
    is_active: bool
    is_verified: bool
    roles: list[str]
    permissions: list[str]
    created_at: datetime

    class Config:
        from_attributes = True