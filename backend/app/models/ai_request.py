# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class AIRequest(Base):
    __tablename__ = "ai_requests"

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    request_type = Column(String(100), nullable=False)
    prompt = Column(Text, nullable=False)
    context_data = Column(Text, nullable=True)  # JSON
    status = Column(String(50), default="PENDING")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    started_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    organization = relationship("Organization")
    user = relationship("User")
    responses = relationship("AIResponse", back_populates="request")

    def __repr__(self):
        return f"<AIRequest(id={self.id}, type='{self.request_type}')>"
