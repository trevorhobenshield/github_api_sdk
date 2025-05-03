

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PersonalAccessTokenRequestReviewParams"]


class PersonalAccessTokenRequestReviewParams(TypedDict, total=False):
    action: Required[Literal["approve", "deny"]]
    """Action to apply to the requests."""

    pat_request_ids: Iterable[int]
    """
    Unique identifiers of the requests for access via fine-grained personal access
    token. Must be formed of between 1 and 100 `pat_request_id` values.
    """

    reason: str | None
    """Reason for approving or denying the requests. Max 1024 characters."""
