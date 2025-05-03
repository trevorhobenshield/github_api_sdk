

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..orgs.issue_type import IssueType
from ..orgs.simple_user import SimpleUser
from ..users.repository import Repository
from ..applications.user import User
from ..gists.author_association import AuthorAssociation
from ..repos.nullable_milestone import NullableMilestone
from ..search_result_text_match import SearchResultTextMatch
from ..orgs.teams.reaction_rollup import ReactionRollup
from ..repos.nullable_integration import NullableIntegration

__all__ = ["IssueSearchResponse", "Item", "ItemLabel", "ItemPullRequest", "ItemSubIssuesSummary"]


class ItemLabel(BaseModel):
    id: Optional[int] = None

    color: Optional[str] = None

    default: Optional[bool] = None

    description: Optional[str] = None

    name: Optional[str] = None

    node_id: Optional[str] = None

    url: Optional[str] = None


class ItemPullRequest(BaseModel):
    diff_url: Optional[str] = None

    html_url: Optional[str] = None

    patch_url: Optional[str] = None

    url: Optional[str] = None

    merged_at: Optional[datetime] = None


class ItemSubIssuesSummary(BaseModel):
    completed: int

    percent_completed: int

    total: int


class Item(BaseModel):
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

    labels: List[ItemLabel]

    labels_url: str

    locked: bool

    milestone: Optional[NullableMilestone] = None
    """A collection of related issues and pull requests."""

    node_id: str

    number: int

    repository_url: str

    score: float

    state: str

    title: str

    updated_at: datetime

    url: str

    user: Optional[User] = None
    """A GitHub user."""

    active_lock_reason: Optional[str] = None

    assignees: Optional[List[SimpleUser]] = None

    body: Optional[str] = None

    body_html: Optional[str] = None

    body_text: Optional[str] = None

    draft: Optional[bool] = None

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    pull_request: Optional[ItemPullRequest] = None

    reactions: Optional[ReactionRollup] = None

    repository: Optional[Repository] = None
    """A repository on GitHub."""

    state_reason: Optional[str] = None

    sub_issues_summary: Optional[ItemSubIssuesSummary] = None

    text_matches: Optional[List[SearchResultTextMatch]] = None

    timeline_url: Optional[str] = None

    type: Optional[IssueType] = None
    """The type of issue."""


class IssueSearchResponse(BaseModel):
    incomplete_results: bool

    items: List[Item]

    total_count: int
