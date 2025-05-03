

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["OrganizationFull", "Plan"]


class Plan(BaseModel):
    name: str

    private_repos: int

    space: int

    filled_seats: Optional[int] = None

    seats: Optional[int] = None


class OrganizationFull(BaseModel):
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

    advanced_security_enabled_for_new_repositories: Optional[bool] = None
    """
    **Endpoint closing down notice.** Please use
    [code security configurations](https://docs.github.com/rest/code-security/configurations)
    instead.

    Whether GitHub Advanced Security is enabled for new repositories and
    repositories transferred to this organization.

    This field is only visible to organization owners or members of a team with the
    security manager role.
    """

    billing_email: Optional[str] = None

    blog: Optional[str] = None

    collaborators: Optional[int] = None
    """The number of collaborators on private repositories.

    This field may be null if the number of private repositories is over 50,000.
    """

    company: Optional[str] = None

    default_repository_permission: Optional[str] = None

    dependabot_alerts_enabled_for_new_repositories: Optional[bool] = None
    """
    **Endpoint closing down notice.** Please use
    [code security configurations](https://docs.github.com/rest/code-security/configurations)
    instead.

    Whether Dependabot alerts are automatically enabled for new repositories and
    repositories transferred to this organization.

    This field is only visible to organization owners or members of a team with the
    security manager role.
    """

    dependabot_security_updates_enabled_for_new_repositories: Optional[bool] = None
    """
    **Endpoint closing down notice.** Please use
    [code security configurations](https://docs.github.com/rest/code-security/configurations)
    instead.

    Whether Dependabot security updates are automatically enabled for new
    repositories and repositories transferred to this organization.

    This field is only visible to organization owners or members of a team with the
    security manager role.
    """

    dependency_graph_enabled_for_new_repositories: Optional[bool] = None
    """
    **Endpoint closing down notice.** Please use
    [code security configurations](https://docs.github.com/rest/code-security/configurations)
    instead.

    Whether dependency graph is automatically enabled for new repositories and
    repositories transferred to this organization.

    This field is only visible to organization owners or members of a team with the
    security manager role.
    """

    deploy_keys_enabled_for_repositories: Optional[bool] = None
    """
    Controls whether or not deploy keys may be added and used for repositories in
    the organization.
    """

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

    plan: Optional[Plan] = None

    private_gists: Optional[int] = None

    secret_scanning_enabled_for_new_repositories: Optional[bool] = None
    """
    **Endpoint closing down notice.** Please use
    [code security configurations](https://docs.github.com/rest/code-security/configurations)
    instead.

    Whether secret scanning is automatically enabled for new repositories and
    repositories transferred to this organization.

    This field is only visible to organization owners or members of a team with the
    security manager role.
    """

    secret_scanning_push_protection_custom_link: Optional[str] = None
    """
    An optional URL string to display to contributors who are blocked from pushing a
    secret.
    """

    secret_scanning_push_protection_custom_link_enabled: Optional[bool] = None
    """
    Whether a custom link is shown to contributors who are blocked from pushing a
    secret by push protection.
    """

    secret_scanning_push_protection_enabled_for_new_repositories: Optional[bool] = None
    """
    **Endpoint closing down notice.** Please use
    [code security configurations](https://docs.github.com/rest/code-security/configurations)
    instead.

    Whether secret scanning push protection is automatically enabled for new
    repositories and repositories transferred to this organization.

    This field is only visible to organization owners or members of a team with the
    security manager role.
    """

    total_private_repos: Optional[int] = None

    twitter_username: Optional[str] = None

    two_factor_requirement_enabled: Optional[bool] = None

    web_commit_signoff_required: Optional[bool] = None
