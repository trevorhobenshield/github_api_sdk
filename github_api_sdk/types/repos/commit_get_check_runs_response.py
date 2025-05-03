

from typing import List

from ..._models import BaseModel
from .check_run import CheckRun

__all__ = ["CommitGetCheckRunsResponse"]


class CommitGetCheckRunsResponse(BaseModel):
    check_runs: List[CheckRun]

    total_count: int
