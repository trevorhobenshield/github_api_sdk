

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...orgs.actions.allowed_actions import AllowedActions

__all__ = ["PermissionUpdateParams"]


class PermissionUpdateParams(TypedDict, total=False):
    owner: Required[str]

    enabled: Required[bool]
    """Whether GitHub Actions is enabled on the repository."""

    allowed_actions: AllowedActions
    """
    The permissions policy that controls the actions and reusable workflows that are
    allowed to run.
    """
