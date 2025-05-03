

from typing import List
from typing_extensions import TypeAlias

from .issue_comment import IssueComment

__all__ = ["CommentListResponse"]

CommentListResponse: TypeAlias = List[IssueComment]
