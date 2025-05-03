

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["NetworkConfiguration"]


class NetworkConfiguration(BaseModel):
    id: str
    """The unique identifier of the network configuration."""

    created_on: Optional[datetime] = None
    """The time at which the network configuration was created, in ISO 8601 format."""

    name: str
    """The name of the network configuration."""

    compute_service: Optional[Literal["none", "actions", "codespaces"]] = None
    """The hosted compute service the network configuration supports."""

    network_settings_ids: Optional[List[str]] = None
    """The unique identifier of each network settings in the configuration."""
