# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class TaskCompletion(Base):
    __tablename__ = "task_completions"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    outlet_id = Column(Integer, ForeignKey("outlets.id"), nullable=False)
    completion_notes = Column(Text, nullable=True)
    temperature_readings = Column(Text, nullable=True)  # JSON
    photos = Column(Text, nullable=True)  # JSON array of URLs
    completed_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    task = relationship("Task", back_populates="completions")
    user = relationship("User", back_populates="task_completions")
    outlet = relationship("Outlet", back_populates="task_completions")

    def __repr__(self):
        return f"<TaskCompletion(id={self.id}, task_id={self.task_id})>"
