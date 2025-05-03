

from typing import List
from typing_extensions import TypeAlias

from ..repositories import Repositories

__all__ = ["RepositoryListResponse"]

RepositoryListResponse: TypeAlias = List[Repositories]
