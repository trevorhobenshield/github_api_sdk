

from datetime import datetime

from ...._models import BaseModel

__all__ = ["Traffic"]


class Traffic(BaseModel):
    count: int

    timestamp: datetime

    uniques: int
