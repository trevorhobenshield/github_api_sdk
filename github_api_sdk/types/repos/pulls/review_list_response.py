

from typing import List
from typing_extensions import TypeAlias

from .pull_request_review import PullRequestReview

__all__ = ["ReviewListResponse"]

ReviewListResponse: TypeAlias = List[PullRequestReview]
