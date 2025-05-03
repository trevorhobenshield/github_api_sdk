

from typing import Optional

from ..._models import BaseModel

__all__ = ["User"]


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

    site_admin: bool

    starred_url: str

    subscriptions_url: str

    type: str

    url: str

    email: Optional[str] = None

    name: Optional[str] = None

    starred_at: Optional[str] = None

    user_view_type: Optional[str] = None
