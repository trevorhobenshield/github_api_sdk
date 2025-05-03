

from typing import List
from typing_extensions import TypeAlias

from .repository import Repository

__all__ = ["StarredListResponse"]

StarredListResponse: TypeAlias = List[Repository]
