

from typing import List, Optional

from ...._models import BaseModel
from ..repository import Repository

__all__ = ["RepositoryListResponse"]


class RepositoryListResponse(BaseModel):
    repositories: List[Repository]

    total_count: int

    repository_selection: Optional[str] = None
