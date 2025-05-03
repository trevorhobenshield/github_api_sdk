

from typing import List

from .artifact import Artifact
from ...._models import BaseModel

__all__ = ["ArtifactListResponse"]


class ArtifactListResponse(BaseModel):
    artifacts: List[Artifact]

    total_count: int
