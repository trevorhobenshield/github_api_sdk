

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import TypedDict

from .permissions_param import PermissionsParam

__all__ = ["InstallationCreateAccessTokenParams"]


class InstallationCreateAccessTokenParams(TypedDict, total=False):
    permissions: PermissionsParam
    """The permissions granted to the user access token."""

    repositories: list[str]
    """List of repository names that the token should have access to"""

    repository_ids: Iterable[int]
    """List of repository IDs that the token should have access to"""
