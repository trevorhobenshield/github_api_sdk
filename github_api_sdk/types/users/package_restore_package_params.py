

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PackageRestorePackageParams"]


class PackageRestorePackageParams(TypedDict, total=False):
    username: Required[str]

    package_type: Required[Literal["npm", "maven", "rubygems", "docker", "nuget", "container"]]

    token: str
    """package token"""
