

from typing import List

from ..._models import BaseModel
from .check_run import CheckRun

__all__ = ["CheckSuiteListCheckRunsResponse"]


class CheckSuiteListCheckRunsResponse(BaseModel):
    check_runs: List[CheckRun]

    total_count: int
