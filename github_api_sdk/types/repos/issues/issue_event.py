

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...orgs.team import Team
from ...orgs.issue_type import IssueType
from ...orgs.simple_user import SimpleUser
from ...users.repository import Repository
from ...applications.user import User
from ..nullable_milestone import NullableMilestone
from ..sub_issues_summary import SubIssuesSummary
from ..nullable_integration import NullableIntegration
from ...gists.author_association import AuthorAssociation
from ...orgs.teams.reaction_rollup import ReactionRollup

__all__ = [
    "IssueEvent",
    "DismissedReview",
    "Issue",
    "IssueLabel",
    "IssueLabelUnionMember1",
    "IssuePullRequest",
    "Label",
    "Milestone",
    "ProjectCard",
    "Rename",
]


class DismissedReview(BaseModel):
    dismissal_message: Optional[str] = None

    review_id: int

    state: str

    dismissal_commit_id: Optional[str] = None


class IssueLabelUnionMember1(BaseModel):
    id: Optional[int] = None

    color: Optional[str] = None

    default: Optional[bool] = None

    description: Optional[str] = None

    name: Optional[str] = None

    node_id: Optional[str] = None

    url: Optional[str] = None


IssueLabel: TypeAlias = Union[str, IssueLabelUnionMember1]


class IssuePullRequest(BaseModel):
    diff_url: Optional[str] = None

    html_url: Optional[str] = None

    patch_url: Optional[str] = None

    url: Optional[str] = None

    merged_at: Optional[datetime] = None


class Issue(BaseModel):
    id: int

    assignee: Optional[User] = None
    """A GitHub user."""

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    closed_at: Optional[datetime] = None

    comments: int

    comments_url: str

    created_at: datetime

    events_url: str

    html_url: str

    labels: List[IssueLabel]
    """
    Labels to associate with this issue; pass one or more label names to replace the
    set of labels on this issue; send an empty array to clear all labels from the
    issue; note that the labels are silently dropped for users without push access
    to the repository
    """

    labels_url: str

    locked: bool

    milestone: Optional[NullableMilestone] = None
    """A collection of related issues and pull requests."""

    node_id: str

    number: int
    """Number uniquely identifying the issue within its repository"""

    repository_url: str

    state: str
    """State of the issue; either 'open' or 'closed'"""

    title: str
    """Title of the issue"""

    updated_at: datetime

    url: str
    """URL for the issue"""

    user: Optional[User] = None
    """A GitHub user."""

    active_lock_reason: Optional[str] = None

    assignees: Optional[List[SimpleUser]] = None

    body: Optional[str] = None
    """Contents of the issue"""

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    closed_by: Optional[User] = None
    """A GitHub user."""

    draft: Optional[bool] = None

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    pull_request: Optional[IssuePullRequest] = None

    reactions: Optional[ReactionRollup] = None

    repository: Optional[Repository] = None
    """A repository on GitHub."""

    state_reason: Optional[Literal["completed", "reopened", "not_planned"]] = None
    """The reason for the current state"""

    sub_issues_summary: Optional[SubIssuesSummary] = None

    timeline_url: Optional[str] = None

    type: Optional[IssueType] = None
    """The type of issue."""


class Label(BaseModel):
    color: Optional[str] = None

    name: Optional[str] = None


class Milestone(BaseModel):
    title: str


class ProjectCard(BaseModel):
    id: int

    column_name: str

    project_id: int

    project_url: str

    url: str

    previous_column_name: Optional[str] = None


class Rename(BaseModel):
    from_: str = FieldInfo(alias="from")

    to: str


class IssueEvent(BaseModel):
    id: int

    actor: Optional[User] = None
    """A GitHub user."""

    commit_id: Optional[str] = None

    commit_url: Optional[str] = None

    created_at: datetime

    event: str

    node_id: str

    url: str

    assignee: Optional[User] = None
    """A GitHub user."""

    assigner: Optional[User] = None
    """A GitHub user."""

    author_association: Optional[AuthorAssociation] = None
    """How the author is associated with the repository."""

    dismissed_review: Optional[DismissedReview] = None

    issue: Optional[Issue] = None
    """
    Issues are a great way to keep track of tasks, enhancements, and bugs for your
    projects.
    """

    label: Optional[Label] = None
    """Issue Event Label"""

    lock_reason: Optional[str] = None

    milestone: Optional[Milestone] = None
    """Issue Event Milestone"""

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    project_card: Optional[ProjectCard] = None
    """Issue Event Project Card"""

    rename: Optional[Rename] = None
    """Issue Event Rename"""

    requested_reviewer: Optional[User] = None
    """A GitHub user."""

    requested_team: Optional[Team] = None
    """
    Groups of organization members that gives permissions on specified repositories.
    """

    review_requester: Optional[User] = None
    """A GitHub user."""
