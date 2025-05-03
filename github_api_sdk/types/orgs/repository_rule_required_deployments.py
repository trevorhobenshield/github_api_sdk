

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleRequiredDeployments", "Parameters"]


class Parameters(BaseModel):
    required_deployment_environments: List[str]
    """
    The environments that must be successfully deployed to before branches can be
    merged.
    """


class RepositoryRuleRequiredDeployments(BaseModel):
    type: Literal["required_deployments"]

    parameters: Optional[Parameters] = None
