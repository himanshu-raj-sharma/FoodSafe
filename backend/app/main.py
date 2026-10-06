# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Author: Himanshu Raj

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import time

from .core.config import get_settings
from .core.database import create_database_indexes
from .api.v1 import api_router
from .core.exceptions import FoodsafeHTTPException

Settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    # Startup
    print("Starting FoodSafe backend...")

    # Initialize database indexes
    create_database_indexes()

    # Log startup
    import logging
    logger = logging.getLogger("foodsafe")
    logger.info("FoodSafe backend started successfully")

    yield

    # Shutdown
    print("Shutting down FoodSafe backend...")
    logger.info("FoodSafe backend shut down successfully")

app = FastAPI(
    title="FoodSafe API",
    description="Food Safety Operations & Intelligence Platform API",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add custom exception handlers
@app.exception_handler(FoodsafeHTTPException)
async def foodsafe_exception_handler(request: Request, exc: FoodsafeHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.error_code.value,
                "message": exc.detail,
            }
        },
        headers=exc.headers,
    )

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": time.time()}

@app.get("/ready")
async def readiness_check():
    """Readiness check endpoint."""
    try:
        from .core.database import engine
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        return {"status": "ready"}
    except Exception as e:
        raise FoodsafeHTTPException(
            status_code=503,
            detail="Service not ready",
            error_code="service_not_ready",
        )

app.include_router(api_router)