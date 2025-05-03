

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentUpdateParams"]


class CommentUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: Required[str]
    """The contents of the comment"""
