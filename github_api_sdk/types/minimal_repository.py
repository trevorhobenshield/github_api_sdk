

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .code_of_conduct import CodeOfConduct
from .orgs.simple_user import SimpleUser
from .orgs.security_and_analysis import SecurityAndAnalysis

__all__ = ["MinimalRepository", "License", "Permissions"]


class License(BaseModel):
    key: Optional[str] = None

    name: Optional[str] = None

    node_id: Optional[str] = None

    spdx_id: Optional[str] = None

    url: Optional[str] = None


class Permissions(BaseModel):
    admin: Optional[bool] = None

    maintain: Optional[bool] = None

    pull: Optional[bool] = None

    push: Optional[bool] = None

    triage: Optional[bool] = None


class MinimalRepository(BaseModel):
    id: int

    archive_url: str

    assignees_url: str

    blobs_url: str

    branches_url: str

    collaborators_url: str

    comments_url: str

    commits_url: str

    compare_url: str

    contents_url: str

    contributors_url: str

    deployments_url: str

    description: Optional[str] = None

    downloads_url: str

    events_url: str

    fork: bool

    forks_url: str

    full_name: str

    git_commits_url: str

    git_refs_url: str

    git_tags_url: str

    hooks_url: str

    html_url: str

    issue_comment_url: str

    issue_events_url: str

    issues_url: str

    keys_url: str

    labels_url: str

    languages_url: str

    merges_url: str

    milestones_url: str

    name: str

    node_id: str

    notifications_url: str

    owner: SimpleUser
    """A GitHub user."""

    private: bool

    pulls_url: str

    releases_url: str

    stargazers_url: str

    statuses_url: str

    subscribers_url: str

    subscription_url: str

    tags_url: str

    teams_url: str

    trees_url: str

    url: str

    allow_forking: Optional[bool] = None

    archived: Optional[bool] = None

    clone_url: Optional[str] = None

    code_of_conduct: Optional[CodeOfConduct] = None
    """Code Of Conduct"""

    created_at: Optional[datetime] = None

    default_branch: Optional[str] = None

    delete_branch_on_merge: Optional[bool] = None

    disabled: Optional[bool] = None

    forks: Optional[int] = None

    forks_count: Optional[int] = None

    git_url: Optional[str] = None

    has_discussions: Optional[bool] = None

    has_downloads: Optional[bool] = None

    has_issues: Optional[bool] = None

    has_pages: Optional[bool] = None

    has_projects: Optional[bool] = None

    has_wiki: Optional[bool] = None

    homepage: Optional[str] = None

    is_template: Optional[bool] = None

    language: Optional[str] = None

    license: Optional[License] = None

    mirror_url: Optional[str] = None

    network_count: Optional[int] = None

    open_issues: Optional[int] = None

    open_issues_count: Optional[int] = None

    permissions: Optional[Permissions] = None

    pushed_at: Optional[datetime] = None

    role_name: Optional[str] = None

    security_and_analysis: Optional[SecurityAndAnalysis] = None

    size: Optional[int] = None
    """The size of the repository, in kilobytes.

    Size is calculated hourly. When a repository is initially created, the size
    is 0.
    """

    ssh_url: Optional[str] = None

    stargazers_count: Optional[int] = None

    subscribers_count: Optional[int] = None

    svn_url: Optional[str] = None

    temp_clone_token: Optional[str] = None

    topics: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    visibility: Optional[str] = None

    watchers: Optional[int] = None

    watchers_count: Optional[int] = None

    web_commit_signoff_required: Optional[bool] = None
