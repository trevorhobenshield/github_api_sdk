

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PackageRestoreParams"]


class PackageRestoreParams(TypedDict, total=False):
    org: Required[str]

    package_type: Required[Literal["npm", "maven", "rubygems", "docker", "nuget", "container"]]

    token: str
    """package token"""
