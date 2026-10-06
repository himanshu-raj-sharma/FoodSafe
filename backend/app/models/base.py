# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional

from ..core.database import Base
class TimestampMixin:
    """Mixin class for models with created_at and updated_at timestamps."""

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
class SoftDeleteMixin:
    """Mixin class for models with soft delete functionality."""

    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def is_deleted(self) -> bool:
        return self.deleted_at is not None
class BaseModel(Base, TimestampMixin, SoftDeleteMixin):
    """Base model class combining timestamps and soft delete."""

    __abstract__ = True

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"