

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["APISubjectStatsResponse", "APISubjectStatsResponseItem"]


class APISubjectStatsResponseItem(BaseModel):
    last_rate_limited_timestamp: Optional[str] = None

    last_request_timestamp: Optional[str] = None

    rate_limited_request_count: Optional[int] = None

    subject_id: Optional[int] = None

    subject_name: Optional[str] = None

    subject_type: Optional[str] = None

    total_request_count: Optional[int] = None


APISubjectStatsResponse: TypeAlias = List[APISubjectStatsResponseItem]
