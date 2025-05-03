

from typing import List
from typing_extensions import TypeAlias

from .gist_comment import GistComment

__all__ = ["CommentListResponse"]

CommentListResponse: TypeAlias = List[GistComment]
