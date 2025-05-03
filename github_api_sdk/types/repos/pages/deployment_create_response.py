

from typing import Union, Optional

from ...._models import BaseModel

__all__ = ["DeploymentCreateResponse"]


class DeploymentCreateResponse(BaseModel):
    id: Union[int, str]
    """The ID of the GitHub Pages deployment.

    This is the Git SHA of the deployed commit.
    """

    page_url: str
    """The URI to the deployed GitHub Pages."""

    status_url: str
    """The URI to monitor GitHub Pages deployment status."""

    preview_url: Optional[str] = None
    """The URI to the deployed GitHub Pages preview."""
