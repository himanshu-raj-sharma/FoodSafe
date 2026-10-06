# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Author: Himanshu Raj

import os
from datetime import datetime, timedelta, timezone
from typing import Optional, Union
from uuid import uuid4

import bcrypt
from fastapi import HTTPException, status
from jose import JWTError, jwt

from .config import get_settings

Settings = get_settings()
def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt(Settings.BCRYPT_ROUNDS)
    return bcrypt.hash(password.encode("utf-8"), salt).decode("utf-8")
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hash."""
    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except Exception:
        return False
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=Settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        Settings.JWT_SECRET,
        algorithm="HS256"
    )
    return encoded_jwt
def create_refresh_token(data: dict) -> str:
    """Create a JWT refresh token."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=Settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        Settings.JWT_SECRET,
        algorithm="HS256"
    )
    return encoded_jwt
def verify_token(token: str) -> dict:
    """Verify a JWT token and return its payload."""
    try:
        payload = jwt.decode(
            token,
            Settings.JWT_SECRET,
            algorithms=["HS256"]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
def generate_api_key() -> str:
    """Generate a secure API key."""
    return f"fs_{uuid4().hex}_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}"
def encrypt_sensitive_data(data: str) -> str:
    """Encrypt sensitive data."""
    # TODO: Implement proper encryption
    # For now, just return data as-is
    return data
def decrypt_sensitive_data(encrypted_data: str) -> str:
    """Decrypt sensitive data."""
    # TODO: Implement proper decryption
    # For now, just return data as-is
    return encrypted_data