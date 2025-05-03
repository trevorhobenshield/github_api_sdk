

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import FileTypes

__all__ = ["AssetUploadParams"]


class AssetUploadParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    name: Required[str]

    label: str

    body: FileTypes
    """The raw file data"""
