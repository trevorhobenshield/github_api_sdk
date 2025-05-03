

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OrgPrivateRegistryConfiguration"]


class OrgPrivateRegistryConfiguration(BaseModel):
    created_at: datetime

    name: str
    """The name of the private registry configuration."""

    registry_type: Literal["maven_repository"]
    """The registry type."""

    updated_at: datetime

    visibility: Literal["all", "private", "selected"]
    """Which type of organization repositories have access to the private registry."""

    username: Optional[str] = None
    """The username to use when authenticating with the private registry."""
