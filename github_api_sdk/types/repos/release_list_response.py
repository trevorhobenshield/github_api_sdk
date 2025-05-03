

from typing import List
from typing_extensions import TypeAlias

from .release import Release

__all__ = ["ReleaseListResponse"]

ReleaseListResponse: TypeAlias = List[Release]
