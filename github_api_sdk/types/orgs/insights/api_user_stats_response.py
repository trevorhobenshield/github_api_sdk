

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["APIUserStatsResponse", "APIUserStatsResponseItem"]


class APIUserStatsResponseItem(BaseModel):
    actor_id: Optional[int] = None

    actor_name: Optional[str] = None

    actor_type: Optional[str] = None

    integration_id: Optional[int] = None

    last_rate_limited_timestamp: Optional[str] = None

    last_request_timestamp: Optional[str] = None

    oauth_application_id: Optional[int] = None

    rate_limited_request_count: Optional[int] = None

    total_request_count: Optional[int] = None


APIUserStatsResponse: TypeAlias = List[APIUserStatsResponseItem]
