

from typing import List
from typing_extensions import TypeAlias

from .git_ref import GitRef

__all__ = ["GitListMatchingRefsResponse"]

GitListMatchingRefsResponse: TypeAlias = List[GitRef]
