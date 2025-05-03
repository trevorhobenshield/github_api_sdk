

from typing import List
from typing_extensions import TypeAlias

from .commit import Commit

__all__ = ["PullListCommitsResponse"]

PullListCommitsResponse: TypeAlias = List[Commit]
