

from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["RunnerImage"]


class RunnerImage(BaseModel):
    id: str
    """The ID of the image.

    Use this ID for the `image` parameter when creating a new larger runner.
    """

    display_name: str
    """Display name for this image."""

    platform: str
    """The operating system of the image."""

    size_gb: int
    """Image size in GB."""

    source: Literal["github", "partner", "custom"]
    """The image provider."""
