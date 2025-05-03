

from typing import Optional

from ..._models import BaseModel
from .simple_user import SimpleUser

__all__ = ["Invitation"]


class Invitation(BaseModel):
    id: int

    created_at: str

    email: Optional[str] = None

    invitation_teams_url: str

    inviter: SimpleUser
    """A GitHub user."""

    login: Optional[str] = None

    node_id: str

    role: str

    team_count: int

    failed_at: Optional[str] = None

    failed_reason: Optional[str] = None

    invitation_source: Optional[str] = None
