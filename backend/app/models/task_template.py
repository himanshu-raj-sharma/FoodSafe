# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class TaskTemplate(Base):
    __tablename__ = "task_templates"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    task_type = Column(String(50), nullable=False)  # inspection, cleaning, temperature_check, etc.
    frequency = Column(String(50), default="daily")
    checklist_items = Column(Text, nullable=True)
    required_roles = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    organization = relationship("Organization", back_populates="task_templates")
    tasks = relationship("Task", back_populates="template")

    def __repr__(self):
        return f"<TaskTemplate(id={self.id}, title='{self.title}')>"
