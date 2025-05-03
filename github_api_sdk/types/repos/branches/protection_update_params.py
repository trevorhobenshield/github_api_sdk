

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = [
    "ProtectionUpdateParams",
    "RequiredPullRequestReviews",
    "RequiredPullRequestReviewsBypassPullRequestAllowances",
    "RequiredPullRequestReviewsDismissalRestrictions",
    "RequiredStatusChecks",
    "RequiredStatusChecksCheck",
    "Restrictions",
]


class ProtectionUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    enforce_admins: Required[bool | None]
    """Enforce all configured restrictions for administrators.

    Set to `true` to enforce required status checks for repository administrators.
    Set to `null` to disable.
    """

    required_pull_request_reviews: Required[RequiredPullRequestReviews | None]
    """Require at least one approving review on a pull request, before merging.

    Set to `null` to disable.
    """

    required_status_checks: Required[RequiredStatusChecks | None]
    """Require status checks to pass before merging. Set to `null` to disable."""

    restrictions: Required[Restrictions | None]
    """Restrict who can push to the protected branch.

    User, app, and team `restrictions` are only available for organization-owned
    repositories. Set to `null` to disable.
    """

    allow_deletions: bool
    """
    Allows deletion of the protected branch by anyone with write access to the
    repository. Set to `false` to prevent deletion of the protected branch. Default:
    `false`. For more information, see
    "[Enabling force pushes to a protected branch](https://docs.github.com/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)"
    in the GitHub Help documentation.
    """

    allow_force_pushes: bool | None
    """
    Permits force pushes to the protected branch by anyone with write access to the
    repository. Set to `true` to allow force pushes. Set to `false` or `null` to
    block force pushes. Default: `false`. For more information, see
    "[Enabling force pushes to a protected branch](https://docs.github.com/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)"
    in the GitHub Help documentation."
    """

    allow_fork_syncing: bool
    """Whether users can pull changes from upstream when the branch is locked.

    Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    Default: `false`.
    """

    block_creations: bool
    """
    If set to `true`, the `restrictions` branch protection settings which limits who
    can push will also block pushes which create new branches, unless the push is
    initiated by a user, team, or app which has the ability to push. Set to `true`
    to restrict new branch creation. Default: `false`.
    """

    lock_branch: bool
    """Whether to set the branch as read-only.

    If this is true, users will not be able to push to the branch. Default: `false`.
    """

    required_conversation_resolution: bool
    """
    Requires all conversations on code to be resolved before a pull request can be
    merged into a branch that matches this rule. Set to `false` to disable. Default:
    `false`.
    """

    required_linear_history: bool
    """
    Enforces a linear commit Git history, which prevents anyone from pushing merge
    commits to a branch. Set to `true` to enforce a linear commit history. Set to
    `false` to disable a linear commit Git history. Your repository must allow
    squash merging or rebase merging before you can enable a linear commit history.
    Default: `false`. For more information, see
    "[Requiring a linear commit history](https://docs.github.com/github/administering-a-repository/requiring-a-linear-commit-history)"
    in the GitHub Help documentation.
    """


class RequiredPullRequestReviewsBypassPullRequestAllowances(TypedDict, total=False):
    apps: list[str]
    """The list of app `slug`s allowed to bypass pull request requirements."""

    teams: list[str]
    """The list of team `slug`s allowed to bypass pull request requirements."""

    users: list[str]
    """The list of user `login`s allowed to bypass pull request requirements."""


class RequiredPullRequestReviewsDismissalRestrictions(TypedDict, total=False):
    apps: list[str]
    """The list of app `slug`s with dismissal access"""

    teams: list[str]
    """The list of team `slug`s with dismissal access"""

    users: list[str]
    """The list of user `login`s with dismissal access"""


class RequiredPullRequestReviews(TypedDict, total=False):
    bypass_pull_request_allowances: RequiredPullRequestReviewsBypassPullRequestAllowances
    """Allow specific users, teams, or apps to bypass pull request requirements."""

    dismiss_stale_reviews: bool
    """
    Set to `true` if you want to automatically dismiss approving reviews when
    someone pushes a new commit.
    """

    dismissal_restrictions: RequiredPullRequestReviewsDismissalRestrictions
    """Specify which users, teams, and apps can dismiss pull request reviews.

    Pass an empty `dismissal_restrictions` object to disable. User and team
    `dismissal_restrictions` are only available for organization-owned repositories.
    Omit this parameter for personal repositories.
    """

    require_code_owner_reviews: bool
    """
    Blocks merging pull requests until
    [code owners](https://docs.github.com/articles/about-code-owners/) review them.
    """

    require_last_push_approval: bool
    """
    Whether the most recent push must be approved by someone other than the person
    who pushed it. Default: `false`.
    """

    required_approving_review_count: int
    """Specify the number of reviewers required to approve pull requests.

    Use a number between 1 and 6 or 0 to not require reviewers.
    """


class RequiredStatusChecksCheck(TypedDict, total=False):
    context: Required[str]
    """The name of the required check"""

    app_id: int
    """The ID of the GitHub App that must provide this check.

    Omit this field to automatically select the GitHub App that has recently
    provided this check, or any app if it was not set by a GitHub App. Pass -1 to
    explicitly allow any app to set the status.
    """


class RequiredStatusChecks(TypedDict, total=False):
    contexts: Required[list[str]]
    """
    **Closing down notice**: The list of status checks to require in order to merge
    into this branch. If any of these checks have recently been set by a particular
    GitHub App, they will be required to come from that app in future for the branch
    to merge. Use `checks` instead of `contexts` for more fine-grained control.
    """

    strict: Required[bool]
    """Require branches to be up to date before merging."""

    checks: Iterable[RequiredStatusChecksCheck]
    """The list of status checks to require in order to merge into this branch."""


class Restrictions(TypedDict, total=False):
    teams: Required[list[str]]
    """The list of team `slug`s with push access"""

    users: Required[list[str]]
    """The list of user `login`s with push access"""

    apps: list[str]
    """The list of app `slug`s with push access"""
