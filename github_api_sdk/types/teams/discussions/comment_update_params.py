

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentUpdateParams"]


class CommentUpdateParams(TypedDict, total=False):
    team_id: Required[int]

    discussion_number: Required[int]

    body: Required[str]
    """The discussion comment's body text."""
