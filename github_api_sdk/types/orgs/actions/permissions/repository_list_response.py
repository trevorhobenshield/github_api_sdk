

from typing import List

from ....._models import BaseModel
from ....users.repository import Repository

__all__ = ["RepositoryListResponse"]


class RepositoryListResponse(BaseModel):
    repositories: List[Repository]

    total_count: float
