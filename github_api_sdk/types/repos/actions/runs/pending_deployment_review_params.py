

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PendingDeploymentReviewParams"]


class PendingDeploymentReviewParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    comment: Required[str]
    """A comment to accompany the deployment review"""

    environment_ids: Required[Iterable[int]]
    """The list of environment ids to approve or reject"""

    state: Required[Literal["approved", "rejected"]]
    """Whether to approve or reject deployment to the specified environments."""
