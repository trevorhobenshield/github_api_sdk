

from typing import Optional

from ....._models import BaseModel

__all__ = ["APIInsightsTimeStatsItems"]


class APIInsightsTimeStatsItems(BaseModel):
    rate_limited_request_count: Optional[int] = None

    timestamp: Optional[str] = None

    total_request_count: Optional[int] = None
