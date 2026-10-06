# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional

from .base import Base

class CorrectiveActionVerification(Base):
    __tablename__ = "corrective_action_verifications"

    id = Column(Integer, primary_key=True)
    capa_id = Column(Integer, ForeignKey("corrective_actions.id"), nullable=False)
    verifier_id = Column(Integer, ForeignKey("users.id"))
    verification_result = Column(String(50), nullable=False)  # passed, failed
    comments = Column(Text, nullable=True)
    verified_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    capa = relationship("CorrectiveAction", back_populates="verifications")
    verifier = relationship("User", back_populates="verified_capas")

    def __repr__(self):
        return f"<CorrectiveActionVerification(id={self.id}, result='{self.verification_result}')>"
