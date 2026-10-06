# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import List, Optional
from datetime import datetime

from .base import Base
class User(Base):
    __tablename__ = "users"
    __table_args__ = (
        Index("idx_users_email", "email"),
        Index("idx_users_username", "username"),
    )

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    phone = Column(String(50), nullable=True)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    email_verified_at = Column(DateTime(timezone=True), nullable=True)
    last_login_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    organization = relationship("Organization", back_populates="users")
    memberships = relationship("OrganizationMembership", back_populates="user")
    tasks = relationship("Task", back_populates="user")
    task_completions = relationship("TaskCompletion", back_populates="user")
    incidents = relationship("Incident", back_populates="reporter")
    assigned_incidents = relationship("Incident", foreign_keys="[Incident.assigned_to_id]", back_populates="assignee")
    assigned_capas = relationship("CorrectiveAction", back_populates="assignee")
    submitted_capas = relationship("CorrectiveAction", foreign_keys=["CorrectiveAction.submitted_by_id"], back_populates="submitter")
    completed_capas = relationship("CorrectiveAction", foreign_keys="[CorrectiveAction.completed_by_id]", back_populates="completer")
    verified_capas = relationship("CorrectiveActionVerification", back_populates="verifier")
    delivered_items = relationship("DeliveryItem", back_populates="delivered_by")
    traceability_events = relationship("TraceabilityEvent", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"

    @property
    def full_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.username

    @property
    def is_active_user(self) -> bool:
        return self.is_active and self.deleted_at is None
