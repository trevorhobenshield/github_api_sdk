

from typing import List
from typing_extensions import TypeAlias

from .copilot_usage_metrics_day import CopilotUsageMetricsDay

__all__ = ["CopilotGetMetricsResponse"]

CopilotGetMetricsResponse: TypeAlias = List[CopilotUsageMetricsDay]
