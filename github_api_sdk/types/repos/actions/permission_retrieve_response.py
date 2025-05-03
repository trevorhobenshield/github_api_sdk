

from typing import Optional

from ...._models import BaseModel
from ...orgs.actions.allowed_actions import AllowedActions

__all__ = ["PermissionRetrieveResponse"]


class PermissionRetrieveResponse(BaseModel):
    enabled: bool
    """Whether GitHub Actions is enabled on the repository."""

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
