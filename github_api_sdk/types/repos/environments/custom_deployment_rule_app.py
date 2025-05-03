


from ...._models import BaseModel

__all__ = ["CustomDeploymentRuleApp"]


class CustomDeploymentRuleApp(BaseModel):
    id: int
    """The unique identifier of the deployment protection rule integration."""

    integration_url: str
    """The URL for the endpoint to get details about the app."""

    node_id: str
    """The node ID for the deployment protection rule integration."""

    slug: str
    """The slugified name of the deployment protection rule integration."""
