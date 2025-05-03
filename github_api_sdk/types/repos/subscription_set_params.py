

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubscriptionSetParams"]


class SubscriptionSetParams(TypedDict, total=False):
    owner: Required[str]

    ignored: bool
    """Determines if all notifications should be blocked from this repository."""

    subscribed: bool
    """Determines if notifications should be received from this repository."""
