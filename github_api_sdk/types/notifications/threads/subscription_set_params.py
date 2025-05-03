

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SubscriptionSetParams"]


class SubscriptionSetParams(TypedDict, total=False):
    ignored: bool
    """Whether to block all notifications from a thread."""
