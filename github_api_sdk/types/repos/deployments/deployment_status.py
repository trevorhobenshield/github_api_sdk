

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...applications.user import User
from ..nullable_integration import NullableIntegration

__all__ = ["DeploymentStatus"]


class DeploymentStatus(BaseModel):
    id: int

    created_at: datetime

    creator: Optional[User] = None
    """A GitHub user."""

    deployment_url: str

    description: str
    """A short description of the status."""

    node_id: str

    repository_url: str

    state: Literal["error", "failure", "inactive", "pending", "success", "queued", "in_progress"]
    """The state of the status."""

    target_url: str
    """Closing down notice: the URL to associate with this status."""

    updated_at: datetime

    url: str

    environment: Optional[str] = None
    """The environment of the deployment that the status is for."""

    environment_url: Optional[str] = None
    """The URL for accessing your environment."""

    log_url: Optional[str] = None
    """The URL to associate with this status."""

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """
