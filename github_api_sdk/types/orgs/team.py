

from typing import Optional

from ..._models import BaseModel
from .nullable_team_simple import NullableTeamSimple

__all__ = ["Team", "Permissions"]


class Permissions(BaseModel):
    admin: bool

    maintain: bool

    pull: bool

    push: bool

    triage: bool


class Team(BaseModel):
    id: int

    description: Optional[str] = None

    html_url: str

    members_url: str

    name: str

    node_id: str

    parent: Optional[NullableTeamSimple] = None
    """
    Groups of organization members that gives permissions on specified repositories.
    """

    permission: str

    repositories_url: str

    slug: str

    url: str

    notification_setting: Optional[str] = None

    permissions: Optional[Permissions] = None

    privacy: Optional[str] = None
