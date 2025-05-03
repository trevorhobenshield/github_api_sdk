

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DeploymentBranchPolicy"]


class DeploymentBranchPolicy(BaseModel):
    id: Optional[int] = None
    """The unique identifier of the branch or tag policy."""

    name: Optional[str] = None
    """
    The name pattern that branches or tags must match in order to deploy to the
    environment.
    """

    node_id: Optional[str] = None

    type: Optional[Literal["branch", "tag"]] = None
    """Whether this rule targets a branch or tag."""
