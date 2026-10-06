# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional
from datetime import datetime

from .base import Base

class AIResponse(Base):
    __tablename__ = "ai_responses"

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, ForeignKey("ai_requests.id"), nullable=False)
    response_text = Column(Text, nullable=True)
    suggestions = Column(Text, nullable=True)  # JSON
    risk_score = Column(Integer, nullable=True)
    confidence_score = Column(Integer, nullable=True)
    requires_human_review = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    reviewed_at = Column(DateTime(timezone=True), nullable=True)
    reviewed_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    request = relationship("AIRequest", back_populates="responses")
    reviewer = relationship("User", foreign_keys=[reviewed_by])

    def __repr__(self):
        return f"<AIResponse(id={self.id}, request_id={self.request_id})>"
