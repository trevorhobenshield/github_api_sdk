

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AssetUpdateParams"]


class AssetUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    label: str
    """An alternate short description of the asset. Used in place of the filename."""

    name: str
    """The file name of the asset."""

    state: str
