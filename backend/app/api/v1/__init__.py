# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from fastapi import APIRouter

from .auth import router as auth_router
from .organizations import router as organizations_router
from .outlets import router as outlets_router
from .users import router as users_router
from .tasks import router as tasks_router
from .incidents import router as incidents_router
from .capa import router as capa_router
from .suppliers import router as suppliers_router
from .batches import router as batches_router
from .recalls import router as recalls_router
from .audits import router as audits_router
from .analytics import router as analytics_router
from .notifications import router as notifications_router
from .copilot import router as copilot_router
from .sync import router as sync_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(auth_router)
api_router.include_router(organizations_router)
api_router.include_router(outlets_router)
api_router.include_router(users_router)
api_router.include_router(tasks_router)
api_router.include_router(incidents_router)
api_router.include_router(capa_router)
api_router.include_router(suppliers_router)
api_router.include_router(batches_router)
api_router.include_router(recalls_router)
api_router.include_router(audits_router)
api_router.include_router(analytics_router)
api_router.include_router(notifications_router)
api_router.include_router(copilot_router)
api_router.include_router(sync_router)