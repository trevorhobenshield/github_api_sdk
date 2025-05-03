

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "RunReviewDeploymentProtectionRuleParams",
    "ReviewCustomGatesCommentRequired",
    "ReviewCustomGatesStateRequired",
]


class ReviewCustomGatesCommentRequired(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    comment: Required[str]
    """Comment associated with the pending deployment protection rule.

    **Required when state is not provided.**
    """

    environment_name: Required[str]
    """The name of the environment to approve or reject."""


class ReviewCustomGatesStateRequired(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    environment_name: Required[str]
    """The name of the environment to approve or reject."""

    state: Required[Literal["approved", "rejected"]]
    """Whether to approve or reject deployment to the specified environments."""

    comment: str
    """Optional comment to include with the review."""


RunReviewDeploymentProtectionRuleParams: TypeAlias = Union[
    ReviewCustomGatesCommentRequired, ReviewCustomGatesStateRequired
]
