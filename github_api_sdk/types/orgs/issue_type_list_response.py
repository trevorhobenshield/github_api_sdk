

from typing import List, Optional
from typing_extensions import TypeAlias

from .issue_type import IssueType

__all__ = ["IssueTypeListResponse"]

IssueTypeListResponse: TypeAlias = List[Optional[IssueType]]
