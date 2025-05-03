

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..applications.hook.webhook import Webhook

__all__ = ["Hook", "LastResponse"]


class LastResponse(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    status: Optional[str] = None


class Hook(BaseModel):
    id: int
    """Unique identifier of the webhook."""

    active: bool
    """Determines whether the hook is actually triggered on pushes."""

    config: Webhook
    """Configuration object of the webhook"""

    created_at: datetime

    events: List[str]
    """Determines what events the hook is triggered for. Default: ['push']."""

    last_response: LastResponse

    name: str
    """The name of a valid service, use 'web' for a webhook."""

    ping_url: str

    test_url: str

    type: str

    updated_at: datetime

    url: str

    deliveries_url: Optional[str] = None
