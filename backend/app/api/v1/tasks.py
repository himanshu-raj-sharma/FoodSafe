# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..core.database import get_db_session
from ..schemas.task import TaskCreate, TaskRead, TaskUpdate
from ..models import Task, Outlet
from ..core.exceptions import FoodsafeHTTPException

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskRead)
async def create_task(
    task_data: TaskCreate,
    db = Depends(get_db_session)
):
    """Create a new task."""
    # Verify outlet exists
    outlet = db.get(Outlet, task_data.outlet_id)
    if not outlet:
        raise FoodsafeHTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Outlet not found",
            error_code="resource_not_found",
        )
    # Create task
    task = Task(
        outlet_id=task_data.outlet_id,
        organization_id=task_data.organization_id,
        name=task_data.name,
        description=task_data.description,
        category=task_data.category,
        frequency=task_data.frequency,
        required_evidence=task_data.required_evidence,
        required_note=task_data.required_note,
        threshold=task_data.threshold,
        is_active=task_data.is_active,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task