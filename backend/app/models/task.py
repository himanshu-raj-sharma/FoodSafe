# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime
import enum

from .base import Base

class TaskStatus(str, enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    SKIPPED = "SKIPPED"
    OVERDUE = "OVERDUE"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    outlet_id = Column(Integer, ForeignKey("outlets.id"), nullable=False)
    template_id = Column(Integer, ForeignKey("task_templates.id"), nullable=True)
    assigned_to = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default="PENDING")
    scheduled_date = Column(DateTime(timezone=True), nullable=True)
    completed_date = Column(DateTime(timezone=True), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    organization = relationship("Organization", back_populates="tasks")
    outlet = relationship("Outlet", back_populates="tasks")
    template = relationship("TaskTemplate", back_populates="tasks")
    assignee = relationship("User", back_populates="tasks")
    completions = relationship("TaskCompletion", back_populates="task")

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}')>"
