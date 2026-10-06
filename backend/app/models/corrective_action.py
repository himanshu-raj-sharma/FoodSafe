# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime
import enum

from .base import Base

class CAPAStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    APPROVED = "APPROVED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    VERIFIED = "VERIFIED"
    CLOSED = "CLOSED"

class CorrectiveAction(Base):
    __tablename__ = "corrective_actions"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    type = Column(String(50), nullable=False)  # corrective or preventive
    status = Column(Enum(CAPAStatus), default=CAPAStatus.DRAFT)
    priority = Column(String(20), default="medium")
    assigned_to = Column(Integer, ForeignKey("users.id"))
    due_date = Column(DateTime(timezone=True), nullable=True)
    completed_date = Column(DateTime(timezone=True), nullable=True)
    submitted_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    completed_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    incident = relationship("Incident", back_populates="capas")
    assignee = relationship("User", back_populates="assigned_capas")
    submitter = relationship("User", foreign_keys=[submitted_by], back_populates="submitted_capas")
    completer = relationship("User", foreign_keys=[completed_by], back_populates="completed_capas")
    verifications = relationship("CorrectiveActionVerification", back_populates="capa")

    def __repr__(self):
        return f"<CorrectiveAction(id={self.id}, title='{self.title}')>"
