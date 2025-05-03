

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .machine_spec import MachineSpec

__all__ = ["Runner", "ImageDetails", "PublicIP"]


class ImageDetails(BaseModel):
    id: str
    """The ID of the image.

    Use this ID for the `image` parameter when creating a new larger runner.
    """

    display_name: str
    """Display name for this image."""

    size_gb: int
    """Image size in GB."""

    source: Literal["github", "partner", "custom"]
    """The image provider."""


class PublicIP(BaseModel):
    enabled: Optional[bool] = None
    """Whether public IP is enabled."""

    length: Optional[int] = None
    """The length of the IP prefix."""

    prefix: Optional[str] = None
    """The prefix for the public IP."""


class Runner(BaseModel):
    id: int
    """The unique identifier of the hosted runner."""

    image_details: Optional[ImageDetails] = None
    """Provides details of a hosted runner image"""

    machine_size_details: MachineSpec
    """Provides details of a particular machine spec."""

    name: str
    """The name of the hosted runner."""

    platform: str
    """The operating system of the image."""

    public_ip_enabled: bool
    """Whether public IP is enabled for the hosted runners."""

    status: Literal["Ready", "Provisioning", "Shutdown", "Deleting", "Stuck"]
    """The status of the runner."""

    last_active_on: Optional[datetime] = None
    """The time at which the runner was last used, in ISO 8601 format."""

    maximum_runners: Optional[int] = None
    """The maximum amount of hosted runners.

    Runners will not scale automatically above this number. Use this setting to
    limit your cost.
    """

    public_ips: Optional[List[PublicIP]] = None
    """The public IP ranges when public IP is enabled for the hosted runners."""

    runner_group_id: Optional[int] = None
    """The unique identifier of the group that the hosted runner belongs to."""
