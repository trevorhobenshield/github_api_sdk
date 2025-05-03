

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ThreadSubscription"]


class ThreadSubscription(BaseModel):
    created_at: Optional[datetime] = None

    ignored: bool

    reason: Optional[str] = None

    subscribed: bool

    url: str

    repository_url: Optional[str] = None

    thread_url: Optional[str] = None
