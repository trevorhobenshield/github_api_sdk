

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    team_id: Required[int]

    body: Required[str]
    """The discussion comment's body text."""
