

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRulePullRequest", "Parameters"]


class Parameters(BaseModel):
    dismiss_stale_reviews_on_push: bool
    """
    New, reviewable commits pushed will dismiss previous pull request review
    approvals.
    """

    require_code_owner_review: bool
    """
    Require an approving review in pull requests that modify files that have a
    designated code owner.
    """

    require_last_push_approval: bool
    """
    Whether the most recent reviewable push must be approved by someone other than
    the person who pushed it.
    """

    required_approving_review_count: int
    """
    The number of approving reviews that are required before a pull request can be
    merged.
    """

    required_review_thread_resolution: bool
    """All conversations on code must be resolved before a pull request can be merged."""

    allowed_merge_methods: Optional[List[Literal["merge", "squash", "rebase"]]] = None
    """Array of allowed merge methods.

    Allowed values include `merge`, `squash`, and `rebase`. At least one option must
    be enabled.
    """

    automatic_copilot_code_review_enabled: Optional[bool] = None
    """
    Automatically request review from Copilot for new pull requests, if the author
    has access to Copilot code review.
    """


class RepositoryRulePullRequest(BaseModel):
    type: Literal["pull_request"]

    parameters: Optional[Parameters] = None
