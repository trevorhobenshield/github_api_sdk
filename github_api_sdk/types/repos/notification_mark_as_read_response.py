

from typing import Optional

from ..._models import BaseModel

__all__ = ["NotificationMarkAsReadResponse"]


class NotificationMarkAsReadResponse(BaseModel):
    message: Optional[str] = None

    url: Optional[str] = None
