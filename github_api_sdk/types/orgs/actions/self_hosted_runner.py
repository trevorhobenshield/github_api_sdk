

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SelfHostedRunner", "Label"]


class Label(BaseModel):
    name: str
    """Name of the label."""

    id: Optional[int] = None
    """Unique identifier of the label."""

    type: Optional[Literal["read-only", "custom"]] = None
    """The type of label.

    Read-only labels are applied automatically when the runner is configured.
    """


class SelfHostedRunner(BaseModel):
    id: int
    """The ID of the runner."""

    busy: bool

    labels: List[Label]

    name: str
    """The name of the runner."""

    os: str
    """The Operating System of the runner."""

    status: str
    """The status of the runner."""

    ephemeral: Optional[bool] = None

    runner_group_id: Optional[int] = None
    """The ID of the runner group."""
