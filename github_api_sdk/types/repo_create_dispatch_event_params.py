

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["RepoCreateDispatchEventParams"]


class RepoCreateDispatchEventParams(TypedDict, total=False):
    owner: Required[str]

    event_type: Required[str]
    """A custom webhook event name. Must be 100 characters or fewer."""

    client_payload: dict[str, object]
    """
    JSON payload with extra information about the webhook event that your action or
    workflow may use. The maximum number of top-level properties is 10. The total
    size of the JSON payload must be less than 64KB.
    """
