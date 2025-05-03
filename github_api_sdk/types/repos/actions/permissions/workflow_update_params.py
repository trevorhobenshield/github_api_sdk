

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....orgs.actions.permissions.default_permissions import DefaultPermissions

__all__ = ["WorkflowUpdateParams"]


class WorkflowUpdateParams(TypedDict, total=False):
    owner: Required[str]

    can_approve_pull_request_reviews: bool
    """Whether GitHub Actions can approve pull requests.

    Enabling this can be a security risk.
    """

    default_workflow_permissions: DefaultPermissions
    """
    The default workflow permissions granted to the GITHUB_TOKEN when running
    workflows.
    """
