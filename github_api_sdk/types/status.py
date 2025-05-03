

from typing import Optional

from .._models import BaseModel
from .applications.user import User

__all__ = ["Status"]


class Status(BaseModel):
    id: int

    avatar_url: Optional[str] = None

    context: str

    created_at: str

    creator: Optional[User] = None
    """A GitHub user."""

    description: Optional[str] = None

    node_id: str

    state: str

    target_url: Optional[str] = None

    updated_at: str

    url: str
