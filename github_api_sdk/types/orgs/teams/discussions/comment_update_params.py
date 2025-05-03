

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentUpdateParams"]


class CommentUpdateParams(TypedDict, total=False):
    org: Required[str]

    team_slug: Required[str]

    discussion_number: Required[int]

    body: Required[str]
    """The discussion comment's body text."""
