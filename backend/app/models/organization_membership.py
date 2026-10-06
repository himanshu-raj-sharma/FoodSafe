# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Table, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import List, Optional
from datetime import datetime

from .base import Base
# Association table for many-to-many relationship between User and Role
user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
    extend_existing=True,
)
class OrganizationMembership(Base):
    __tablename__ = "organization_memberships"
    __table_args__ = (
        Index("idx_membership_user_org", "user_id", "organization_id"),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=True)
    status = Column(String(50), default="active")
    joined_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="memberships")
    organization = relationship("Organization", back_populates="members")
    role = relationship("Role", back_populates="memberships")

    def __repr__(self):
        return f"<OrganizationMembership(id={self.id}, user_id={self.user_id}, org_id={self.organization_id})>"