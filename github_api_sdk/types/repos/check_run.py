

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .nullable_integration import NullableIntegration
from .actions.pull_request_minimal import PullRequestMinimal

__all__ = ["CheckRun", "CheckSuite", "Output", "Deployment"]


class CheckSuite(BaseModel):
    id: int


class Output(BaseModel):
    annotations_count: int

    annotations_url: str

    summary: Optional[str] = None

    text: Optional[str] = None

    title: Optional[str] = None


class Deployment(BaseModel):
    id: int
    """Unique identifier of the deployment"""

    created_at: datetime

    description: Optional[str] = None

    environment: str
    """Name for the target deployment environment."""

    node_id: str

    repository_url: str

    statuses_url: str

    task: str
    """Parameter to specify a task to execute"""

    updated_at: datetime

    url: str

    original_environment: Optional[str] = None

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    production_environment: Optional[bool] = None
    """Specifies if the given environment is one that end-users directly interact with.

    Default: false.
    """

    transient_environment: Optional[bool] = None
    """
    Specifies if the given environment is will no longer exist at some point in the
    future. Default: false.
    """


class CheckRun(BaseModel):
    id: int
    """The id of the check."""

    app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    check_suite: Optional[CheckSuite] = None

    completed_at: Optional[datetime] = None

    conclusion: Optional[
        Literal["success", "failure", "neutral", "cancelled", "skipped", "timed_out", "action_required"]
    ] = None

    details_url: Optional[str] = None

    external_id: Optional[str] = None

    head_sha: str
    """The SHA of the commit that is being checked."""

    html_url: Optional[str] = None

    name: str
    """The name of the check."""

    node_id: str

    output: Output

    pull_requests: List[PullRequestMinimal]
    """
    Pull requests that are open with a `head_sha` or `head_branch` that matches the
    check. The returned pull requests do not necessarily indicate pull requests that
    triggered the check.
    """

    started_at: Optional[datetime] = None

    status: Literal["queued", "in_progress", "completed", "waiting", "requested", "pending"]
    """The phase of the lifecycle that the check is currently in.

    Statuses of waiting, requested, and pending are reserved for GitHub Actions
    check runs.
    """

    url: str

    deployment: Optional[Deployment] = None
    """
    A deployment created as the result of an Actions check run from a workflow that
    references an environment
    """
