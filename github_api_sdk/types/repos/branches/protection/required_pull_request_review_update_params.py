

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RequiredPullRequestReviewUpdateParams", "BypassPullRequestAllowances", "DismissalRestrictions"]


class RequiredPullRequestReviewUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    bypass_pull_request_allowances: BypassPullRequestAllowances
    """Allow specific users, teams, or apps to bypass pull request requirements."""

    dismiss_stale_reviews: bool
    """
    Set to `true` if you want to automatically dismiss approving reviews when
    someone pushes a new commit.
    """

    dismissal_restrictions: DismissalRestrictions
    """Specify which users, teams, and apps can dismiss pull request reviews.

    Pass an empty `dismissal_restrictions` object to disable. User and team
    `dismissal_restrictions` are only available for organization-owned repositories.
    Omit this parameter for personal repositories.
    """

    require_code_owner_reviews: bool
    """
    Blocks merging pull requests until
    [code owners](https://docs.github.com/articles/about-code-owners/) have
    reviewed.
    """

    require_last_push_approval: bool
    """
    Whether the most recent push must be approved by someone other than the person
    who pushed it. Default: `false`
    """

    required_approving_review_count: int
    """Specifies the number of reviewers required to approve pull requests.

    Use a number between 1 and 6 or 0 to not require reviewers.
    """


class BypassPullRequestAllowances(TypedDict, total=False):
    apps: list[str]
    """The list of app `slug`s allowed to bypass pull request requirements."""

    teams: list[str]
    """The list of team `slug`s allowed to bypass pull request requirements."""

    users: list[str]
    """The list of user `login`s allowed to bypass pull request requirements."""


class DismissalRestrictions(TypedDict, total=False):
    apps: list[str]
    """The list of app `slug`s with dismissal access"""

    teams: list[str]
    """The list of team `slug`s with dismissal access"""

    users: list[str]
    """The list of user `login`s with dismissal access"""
