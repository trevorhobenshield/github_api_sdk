

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReviewSubmitParams"]


class ReviewSubmitParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    pull_number: Required[int]

    event: Required[Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"]]
    """The review action you want to perform.

    The review actions include: `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`. When you
    leave this blank, the API returns _HTTP 422 (Unrecognizable entity)_ and sets
    the review action state to `PENDING`, which means you will need to re-submit the
    pull request review using a review action.
    """

    body: str
    """The body text of the pull request review"""
