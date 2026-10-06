# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Boolean, Integer, Text, DateTime, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import List, Optional
from datetime import datetime

from .base import Base
class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default="active")
    tier = Column(String(50), default="starter")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    outlets = relationship("Outlet", back_populates="organization")
    users = relationship("User", back_populates="organization")
    members = relationship("OrganizationMembership", back_populates="organization")
    suppliers = relationship("Supplier", back_populates="organization")
    tasks = relationship("Task", back_populates="organization")
    incidents = relationship("Incident", back_populates="organization")
    batches = relationship("Batch", back_populates="organization")
    audit_packs = relationship("AuditPack", back_populates="organization")
    sync_records = relationship("SyncRecord", back_populates="organization")
    audit_logs = relationship("AuditLog", back_populates="organization")

    def __repr__(self):
        return f"<Organization(id={self.id}, name='{self.name}')>"

    @property
    def is_active(self) -> bool:
        return self.status == "active" and self.deleted_at is None