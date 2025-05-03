

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .nullable_team_simple import NullableTeamSimple

__all__ = ["TeamFull", "Organization", "OrganizationPlan"]


class OrganizationPlan(BaseModel):
    name: str

    private_repos: int

    space: int

    filled_seats: Optional[int] = None

    seats: Optional[int] = None


class Organization(BaseModel):
    id: int

    archived_at: Optional[datetime] = None

    avatar_url: str

    created_at: datetime

    description: Optional[str] = None

    events_url: str

    followers: int

    following: int

    has_organization_projects: bool

    has_repository_projects: bool

    hooks_url: str

    html_url: str

    issues_url: str

    login: str

    members_url: str

    node_id: str

    public_gists: int

    public_members_url: str

    public_repos: int

    repos_url: str

    type: str

    updated_at: datetime

    url: str

    billing_email: Optional[str] = None

    blog: Optional[str] = None

    collaborators: Optional[int] = None

    company: Optional[str] = None

    default_repository_permission: Optional[str] = None

    disk_usage: Optional[int] = None

    email: Optional[str] = None

    is_verified: Optional[bool] = None

    location: Optional[str] = None

    members_allowed_repository_creation_type: Optional[str] = None

    members_can_create_internal_repositories: Optional[bool] = None

    members_can_create_pages: Optional[bool] = None

    members_can_create_private_pages: Optional[bool] = None

    members_can_create_private_repositories: Optional[bool] = None

    members_can_create_public_pages: Optional[bool] = None

    members_can_create_public_repositories: Optional[bool] = None

    members_can_create_repositories: Optional[bool] = None

    members_can_fork_private_repositories: Optional[bool] = None

    name: Optional[str] = None

    owned_private_repos: Optional[int] = None

    plan: Optional[OrganizationPlan] = None

    private_gists: Optional[int] = None

    total_private_repos: Optional[int] = None

    twitter_username: Optional[str] = None

    two_factor_requirement_enabled: Optional[bool] = None

    web_commit_signoff_required: Optional[bool] = None


class TeamFull(BaseModel):
    id: int
    """Unique identifier of the team"""

    created_at: datetime

    description: Optional[str] = None

    html_url: str

    members_count: int

    members_url: str

    name: str
    """Name of the team"""

    node_id: str

    organization: Organization
    """Team Organization"""

    permission: str
    """Permission that the team will have for its repositories"""

    repos_count: int

    repositories_url: str

    slug: str

    updated_at: datetime

    url: str
    """URL for the team"""

    ldap_dn: Optional[str] = None
    """Distinguished Name (DN) that team maps to within LDAP environment"""

    notification_setting: Optional[Literal["notifications_enabled", "notifications_disabled"]] = None
    """The notification setting the team has set"""

    parent: Optional[NullableTeamSimple] = None
    """
    Groups of organization members that gives permissions on specified repositories.
    """

    privacy: Optional[Literal["closed", "secret"]] = None
    """The level of privacy this team should have"""
