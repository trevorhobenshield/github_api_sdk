

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CollaboratorListResponse", "CollaboratorListResponseItem", "CollaboratorListResponseItemPermissions"]


class CollaboratorListResponseItemPermissions(BaseModel):
    admin: bool

    pull: bool

    push: bool

    maintain: Optional[bool] = None

    triage: Optional[bool] = None


class CollaboratorListResponseItem(BaseModel):
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

    role_name: str

    site_admin: bool

    starred_url: str

    subscriptions_url: str

    type: str

    url: str

    email: Optional[str] = None

    name: Optional[str] = None

    permissions: Optional[CollaboratorListResponseItemPermissions] = None

    user_view_type: Optional[str] = None


CollaboratorListResponse: TypeAlias = List[CollaboratorListResponseItem]
