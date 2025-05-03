

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IssueType"]


class IssueType(BaseModel):
    id: int
    """The unique identifier of the issue type."""

    description: Optional[str] = None
    """The description of the issue type."""

    name: str
    """The name of the issue type."""

    node_id: str
    """The node identifier of the issue type."""

    color: Optional[Literal["gray", "blue", "green", "yellow", "orange", "red", "pink", "purple"]] = None
    """The color of the issue type."""

    created_at: Optional[datetime] = None
    """The time the issue type created."""

    is_enabled: Optional[bool] = None
    """The enabled state of the issue type."""

    updated_at: Optional[datetime] = None
    """The time the issue type last updated."""
