# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from ..models import User
from .base_repository import BaseRepository

class UserRepository(BaseRepository):
    """Repository for User entity."""

    model = User

    def get_by_email(self, email: str, organization_id: int) -> Optional[User]:
        """Get user by email within an organization."""
        query = select(User).where(
            User.email == email,
            User.organization_id == organization_id,
        )
        result = self.db.scalar(query)
        return result