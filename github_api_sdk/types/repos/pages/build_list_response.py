

from typing import List
from typing_extensions import TypeAlias

from .page_build import PageBuild

__all__ = ["BuildListResponse"]

BuildListResponse: TypeAlias = List[PageBuild]
