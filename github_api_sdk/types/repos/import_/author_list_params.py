

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthorListParams"]


class AuthorListParams(TypedDict, total=False):
    owner: Required[str]

    since: int
    """A user ID. Only return users with an ID greater than this ID."""
