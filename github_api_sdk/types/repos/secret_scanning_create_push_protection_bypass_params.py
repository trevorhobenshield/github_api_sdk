

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .push_protection_bypass_reason import PushProtectionBypassReason

__all__ = ["SecretScanningCreatePushProtectionBypassParams"]


class SecretScanningCreatePushProtectionBypassParams(TypedDict, total=False):
    owner: Required[str]

    placeholder_id: Required[str]
    """The ID of the push protection bypass placeholder.

    This value is returned on any push protected routes.
    """

    reason: Required[PushProtectionBypassReason]
    """The reason for bypassing push protection."""
