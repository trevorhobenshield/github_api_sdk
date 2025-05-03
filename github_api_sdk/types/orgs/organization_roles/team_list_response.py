

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ..nullable_team_simple import NullableTeamSimple

__all__ = ["TeamListResponse", "TeamListResponseItem", "TeamListResponseItemPermissions"]


class TeamListResponseItemPermissions(BaseModel):
    admin: bool

    maintain: bool

    pull: bool

    push: bool

    triage: bool


class TeamListResponseItem(BaseModel):
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

    assignment: Optional[Literal["direct", "indirect", "mixed"]] = None
    """Determines if the team has a direct, indirect, or mixed relationship to a role"""

    notification_setting: Optional[str] = None

    permissions: Optional[TeamListResponseItemPermissions] = None

    privacy: Optional[str] = None


TeamListResponse: TypeAlias = List[TeamListResponseItem]
