

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Job", "Step"]


class Step(BaseModel):
    conclusion: Optional[str] = None
    """The outcome of the job."""

    name: str
    """The name of the job."""

    number: int

    status: Literal["queued", "in_progress", "completed"]
    """The phase of the lifecycle that the job is currently in."""

    completed_at: Optional[datetime] = None
    """The time that the job finished, in ISO 8601 format."""

    started_at: Optional[datetime] = None
    """The time that the step started, in ISO 8601 format."""


class Job(BaseModel):
    id: int
    """The id of the job."""

    check_run_url: str

    completed_at: Optional[datetime] = None
    """The time that the job finished, in ISO 8601 format."""

    conclusion: Optional[
        Literal["success", "failure", "neutral", "cancelled", "skipped", "timed_out", "action_required"]
    ] = None
    """The outcome of the job."""

    created_at: datetime
    """The time that the job created, in ISO 8601 format."""

    head_branch: Optional[str] = None
    """The name of the current branch."""

    head_sha: str
    """The SHA of the commit that is being run."""

    html_url: Optional[str] = None

    labels: List[str]
    """Labels for the workflow job.

    Specified by the "runs_on" attribute in the action's workflow file.
    """

    name: str
    """The name of the job."""

    node_id: str

    run_id: int
    """The id of the associated workflow run."""

    run_url: str

    runner_group_id: Optional[int] = None
    """The ID of the runner group to which this job has been assigned.

    (If a runner hasn't yet been assigned, this will be null.)
    """

    runner_group_name: Optional[str] = None
    """The name of the runner group to which this job has been assigned.

    (If a runner hasn't yet been assigned, this will be null.)
    """

    runner_id: Optional[int] = None
    """The ID of the runner to which this job has been assigned.

    (If a runner hasn't yet been assigned, this will be null.)
    """

    runner_name: Optional[str] = None
    """The name of the runner to which this job has been assigned.

    (If a runner hasn't yet been assigned, this will be null.)
    """

    started_at: datetime
    """The time that the job started, in ISO 8601 format."""

    status: Literal["queued", "in_progress", "completed", "waiting", "requested", "pending"]
    """The phase of the lifecycle that the job is currently in."""

    url: str

    workflow_name: Optional[str] = None
    """The name of the workflow."""

    run_attempt: Optional[int] = None
    """
    Attempt number of the associated workflow run, 1 for first attempt and higher if
    the workflow was re-run.
    """

    steps: Optional[List[Step]] = None
    """Steps in this job."""
