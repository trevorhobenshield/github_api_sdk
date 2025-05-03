

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PrivateUser", "Plan"]


class Plan(BaseModel):
    collaborators: int

    name: str

    private_repos: int

    space: int


class PrivateUser(BaseModel):
    id: int

    avatar_url: str

    bio: Optional[str] = None

    blog: Optional[str] = None

    collaborators: int

    company: Optional[str] = None

    created_at: datetime

    disk_usage: int

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

    owned_private_repos: int

    private_gists: int

    public_gists: int

    public_repos: int

    received_events_url: str

    repos_url: str

    site_admin: bool

    starred_url: str

    subscriptions_url: str

    total_private_repos: int

    two_factor_authentication: bool

    type: str

    updated_at: datetime

    url: str

    business_plus: Optional[bool] = None

    ldap_dn: Optional[str] = None

    notification_email: Optional[str] = None

    plan: Optional[Plan] = None

    twitter_username: Optional[str] = None

    user_view_type: Optional[str] = None
