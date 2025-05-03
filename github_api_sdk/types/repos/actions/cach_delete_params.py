

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CachDeleteParams"]


class CachDeleteParams(TypedDict, total=False):
    owner: Required[str]

    key: Required[str]
    """A key for identifying the cache."""

    ref: str
    """The full Git reference for narrowing down the cache.

    The `ref` for a branch should be formatted as `refs/heads/<branch name>`. To
    reference a pull request use `refs/pull/<number>/merge`.
    """
