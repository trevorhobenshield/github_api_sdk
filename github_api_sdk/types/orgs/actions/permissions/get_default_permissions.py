


from ....._models import BaseModel
from .default_permissions import DefaultPermissions

__all__ = ["GetDefaultPermissions"]


class GetDefaultPermissions(BaseModel):
    can_approve_pull_request_reviews: bool
    """Whether GitHub Actions can approve pull requests.

    Enabling this can be a security risk.
    """

    default_workflow_permissions: DefaultPermissions
    """
    The default workflow permissions granted to the GITHUB_TOKEN when running
    workflows.
    """
