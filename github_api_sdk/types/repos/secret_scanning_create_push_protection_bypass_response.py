

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .push_protection_bypass_reason import PushProtectionBypassReason

__all__ = ["SecretScanningCreatePushProtectionBypassResponse"]


class SecretScanningCreatePushProtectionBypassResponse(BaseModel):
    expire_at: Optional[datetime] = None
    """
    The time that the bypass will expire in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    reason: Optional[PushProtectionBypassReason] = None
    """The reason for bypassing push protection."""

    token_type: Optional[str] = None
    """The token type this bypass is for."""
