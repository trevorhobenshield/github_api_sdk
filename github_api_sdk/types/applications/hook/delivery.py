

from typing import Dict, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Delivery", "Request", "Response"]


class Request(BaseModel):
    headers: Optional[Dict[str, object]] = None
    """The request headers sent with the webhook delivery."""

    payload: Optional[Dict[str, object]] = None
    """The webhook payload."""


class Response(BaseModel):
    headers: Optional[Dict[str, object]] = None
    """The response headers received when the delivery was made."""

    payload: Optional[str] = None
    """The response payload received."""


class Delivery(BaseModel):
    id: int
    """Unique identifier of the delivery."""

    action: Optional[str] = None
    """The type of activity for the event that triggered the delivery."""

    delivered_at: datetime
    """Time when the delivery was delivered."""

    duration: float
    """Time spent delivering."""

    event: str
    """The event that triggered the delivery."""

    guid: str
    """
    Unique identifier for the event (shared with all deliveries for all webhooks
    that subscribe to this event).
    """

    installation_id: Optional[int] = None
    """The id of the GitHub App installation associated with this event."""

    redelivery: bool
    """Whether the delivery is a redelivery."""

    repository_id: Optional[int] = None
    """The id of the repository associated with this event."""

    request: Request

    response: Response

    status: str
    """Description of the status of the attempted delivery"""

    status_code: int
    """Status code received when delivery was made."""

    throttled_at: Optional[datetime] = None
    """Time when the webhook delivery was throttled."""

    url: Optional[str] = None
    """The URL target of the delivery."""
