

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RequestedReviewerRequestParams"]


class RequestedReviewerRequestParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    reviewers: list[str]
    """An array of user `login`s that will be requested."""

    team_reviewers: list[str]
    """An array of team `slug`s that will be requested."""
