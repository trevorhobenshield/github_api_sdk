

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReviewDismissParams"]


class ReviewDismissParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    pull_number: Required[int]

    message: Required[str]
    """The message for the pull request review dismissal"""

    event: Literal["DISMISS"]
