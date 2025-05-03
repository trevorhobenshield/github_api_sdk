

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRulePullRequestParam", "Parameters"]


class Parameters(TypedDict, total=False):
    dismiss_stale_reviews_on_push: Required[bool]
    """
    New, reviewable commits pushed will dismiss previous pull request review
    approvals.
    """

    require_code_owner_review: Required[bool]
    """
    Require an approving review in pull requests that modify files that have a
    designated code owner.
    """

    require_last_push_approval: Required[bool]
    """
    Whether the most recent reviewable push must be approved by someone other than
    the person who pushed it.
    """

    required_approving_review_count: Required[int]
    """
    The number of approving reviews that are required before a pull request can be
    merged.
    """

    required_review_thread_resolution: Required[bool]
    """All conversations on code must be resolved before a pull request can be merged."""

    allowed_merge_methods: list[Literal["merge", "squash", "rebase"]]
    """Array of allowed merge methods.

    Allowed values include `merge`, `squash`, and `rebase`. At least one option must
    be enabled.
    """

    automatic_copilot_code_review_enabled: bool
    """
    Automatically request review from Copilot for new pull requests, if the author
    has access to Copilot code review.
    """


class RepositoryRulePullRequestParam(TypedDict, total=False):
    type: Required[Literal["pull_request"]]

    parameters: Parameters
