

from typing import List, Optional

from ...._models import BaseModel
from .custom_deployment_rule_app import CustomDeploymentRuleApp

__all__ = ["DeploymentProtectionRuleListIntegrationsResponse"]


class DeploymentProtectionRuleListIntegrationsResponse(BaseModel):
    available_custom_deployment_protection_rule_integrations: Optional[List[CustomDeploymentRuleApp]] = None

    total_count: Optional[int] = None
    """
    The total number of custom deployment protection rule integrations available for
    this environment.
    """
