

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReviewUpdateParams"]


class ReviewUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    pull_number: Required[int]

    body: Required[str]
    """The body text of the pull request review."""
