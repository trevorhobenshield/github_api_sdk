

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .simple_user import SimpleUser
from ..users.repository import Repository
from ..applications.user import User
from .security_and_analysis import SecurityAndAnalysis
from .nullable_license_simple import NullableLicenseSimple

__all__ = ["FullRepository", "CodeOfConduct", "Permissions", "TemplateRepository", "TemplateRepositoryPermissions"]


class CodeOfConduct(BaseModel):
    html_url: Optional[str] = None

    key: str

    name: str

    url: str


class Permissions(BaseModel):
    admin: bool

    pull: bool

    push: bool

    maintain: Optional[bool] = None

    triage: Optional[bool] = None


class TemplateRepositoryPermissions(BaseModel):
    admin: bool

    pull: bool

    push: bool

    maintain: Optional[bool] = None

    triage: Optional[bool] = None


class TemplateRepository(BaseModel):
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

    owner: SimpleUser
    """A GitHub user."""

    private: bool
    """Whether the repository is private or public."""

    pulls_url: str

    pushed_at: Optional[datetime] = None

    releases_url: str

    size: int
    """The size of the repository, in kilobytes.

    Size is calculated hourly. When a repository is initially created, the size
    is 0.
    """

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

    allow_update_branch: Optional[bool] = None
    """
    Whether or not a pull request head branch that is behind its base branch can
    always be updated even if it is not required to be up to date before merging.
    """

    anonymous_access_enabled: Optional[bool] = None
    """Whether anonymous git access is enabled for this repository"""

    delete_branch_on_merge: Optional[bool] = None
    """Whether to delete head branches when pull requests are merged"""

    has_discussions: Optional[bool] = None
    """Whether discussions are enabled."""

    is_template: Optional[bool] = None
    """
    Whether this repository acts as a template that can be used to generate new
    repositories.
    """

    master_branch: Optional[str] = None

    merge_commit_message: Optional[Literal["PR_BODY", "PR_TITLE", "BLANK"]] = None
    """The default value for a merge commit message.

    - `PR_TITLE` - default to the pull request's title.
    - `PR_BODY` - default to the pull request's body.
    - `BLANK` - default to a blank commit message.
    """

    merge_commit_title: Optional[Literal["PR_TITLE", "MERGE_MESSAGE"]] = None
    """The default value for a merge commit title.

    - `PR_TITLE` - default to the pull request's title.
    - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g.,
      Merge pull request #123 from branch-name).
    """

    permissions: Optional[TemplateRepositoryPermissions] = None

    squash_merge_commit_message: Optional[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]] = None
    """The default value for a squash merge commit message:

    - `PR_BODY` - default to the pull request's body.
    - `COMMIT_MESSAGES` - default to the branch's commit messages.
    - `BLANK` - default to a blank commit message.
    """

    squash_merge_commit_title: Optional[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]] = None
    """The default value for a squash merge commit title:

    - `PR_TITLE` - default to the pull request's title.
    - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or
      the pull request's title (when more than one commit).
    """

    starred_at: Optional[str] = None

    temp_clone_token: Optional[str] = None

    topics: Optional[List[str]] = None

    use_squash_pr_title_as_default: Optional[bool] = None
    """Whether a squash merge commit can use the pull request title as default.

    \\**\\**This property is closing down. Please use `squash_merge_commit_title`
    instead.
    """

    visibility: Optional[str] = None
    """The repository visibility: public, private, or internal."""

    web_commit_signoff_required: Optional[bool] = None
    """Whether to require contributors to sign off on web-based commits"""


class FullRepository(BaseModel):
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

    has_discussions: bool

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

    network_count: int

    node_id: str

    notifications_url: str

    open_issues: int

    open_issues_count: int

    owner: SimpleUser
    """A GitHub user."""

    private: bool

    pulls_url: str

    pushed_at: datetime

    releases_url: str

    size: int
    """The size of the repository, in kilobytes.

    Size is calculated hourly. When a repository is initially created, the size
    is 0.
    """

    ssh_url: str

    stargazers_count: int

    stargazers_url: str

    statuses_url: str

    subscribers_count: int

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

    allow_update_branch: Optional[bool] = None

    anonymous_access_enabled: Optional[bool] = None
    """Whether anonymous git access is allowed."""

    code_of_conduct: Optional[CodeOfConduct] = None
    """Code of Conduct Simple"""

    custom_properties: Optional[Dict[str, object]] = None
    """The custom properties that were defined for the repository.

    The keys are the custom property names, and the values are the corresponding
    custom property values.
    """

    delete_branch_on_merge: Optional[bool] = None

    has_downloads: Optional[bool] = None

    is_template: Optional[bool] = None

    master_branch: Optional[str] = None

    merge_commit_message: Optional[Literal["PR_BODY", "PR_TITLE", "BLANK"]] = None
    """The default value for a merge commit message.

    - `PR_TITLE` - default to the pull request's title.
    - `PR_BODY` - default to the pull request's body.
    - `BLANK` - default to a blank commit message.
    """

    merge_commit_title: Optional[Literal["PR_TITLE", "MERGE_MESSAGE"]] = None
    """The default value for a merge commit title.

    - `PR_TITLE` - default to the pull request's title.
    - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g.,
      Merge pull request #123 from branch-name).
    """

    organization: Optional[User] = None
    """A GitHub user."""

    parent: Optional[Repository] = None
    """A repository on GitHub."""

    permissions: Optional[Permissions] = None

    security_and_analysis: Optional[SecurityAndAnalysis] = None

    source: Optional[Repository] = None
    """A repository on GitHub."""

    squash_merge_commit_message: Optional[Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]] = None
    """The default value for a squash merge commit message:

    - `PR_BODY` - default to the pull request's body.
    - `COMMIT_MESSAGES` - default to the branch's commit messages.
    - `BLANK` - default to a blank commit message.
    """

    squash_merge_commit_title: Optional[Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]] = None
    """The default value for a squash merge commit title:

    - `PR_TITLE` - default to the pull request's title.
    - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or
      the pull request's title (when more than one commit).
    """

    temp_clone_token: Optional[str] = None

    template_repository: Optional[TemplateRepository] = None
    """A repository on GitHub."""

    topics: Optional[List[str]] = None

    use_squash_pr_title_as_default: Optional[bool] = None

    visibility: Optional[str] = None
    """The repository visibility: public, private, or internal."""

    web_commit_signoff_required: Optional[bool] = None
