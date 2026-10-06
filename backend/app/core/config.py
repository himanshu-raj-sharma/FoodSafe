# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Author: Himanshu Raj

import os
from functools import lru_cache
from typing import Any

import pydantic_settings
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_extra = "allow",
        case_sensitive = True,
    )

    # Database
    DATABASE_URL: str = Field(
        default="postgresql://postgres:password@localhost:5432/foodsafe",
        description="PostgreSQL database connection string",
    )
    DATABASE_POOL_SIZE: int = Field(default=20, description="Connection pool size")

    # JWT
    JWT_SECRET: str = Field(
        default="your_super_secret_jwt_key_change_this_in_production",
        description="Secret key for JWT signing",
    )
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=1440, description="Access token expiration in minutes")
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7, description="Refresh token expiration in days")

    # Object Storage
    OBJECT_STORAGE_ENDPOINT: str = Field(
        default="http://localhost:9000",
        description="Object storage endpoint",
    )
    OBJECT_STORAGE_BUCKET: str = Field(
        default="foodsafe-evidence",
        description="Default bucket for evidence storage",
    )
    OBJECT_STORAGE_ACCESS_KEY: str = Field(
        default="minioadmin",
        description="Access key for object storage",
    )
    OBJECT_STORAGE_SECRET_KEY: str = Field(
        default="minioadmin",
        description="Secret key for object storage",
    )

    # AI Provider
    AI_PROVIDER: str = Field(default="mock", description="AI provider: mock, openai, anthropic")
    AI_API_KEY: str = Field(default="", description="API key for AI provider")
    AI_MODEL: str = Field(default="gpt-4", description="Model to use for AI")

    # Security
    BCRYPT_ROUNDS: int = Field(default=12, description="Bcrypt work factor")
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = Field(default=100, description="Rate limiting requests per minute")

    # Server
    HOST: str = Field(default="0.0.0.0", description="Server host")
    PORT: int = Field(default=8000, description="Server port")
    ENVIRONMENT: str = Field(default="development", description="Environment: development, staging, production")

    # CORS
    CORS_ORIGINS: str = Field(
        default="http://localhost:3000,http://127.0.0.1:3000",
        description="Allowed CORS origins (comma-separated)",
    )

    # Logging
    LOG_LEVEL: str = Field(default="INFO", description="Log level")
    LOG_FILE: str = Field(default="app.log", description="Log file path")

    # File Upload
    MAX_UPLOAD_SIZE: int = Field(default=10 * 1024 * 1024, description="Maximum upload size in bytes (10MB)")
    ALLOWED_EXTENSIONS: str = Field(default="jpg,jpeg,png,pdf", description="Allowed file extensions (comma-separated)")

    # Encryption
    ENCRYPTION_KEY: str = Field(default="", description="Encryption key for sensitive data")

    @property
    def cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]

    @property
    def allowed_extensions_list(self) -> list[str]:
        return [ext.strip().lower() for ext in self.ALLOWED_EXTENSIONS.split(",")]

@lru_cache

def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()