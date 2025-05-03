

from typing import List

from .job import Job
from ...._models import BaseModel

__all__ = ["RunListJobsResponse"]


class RunListJobsResponse(BaseModel):
    jobs: List[Job]

    total_count: int
