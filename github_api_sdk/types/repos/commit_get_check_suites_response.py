

from typing import List

from ..._models import BaseModel
from .check_suite import CheckSuite

__all__ = ["CommitGetCheckSuitesResponse"]


class CommitGetCheckSuitesResponse(BaseModel):
    check_suites: List[CheckSuite]

    total_count: int
