

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContentRetrieveParams"]


class ContentRetrieveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    ref: str
    """The name of the commit/branch/tag. Default: the repository’s default branch."""
