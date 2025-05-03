


from ...._models import BaseModel
from .custom_deployment_rule_app import CustomDeploymentRuleApp

__all__ = ["DeploymentProtectionRule"]


class DeploymentProtectionRule(BaseModel):
    id: int
    """The unique identifier for the deployment protection rule."""

    app: CustomDeploymentRuleApp
    """A GitHub App that is providing a custom deployment protection rule."""

    enabled: bool
    """Whether the deployment protection rule is enabled for the environment."""

    node_id: str
    """The node ID for the deployment protection rule."""
