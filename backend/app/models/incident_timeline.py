# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from typing import Optional

from .base import Base

class IncidentTimeline(Base):
    __tablename__ = "incident_timeline"

    id = Column(Integer, primary_key=True)
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=False)
    event_type = Column(String(100), nullable=False)
    event_description = Column(Text, nullable=True)
    performed_by = Column(Integer, ForeignKey("users.id"))
    performed_at = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    incident = relationship("Incident", back_populates="timeline")

    def __repr__(self):
        return f"<IncidentTimeline(id={self.id}, event='{self.event_type}')>"
