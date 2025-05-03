

from typing import List
from typing_extensions import TypeAlias

from .repos.issue import Issue

__all__ = ["IssueListResponse"]

IssueListResponse: TypeAlias = List[Issue]
