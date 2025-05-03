

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .allowed_actions import AllowedActions
from .enabled_repositories import EnabledRepositories

__all__ = ["PermissionSetParams"]


class PermissionSetParams(TypedDict, total=False):
    enabled_repositories: Required[EnabledRepositories]
    """
    The policy that controls the repositories in the organization that are allowed
    to run GitHub Actions.
    """

    allowed_actions: AllowedActions
    """
    The permissions policy that controls the actions and reusable workflows that are
    allowed to run.
    """
