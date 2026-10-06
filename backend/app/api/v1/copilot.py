# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ...core.database import get_db_session
from ...schemas.copilot import CopilotRequest, CopilotResponse
from ...services.ai_service import AIService

router = APIRouter(prefix="/copilot", tags=["copilot"])

@router.post("/ask", response_model=CopilotResponse)
async def ask_copilot(
    request_data: CopilotRequest,
    db = Depends(get_db_session)
):
    """Ask the AI copilot for assistance."""
    ai_service = AIService(db)
    response = await ai_service.generate_response(request_data)
    return response