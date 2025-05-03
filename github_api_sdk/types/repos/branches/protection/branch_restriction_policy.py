

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["BranchRestrictionPolicy", "App", "AppOwner", "AppPermissions", "Team", "User"]


class AppOwner(BaseModel):
    id: Optional[int] = None

    avatar_url: Optional[str] = None

    description: Optional[str] = None

    events_url: Optional[str] = None

    followers_url: Optional[str] = None

    following_url: Optional[str] = None

    gists_url: Optional[str] = None

    gravatar_id: Optional[str] = None

    hooks_url: Optional[str] = None

    html_url: Optional[str] = None

    issues_url: Optional[str] = None

    login: Optional[str] = None

    members_url: Optional[str] = None

    node_id: Optional[str] = None

    organizations_url: Optional[str] = None

    public_members_url: Optional[str] = None

    received_events_url: Optional[str] = None

    repos_url: Optional[str] = None

    site_admin: Optional[bool] = None

    starred_url: Optional[str] = None

    subscriptions_url: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    user_view_type: Optional[str] = None


class AppPermissions(BaseModel):
    contents: Optional[str] = None

    issues: Optional[str] = None

    metadata: Optional[str] = None

    single_file: Optional[str] = None


class App(BaseModel):
    id: Optional[int] = None

    client_id: Optional[str] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    events: Optional[List[str]] = None

    external_url: Optional[str] = None

    html_url: Optional[str] = None

    name: Optional[str] = None

    node_id: Optional[str] = None

    owner: Optional[AppOwner] = None

    permissions: Optional[AppPermissions] = None

    slug: Optional[str] = None

    updated_at: Optional[str] = None


class Team(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    html_url: Optional[str] = None

    members_url: Optional[str] = None

    name: Optional[str] = None

    node_id: Optional[str] = None

    notification_setting: Optional[str] = None

    parent: Optional[str] = None

    permission: Optional[str] = None

    privacy: Optional[str] = None

    repositories_url: Optional[str] = None

    slug: Optional[str] = None

    url: Optional[str] = None


class User(BaseModel):
    id: Optional[int] = None

    avatar_url: Optional[str] = None

    events_url: Optional[str] = None

    followers_url: Optional[str] = None

    following_url: Optional[str] = None

    gists_url: Optional[str] = None

    gravatar_id: Optional[str] = None

    html_url: Optional[str] = None

    login: Optional[str] = None

    node_id: Optional[str] = None

    organizations_url: Optional[str] = None

    received_events_url: Optional[str] = None

    repos_url: Optional[str] = None

    site_admin: Optional[bool] = None

    starred_url: Optional[str] = None

    subscriptions_url: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    user_view_type: Optional[str] = None


class BranchRestrictionPolicy(BaseModel):
    apps: List[App]

    apps_url: str

    teams: List[Team]

    teams_url: str

    url: str

    users: List[User]

    users_url: str
