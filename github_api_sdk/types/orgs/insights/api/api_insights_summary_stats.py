

from typing import Optional

from ....._models import BaseModel

__all__ = ["APIInsightsSummaryStats"]


class APIInsightsSummaryStats(BaseModel):
    rate_limited_request_count: Optional[int] = None
    """
    The total number of requests that were rate limited within the queried time
    period
    """

    total_request_count: Optional[int] = None
    """The total number of requests within the queried time period"""
