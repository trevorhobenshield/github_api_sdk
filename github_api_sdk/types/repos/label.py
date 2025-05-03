

from typing import Optional

from ..._models import BaseModel

__all__ = ["Label"]


class Label(BaseModel):
    id: int
    """Unique identifier for the label."""

    color: str
    """6-character hex code, without the leading #, identifying the color"""

    default: bool
    """Whether this label comes by default in a new repository."""

    description: Optional[str] = None
    """Optional description of the label, such as its purpose."""

    name: str
    """The name of the label."""

    node_id: str

    url: str
    """URL for the label"""
