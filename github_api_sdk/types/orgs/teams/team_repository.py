

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ...applications.user import User
from ..nullable_license_simple import NullableLicenseSimple

__all__ = ["TeamRepository", "Permissions"]


class Permissions(BaseModel):
    admin: bool

    pull: bool

    push: bool

    maintain: Optional[bool] = None

    triage: Optional[bool] = None


class TeamRepository(BaseModel):
    id: int
    """Unique identifier of the repository"""

    archive_url: str

    archived: bool
    """Whether the repository is archived."""

    assignees_url: str

    blobs_url: str

    branches_url: str

    clone_url: str

    collaborators_url: str

    comments_url: str

    commits_url: str

    compare_url: str

    contents_url: str

    contributors_url: str

    created_at: Optional[datetime] = None

    default_branch: str
    """The default branch of the repository."""

    deployments_url: str

    description: Optional[str] = None

    disabled: bool
    """Returns whether or not this repository disabled."""

    downloads_url: str

    events_url: str

    fork: bool

    forks: int

    forks_count: int

    forks_url: str

    full_name: str

    git_commits_url: str

    git_refs_url: str

    git_tags_url: str

    git_url: str

    has_downloads: bool
    """Whether downloads are enabled."""

    has_issues: bool
    """Whether issues are enabled."""

    has_pages: bool

    has_projects: bool
    """Whether projects are enabled."""

    has_wiki: bool
    """Whether the wiki is enabled."""

    homepage: Optional[str] = None

    hooks_url: str

    html_url: str

    issue_comment_url: str

    issue_events_url: str

    issues_url: str

    keys_url: str

    labels_url: str

    language: Optional[str] = None

    languages_url: str

    license: Optional[NullableLicenseSimple] = None
    """License Simple"""

    merges_url: str

    milestones_url: str

    mirror_url: Optional[str] = None

    name: str
    """The name of the repository."""

    node_id: str

    notifications_url: str

    open_issues: int

    open_issues_count: int

    owner: Optional[User] = None
    """A GitHub user."""

    private: bool
    """Whether the repository is private or public."""

    pulls_url: str

    pushed_at: Optional[datetime] = None

    releases_url: str

    size: int

    ssh_url: str

    stargazers_count: int

    stargazers_url: str

    statuses_url: str

    subscribers_url: str

    subscription_url: str

    svn_url: str

    tags_url: str

    teams_url: str

    trees_url: str

    updated_at: Optional[datetime] = None

    url: str

    watchers: int

    watchers_count: int

    allow_auto_merge: Optional[bool] = None
    """Whether to allow Auto-merge to be used on pull requests."""

    allow_forking: Optional[bool] = None
    """Whether to allow forking this repo"""

    allow_merge_commit: Optional[bool] = None
    """Whether to allow merge commits for pull requests."""

    allow_rebase_merge: Optional[bool] = None
    """Whether to allow rebase merges for pull requests."""

    allow_squash_merge: Optional[bool] = None
    """Whether to allow squash merges for pull requests."""

    delete_branch_on_merge: Optional[bool] = None
    """Whether to delete head branches when pull requests are merged"""

    is_template: Optional[bool] = None
    """
    Whether this repository acts as a template that can be used to generate new
    repositories.
    """

    master_branch: Optional[str] = None

    network_count: Optional[int] = None

    permissions: Optional[Permissions] = None

    role_name: Optional[str] = None

    subscribers_count: Optional[int] = None

    temp_clone_token: Optional[str] = None

    topics: Optional[List[str]] = None

    visibility: Optional[str] = None
    """The repository visibility: public, private, or internal."""

    web_commit_signoff_required: Optional[bool] = None
    """Whether to require contributors to sign off on web-based commits"""
