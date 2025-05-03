

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PrivateRegistryCreateResponse"]


class PrivateRegistryCreateResponse(BaseModel):
    created_at: datetime

    name: str
    """The name of the private registry configuration."""

    registry_type: Literal["maven_repository"]
    """The registry type."""

    updated_at: datetime

    visibility: Literal["all", "private", "selected"]
    """Which type of organization repositories have access to the private registry.

    `selected` means only the repositories specified by `selected_repository_ids`
    can access the private registry.
    """

    selected_repository_ids: Optional[List[int]] = None
    """
    An array of repository IDs that can access the organization private registry
    when `visibility` is set to `selected`.
    """

    username: Optional[str] = None
    """The username to use when authenticating with the private registry."""
