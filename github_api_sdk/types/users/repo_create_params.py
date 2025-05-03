

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepoCreateParams"]


class RepoCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the repository."""

    allow_auto_merge: bool
    """Whether to allow Auto-merge to be used on pull requests."""

    allow_merge_commit: bool
    """Whether to allow merge commits for pull requests."""

    allow_rebase_merge: bool
    """Whether to allow rebase merges for pull requests."""

    allow_squash_merge: bool
    """Whether to allow squash merges for pull requests."""

    auto_init: bool
    """Whether the repository is initialized with a minimal README."""

    delete_branch_on_merge: bool
    """Whether to delete head branches when pull requests are merged"""

    description: str
    """A short description of the repository."""

    gitignore_template: str
    """The desired language or platform to apply to the .gitignore."""

    has_discussions: bool
    """Whether discussions are enabled."""

    has_downloads: bool
    """Whether downloads are enabled."""

    has_issues: bool
    """Whether issues are enabled."""

    has_projects: bool
    """Whether projects are enabled."""

    has_wiki: bool
    """Whether the wiki is enabled."""

    homepage: str
    """A URL with more information about the repository."""

    is_template: bool
    """
    Whether this repository acts as a template that can be used to generate new
    repositories.
    """

    license_template: str
    """The license keyword of the open source license for this repository."""

    merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"]
    """The default value for a merge commit message.

    - `PR_TITLE` - default to the pull request's title.
    - `PR_BODY` - default to the pull request's body.
    - `BLANK` - default to a blank commit message.
    """

    merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"]
    """Required when using `merge_commit_message`.

    The default value for a merge commit title.

    - `PR_TITLE` - default to the pull request's title.
    - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g.,
      Merge pull request #123 from branch-name).
    """

    private: bool
    """Whether the repository is private."""

    squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"]
    """The default value for a squash merge commit message:

    - `PR_BODY` - default to the pull request's body.
    - `COMMIT_MESSAGES` - default to the branch's commit messages.
    - `BLANK` - default to a blank commit message.
    """

    squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"]
    """Required when using `squash_merge_commit_message`.

    The default value for a squash merge commit title:

    - `PR_TITLE` - default to the pull request's title.
    - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or
      the pull request's title (when more than one commit).
    """

    team_id: int
    """The id of the team that will be granted access to this repository.

    This is only valid when creating a repository in an organization.
    """
