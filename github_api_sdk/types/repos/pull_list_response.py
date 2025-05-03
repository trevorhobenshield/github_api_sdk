

from typing import List
from typing_extensions import TypeAlias

from .pulls.pull_request_simple import PullRequestSimple

__all__ = ["PullListResponse"]

PullListResponse: TypeAlias = List[PullRequestSimple]
