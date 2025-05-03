

from typing import List
from typing_extensions import TypeAlias

from .commit_comment import CommitComment

__all__ = ["CommentListResponse"]

CommentListResponse: TypeAlias = List[CommitComment]
