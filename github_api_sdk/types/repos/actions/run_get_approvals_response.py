

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ...orgs.simple_user import SimpleUser

__all__ = ["RunGetApprovalsResponse", "RunGetApprovalsResponseItem", "RunGetApprovalsResponseItemEnvironment"]


class RunGetApprovalsResponseItemEnvironment(BaseModel):
    id: Optional[int] = None
    """The id of the environment."""

    created_at: Optional[datetime] = None
    """The time that the environment was created, in ISO 8601 format."""

    html_url: Optional[str] = None

    name: Optional[str] = None
    """The name of the environment."""

    node_id: Optional[str] = None

    updated_at: Optional[datetime] = None
    """The time that the environment was last updated, in ISO 8601 format."""

    url: Optional[str] = None


class RunGetApprovalsResponseItem(BaseModel):
    comment: str
    """The comment submitted with the deployment review"""

    environments: List[RunGetApprovalsResponseItemEnvironment]
    """The list of environments that were approved or rejected"""

    state: Literal["approved", "rejected", "pending"]
    """
    Whether deployment to the environment(s) was approved or rejected or pending
    (with comments)
    """

    user: SimpleUser
    """A GitHub user."""


RunGetApprovalsResponse: TypeAlias = List[RunGetApprovalsResponseItem]
