

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["RepositorySubscription"]


class RepositorySubscription(BaseModel):
    created_at: datetime

    ignored: bool
    """Determines if all notifications should be blocked from this repository."""

    reason: Optional[str] = None

    repository_url: str

    subscribed: bool
    """Determines if notifications should be received from this repository."""

    url: str
