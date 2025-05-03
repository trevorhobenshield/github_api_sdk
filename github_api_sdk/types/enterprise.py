

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Enterprise"]


class Enterprise(BaseModel):
    id: int
    """Unique identifier of the enterprise"""

    avatar_url: str

    created_at: Optional[datetime] = None

    html_url: str

    name: str
    """The name of the enterprise."""

    node_id: str

    slug: str
    """The slug url identifier for the enterprise."""

    updated_at: Optional[datetime] = None

    description: Optional[str] = None
    """A short description of the enterprise."""

    website_url: Optional[str] = None
    """The enterprise's website URL."""
