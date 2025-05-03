

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RepositorySetParams"]


class RepositorySetParams(TypedDict, total=False):
    org: Required[str]

    selected_repository_ids: Required[Iterable[int]]
    """List of repository IDs that can access the runner group."""
