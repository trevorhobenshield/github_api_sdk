

from typing import List

from .workflow import Workflow
from ...._models import BaseModel

__all__ = ["WorkflowListResponse"]


class WorkflowListResponse(BaseModel):
    total_count: int

    workflows: List[Workflow]
