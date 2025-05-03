

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ...orgs.simple_user import SimpleUser
from ...minimal_repository import MinimalRepository
from .pull_request_minimal import PullRequestMinimal

__all__ = ["WorkflowRun", "HeadCommit", "HeadCommitAuthor", "HeadCommitCommitter", "ReferencedWorkflow"]


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


class ReferencedWorkflow(BaseModel):
    path: str

    sha: str

    ref: Optional[str] = None


class WorkflowRun(BaseModel):
    id: int
    """The ID of the workflow run."""

    artifacts_url: str
    """The URL to the artifacts for the workflow run."""

    cancel_url: str
    """The URL to cancel the workflow run."""

    check_suite_url: str
    """The URL to the associated check suite."""

    conclusion: Optional[str] = None

    created_at: datetime

    display_title: str
    """
    The event-specific title associated with the run or the run-name if set, or the
    value of `run-name` if it is set in the workflow.
    """

    event: str

    head_branch: Optional[str] = None

    head_commit: Optional[HeadCommit] = None
    """A commit."""

    head_repository: MinimalRepository
    """Minimal Repository"""

    head_sha: str
    """
    The SHA of the head commit that points to the version of the workflow being run.
    """

    html_url: str

    jobs_url: str
    """The URL to the jobs for the workflow run."""

    logs_url: str
    """The URL to download the logs for the workflow run."""

    node_id: str

    path: str
    """The full path of the workflow"""

    pull_requests: Optional[List[PullRequestMinimal]] = None
    """
    Pull requests that are open with a `head_sha` or `head_branch` that matches the
    workflow run. The returned pull requests do not necessarily indicate pull
    requests that triggered the run.
    """

    repository: MinimalRepository
    """Minimal Repository"""

    rerun_url: str
    """The URL to rerun the workflow run."""

    run_number: int
    """The auto incrementing run number for the workflow run."""

    status: Optional[str] = None

    updated_at: datetime

    url: str
    """The URL to the workflow run."""

    workflow_id: int
    """The ID of the parent workflow."""

    workflow_url: str
    """The URL to the workflow."""

    actor: Optional[SimpleUser] = None
    """A GitHub user."""

    check_suite_id: Optional[int] = None
    """The ID of the associated check suite."""

    check_suite_node_id: Optional[str] = None
    """The node ID of the associated check suite."""

    head_repository_id: Optional[int] = None

    name: Optional[str] = None
    """The name of the workflow run."""

    previous_attempt_url: Optional[str] = None
    """The URL to the previous attempted run of this workflow, if one exists."""

    referenced_workflows: Optional[List[ReferencedWorkflow]] = None

    run_attempt: Optional[int] = None
    """
    Attempt number of the run, 1 for first attempt and higher if the workflow was
    re-run.
    """

    run_started_at: Optional[datetime] = None
    """The start time of the latest run. Resets on re-run."""

    triggering_actor: Optional[SimpleUser] = None
    """A GitHub user."""
