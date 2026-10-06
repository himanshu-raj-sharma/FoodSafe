# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Author: Himanshu Raj

from fastapi import HTTPException, status
from typing import Any, Dict, Optional
from enum import Enum
class FoodsafeErrorCode(str, Enum):
    """Error codes for FoodSafe API.

    Owner: Himanshu Raj
    """
    # Authentication
    INVALID_CREDENTIALS = "invalid_credentials"
    TOKEN_EXPIRED = "token_expired"
    TOKEN_INVALID = "token_invalid"
    USER_NOT_FOUND = "user_not_found"
    EMAIL_ALREADY_EXISTS = "email_already_exists"
    INCORRECT_PASSWORD = "incorrect_password"

    # Authorization
    INSUFFICIENT_PERMISSIONS = "insufficient_permissions"
    TENANT_ACCESS_DENIED = "tenant_access_denied"
    ORGANIZATION_NOT_FOUND = "organization_not_found"

    # Business
    CONFLICTING_OPERATION = "conflicting_operation"
    VALIDATION_ERROR = "validation_error"
    RESOURCE_NOT_FOUND = "resource_not_found"
    OPERATION_NOT_ALLOWED = "operation_not_allowed"

    # System
    INTERNAL_SERVER_ERROR = "internal_server_error"
    DATABASE_ERROR = "database_error"
    CONFIGURATION_ERROR = "configuration_error"
class FoodsafeHTTPException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
        error_code: FoodsafeErrorCode,
        headers: Optional[Dict[str, str]] = None,
    ):
        super().__init__(status_code, detail, headers)
        self.error_code = error_code
class ValidationError(FoodsafeHTTPException):
    def __init__(self, detail: str, field: Optional[str] = None):
        super(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
            error_code=FoodsafeErrorCode.VALIDATION_ERROR,
            headers=None,
        )
        self.field = field
class ConflictError(FoodsafeHTTPException):
    def __init__(self, detail: str):
        super(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
            error_code=FoodsafeErrorCode.CONFLICTING_OPERATION,
            headers=None,
        )
class ResourceNotFoundError(FoodsafeHTTPException):
    def __init__(self, resource_type: str, resource_id: Any):
        detail = f"{resource_type} with ID '{resource_id}' not found"
        super(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
            error_code=FoodsafeErrorCode.RESOURCE_NOT_FOUND,
            headers=None,
        )
class UnauthorizedError(FoodsafeHTTPException):
    def __init__(self, detail: str = "Unauthorized"):
        super(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            error_code=FoodsafeErrorCode.INVALID_CREDENTIALS,
            headers={"WWW-Authenticate": "Bearer"},
        )
class ForbiddenError(FoodsafeHTTPException):
    def __init__(self, detail: str = "Forbidden"):
        super(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
            error_code=FoodsafeErrorCode.INSUFFICIENT_PERMISSIONS,
            headers=None,
        )
class TenantAccessError(FoodsafeHTTPException):
    def __init__(self, detail: str = "Access denied to this tenant's data"):
        super(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
            error_code=FoodsafeErrorCode.TENANT_ACCESS_DENIED,
            headers=None,
        )
class DatabaseError(FoodsafeHTTPException):
    def __init__(self, detail: str):
        super(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            error_code=FoodsafeErrorCode.DATABASE_ERROR,
            headers=None,
        )