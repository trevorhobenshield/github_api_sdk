

from typing import List
from typing_extensions import TypeAlias

from ..issue import Issue

__all__ = ["SubIssueListResponse"]

SubIssueListResponse: TypeAlias = List[Issue]
