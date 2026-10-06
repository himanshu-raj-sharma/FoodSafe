# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Author: Himanshu Raj

import logging
from datetime import datetime
from typing import Dict, Any, Optional
from functools import wraps

from .config import get_settings

Settings = get_settings()

# Configure root logger
logging.basicConfig(
    level=getattr(logging, Settings.LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(Settings.LOG_FILE),
    ],
)
logger = logging.getLogger("foodsafe")
def log_request_response(func):
    """Decorator to log request/response details."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        request_id = f"req_{datetime.now().timestamp()}"

        # Add request ID to the request context if available
        try:
            from fastapi import Request
            # This is a simplified version - would need to be adapted for actual request context
            logger.info(f"[{request_id}] Request started for {func.__name__}")
        except ImportError:
            pass

        try:
            result = func(*args, **kwargs)
            duration = (datetime.now() - start_time).total_seconds()
            logger.info(f"[{request_id}] Request completed for {func.__name__} in {duration:.2f}s")
            return result
        except Exception as e:
            duration = (datetime.now() - start_time).total_seconds()
            logger.error(f"[{request_id}] Request failed for {func.__name__} after {duration:.2f}s: {str(e)}")
            raise

    return wrapper
def log_event(
    event_type: str,
    entity_type: str,
    entity_id: Optional[int] = None,
    user_id: Optional[int] = None,
    organization_id: Optional[int] = None,
    details: Optional[Dict[str, Any]] = None,
    level: str = "INFO",
):
    """Log a business event."""
    log_data = {
        "event_type": event_type,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "user_id": user_id,
        "organization_id": organization_id,
        "details": details or {},
        "timestamp": datetime.utcnow().isoformat(),
    }

    getattr(logger, level.lower())(
        f"Business event: {event_type} - {entity_type}#{entity_id if entity_id else 'N/A'}",
        extra=log_data,
    )