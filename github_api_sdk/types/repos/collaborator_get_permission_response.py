

from typing import Optional

from ..._models import BaseModel

__all__ = ["CollaboratorGetPermissionResponse", "User", "UserPermissions"]


class UserPermissions(BaseModel):
    admin: bool

    pull: bool

    push: bool

    maintain: Optional[bool] = None

    triage: Optional[bool] = None


class User(BaseModel):
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

    permissions: Optional[UserPermissions] = None

    user_view_type: Optional[str] = None


class CollaboratorGetPermissionResponse(BaseModel):
    permission: str

    role_name: str

    user: Optional[User] = None
    """Collaborator"""
