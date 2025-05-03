

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DependencyGraphCompareParams"]


class DependencyGraphCompareParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    name: str
    """
    The full path, relative to the repository root, of the dependency manifest file.
    """
