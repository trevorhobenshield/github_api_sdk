

from typing import List

from ...._models import BaseModel

__all__ = ["HostedRunnerGetPlatformsResponse"]


class HostedRunnerGetPlatformsResponse(BaseModel):
    platforms: List[str]

    total_count: int
