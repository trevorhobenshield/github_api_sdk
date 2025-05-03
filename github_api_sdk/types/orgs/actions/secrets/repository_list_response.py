

from typing import List

from ....._models import BaseModel
from ....minimal_repository import MinimalRepository

__all__ = ["RepositoryListResponse"]


class RepositoryListResponse(BaseModel):
    repositories: List[MinimalRepository]

    total_count: int
