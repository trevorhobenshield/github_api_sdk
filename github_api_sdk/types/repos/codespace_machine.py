

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CodespaceMachine"]


class CodespaceMachine(BaseModel):
    cpus: int
    """How many cores are available to the codespace."""

    display_name: str
    """The display name of the machine includes cores, memory, and storage."""

    memory_in_bytes: int
    """How much memory is available to the codespace."""

    name: str
    """The name of the machine."""

    operating_system: str
    """The operating system of the machine."""

    prebuild_availability: Optional[Literal["none", "ready", "in_progress"]] = None
    """
    Whether a prebuild is currently available when creating a codespace for this
    machine and repository. If a branch was not specified as a ref, the default
    branch will be assumed. Value will be "null" if prebuilds are not supported or
    prebuild availability could not be determined. Value will be "none" if no
    prebuild is available. Latest values "ready" and "in_progress" indicate the
    prebuild availability status.
    """

    storage_in_bytes: int
    """How much storage is available to the codespace."""
