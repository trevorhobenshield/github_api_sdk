

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..applications.user import User
from ..minimal_repository import MinimalRepository

__all__ = ["RepositoryInvitation"]


class RepositoryInvitation(BaseModel):
    id: int
    """Unique identifier of the repository invitation."""

    created_at: datetime

    html_url: str

    invitee: Optional[User] = None
    """A GitHub user."""

    inviter: Optional[User] = None
    """A GitHub user."""

    node_id: str

    permissions: Literal["read", "write", "admin", "triage", "maintain"]
    """The permission associated with the invitation."""

    repository: MinimalRepository
    """Minimal Repository"""

    url: str
    """URL for the repository invitation"""

    expired: Optional[bool] = None
    """Whether or not the invitation has expired"""
