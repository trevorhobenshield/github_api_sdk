

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..link import Link
from ...._models import BaseModel
from ...orgs.team import Team
from ..auto_merge import AutoMerge
from ...orgs.simple_user import SimpleUser
from ...users.repository import Repository
from ...applications.user import User
from ..nullable_milestone import NullableMilestone
from ...gists.author_association import AuthorAssociation

__all__ = ["PullRequestSimple", "_Links", "Base", "Head", "Label"]


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

    user: Optional[User] = None
    """A GitHub user."""


class Head(BaseModel):
    label: str

    ref: str

    repo: Repository
    """A repository on GitHub."""

    sha: str

    user: Optional[User] = None
    """A GitHub user."""


class Label(BaseModel):
    id: int

    color: str

    default: bool

    description: str

    name: str

    node_id: str

    url: str


class PullRequestSimple(BaseModel):
    id: int

    api_links: _Links = FieldInfo(alias="_links")

    assignee: Optional[User] = None
    """A GitHub user."""

    author_association: AuthorAssociation
    """How the author is associated with the repository."""

    auto_merge: Optional[AutoMerge] = None
    """The status of auto merging a pull request."""

    base: Base

    body: Optional[str] = None

    closed_at: Optional[datetime] = None

    comments_url: str

    commits_url: str

    created_at: datetime

    diff_url: str

    head: Head

    html_url: str

    issue_url: str

    labels: List[Label]

    locked: bool

    merge_commit_sha: Optional[str] = None

    merged_at: Optional[datetime] = None

    milestone: Optional[NullableMilestone] = None
    """A collection of related issues and pull requests."""

    node_id: str

    number: int

    patch_url: str

    review_comment_url: str

    review_comments_url: str

    state: str

    statuses_url: str

    title: str

    updated_at: datetime

    url: str

    user: Optional[User] = None
    """A GitHub user."""

    active_lock_reason: Optional[str] = None

    assignees: Optional[List[SimpleUser]] = None

    draft: Optional[bool] = None
    """Indicates whether or not the pull request is a draft."""

    requested_reviewers: Optional[List[SimpleUser]] = None

    requested_teams: Optional[List[Team]] = None
