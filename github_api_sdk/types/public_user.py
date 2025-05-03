

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PublicUser", "Plan"]


class Plan(BaseModel):
    collaborators: int

    name: str

    private_repos: int

    space: int


class PublicUser(BaseModel):
    id: int

    avatar_url: str

    bio: Optional[str] = None

    blog: Optional[str] = None

    company: Optional[str] = None

    created_at: datetime

    email: Optional[str] = None

    events_url: str

    followers: int

    followers_url: str

    following: int

    following_url: str

    gists_url: str

    gravatar_id: Optional[str] = None

    hireable: Optional[bool] = None

    html_url: str

    location: Optional[str] = None

    login: str

    name: Optional[str] = None

    node_id: str

    organizations_url: str

    public_gists: int

    public_repos: int

    received_events_url: str

    repos_url: str

    site_admin: bool

    starred_url: str

    subscriptions_url: str

    type: str

    updated_at: datetime

    url: str

    collaborators: Optional[int] = None

    disk_usage: Optional[int] = None

    notification_email: Optional[str] = None

    owned_private_repos: Optional[int] = None

    plan: Optional[Plan] = None

    private_gists: Optional[int] = None

    total_private_repos: Optional[int] = None

    twitter_username: Optional[str] = None

    user_view_type: Optional[str] = None
