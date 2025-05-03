

from typing import List

from ...._models import BaseModel
from .workflow_run import WorkflowRun

__all__ = ["RunListResponse"]


class RunListResponse(BaseModel):
    total_count: int

    workflow_runs: List[WorkflowRun]
