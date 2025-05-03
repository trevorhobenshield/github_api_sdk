

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleWorkflows", "Parameters", "ParametersWorkflow"]


class ParametersWorkflow(BaseModel):
    path: str
    """The path to the workflow file"""

    repository_id: int
    """The ID of the repository where the workflow is defined"""

    ref: Optional[str] = None
    """The ref (branch or tag) of the workflow file to use"""

    sha: Optional[str] = None
    """The commit SHA of the workflow file to use"""


class Parameters(BaseModel):
    workflows: List[ParametersWorkflow]
    """Workflows that must pass for this rule to pass."""

    do_not_enforce_on_create: Optional[bool] = None
    """
    Allow repositories and branches to be created if a check would otherwise
    prohibit it.
    """


class RepositoryRuleWorkflows(BaseModel):
    type: Literal["workflows"]

    parameters: Optional[Parameters] = None
