

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..orgs.team import Team
from ..orgs.simple_user import SimpleUser
from .deployment_reviewer_type import DeploymentReviewerType
from .deployment_branch_policy_settings import DeploymentBranchPolicySettings

__all__ = [
    "Environment",
    "ProtectionRule",
    "ProtectionRuleUnionMember0",
    "ProtectionRuleUnionMember1",
    "ProtectionRuleUnionMember1Reviewer",
    "ProtectionRuleUnionMember1ReviewerReviewer",
    "ProtectionRuleUnionMember2",
]


class ProtectionRuleUnionMember0(BaseModel):
    id: int

    node_id: str

    type: str

    wait_timer: Optional[int] = None
    """The amount of time to delay a job after the job is initially triggered.

    The time (in minutes) must be an integer between 0 and 43,200 (30 days).
    """


ProtectionRuleUnionMember1ReviewerReviewer: TypeAlias = Union[SimpleUser, Team]


class ProtectionRuleUnionMember1Reviewer(BaseModel):
    reviewer: Optional[ProtectionRuleUnionMember1ReviewerReviewer] = None
    """A GitHub user."""

    type: Optional[DeploymentReviewerType] = None
    """The type of reviewer."""


class ProtectionRuleUnionMember1(BaseModel):
    id: int

    node_id: str

    type: str

    prevent_self_review: Optional[bool] = None
    """
    Whether deployments to this environment can be approved by the user who created
    the deployment.
    """

    reviewers: Optional[List[ProtectionRuleUnionMember1Reviewer]] = None
    """The people or teams that may approve jobs that reference the environment.

    You can list up to six users or teams as reviewers. The reviewers must have at
    least read access to the repository. Only one of the required reviewers needs to
    approve the job for it to proceed.
    """


class ProtectionRuleUnionMember2(BaseModel):
    id: int

    node_id: str

    type: str


ProtectionRule: TypeAlias = Union[ProtectionRuleUnionMember0, ProtectionRuleUnionMember1, ProtectionRuleUnionMember2]


class Environment(BaseModel):
    id: int
    """The id of the environment."""

    created_at: datetime
    """The time that the environment was created, in ISO 8601 format."""

    html_url: str

    name: str
    """The name of the environment."""

    node_id: str

    updated_at: datetime
    """The time that the environment was last updated, in ISO 8601 format."""

    url: str

    deployment_branch_policy: Optional[DeploymentBranchPolicySettings] = None
    """The type of deployment branch policy for this environment.

    To allow all branches to deploy, set to `null`.
    """

    protection_rules: Optional[List[ProtectionRule]] = None
    """Built-in deployment protection rules for the environment."""
