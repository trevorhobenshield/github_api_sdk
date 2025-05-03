

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DiscussionUpdateParams"]


class DiscussionUpdateParams(TypedDict, total=False):
    team_id: Required[int]

    body: str
    """The discussion post's body text."""

    title: str
    """The discussion post's title."""
