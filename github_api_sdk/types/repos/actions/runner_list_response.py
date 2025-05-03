

from typing import List

from ...._models import BaseModel
from ...orgs.actions.self_hosted_runner import SelfHostedRunner

__all__ = ["RunnerListResponse"]


class RunnerListResponse(BaseModel):
    runners: List[SelfHostedRunner]

    total_count: int
