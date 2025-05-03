

from typing import List

from .groups import Groups
from ...._models import BaseModel

__all__ = ["RunnerGroupListResponse"]


class RunnerGroupListResponse(BaseModel):
    runner_groups: List[Groups]

    total_count: float
