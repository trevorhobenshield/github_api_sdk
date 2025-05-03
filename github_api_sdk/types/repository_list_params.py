

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RepositoryListParams"]


class RepositoryListParams(TypedDict, total=False):
    since: int
    """A repository ID. Only return repositories with an ID greater than this ID."""
