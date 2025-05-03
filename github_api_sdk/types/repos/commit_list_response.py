

from typing import List
from typing_extensions import TypeAlias

from .commit import Commit

__all__ = ["CommitListResponse"]

CommitListResponse: TypeAlias = List[Commit]
