

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..applications.user import User
from ..search_result_text_match import SearchResultTextMatch
from ..orgs.nullable_license_simple import NullableLicenseSimple

__all__ = ["RepositorySearchResponse", "Item", "ItemPermissions"]


class ItemPermissions(BaseModel):
    admin: bool

    pull: bool

    push: bool

    maintain: Optional[bool] = None

    triage: Optional[bool] = None


class Item(BaseModel):
    id: int

    archive_url: str

    archived: bool

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

    created_at: datetime

    default_branch: str

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

    has_issues: bool

    has_pages: bool

    has_projects: bool

    has_wiki: bool

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

    node_id: str

    notifications_url: str

    open_issues: int

    open_issues_count: int

    owner: Optional[User] = None
    """A GitHub user."""

    private: bool

    pulls_url: str

    pushed_at: datetime

    releases_url: str

    score: float

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

    updated_at: datetime

    url: str

    watchers: int

    watchers_count: int

    allow_auto_merge: Optional[bool] = None

    allow_forking: Optional[bool] = None

    allow_merge_commit: Optional[bool] = None

    allow_rebase_merge: Optional[bool] = None

    allow_squash_merge: Optional[bool] = None

    delete_branch_on_merge: Optional[bool] = None

    has_discussions: Optional[bool] = None

    is_template: Optional[bool] = None

    master_branch: Optional[str] = None

    permissions: Optional[ItemPermissions] = None

    temp_clone_token: Optional[str] = None

    text_matches: Optional[List[SearchResultTextMatch]] = None

    topics: Optional[List[str]] = None

    visibility: Optional[str] = None
    """The repository visibility: public, private, or internal."""

    web_commit_signoff_required: Optional[bool] = None


class RepositorySearchResponse(BaseModel):
    incomplete_results: bool

    items: List[Item]

    total_count: int
