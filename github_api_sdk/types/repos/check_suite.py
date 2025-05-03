

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..minimal_repository import MinimalRepository
from .nullable_integration import NullableIntegration
from .actions.pull_request_minimal import PullRequestMinimal

__all__ = ["CheckSuite", "HeadCommit", "HeadCommitAuthor", "HeadCommitCommitter"]


class HeadCommitAuthor(BaseModel):
    email: str
    """Git email address of the commit's author"""

    name: str
    """Name of the commit's author"""


class HeadCommitCommitter(BaseModel):
    email: str
    """Git email address of the commit's committer"""

    name: str
    """Name of the commit's committer"""


class HeadCommit(BaseModel):
    id: str
    """SHA for the commit"""

    author: Optional[HeadCommitAuthor] = None
    """Information about the Git author"""

    committer: Optional[HeadCommitCommitter] = None
    """Information about the Git committer"""

    message: str
    """Message describing the purpose of the commit"""

    timestamp: datetime
    """Timestamp of the commit"""

    tree_id: str
    """SHA for the commit's tree"""


class CheckSuite(BaseModel):
    id: int

    after: Optional[str] = None

    app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    before: Optional[str] = None

    check_runs_url: str

    conclusion: Optional[
        Literal[
            "success",
            "failure",
            "neutral",
            "cancelled",
            "skipped",
            "timed_out",
            "action_required",
            "startup_failure",
            "stale",
        ]
    ] = None

    created_at: Optional[datetime] = None

    head_branch: Optional[str] = None

    head_commit: HeadCommit
    """A commit."""

    head_sha: str
    """The SHA of the head commit that is being checked."""

    latest_check_runs_count: int

    node_id: str

    pull_requests: Optional[List[PullRequestMinimal]] = None

    repository: MinimalRepository
    """Minimal Repository"""

    status: Optional[Literal["queued", "in_progress", "completed", "waiting", "requested", "pending"]] = None
    """The phase of the lifecycle that the check suite is currently in.

    Statuses of waiting, requested, and pending are reserved for GitHub Actions
    check suites.
    """

    updated_at: Optional[datetime] = None

    url: Optional[str] = None

    rerequestable: Optional[bool] = None

    runs_rerequestable: Optional[bool] = None
