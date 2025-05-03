

from typing import List
from typing_extensions import TypeAlias

from .pull_request_review_comment import PullRequestReviewComment

__all__ = ["CommentListResponse"]

CommentListResponse: TypeAlias = List[PullRequestReviewComment]
