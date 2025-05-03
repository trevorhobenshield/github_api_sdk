

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentReplyParams"]


class CommentReplyParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    pull_number: Required[int]

    body: Required[str]
    """The text of the review comment."""
