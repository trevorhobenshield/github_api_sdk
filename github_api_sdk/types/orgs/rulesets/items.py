

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Items"]


class Items(BaseModel):
    id: Optional[int] = None
    """The unique identifier of the rule insight."""

    actor_id: Optional[int] = None
    """The number that identifies the user."""

    actor_name: Optional[str] = None
    """The handle for the GitHub user account."""

    after_sha: Optional[str] = None
    """The last commit sha in the push evaluation."""

    before_sha: Optional[str] = None
    """The first commit sha before the push evaluation."""

    evaluation_result: Optional[Literal["pass", "fail", "bypass"]] = None
    """
    The result of the rule evaluations for rules with the `active` and `evaluate`
    enforcement statuses, demonstrating whether rules would pass or fail if all
    rules in the rule suite were `active`.
    """

    pushed_at: Optional[datetime] = None

    ref: Optional[str] = None
    """The ref name that the evaluation ran on."""

    repository_id: Optional[int] = None
    """The ID of the repository associated with the rule evaluation."""

    repository_name: Optional[str] = None
    """The name of the repository without the `.git` extension."""

    result: Optional[Literal["pass", "fail", "bypass"]] = None
    """
    The result of the rule evaluations for rules with the `active` enforcement
    status.
    """
