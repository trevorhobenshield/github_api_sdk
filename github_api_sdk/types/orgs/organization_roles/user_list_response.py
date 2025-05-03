

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from ..team_simple import TeamSimple

__all__ = ["UserListResponse", "UserListResponseItem"]


class UserListResponseItem(BaseModel):
    id: int

    avatar_url: str

    events_url: str

    followers_url: str

    following_url: str

    gists_url: str

    gravatar_id: Optional[str] = None

    html_url: str

    login: str

    node_id: str

    organizations_url: str

    received_events_url: str

    repos_url: str

    site_admin: bool

    starred_url: str

    subscriptions_url: str

    type: str

    url: str

    assignment: Optional[Literal["direct", "indirect", "mixed"]] = None
    """Determines if the user has a direct, indirect, or mixed relationship to a role"""

    email: Optional[str] = None

    inherited_from: Optional[List[TeamSimple]] = None
    """Team the user has gotten the role through"""

    name: Optional[str] = None

    starred_at: Optional[str] = None

    user_view_type: Optional[str] = None


UserListResponse: TypeAlias = List[UserListResponseItem]
