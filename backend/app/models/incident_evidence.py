# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional

from .base import Base

class IncidentEvidence(Base):
    __tablename__ = "incident_evidence"

    id = Column(Integer, primary_key=True)
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=False)
    file_url = Column(String(500), nullable=False)
    file_type = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    uploaded_by = Column(Integer, ForeignKey("users.id"))
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    incident = relationship("Incident", back_populates="evidence")

    def __repr__(self):
        return f"<IncidentEvidence(id={self.id}, file='{self.file_url}')>"
