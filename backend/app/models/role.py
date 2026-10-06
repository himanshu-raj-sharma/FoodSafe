# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Table, Boolean, Index, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import List, Optional
from datetime import datetime

from .base import Base
# Association table for many-to-many relationship between Role and Permission
role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("permissions.id"), primary_key=True),
    extend_existing=True,
)
class Role(Base):
    __tablename__ = "roles"
    __table_args__ = (
        Index("idx_roles_name_org", "name", "organization_id"),
    )

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    organization = relationship("Organization", back_populates="roles")
    users = relationship("User", secondary="organization_memberships", back_populates="roles")
    permissions = relationship("Permission", secondary=role_permissions, back_populates="roles")

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}')>"