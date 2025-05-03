

from typing import Optional

from ...._models import BaseModel
from .allowed_actions import AllowedActions
from .enabled_repositories import EnabledRepositories

__all__ = ["PermissionGetResponse"]


class PermissionGetResponse(BaseModel):
    enabled_repositories: EnabledRepositories
    """
    The policy that controls the repositories in the organization that are allowed
    to run GitHub Actions.
    """

    allowed_actions: Optional[AllowedActions] = None
    """
    The permissions policy that controls the actions and reusable workflows that are
    allowed to run.
    """

    selected_actions_url: Optional[str] = None
    """
    The API URL to use to get or set the actions and reusable workflows that are
    allowed to run, when `allowed_actions` is set to `selected`.
    """

    selected_repositories_url: Optional[str] = None
    """
    The API URL to use to get or set the selected repositories that are allowed to
    run GitHub Actions, when `enabled_repositories` is set to `selected`.
    """
