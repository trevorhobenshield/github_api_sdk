

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Item"]


class Item(BaseModel):
    id: int
    """Unique identifier of the webhook delivery."""

    action: Optional[str] = None
    """The type of activity for the event that triggered the delivery."""

    delivered_at: datetime
    """Time when the webhook delivery occurred."""

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
    """Whether the webhook delivery is a redelivery."""

    repository_id: Optional[int] = None
    """The id of the repository associated with this event."""

    status: str
    """Describes the response returned after attempting the delivery."""

    status_code: int
    """Status code received when delivery was made."""

    throttled_at: Optional[datetime] = None
    """Time when the webhook delivery was throttled."""
