

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .deployment_reviewer_type import DeploymentReviewerType
from .deployment_branch_policy_settings_param import DeploymentBranchPolicySettingsParam

__all__ = ["EnvironmentCreateOrUpdateParams", "Reviewer"]


class EnvironmentCreateOrUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    deployment_branch_policy: DeploymentBranchPolicySettingsParam | None
    """The type of deployment branch policy for this environment.

    To allow all branches to deploy, set to `null`.
    """

    prevent_self_review: bool
    """
    Whether or not a user who created the job is prevented from approving their own
    job.
    """

    reviewers: Iterable[Reviewer] | None
    """The people or teams that may review jobs that reference the environment.

    You can list up to six users or teams as reviewers. The reviewers must have at
    least read access to the repository. Only one of the required reviewers needs to
    approve the job for it to proceed.
    """

    wait_timer: int
    """The amount of time to delay a job after the job is initially triggered.

    The time (in minutes) must be an integer between 0 and 43,200 (30 days).
    """


class Reviewer(TypedDict, total=False):
    id: int
    """The id of the user or team who can review the deployment"""

    type: DeploymentReviewerType
    """The type of reviewer."""
