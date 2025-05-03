

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ....._models import BaseModel
from ....orgs.team import Team
from ....orgs.simple_user import SimpleUser
from ...deployment_reviewer_type import DeploymentReviewerType

__all__ = [
    "PendingDeploymentListResponse",
    "PendingDeploymentListResponseItem",
    "PendingDeploymentListResponseItemEnvironment",
    "PendingDeploymentListResponseItemReviewer",
    "PendingDeploymentListResponseItemReviewerReviewer",
]


class PendingDeploymentListResponseItemEnvironment(BaseModel):
    id: Optional[int] = None
    """The id of the environment."""

    html_url: Optional[str] = None

    name: Optional[str] = None
    """The name of the environment."""

    node_id: Optional[str] = None

    url: Optional[str] = None


PendingDeploymentListResponseItemReviewerReviewer: TypeAlias = Union[SimpleUser, Team]


class PendingDeploymentListResponseItemReviewer(BaseModel):
    reviewer: Optional[PendingDeploymentListResponseItemReviewerReviewer] = None
    """A GitHub user."""

    type: Optional[DeploymentReviewerType] = None
    """The type of reviewer."""


class PendingDeploymentListResponseItem(BaseModel):
    current_user_can_approve: bool
    """Whether the currently authenticated user can approve the deployment"""

    environment: PendingDeploymentListResponseItemEnvironment

    reviewers: List[PendingDeploymentListResponseItemReviewer]
    """The people or teams that may approve jobs that reference the environment.

    You can list up to six users or teams as reviewers. The reviewers must have at
    least read access to the repository. Only one of the required reviewers needs to
    approve the job for it to proceed.
    """

    wait_timer: int
    """The set duration of the wait timer"""

    wait_timer_started_at: Optional[datetime] = None
    """The time that the wait timer began."""


PendingDeploymentListResponse: TypeAlias = List[PendingDeploymentListResponseItem]
