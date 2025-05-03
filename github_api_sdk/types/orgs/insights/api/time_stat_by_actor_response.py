

from typing import List
from typing_extensions import TypeAlias

from .api_insights_time_stats_items import APIInsightsTimeStatsItems

__all__ = ["TimeStatByActorResponse"]

TimeStatByActorResponse: TypeAlias = List[APIInsightsTimeStatsItems]
