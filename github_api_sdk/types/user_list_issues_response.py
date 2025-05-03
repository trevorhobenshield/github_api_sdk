

from typing import List
from typing_extensions import TypeAlias

from .repos.issue import Issue

__all__ = ["UserListIssuesResponse"]

UserListIssuesResponse: TypeAlias = List[Issue]
