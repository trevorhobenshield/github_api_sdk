

from typing import List

from .runner import Runner
from ...._models import BaseModel

__all__ = ["RunnerGroupListHostedRunnersResponse"]


class RunnerGroupListHostedRunnersResponse(BaseModel):
    runners: List[Runner]

    total_count: float
