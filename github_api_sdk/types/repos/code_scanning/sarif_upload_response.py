

from typing import Optional

from ...._models import BaseModel

__all__ = ["SarifUploadResponse"]


class SarifUploadResponse(BaseModel):
    id: Optional[str] = None
    """An identifier for the upload."""

    url: Optional[str] = None
    """The REST API URL for checking the status of the upload."""
