# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Float, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime
import enum

from .base import Base

class RecallStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class Recall(Base):
    __tablename__ = "recalls"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    recall_number = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    reason = Column(Text, nullable=True)
    status = Column(String(50), default="DRAFT")
    recalled_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    recall_date = Column(DateTime(timezone=True), nullable=True)
    completed_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    organization = relationship("Organization", back_populates="recalls")
    items = relationship("RecallItem", back_populates="recall")
    recalled_by_user = relationship("User", foreign_keys=[recalled_by])

    def __repr__(self):
        return f"<Recall(id={self.id}, number='{self.recall_number}')>"
