

from typing import List

from ....._models import BaseModel
from .runner_image import RunnerImage

__all__ = ["ImageGetGitHubOwnedResponse"]


class ImageGetGitHubOwnedResponse(BaseModel):
    images: List[RunnerImage]

    total_count: int
