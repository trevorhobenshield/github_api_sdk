

from typing import List
from typing_extensions import TypeAlias

from .repository import Repository

__all__ = ["RepoListResponse"]

RepoListResponse: TypeAlias = List[Repository]
