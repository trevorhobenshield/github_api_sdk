

from typing import List, Optional

from ...._models import BaseModel
from .deployment_protection_rule import DeploymentProtectionRule

__all__ = ["DeploymentProtectionRuleListResponse"]


class DeploymentProtectionRuleListResponse(BaseModel):
    custom_deployment_protection_rules: Optional[List[DeploymentProtectionRule]] = None

    total_count: Optional[int] = None
    """The number of enabled custom deployment protection rules for this environment"""
