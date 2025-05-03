

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentUpdateParams"]


class CommentUpdateParams(TypedDict, total=False):
    gist_id: Required[str]

    body: Required[str]
    """The comment text."""
