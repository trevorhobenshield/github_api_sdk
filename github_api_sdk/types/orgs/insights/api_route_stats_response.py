

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["APIRouteStatsResponse", "APIRouteStatsResponseItem"]


class APIRouteStatsResponseItem(BaseModel):
    api_route: Optional[str] = None
    """The API path's route template"""

    http_method: Optional[str] = None
    """The HTTP method"""

    last_rate_limited_timestamp: Optional[str] = None

    last_request_timestamp: Optional[str] = None

    rate_limited_request_count: Optional[int] = None
    """
    The total number of requests that were rate limited within the queried time
    period
    """

    total_request_count: Optional[int] = None
    """The total number of requests within the queried time period"""


APIRouteStatsResponse: TypeAlias = List[APIRouteStatsResponseItem]
