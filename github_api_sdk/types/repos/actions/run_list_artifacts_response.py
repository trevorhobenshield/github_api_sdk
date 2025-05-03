

from typing import List

from .artifact import Artifact
from ...._models import BaseModel

__all__ = ["RunListArtifactsResponse"]


class RunListArtifactsResponse(BaseModel):
    artifacts: List[Artifact]

    total_count: int
