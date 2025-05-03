

from typing import List

from .runner import Runner
from ...._models import BaseModel

__all__ = ["HostedRunnerListResponse"]


class HostedRunnerListResponse(BaseModel):
    runners: List[Runner]

    total_count: int
