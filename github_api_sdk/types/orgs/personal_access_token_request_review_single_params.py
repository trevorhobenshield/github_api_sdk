

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PersonalAccessTokenRequestReviewSingleParams"]


class PersonalAccessTokenRequestReviewSingleParams(TypedDict, total=False):
    org: Required[str]

    action: Required[Literal["approve", "deny"]]
    """Action to apply to the request."""

    reason: str | None
    """Reason for approving or denying the request. Max 1024 characters."""
