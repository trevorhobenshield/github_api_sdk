

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepoCreateParams"]


class RepoCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the repository."""

    allow_auto_merge: bool
    """
    Either `true` to allow auto-merge on pull requests, or `false` to disallow
    auto-merge.
    """

    allow_merge_commit: bool
    """
    Either `true` to allow merging pull requests with a merge commit, or `false` to
    prevent merging pull requests with merge commits.
    """

    allow_rebase_merge: bool
    """
    Either `true` to allow rebase-merging pull requests, or `false` to prevent
    rebase-merging.
    """

    allow_squash_merge: bool
    """
    Either `true` to allow squash-merging pull requests, or `false` to prevent
    squash-merging.
    """

    auto_init: bool
    """Pass `true` to create an initial commit with empty README."""

    custom_properties: dict[str, object]
    """The custom properties for the new repository.

    The keys are the custom property names, and the values are the corresponding
    custom property values.
    """

    delete_branch_on_merge: bool
    """
    Either `true` to allow automatically deleting head branches when pull requests
    are merged, or `false` to prevent automatic deletion. **The authenticated user
    must be an organization owner to set this property to `true`.**
    """

    description: str
    """A short description of the repository."""

    gitignore_template: str
    """
    Desired language or platform
    [.gitignore template](https://github.com/github/gitignore) to apply. Use the
    name of the template without the extension. For example, "Haskell".
    """

    has_downloads: bool
    """Whether downloads are enabled."""

    has_issues: bool
    """Either `true` to enable issues for this repository or `false` to disable them."""

    has_projects: bool
    """Either `true` to enable projects for this repository or `false` to disable them.

    **Note:** If you're creating a repository in an organization that has disabled
    repository projects, the default is `false`, and if you pass `true`, the API
    returns an error.
    """

    has_wiki: bool
    """Either `true` to enable the wiki for this repository or `false` to disable it."""

    homepage: str
    """A URL with more information about the repository."""

    is_template: bool
    """
    Either `true` to make this repo available as a template repository or `false` to
    prevent it.
    """

    license_template: str
    """
    Choose an [open source license template](https://choosealicense.com/) that best
    suits your needs, and then use the
    [license keyword](https://docs.github.com/articles/licensing-a-repository/#searching-github-by-license-type)
    as the `license_template` string. For example, "mit" or "mpl-2.0".
    """

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

    use_squash_pr_title_as_default: bool
    """
    Either `true` to allow squash-merge commits to use pull request title, or
    `false` to use commit message. \\**\\**This property is closing down. Please use
    `squash_merge_commit_title` instead.
    """

    visibility: Literal["public", "private"]
    """The visibility of the repository."""
