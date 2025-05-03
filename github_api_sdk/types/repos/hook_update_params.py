

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..applications.hook.webhook_param import WebhookParam

__all__ = ["HookUpdateParams"]


class HookUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    active: bool
    """Determines if notifications are sent when the webhook is triggered.

    Set to `true` to send notifications.
    """

    add_events: list[str]
    """
    Determines a list of events to be added to the list of events that the Hook
    triggers for.
    """

    config: WebhookParam
    """Configuration object of the webhook"""

    events: list[str]
    """
    Determines what [events](https://docs.github.com/webhooks/event-payloads) the
    hook is triggered for. This replaces the entire array of events.
    """

    remove_events: list[str]
    """
    Determines a list of events to be removed from the list of events that the Hook
    triggers for.
    """
