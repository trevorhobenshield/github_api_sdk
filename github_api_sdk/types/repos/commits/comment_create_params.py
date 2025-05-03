

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: Required[str]
    """The contents of the comment."""

    line: int
    """**Closing down notice**.

    Use **position** parameter instead. Line number in the file to comment on.
    """

    path: str
    """Relative path of the file to comment on."""

    position: int
    """Line index in the diff to comment on."""
