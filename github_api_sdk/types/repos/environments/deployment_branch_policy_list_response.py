

from typing import List

from ...._models import BaseModel
from .deployment_branch_policy import DeploymentBranchPolicy

__all__ = ["DeploymentBranchPolicyListResponse"]


class DeploymentBranchPolicyListResponse(BaseModel):
    branch_policies: List[DeploymentBranchPolicy]

    total_count: int
    """The number of deployment branch policies for the environment."""
