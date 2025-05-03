

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthorMapParams"]


class AuthorMapParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    email: str
    """The new Git author email."""

    name: str
    """The new Git author name."""
