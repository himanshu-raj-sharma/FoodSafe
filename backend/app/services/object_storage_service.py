# FoodSafe © 2026 Himanshu Raj. All rights reserved.
# Owner: Himanshu Raj

from typing import Optional, BinaryIO
import hashlib
import uuid
from datetime import datetime, timedelta

from ..core.config import get_settings

Settings = get_settings()
class ObjectStorageService:
    """Service for managing object storage operations."""

    def __init__(self):
        self.endpoint = Settings.OBJECT_STORAGE_ENDPOINT
        self.bucket = Settings.OBJECT_STORAGE_BUCKET
        self.access_key = Settings.OBJECT_STORAGE_ACCESS_KEY
        self.secret_key = Settings.OBJECT_STORAGE_SECRET_KEY

    def upload_file(
        self,
        file_data: BinaryIO,
        filename: str,
        mime_type: str,
        organization_id: int,
        user_id: int,
    ) -> dict:
        """Upload a file to object storage."""
        # Generate unique object key
        file_id = str(uuid.uuid4())
        extension = filename.rsplit(".", 1)[-1] if "." in filename else ""
        object_key = f"org_{organization_id}/{datetime.now().strftime('%Y/%m/%d')}/{file_id}.{extension}"

        # Calculate checksum
        file_data.seek(0)
        checksum = hashlib.sha256(file_data.read()).hexdigest()
        file_data.seek(0)

        # In a real implementation, this would upload to actual storage
        # For now, return metadata
        return {
            "object_key": object_key,
            "filename": filename,
            "mime_type": mime_type,
            "size": len(file_data.read()),
            "checksum": checksum,
            "uploaded_by": user_id,
            "organization_id": organization_id,
            "uploaded_at": datetime.utcnow().isoformat(),
        }

    def generate_signed_url(self, object_key: str, expires_in: int = 3600) -> str:
        """Generate a signed URL for downloading a file."""
        # In a real implementation, this would generate a signed URL
        # For now, return a placeholder URL
        return f"{self.endpoint}/{self.bucket}/{object_key}?expires={expires_in}"

    def delete_file(self, object_key: str) -> bool:
        """Delete a file from object storage."""
        # In a real implementation, this would delete from storage
        return True

    def validate_file(self, file_data: BinaryIO, filename: str, mime_type: str) -> bool:
        """Validate file before upload."""
        # Check file extension
        allowed_extensions = Settings.allowed_extensions_list
        extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
        if extension not in allowed_extensions:
            return False

        # Check MIME type
        if mime_type and not mime_type.startswith(("image/", "application/pdf")):
            return False

        # Check file size
        file_data.seek(0, 2)  # Seek to end
        file_size = file_data.tell()
        file_data.seek(0)
        if file_size > Settings.MAX_UPLOAD_SIZE:
            return False

        return True