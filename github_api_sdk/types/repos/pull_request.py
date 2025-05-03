

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .link import Link
from ..._models import BaseModel
from .auto_merge import AutoMerge
from ..orgs.simple_user import SimpleUser
from ..orgs.team_simple import TeamSimple
from ..users.repository import Repository
from ..applications.user import User
from .nullable_milestone import NullableMilestone
from ..gists.author_association import AuthorAssociation

__all__ = ["PullRequest", "_Links", "Base", "Head", "Label"]


class _Links(BaseModel):
    comments: Link
    """Hypermedia Link"""

    commits: Link
    """Hypermedia Link"""

    html: Link
    """Hypermedia Link"""

    issue: Link
    """Hypermedia Link"""

    review_comment: Link
    """Hypermedia Link"""

    review_comments: Link
    """Hypermedia Link"""

    self: Link
    """Hypermedia Link"""

    statuses: Link
    """Hypermedia Link"""


class Base(BaseModel):
    label: str

    ref: str

    repo: Repository
    """A repository on GitHub."""

    sha: str

    user: SimpleUser
    """A GitHub user."""


class Head(BaseModel):
    label: str

    ref: str

    repo: Repository
    """A repository on GitHub."""

    sha: str

    user: SimpleUser
    """A GitHub user."""


class Label(BaseModel):
    id: int

    color: str

    default: bool

    description: Optional[str] = None

    name: str

    node_id: str

    url: str


class PullRequest(BaseModel):
    id: int

    api_links: _Links = FieldInfo(alias="_links")

    additions: int

    assignee: Optional[User] = None
    """A GitHub user."""

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    auto_merge: Optional[AutoMerge] = None
    """The status of auto merging a pull request."""

    base: Base

    body: Optional[str] = None

    changed_files: int

    closed_at: Optional[datetime] = None

    comments: int

    comments_url: str

    commits: int

    commits_url: str

    created_at: datetime

    deletions: int

    diff_url: str

    head: Head

    html_url: str

    issue_url: str

    labels: List[Label]

    locked: bool

    maintainer_can_modify: bool
    """Indicates whether maintainers can modify the pull request."""

    merge_commit_sha: Optional[str] = None

    mergeable: Optional[bool] = None

    mergeable_state: str

    merged: bool

    merged_at: Optional[datetime] = None

    merged_by: Optional[User] = None
    """A GitHub user."""

    milestone: Optional[NullableMilestone] = None
    """A collection of related issues and pull requests."""

    node_id: str

    number: int
    """Number uniquely identifying the pull request within its repository."""

    patch_url: str

    review_comment_url: str

    review_comments: int

    review_comments_url: str

    state: Literal["open", "closed"]
    """State of this Pull Request. Either `open` or `closed`."""

    statuses_url: str

    title: str
    """The title of the pull request."""

    updated_at: datetime

    url: str

    user: SimpleUser
    """A GitHub user."""

    active_lock_reason: Optional[str] = None

    assignees: Optional[List[SimpleUser]] = None

    draft: Optional[bool] = None
    """Indicates whether or not the pull request is a draft."""

    rebaseable: Optional[bool] = None

    requested_reviewers: Optional[List[SimpleUser]] = None

    requested_teams: Optional[List[TeamSimple]] = None
