

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..orgs.issue_type import IssueType
from ..orgs.simple_user import SimpleUser
from ..users.repository import Repository
from ..applications.user import User
from .nullable_milestone import NullableMilestone
from .sub_issues_summary import SubIssuesSummary
from .nullable_integration import NullableIntegration
from ..gists.author_association import AuthorAssociation
from ..orgs.teams.reaction_rollup import ReactionRollup

__all__ = ["Issue", "Label", "LabelUnionMember1", "PullRequest"]


class LabelUnionMember1(BaseModel):
    id: Optional[int] = None

    color: Optional[str] = None

    default: Optional[bool] = None

    description: Optional[str] = None

    name: Optional[str] = None

    node_id: Optional[str] = None

    url: Optional[str] = None


Label: TypeAlias = Union[str, LabelUnionMember1]


class PullRequest(BaseModel):
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

    labels: List[Label]
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

    pull_request: Optional[PullRequest] = None

    reactions: Optional[ReactionRollup] = None

    repository: Optional[Repository] = None
    """A repository on GitHub."""

    state_reason: Optional[Literal["completed", "reopened", "not_planned"]] = None
    """The reason for the current state"""

    sub_issues_summary: Optional[SubIssuesSummary] = None

    timeline_url: Optional[str] = None

    type: Optional[IssueType] = None
    """The type of issue."""
