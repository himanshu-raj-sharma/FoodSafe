# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime
import enum

from .base import Base

class NotificationType(str, enum.Enum):
    TASK_ASSIGNED = "TASK_ASSIGNED"
    INCIDENT_REPORTED = "INCIDENT_REPORTED"
    CAPA_CREATED = "CAPA_CREATED"
    CAPA_DUE = "CAPA_DUE"
    REMINDER = "REMINDER"
    SYSTEM = "SYSTEM"

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String(50), nullable=False)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=True)
    is_read = Column(Boolean, default=False)
    related_entity_type = Column(String(50), nullable=True)
    related_entity_id = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    read_at = Column(DateTime(timezone=True), nullable=True)

    organization = relationship("Organization")
    user = relationship("User")

    def __repr__(self):
        return f"<Notification(id={self.id}, type='{self.type}')>"
