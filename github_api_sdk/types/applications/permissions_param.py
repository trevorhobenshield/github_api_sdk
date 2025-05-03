

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PermissionsParam"]


class PermissionsParam(TypedDict, total=False):
    actions: Literal["read", "write"]
    """
    The level of permission to grant the access token for GitHub Actions workflows,
    workflow runs, and artifacts.
    """

    administration: Literal["read", "write"]
    """
    The level of permission to grant the access token for repository creation,
    deletion, settings, teams, and collaborators creation.
    """

    checks: Literal["read", "write"]
    """The level of permission to grant the access token for checks on code."""

    codespaces: Literal["read", "write"]
    """
    The level of permission to grant the access token to create, edit, delete, and
    list Codespaces.
    """

    contents: Literal["read", "write"]
    """
    The level of permission to grant the access token for repository contents,
    commits, branches, downloads, releases, and merges.
    """

    dependabot_secrets: Literal["read", "write"]
    """The level of permission to grant the access token to manage Dependabot secrets."""

    deployments: Literal["read", "write"]
    """
    The level of permission to grant the access token for deployments and deployment
    statuses.
    """

    email_addresses: Literal["read", "write"]
    """
    The level of permission to grant the access token to manage the email addresses
    belonging to a user.
    """

    environments: Literal["read", "write"]
    """
    The level of permission to grant the access token for managing repository
    environments.
    """

    followers: Literal["read", "write"]
    """
    The level of permission to grant the access token to manage the followers
    belonging to a user.
    """

    git_ssh_keys: Literal["read", "write"]
    """The level of permission to grant the access token to manage git SSH keys."""

    gpg_keys: Literal["read", "write"]
    """
    The level of permission to grant the access token to view and manage GPG keys
    belonging to a user.
    """

    interaction_limits: Literal["read", "write"]
    """
    The level of permission to grant the access token to view and manage interaction
    limits on a repository.
    """

    issues: Literal["read", "write"]
    """
    The level of permission to grant the access token for issues and related
    comments, assignees, labels, and milestones.
    """

    members: Literal["read", "write"]
    """
    The level of permission to grant the access token for organization teams and
    members.
    """

    metadata: Literal["read", "write"]
    """
    The level of permission to grant the access token to search repositories, list
    collaborators, and access repository metadata.
    """

    organization_administration: Literal["read", "write"]
    """
    The level of permission to grant the access token to manage access to an
    organization.
    """

    organization_announcement_banners: Literal["read", "write"]
    """
    The level of permission to grant the access token to view and manage
    announcement banners for an organization.
    """

    organization_copilot_seat_management: Literal["write"]
    """
    The level of permission to grant the access token for managing access to GitHub
    Copilot for members of an organization with a Copilot Business subscription.
    This property is in public preview and is subject to change.
    """

    organization_custom_org_roles: Literal["read", "write"]
    """
    The level of permission to grant the access token for custom organization roles
    management.
    """

    organization_custom_properties: Literal["read", "write", "admin"]
    """
    The level of permission to grant the access token for custom property
    management.
    """

    organization_custom_roles: Literal["read", "write"]
    """
    The level of permission to grant the access token for custom repository roles
    management.
    """

    organization_events: Literal["read"]
    """
    The level of permission to grant the access token to view events triggered by an
    activity in an organization.
    """

    organization_hooks: Literal["read", "write"]
    """
    The level of permission to grant the access token to manage the post-receive
    hooks for an organization.
    """

    organization_packages: Literal["read", "write"]
    """
    The level of permission to grant the access token for organization packages
    published to GitHub Packages.
    """

    organization_personal_access_token_requests: Literal["read", "write"]
    """
    The level of permission to grant the access token for viewing and managing
    fine-grained personal access tokens that have been approved by an organization.
    """

    organization_personal_access_tokens: Literal["read", "write"]
    """
    The level of permission to grant the access token for viewing and managing
    fine-grained personal access token requests to an organization.
    """

    organization_plan: Literal["read"]
    """
    The level of permission to grant the access token for viewing an organization's
    plan.
    """

    organization_projects: Literal["read", "write", "admin"]
    """
    The level of permission to grant the access token to manage organization
    projects and projects public preview (where available).
    """

    organization_secrets: Literal["read", "write"]
    """
    The level of permission to grant the access token to manage organization
    secrets.
    """

    organization_self_hosted_runners: Literal["read", "write"]
    """
    The level of permission to grant the access token to view and manage GitHub
    Actions self-hosted runners available to an organization.
    """

    organization_user_blocking: Literal["read", "write"]
    """
    The level of permission to grant the access token to view and manage users
    blocked by the organization.
    """

    packages: Literal["read", "write"]
    """
    The level of permission to grant the access token for packages published to
    GitHub Packages.
    """

    pages: Literal["read", "write"]
    """
    The level of permission to grant the access token to retrieve Pages statuses,
    configuration, and builds, as well as create new builds.
    """

    profile: Literal["write"]
    """
    The level of permission to grant the access token to manage the profile settings
    belonging to a user.
    """

    pull_requests: Literal["read", "write"]
    """
    The level of permission to grant the access token for pull requests and related
    comments, assignees, labels, milestones, and merges.
    """

    repository_custom_properties: Literal["read", "write"]
    """
    The level of permission to grant the access token to view and edit custom
    properties for a repository, when allowed by the property.
    """

    repository_hooks: Literal["read", "write"]
    """
    The level of permission to grant the access token to manage the post-receive
    hooks for a repository.
    """

    repository_projects: Literal["read", "write", "admin"]
    """
    The level of permission to grant the access token to manage repository projects,
    columns, and cards.
    """

    secret_scanning_alerts: Literal["read", "write"]
    """
    The level of permission to grant the access token to view and manage secret
    scanning alerts.
    """

    secrets: Literal["read", "write"]
    """The level of permission to grant the access token to manage repository secrets."""

    security_events: Literal["read", "write"]
    """
    The level of permission to grant the access token to view and manage security
    events like code scanning alerts.
    """

    single_file: Literal["read", "write"]
    """The level of permission to grant the access token to manage just a single file."""

    starring: Literal["read", "write"]
    """
    The level of permission to grant the access token to list and manage
    repositories a user is starring.
    """

    statuses: Literal["read", "write"]
    """The level of permission to grant the access token for commit statuses."""

    team_discussions: Literal["read", "write"]
    """
    The level of permission to grant the access token to manage team discussions and
    related comments.
    """

    vulnerability_alerts: Literal["read", "write"]
    """The level of permission to grant the access token to manage Dependabot alerts."""

    workflows: Literal["write"]
    """
    The level of permission to grant the access token to update GitHub Actions
    workflow files.
    """
