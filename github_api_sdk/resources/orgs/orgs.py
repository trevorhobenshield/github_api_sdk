from __future__ import annotations

from datetime import datetime
from typing import Union

import httpx
from typing_extensions import Literal

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types import (
    org_list_attestations_params,
    org_list_events_params,
    org_list_failed_invitations_params,
    org_list_installations_params,
    org_list_issues_params,
    org_list_security_advisories_params,
    org_set_security_feature_params,
    org_update_params,
)
from ...types.applications.installation import Installation
from ...types.org_list_attestations_response import OrgListAttestationsResponse
from ...types.org_list_events_response import OrgListEventsResponse
from ...types.org_list_failed_invitations_response import OrgListFailedInvitationsResponse
from ...types.org_list_installations_response import OrgListInstallationsResponse
from ...types.org_list_issues_response import OrgListIssuesResponse
from ...types.org_list_security_advisories_response import OrgListSecurityAdvisoriesResponse
from ...types.organization_full import OrganizationFull
from .actions.actions import (
    ActionsResource,
    ActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResource,
    AsyncActionsResourceWithRawResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from .blocks import (
    AsyncBlocksResource,
    AsyncBlocksResourceWithRawResponse,
    AsyncBlocksResourceWithStreamingResponse,
    BlocksResource,
    BlocksResourceWithRawResponse,
    BlocksResourceWithStreamingResponse,
)
from .campaigns import (
    AsyncCampaignsResource,
    AsyncCampaignsResourceWithRawResponse,
    AsyncCampaignsResourceWithStreamingResponse,
    CampaignsResource,
    CampaignsResourceWithRawResponse,
    CampaignsResourceWithStreamingResponse,
)
from .code_scanning import (
    AsyncCodeScanningResource,
    AsyncCodeScanningResourceWithRawResponse,
    AsyncCodeScanningResourceWithStreamingResponse,
    CodeScanningResource,
    CodeScanningResourceWithRawResponse,
    CodeScanningResourceWithStreamingResponse,
)
from .code_security.code_security import (
    AsyncCodeSecurityResource,
    AsyncCodeSecurityResourceWithRawResponse,
    AsyncCodeSecurityResourceWithStreamingResponse,
    CodeSecurityResource,
    CodeSecurityResourceWithRawResponse,
    CodeSecurityResourceWithStreamingResponse,
)
from .codespaces.codespaces import (
    AsyncCodespacesResource,
    AsyncCodespacesResourceWithRawResponse,
    AsyncCodespacesResourceWithStreamingResponse,
    CodespacesResource,
    CodespacesResourceWithRawResponse,
    CodespacesResourceWithStreamingResponse,
)
from .copilot.copilot import (
    AsyncCopilotResource,
    AsyncCopilotResourceWithRawResponse,
    AsyncCopilotResourceWithStreamingResponse,
    CopilotResource,
    CopilotResourceWithRawResponse,
    CopilotResourceWithStreamingResponse,
)
from .dependabot.dependabot import (
    AsyncDependabotResource,
    AsyncDependabotResourceWithRawResponse,
    AsyncDependabotResourceWithStreamingResponse,
    DependabotResource,
    DependabotResourceWithRawResponse,
    DependabotResourceWithStreamingResponse,
)
from .docker import (
    AsyncDockerResource,
    AsyncDockerResourceWithRawResponse,
    AsyncDockerResourceWithStreamingResponse,
    DockerResource,
    DockerResourceWithRawResponse,
    DockerResourceWithStreamingResponse,
)
from .hooks.hooks import (
    AsyncHooksResource,
    AsyncHooksResourceWithRawResponse,
    AsyncHooksResourceWithStreamingResponse,
    HooksResource,
    HooksResourceWithRawResponse,
    HooksResourceWithStreamingResponse,
)
from .insights.insights import (
    AsyncInsightsResource,
    AsyncInsightsResourceWithRawResponse,
    AsyncInsightsResourceWithStreamingResponse,
    InsightsResource,
    InsightsResourceWithRawResponse,
    InsightsResourceWithStreamingResponse,
)
from .interaction_limits import (
    AsyncInteractionLimitsResource,
    AsyncInteractionLimitsResourceWithRawResponse,
    AsyncInteractionLimitsResourceWithStreamingResponse,
    InteractionLimitsResource,
    InteractionLimitsResourceWithRawResponse,
    InteractionLimitsResourceWithStreamingResponse,
)
from .invitations import (
    AsyncInvitationsResource,
    AsyncInvitationsResourceWithRawResponse,
    AsyncInvitationsResourceWithStreamingResponse,
    InvitationsResource,
    InvitationsResourceWithRawResponse,
    InvitationsResourceWithStreamingResponse,
)
from .issue_types import (
    AsyncIssueTypesResource,
    AsyncIssueTypesResourceWithRawResponse,
    AsyncIssueTypesResourceWithStreamingResponse,
    IssueTypesResource,
    IssueTypesResourceWithRawResponse,
    IssueTypesResourceWithStreamingResponse,
)
from .members.members import (
    AsyncMembersResource,
    AsyncMembersResourceWithRawResponse,
    AsyncMembersResourceWithStreamingResponse,
    MembersResource,
    MembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
)
from .memberships import (
    AsyncMembershipsResource,
    AsyncMembershipsResourceWithRawResponse,
    AsyncMembershipsResourceWithStreamingResponse,
    MembershipsResource,
    MembershipsResourceWithRawResponse,
    MembershipsResourceWithStreamingResponse,
)
from .migrations.migrations import (
    AsyncMigrationsResource,
    AsyncMigrationsResourceWithRawResponse,
    AsyncMigrationsResourceWithStreamingResponse,
    MigrationsResource,
    MigrationsResourceWithRawResponse,
    MigrationsResourceWithStreamingResponse,
)
from .organization_roles.organization_roles import (
    AsyncOrganizationRolesResource,
    AsyncOrganizationRolesResourceWithRawResponse,
    AsyncOrganizationRolesResourceWithStreamingResponse,
    OrganizationRolesResource,
    OrganizationRolesResourceWithRawResponse,
    OrganizationRolesResourceWithStreamingResponse,
)
from .outside_collaborators import (
    AsyncOutsideCollaboratorsResource,
    AsyncOutsideCollaboratorsResourceWithRawResponse,
    AsyncOutsideCollaboratorsResourceWithStreamingResponse,
    OutsideCollaboratorsResource,
    OutsideCollaboratorsResourceWithRawResponse,
    OutsideCollaboratorsResourceWithStreamingResponse,
)
from .packages.packages import (
    AsyncPackagesResource,
    AsyncPackagesResourceWithRawResponse,
    AsyncPackagesResourceWithStreamingResponse,
    PackagesResource,
    PackagesResourceWithRawResponse,
    PackagesResourceWithStreamingResponse,
)
from .personal_access_token_requests import (
    AsyncPersonalAccessTokenRequestsResource,
    AsyncPersonalAccessTokenRequestsResourceWithRawResponse,
    AsyncPersonalAccessTokenRequestsResourceWithStreamingResponse,
    PersonalAccessTokenRequestsResource,
    PersonalAccessTokenRequestsResourceWithRawResponse,
    PersonalAccessTokenRequestsResourceWithStreamingResponse,
)
from .personal_access_tokens import (
    AsyncPersonalAccessTokensResource,
    AsyncPersonalAccessTokensResourceWithRawResponse,
    AsyncPersonalAccessTokensResourceWithStreamingResponse,
    PersonalAccessTokensResource,
    PersonalAccessTokensResourceWithRawResponse,
    PersonalAccessTokensResourceWithStreamingResponse,
)
from .private_registries import (
    AsyncPrivateRegistriesResource,
    AsyncPrivateRegistriesResourceWithRawResponse,
    AsyncPrivateRegistriesResourceWithStreamingResponse,
    PrivateRegistriesResource,
    PrivateRegistriesResourceWithRawResponse,
    PrivateRegistriesResourceWithStreamingResponse,
)
from .projects import (
    AsyncProjectsResource,
    AsyncProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithStreamingResponse,
    ProjectsResource,
    ProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
)
from .properties.properties import (
    AsyncPropertiesResource,
    AsyncPropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithStreamingResponse,
    PropertiesResource,
    PropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
)
from .public_members import (
    AsyncPublicMembersResource,
    AsyncPublicMembersResourceWithRawResponse,
    AsyncPublicMembersResourceWithStreamingResponse,
    PublicMembersResource,
    PublicMembersResourceWithRawResponse,
    PublicMembersResourceWithStreamingResponse,
)
from .repos import (
    AsyncReposResource,
    AsyncReposResourceWithRawResponse,
    AsyncReposResourceWithStreamingResponse,
    ReposResource,
    ReposResourceWithRawResponse,
    ReposResourceWithStreamingResponse,
)
from .rulesets.rulesets import (
    AsyncRulesetsResource,
    AsyncRulesetsResourceWithRawResponse,
    AsyncRulesetsResourceWithStreamingResponse,
    RulesetsResource,
    RulesetsResourceWithRawResponse,
    RulesetsResourceWithStreamingResponse,
)
from .secret_scanning import (
    AsyncSecretScanningResource,
    AsyncSecretScanningResourceWithRawResponse,
    AsyncSecretScanningResourceWithStreamingResponse,
    SecretScanningResource,
    SecretScanningResourceWithRawResponse,
    SecretScanningResourceWithStreamingResponse,
)
from .security_managers.security_managers import (
    AsyncSecurityManagersResource,
    AsyncSecurityManagersResourceWithRawResponse,
    AsyncSecurityManagersResourceWithStreamingResponse,
    SecurityManagersResource,
    SecurityManagersResourceWithRawResponse,
    SecurityManagersResourceWithStreamingResponse,
)
from .settings.settings import (
    AsyncSettingsResource,
    AsyncSettingsResourceWithRawResponse,
    AsyncSettingsResourceWithStreamingResponse,
    SettingsResource,
    SettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
)
from .teams.teams import (
    AsyncTeamsResource,
    AsyncTeamsResourceWithRawResponse,
    AsyncTeamsResourceWithStreamingResponse,
    TeamsResource,
    TeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
)

__all__ = ["OrgsResource", "AsyncOrgsResource"]


class OrgsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def blocks(self) -> BlocksResource:
        return BlocksResource(self._client)

    @cached_property
    def campaigns(self) -> CampaignsResource:
        return CampaignsResource(self._client)

    @cached_property
    def code_scanning(self) -> CodeScanningResource:
        return CodeScanningResource(self._client)

    @cached_property
    def code_security(self) -> CodeSecurityResource:
        return CodeSecurityResource(self._client)

    @cached_property
    def codespaces(self) -> CodespacesResource:
        return CodespacesResource(self._client)

    @cached_property
    def copilot(self) -> CopilotResource:
        return CopilotResource(self._client)

    @cached_property
    def dependabot(self) -> DependabotResource:
        return DependabotResource(self._client)

    @cached_property
    def docker(self) -> DockerResource:
        return DockerResource(self._client)

    @cached_property
    def hooks(self) -> HooksResource:
        return HooksResource(self._client)

    @cached_property
    def insights(self) -> InsightsResource:
        return InsightsResource(self._client)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResource:
        return InteractionLimitsResource(self._client)

    @cached_property
    def invitations(self) -> InvitationsResource:
        return InvitationsResource(self._client)

    @cached_property
    def issue_types(self) -> IssueTypesResource:
        return IssueTypesResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def memberships(self) -> MembershipsResource:
        return MembershipsResource(self._client)

    @cached_property
    def migrations(self) -> MigrationsResource:
        return MigrationsResource(self._client)

    @cached_property
    def organization_roles(self) -> OrganizationRolesResource:
        return OrganizationRolesResource(self._client)

    @cached_property
    def outside_collaborators(self) -> OutsideCollaboratorsResource:
        return OutsideCollaboratorsResource(self._client)

    @cached_property
    def packages(self) -> PackagesResource:
        return PackagesResource(self._client)

    @cached_property
    def personal_access_token_requests(self) -> PersonalAccessTokenRequestsResource:
        return PersonalAccessTokenRequestsResource(self._client)

    @cached_property
    def personal_access_tokens(self) -> PersonalAccessTokensResource:
        return PersonalAccessTokensResource(self._client)

    @cached_property
    def private_registries(self) -> PrivateRegistriesResource:
        return PrivateRegistriesResource(self._client)

    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def properties(self) -> PropertiesResource:
        return PropertiesResource(self._client)

    @cached_property
    def public_members(self) -> PublicMembersResource:
        return PublicMembersResource(self._client)

    @cached_property
    def repos(self) -> ReposResource:
        return ReposResource(self._client)

    @cached_property
    def rulesets(self) -> RulesetsResource:
        return RulesetsResource(self._client)

    @cached_property
    def secret_scanning(self) -> SecretScanningResource:
        return SecretScanningResource(self._client)

    @cached_property
    def security_managers(self) -> SecurityManagersResource:
        return SecurityManagersResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def teams(self) -> TeamsResource:
        return TeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return OrgsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationFull:
        """
        Gets information about an organization.

        When the value of `two_factor_requirement_enabled` is `true`, the organization
        requires all members, billing managers, outside collaborators, guest
        collaborators, repository collaborators, or everyone with access to any
        repository within the organization to enable
        [two-factor authentication](https://docs.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/).

        To see the full details about an organization, the authenticated user must be an
        organization owner.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to see the full details about an organization.

        To see information about an organization's GitHub plan, GitHub Apps need the
        `Organization plan` permission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationFull,
        )

    def update(
        self,
        org: str,
        *,
        advanced_security_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        billing_email: str | NotGiven = NOT_GIVEN,
        blog: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        default_repository_permission: Literal["read", "write", "admin", "none"] | NotGiven = NOT_GIVEN,
        dependabot_alerts_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        dependabot_security_updates_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        dependency_graph_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        deploy_keys_enabled_for_repositories: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        has_organization_projects: bool | NotGiven = NOT_GIVEN,
        has_repository_projects: bool | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        members_allowed_repository_creation_type: Literal["all", "private", "none"] | NotGiven = NOT_GIVEN,
        members_can_create_internal_repositories: bool | NotGiven = NOT_GIVEN,
        members_can_create_pages: bool | NotGiven = NOT_GIVEN,
        members_can_create_private_pages: bool | NotGiven = NOT_GIVEN,
        members_can_create_private_repositories: bool | NotGiven = NOT_GIVEN,
        members_can_create_public_pages: bool | NotGiven = NOT_GIVEN,
        members_can_create_public_repositories: bool | NotGiven = NOT_GIVEN,
        members_can_create_repositories: bool | NotGiven = NOT_GIVEN,
        members_can_fork_private_repositories: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        secret_scanning_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection_custom_link: str | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection_custom_link_enabled: bool | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        twitter_username: str | NotGiven = NOT_GIVEN,
        web_commit_signoff_required: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationFull:
        """
        > [!WARNING] > **Closing down notice:** GitHub will replace and discontinue
        > `members_allowed_repository_creation_type` in favor of more granular
        > permissions. The new input parameters are
        > `members_can_create_public_repositories`,
        > `members_can_create_private_repositories` for all organizations and
        > `members_can_create_internal_repositories` for organizations associated with
        > an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise
        > Server 2.20+. For more information, see the
        > [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).

        > [!WARNING] > **Closing down notice:** Code security product enablement for new
        > repositories through the organization API is closing down. Please use
        > [code security configurations](https://docs.github.com/rest/code-security/configurations#set-a-code-security-configuration-as-a-default-for-an-organization)
        > to set defaults instead. For more information on setting a default security
        > configuration, see the
        > [changelog](https://github.blog/changelog/2024-07-09-sunsetting-security-settings-defaults-parameters-in-the-organizations-rest-api/).

        Updates the organization's profile and member privileges.

        The authenticated user must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` or
        `repo` scope to use this endpoint.

        Args:
          advanced_security_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether GitHub Advanced Security is automatically enabled for new repositories
              and repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          billing_email: Billing email address. This address is not publicized.

          company: The company name.

          default_repository_permission: Default permission level members have for organization repositories.

          dependabot_alerts_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether Dependabot alerts are automatically enabled for new repositories and
              repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          dependabot_security_updates_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether Dependabot security updates are automatically enabled for new
              repositories and repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          dependency_graph_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether dependency graph is automatically enabled for new repositories and
              repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          deploy_keys_enabled_for_repositories: Controls whether or not deploy keys may be added and used for repositories in
              the organization.

          description: The description of the company. The maximum size is 160 characters.

          email: The publicly visible email address.

          has_organization_projects: Whether an organization can use organization projects.

          has_repository_projects: Whether repositories that belong to the organization can use repository
              projects.

          location: The location.

          members_allowed_repository_creation_type: Specifies which types of repositories non-admin organization members can create.
              `private` is only available to repositories that are part of an organization on
              GitHub Enterprise Cloud. **Note:** This parameter is closing down and will be
              removed in the future. Its return value ignores internal repositories. Using
              this parameter overrides values set in `members_can_create_repositories`. See
              the parameter deprecation notice in the operation description for details.

          members_can_create_internal_repositories: Whether organization members can create internal repositories, which are visible
              to all enterprise members. You can only allow members to create internal
              repositories if your organization is associated with an enterprise account using
              GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information,
              see
              "[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)"
              in the GitHub Help documentation.

          members_can_create_pages: Whether organization members can create GitHub Pages sites. Existing published
              sites will not be impacted.

          members_can_create_private_pages: Whether organization members can create private GitHub Pages sites. Existing
              published sites will not be impacted.

          members_can_create_private_repositories: Whether organization members can create private repositories, which are visible
              to organization members with permission. For more information, see
              "[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)"
              in the GitHub Help documentation.

          members_can_create_public_pages: Whether organization members can create public GitHub Pages sites. Existing
              published sites will not be impacted.

          members_can_create_public_repositories: Whether organization members can create public repositories, which are visible
              to anyone. For more information, see
              "[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)"
              in the GitHub Help documentation.

          members_can_create_repositories: Whether of non-admin organization members can create repositories. **Note:** A
              parameter can override this parameter. See
              `members_allowed_repository_creation_type` in this table for details.

          members_can_fork_private_repositories: Whether organization members can fork private organization repositories.

          name: The shorthand name of the company.

          secret_scanning_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether secret scanning is automatically enabled for new repositories and
              repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          secret_scanning_push_protection_custom_link: If `secret_scanning_push_protection_custom_link_enabled` is true, the URL that
              will be displayed to contributors who are blocked from pushing a secret.

          secret_scanning_push_protection_custom_link_enabled: Whether a custom link is shown to contributors who are blocked from pushing a
              secret by push protection.

          secret_scanning_push_protection_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether secret scanning push protection is automatically enabled for new
              repositories and repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          twitter_username: The Twitter username of the company.

          web_commit_signoff_required: Whether contributors to organization repositories are required to sign off on
              commits they make through GitHub's web interface.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._patch(
            f"/orgs/{org}",
            body=maybe_transform(
                {
                    "advanced_security_enabled_for_new_repositories": advanced_security_enabled_for_new_repositories,
                    "billing_email": billing_email,
                    "blog": blog,
                    "company": company,
                    "default_repository_permission": default_repository_permission,
                    "dependabot_alerts_enabled_for_new_repositories": dependabot_alerts_enabled_for_new_repositories,
                    "dependabot_security_updates_enabled_for_new_repositories": dependabot_security_updates_enabled_for_new_repositories,
                    "dependency_graph_enabled_for_new_repositories": dependency_graph_enabled_for_new_repositories,
                    "deploy_keys_enabled_for_repositories": deploy_keys_enabled_for_repositories,
                    "description": description,
                    "email": email,
                    "has_organization_projects": has_organization_projects,
                    "has_repository_projects": has_repository_projects,
                    "location": location,
                    "members_allowed_repository_creation_type": members_allowed_repository_creation_type,
                    "members_can_create_internal_repositories": members_can_create_internal_repositories,
                    "members_can_create_pages": members_can_create_pages,
                    "members_can_create_private_pages": members_can_create_private_pages,
                    "members_can_create_private_repositories": members_can_create_private_repositories,
                    "members_can_create_public_pages": members_can_create_public_pages,
                    "members_can_create_public_repositories": members_can_create_public_repositories,
                    "members_can_create_repositories": members_can_create_repositories,
                    "members_can_fork_private_repositories": members_can_fork_private_repositories,
                    "name": name,
                    "secret_scanning_enabled_for_new_repositories": secret_scanning_enabled_for_new_repositories,
                    "secret_scanning_push_protection_custom_link": secret_scanning_push_protection_custom_link,
                    "secret_scanning_push_protection_custom_link_enabled": secret_scanning_push_protection_custom_link_enabled,
                    "secret_scanning_push_protection_enabled_for_new_repositories": secret_scanning_push_protection_enabled_for_new_repositories,
                    "twitter_username": twitter_username,
                    "web_commit_signoff_required": web_commit_signoff_required,
                },
                org_update_params.OrgUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationFull,
        )

    def delete(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes an organization and all its repositories.

        The organization login will be unavailable for 90 days after deletion.

        Please review the Terms of Service regarding account deletion before using this
        endpoint:

        https://docs.github.com/site-policy/github-terms/github-terms-of-service

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._delete(
            f"/orgs/{org}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def get_installation(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Installation:
        """
        Enables an authenticated GitHub App to find the organization's installation
        information.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/installation",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Installation,
        )

    def list_attestations(
        self,
        subject_digest: str,
        *,
        org: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        predicate_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListAttestationsResponse:
        """
        List a collection of artifact attestations with a given subject digest that are
        associated with repositories owned by an organization.

        The collection of attestations returned by this endpoint is filtered according
        to the authenticated user's permissions; if the authenticated user cannot read a
        repository, the attestations associated with that repository will not be
        included in the response. In addition, when using a fine-grained access token
        the `attestations:read` permission is required.

        **Please note:** in order to offer meaningful security benefits, an
        attestation's signature and timestamps **must** be cryptographically verified,
        and the identity of the attestation signer **must** be validated. Attestations
        can be verified using the
        [GitHub CLI `attestation verify` command](https://cli.github.com/manual/gh_attestation_verify).
        For more information, see
        [our guide on how to use artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          predicate_type: Optional filter for fetching attestations with a given predicate type. This
              option accepts `provenance`, `sbom`, or freeform text for custom predicate
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not subject_digest:
            raise ValueError(f"Expected a non-empty value for `subject_digest` but received {subject_digest!r}")
        return self._get(
            f"/orgs/{org}/attestations/{subject_digest}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "predicate_type": predicate_type,
                    },
                    org_list_attestations_params.OrgListAttestationsParams,
                ),
            ),
            cast_to=OrgListAttestationsResponse,
        )

    def list_events(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListEventsResponse:
        """> [!NOTE] This API is not built to serve real-time use cases.

        Depending on the
        > time of day, event latency can be anywhere from 30s to 6h.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    org_list_events_params.OrgListEventsParams,
                ),
            ),
            cast_to=OrgListEventsResponse,
        )

    def list_failed_invitations(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListFailedInvitationsResponse:
        """
        The return hash contains `failed_at` and `failed_reason` fields which represent
        the time at which the invitation failed and the reason for the failure.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/failed_invitations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    org_list_failed_invitations_params.OrgListFailedInvitationsParams,
                ),
            ),
            cast_to=OrgListFailedInvitationsResponse,
        )

    def list_installations(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListInstallationsResponse:
        """Lists all GitHub Apps in an organization.

        The installation count includes all
        GitHub Apps installed on repositories in the organization.

        The authenticated user must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:read`
        scope to use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/installations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    org_list_installations_params.OrgListInstallationsParams,
                ),
            ),
            cast_to=OrgListInstallationsResponse,
        )

    def list_issues(
        self,
        org: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        filter: Literal["assigned", "created", "mentioned", "subscribed", "repos", "all"] | NotGiven = NOT_GIVEN,
        labels: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "comments"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListIssuesResponse:
        """
        List issues in an organization assigned to the authenticated user.

        > [!NOTE] GitHub's REST API considers every pull request an issue, but not every
        > issue is a pull request. For this reason, "Issues" endpoints may return both
        > issues and pull requests in the response. You can identify pull requests by
        > the `pull_request` key. Be aware that the `id` of a pull request returned from
        > "Issues" endpoints will be an _issue id_. To find out the pull request id, use
        > the
        > "[List pull requests](https://docs.github.com/rest/pulls/pulls#list-pull-requests)"
        > endpoint.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          direction: The direction to sort the results by.

          filter: Indicates which sorts of issues to return. `assigned` means issues assigned to
              you. `created` means issues created by you. `mentioned` means issues mentioning
              you. `subscribed` means issues you're subscribed to updates for. `all` or
              `repos` means all issues you can see, regardless of participation or creation.

          labels: A list of comma separated label names. Example: `bug,ui,@high`

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: What to sort results by.

          state: Indicates the state of the issues to return.

          type: Can be the name of an issue type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/issues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "filter": filter,
                        "labels": labels,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "sort": sort,
                        "state": state,
                        "type": type,
                    },
                    org_list_issues_params.OrgListIssuesParams,
                ),
            ),
            cast_to=OrgListIssuesResponse,
        )

    def list_security_advisories(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "published"] | NotGiven = NOT_GIVEN,
        state: Literal["triage", "draft", "published", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListSecurityAdvisoriesResponse:
        """
        Lists repository security advisories for an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:write` scope to use this endpoint.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          direction: The direction to sort the results by.

          per_page: The number of advisories to return per page. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          state: Filter by the state of the repository advisories. Only advisories of this state
              will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/security-advisories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    org_list_security_advisories_params.OrgListSecurityAdvisoriesParams,
                ),
            ),
            cast_to=OrgListSecurityAdvisoriesResponse,
        )

    def set_security_feature(
        self,
        enablement: Literal["enable_all", "disable_all"],
        *,
        org: str,
        security_product: Literal[
            "dependency_graph",
            "dependabot_alerts",
            "dependabot_security_updates",
            "advanced_security",
            "code_scanning_default_setup",
            "secret_scanning",
            "secret_scanning_push_protection",
        ],
        query_suite: Literal["default", "extended"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Closing down notice:** The ability to enable or disable a
        > security feature for all eligible repositories in an organization is closing
        > down. Please use
        > [code security configurations](https://docs.github.com/rest/code-security/configurations)
        > instead. For more information, see the
        > [changelog](https://github.blog/changelog/2024-07-22-deprecation-of-api-endpoint-to-enable-or-disable-a-security-feature-for-an-organization/).

        Enables or disables the specified security feature for all eligible repositories
        in an organization. For more information, see
        "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

        The authenticated user must be an organization owner or be member of a team with
        the security manager role to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org`,
        `write:org`, or `repo` scopes to use this endpoint.

        Args:
          query_suite: CodeQL query suite to be used. If you specify the `query_suite` parameter, the
              default setup will be configured with this query suite only on all repositories
              that didn't have default setup already configured. It will not change the query
              suite on repositories that already have default setup configured. If you don't
              specify any `query_suite` in your request, the preferred query suite of the
              organization will be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not security_product:
            raise ValueError(f"Expected a non-empty value for `security_product` but received {security_product!r}")
        if not enablement:
            raise ValueError(f"Expected a non-empty value for `enablement` but received {enablement!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/orgs/{org}/{security_product}/{enablement}",
            body=maybe_transform({"query_suite": query_suite}, org_set_security_feature_params.OrgSetSecurityFeatureParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncOrgsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def blocks(self) -> AsyncBlocksResource:
        return AsyncBlocksResource(self._client)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResource:
        return AsyncCampaignsResource(self._client)

    @cached_property
    def code_scanning(self) -> AsyncCodeScanningResource:
        return AsyncCodeScanningResource(self._client)

    @cached_property
    def code_security(self) -> AsyncCodeSecurityResource:
        return AsyncCodeSecurityResource(self._client)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResource:
        return AsyncCodespacesResource(self._client)

    @cached_property
    def copilot(self) -> AsyncCopilotResource:
        return AsyncCopilotResource(self._client)

    @cached_property
    def dependabot(self) -> AsyncDependabotResource:
        return AsyncDependabotResource(self._client)

    @cached_property
    def docker(self) -> AsyncDockerResource:
        return AsyncDockerResource(self._client)

    @cached_property
    def hooks(self) -> AsyncHooksResource:
        return AsyncHooksResource(self._client)

    @cached_property
    def insights(self) -> AsyncInsightsResource:
        return AsyncInsightsResource(self._client)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResource:
        return AsyncInteractionLimitsResource(self._client)

    @cached_property
    def invitations(self) -> AsyncInvitationsResource:
        return AsyncInvitationsResource(self._client)

    @cached_property
    def issue_types(self) -> AsyncIssueTypesResource:
        return AsyncIssueTypesResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        return AsyncMembershipsResource(self._client)

    @cached_property
    def migrations(self) -> AsyncMigrationsResource:
        return AsyncMigrationsResource(self._client)

    @cached_property
    def organization_roles(self) -> AsyncOrganizationRolesResource:
        return AsyncOrganizationRolesResource(self._client)

    @cached_property
    def outside_collaborators(self) -> AsyncOutsideCollaboratorsResource:
        return AsyncOutsideCollaboratorsResource(self._client)

    @cached_property
    def packages(self) -> AsyncPackagesResource:
        return AsyncPackagesResource(self._client)

    @cached_property
    def personal_access_token_requests(self) -> AsyncPersonalAccessTokenRequestsResource:
        return AsyncPersonalAccessTokenRequestsResource(self._client)

    @cached_property
    def personal_access_tokens(self) -> AsyncPersonalAccessTokensResource:
        return AsyncPersonalAccessTokensResource(self._client)

    @cached_property
    def private_registries(self) -> AsyncPrivateRegistriesResource:
        return AsyncPrivateRegistriesResource(self._client)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        return AsyncPropertiesResource(self._client)

    @cached_property
    def public_members(self) -> AsyncPublicMembersResource:
        return AsyncPublicMembersResource(self._client)

    @cached_property
    def repos(self) -> AsyncReposResource:
        return AsyncReposResource(self._client)

    @cached_property
    def rulesets(self) -> AsyncRulesetsResource:
        return AsyncRulesetsResource(self._client)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResource:
        return AsyncSecretScanningResource(self._client)

    @cached_property
    def security_managers(self) -> AsyncSecurityManagersResource:
        return AsyncSecurityManagersResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        return AsyncTeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncOrgsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationFull:
        """
        Gets information about an organization.

        When the value of `two_factor_requirement_enabled` is `true`, the organization
        requires all members, billing managers, outside collaborators, guest
        collaborators, repository collaborators, or everyone with access to any
        repository within the organization to enable
        [two-factor authentication](https://docs.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/).

        To see the full details about an organization, the authenticated user must be an
        organization owner.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to see the full details about an organization.

        To see information about an organization's GitHub plan, GitHub Apps need the
        `Organization plan` permission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationFull,
        )

    async def update(
        self,
        org: str,
        *,
        advanced_security_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        billing_email: str | NotGiven = NOT_GIVEN,
        blog: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        default_repository_permission: Literal["read", "write", "admin", "none"] | NotGiven = NOT_GIVEN,
        dependabot_alerts_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        dependabot_security_updates_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        dependency_graph_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        deploy_keys_enabled_for_repositories: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        has_organization_projects: bool | NotGiven = NOT_GIVEN,
        has_repository_projects: bool | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        members_allowed_repository_creation_type: Literal["all", "private", "none"] | NotGiven = NOT_GIVEN,
        members_can_create_internal_repositories: bool | NotGiven = NOT_GIVEN,
        members_can_create_pages: bool | NotGiven = NOT_GIVEN,
        members_can_create_private_pages: bool | NotGiven = NOT_GIVEN,
        members_can_create_private_repositories: bool | NotGiven = NOT_GIVEN,
        members_can_create_public_pages: bool | NotGiven = NOT_GIVEN,
        members_can_create_public_repositories: bool | NotGiven = NOT_GIVEN,
        members_can_create_repositories: bool | NotGiven = NOT_GIVEN,
        members_can_fork_private_repositories: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        secret_scanning_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection_custom_link: str | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection_custom_link_enabled: bool | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection_enabled_for_new_repositories: bool | NotGiven = NOT_GIVEN,
        twitter_username: str | NotGiven = NOT_GIVEN,
        web_commit_signoff_required: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationFull:
        """
        > [!WARNING] > **Closing down notice:** GitHub will replace and discontinue
        > `members_allowed_repository_creation_type` in favor of more granular
        > permissions. The new input parameters are
        > `members_can_create_public_repositories`,
        > `members_can_create_private_repositories` for all organizations and
        > `members_can_create_internal_repositories` for organizations associated with
        > an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise
        > Server 2.20+. For more information, see the
        > [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).

        > [!WARNING] > **Closing down notice:** Code security product enablement for new
        > repositories through the organization API is closing down. Please use
        > [code security configurations](https://docs.github.com/rest/code-security/configurations#set-a-code-security-configuration-as-a-default-for-an-organization)
        > to set defaults instead. For more information on setting a default security
        > configuration, see the
        > [changelog](https://github.blog/changelog/2024-07-09-sunsetting-security-settings-defaults-parameters-in-the-organizations-rest-api/).

        Updates the organization's profile and member privileges.

        The authenticated user must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` or
        `repo` scope to use this endpoint.

        Args:
          advanced_security_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether GitHub Advanced Security is automatically enabled for new repositories
              and repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          billing_email: Billing email address. This address is not publicized.

          company: The company name.

          default_repository_permission: Default permission level members have for organization repositories.

          dependabot_alerts_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether Dependabot alerts are automatically enabled for new repositories and
              repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          dependabot_security_updates_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether Dependabot security updates are automatically enabled for new
              repositories and repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          dependency_graph_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether dependency graph is automatically enabled for new repositories and
              repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          deploy_keys_enabled_for_repositories: Controls whether or not deploy keys may be added and used for repositories in
              the organization.

          description: The description of the company. The maximum size is 160 characters.

          email: The publicly visible email address.

          has_organization_projects: Whether an organization can use organization projects.

          has_repository_projects: Whether repositories that belong to the organization can use repository
              projects.

          location: The location.

          members_allowed_repository_creation_type: Specifies which types of repositories non-admin organization members can create.
              `private` is only available to repositories that are part of an organization on
              GitHub Enterprise Cloud. **Note:** This parameter is closing down and will be
              removed in the future. Its return value ignores internal repositories. Using
              this parameter overrides values set in `members_can_create_repositories`. See
              the parameter deprecation notice in the operation description for details.

          members_can_create_internal_repositories: Whether organization members can create internal repositories, which are visible
              to all enterprise members. You can only allow members to create internal
              repositories if your organization is associated with an enterprise account using
              GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information,
              see
              "[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)"
              in the GitHub Help documentation.

          members_can_create_pages: Whether organization members can create GitHub Pages sites. Existing published
              sites will not be impacted.

          members_can_create_private_pages: Whether organization members can create private GitHub Pages sites. Existing
              published sites will not be impacted.

          members_can_create_private_repositories: Whether organization members can create private repositories, which are visible
              to organization members with permission. For more information, see
              "[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)"
              in the GitHub Help documentation.

          members_can_create_public_pages: Whether organization members can create public GitHub Pages sites. Existing
              published sites will not be impacted.

          members_can_create_public_repositories: Whether organization members can create public repositories, which are visible
              to anyone. For more information, see
              "[Restricting repository creation in your organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/restricting-repository-creation-in-your-organization)"
              in the GitHub Help documentation.

          members_can_create_repositories: Whether of non-admin organization members can create repositories. **Note:** A
              parameter can override this parameter. See
              `members_allowed_repository_creation_type` in this table for details.

          members_can_fork_private_repositories: Whether organization members can fork private organization repositories.

          name: The shorthand name of the company.

          secret_scanning_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether secret scanning is automatically enabled for new repositories and
              repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          secret_scanning_push_protection_custom_link: If `secret_scanning_push_protection_custom_link_enabled` is true, the URL that
              will be displayed to contributors who are blocked from pushing a secret.

          secret_scanning_push_protection_custom_link_enabled: Whether a custom link is shown to contributors who are blocked from pushing a
              secret by push protection.

          secret_scanning_push_protection_enabled_for_new_repositories: **Endpoint closing down notice.** Please use
              [code security configurations](https://docs.github.com/rest/code-security/configurations)
              instead.

              Whether secret scanning push protection is automatically enabled for new
              repositories and repositories transferred to this organization.

              To use this parameter, you must have admin permissions for the repository or be
              an owner or security manager for the organization that owns the repository. For
              more information, see
              "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

              You can check which security and analysis features are currently enabled by
              using a `GET /orgs/{org}` request.

          twitter_username: The Twitter username of the company.

          web_commit_signoff_required: Whether contributors to organization repositories are required to sign off on
              commits they make through GitHub's web interface.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._patch(
            f"/orgs/{org}",
            body=await async_maybe_transform(
                {
                    "advanced_security_enabled_for_new_repositories": advanced_security_enabled_for_new_repositories,
                    "billing_email": billing_email,
                    "blog": blog,
                    "company": company,
                    "default_repository_permission": default_repository_permission,
                    "dependabot_alerts_enabled_for_new_repositories": dependabot_alerts_enabled_for_new_repositories,
                    "dependabot_security_updates_enabled_for_new_repositories": dependabot_security_updates_enabled_for_new_repositories,
                    "dependency_graph_enabled_for_new_repositories": dependency_graph_enabled_for_new_repositories,
                    "deploy_keys_enabled_for_repositories": deploy_keys_enabled_for_repositories,
                    "description": description,
                    "email": email,
                    "has_organization_projects": has_organization_projects,
                    "has_repository_projects": has_repository_projects,
                    "location": location,
                    "members_allowed_repository_creation_type": members_allowed_repository_creation_type,
                    "members_can_create_internal_repositories": members_can_create_internal_repositories,
                    "members_can_create_pages": members_can_create_pages,
                    "members_can_create_private_pages": members_can_create_private_pages,
                    "members_can_create_private_repositories": members_can_create_private_repositories,
                    "members_can_create_public_pages": members_can_create_public_pages,
                    "members_can_create_public_repositories": members_can_create_public_repositories,
                    "members_can_create_repositories": members_can_create_repositories,
                    "members_can_fork_private_repositories": members_can_fork_private_repositories,
                    "name": name,
                    "secret_scanning_enabled_for_new_repositories": secret_scanning_enabled_for_new_repositories,
                    "secret_scanning_push_protection_custom_link": secret_scanning_push_protection_custom_link,
                    "secret_scanning_push_protection_custom_link_enabled": secret_scanning_push_protection_custom_link_enabled,
                    "secret_scanning_push_protection_enabled_for_new_repositories": secret_scanning_push_protection_enabled_for_new_repositories,
                    "twitter_username": twitter_username,
                    "web_commit_signoff_required": web_commit_signoff_required,
                },
                org_update_params.OrgUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationFull,
        )

    async def delete(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes an organization and all its repositories.

        The organization login will be unavailable for 90 days after deletion.

        Please review the Terms of Service regarding account deletion before using this
        endpoint:

        https://docs.github.com/site-policy/github-terms/github-terms-of-service

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._delete(
            f"/orgs/{org}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def get_installation(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Installation:
        """
        Enables an authenticated GitHub App to find the organization's installation
        information.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/installation",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Installation,
        )

    async def list_attestations(
        self,
        subject_digest: str,
        *,
        org: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        predicate_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListAttestationsResponse:
        """
        List a collection of artifact attestations with a given subject digest that are
        associated with repositories owned by an organization.

        The collection of attestations returned by this endpoint is filtered according
        to the authenticated user's permissions; if the authenticated user cannot read a
        repository, the attestations associated with that repository will not be
        included in the response. In addition, when using a fine-grained access token
        the `attestations:read` permission is required.

        **Please note:** in order to offer meaningful security benefits, an
        attestation's signature and timestamps **must** be cryptographically verified,
        and the identity of the attestation signer **must** be validated. Attestations
        can be verified using the
        [GitHub CLI `attestation verify` command](https://cli.github.com/manual/gh_attestation_verify).
        For more information, see
        [our guide on how to use artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          predicate_type: Optional filter for fetching attestations with a given predicate type. This
              option accepts `provenance`, `sbom`, or freeform text for custom predicate
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not subject_digest:
            raise ValueError(f"Expected a non-empty value for `subject_digest` but received {subject_digest!r}")
        return await self._get(
            f"/orgs/{org}/attestations/{subject_digest}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "predicate_type": predicate_type,
                    },
                    org_list_attestations_params.OrgListAttestationsParams,
                ),
            ),
            cast_to=OrgListAttestationsResponse,
        )

    async def list_events(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListEventsResponse:
        """> [!NOTE] This API is not built to serve real-time use cases.

        Depending on the
        > time of day, event latency can be anywhere from 30s to 6h.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    org_list_events_params.OrgListEventsParams,
                ),
            ),
            cast_to=OrgListEventsResponse,
        )

    async def list_failed_invitations(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListFailedInvitationsResponse:
        """
        The return hash contains `failed_at` and `failed_reason` fields which represent
        the time at which the invitation failed and the reason for the failure.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/failed_invitations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    org_list_failed_invitations_params.OrgListFailedInvitationsParams,
                ),
            ),
            cast_to=OrgListFailedInvitationsResponse,
        )

    async def list_installations(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListInstallationsResponse:
        """Lists all GitHub Apps in an organization.

        The installation count includes all
        GitHub Apps installed on repositories in the organization.

        The authenticated user must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:read`
        scope to use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/installations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    org_list_installations_params.OrgListInstallationsParams,
                ),
            ),
            cast_to=OrgListInstallationsResponse,
        )

    async def list_issues(
        self,
        org: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        filter: Literal["assigned", "created", "mentioned", "subscribed", "repos", "all"] | NotGiven = NOT_GIVEN,
        labels: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "comments"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListIssuesResponse:
        """
        List issues in an organization assigned to the authenticated user.

        > [!NOTE] GitHub's REST API considers every pull request an issue, but not every
        > issue is a pull request. For this reason, "Issues" endpoints may return both
        > issues and pull requests in the response. You can identify pull requests by
        > the `pull_request` key. Be aware that the `id` of a pull request returned from
        > "Issues" endpoints will be an _issue id_. To find out the pull request id, use
        > the
        > "[List pull requests](https://docs.github.com/rest/pulls/pulls#list-pull-requests)"
        > endpoint.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          direction: The direction to sort the results by.

          filter: Indicates which sorts of issues to return. `assigned` means issues assigned to
              you. `created` means issues created by you. `mentioned` means issues mentioning
              you. `subscribed` means issues you're subscribed to updates for. `all` or
              `repos` means all issues you can see, regardless of participation or creation.

          labels: A list of comma separated label names. Example: `bug,ui,@high`

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: What to sort results by.

          state: Indicates the state of the issues to return.

          type: Can be the name of an issue type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/issues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "filter": filter,
                        "labels": labels,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "sort": sort,
                        "state": state,
                        "type": type,
                    },
                    org_list_issues_params.OrgListIssuesParams,
                ),
            ),
            cast_to=OrgListIssuesResponse,
        )

    async def list_security_advisories(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "published"] | NotGiven = NOT_GIVEN,
        state: Literal["triage", "draft", "published", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListSecurityAdvisoriesResponse:
        """
        Lists repository security advisories for an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:write` scope to use this endpoint.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          direction: The direction to sort the results by.

          per_page: The number of advisories to return per page. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          state: Filter by the state of the repository advisories. Only advisories of this state
              will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/security-advisories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    org_list_security_advisories_params.OrgListSecurityAdvisoriesParams,
                ),
            ),
            cast_to=OrgListSecurityAdvisoriesResponse,
        )

    async def set_security_feature(
        self,
        enablement: Literal["enable_all", "disable_all"],
        *,
        org: str,
        security_product: Literal[
            "dependency_graph",
            "dependabot_alerts",
            "dependabot_security_updates",
            "advanced_security",
            "code_scanning_default_setup",
            "secret_scanning",
            "secret_scanning_push_protection",
        ],
        query_suite: Literal["default", "extended"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Closing down notice:** The ability to enable or disable a
        > security feature for all eligible repositories in an organization is closing
        > down. Please use
        > [code security configurations](https://docs.github.com/rest/code-security/configurations)
        > instead. For more information, see the
        > [changelog](https://github.blog/changelog/2024-07-22-deprecation-of-api-endpoint-to-enable-or-disable-a-security-feature-for-an-organization/).

        Enables or disables the specified security feature for all eligible repositories
        in an organization. For more information, see
        "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

        The authenticated user must be an organization owner or be member of a team with
        the security manager role to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org`,
        `write:org`, or `repo` scopes to use this endpoint.

        Args:
          query_suite: CodeQL query suite to be used. If you specify the `query_suite` parameter, the
              default setup will be configured with this query suite only on all repositories
              that didn't have default setup already configured. It will not change the query
              suite on repositories that already have default setup configured. If you don't
              specify any `query_suite` in your request, the preferred query suite of the
              organization will be applied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not security_product:
            raise ValueError(f"Expected a non-empty value for `security_product` but received {security_product!r}")
        if not enablement:
            raise ValueError(f"Expected a non-empty value for `enablement` but received {enablement!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/orgs/{org}/{security_product}/{enablement}",
            body=await async_maybe_transform({"query_suite": query_suite}, org_set_security_feature_params.OrgSetSecurityFeatureParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class OrgsResourceWithRawResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.retrieve = to_raw_response_wrapper(
            orgs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            orgs.update,
        )
        self.delete = to_raw_response_wrapper(
            orgs.delete,
        )
        self.get_installation = to_raw_response_wrapper(
            orgs.get_installation,
        )
        self.list_attestations = to_raw_response_wrapper(
            orgs.list_attestations,
        )
        self.list_events = to_raw_response_wrapper(
            orgs.list_events,
        )
        self.list_failed_invitations = to_raw_response_wrapper(
            orgs.list_failed_invitations,
        )
        self.list_installations = to_raw_response_wrapper(
            orgs.list_installations,
        )
        self.list_issues = to_raw_response_wrapper(
            orgs.list_issues,
        )
        self.list_security_advisories = to_raw_response_wrapper(
            orgs.list_security_advisories,
        )
        self.set_security_feature = to_raw_response_wrapper(
            orgs.set_security_feature,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._orgs.actions)

    @cached_property
    def blocks(self) -> BlocksResourceWithRawResponse:
        return BlocksResourceWithRawResponse(self._orgs.blocks)

    @cached_property
    def campaigns(self) -> CampaignsResourceWithRawResponse:
        return CampaignsResourceWithRawResponse(self._orgs.campaigns)

    @cached_property
    def code_scanning(self) -> CodeScanningResourceWithRawResponse:
        return CodeScanningResourceWithRawResponse(self._orgs.code_scanning)

    @cached_property
    def code_security(self) -> CodeSecurityResourceWithRawResponse:
        return CodeSecurityResourceWithRawResponse(self._orgs.code_security)

    @cached_property
    def codespaces(self) -> CodespacesResourceWithRawResponse:
        return CodespacesResourceWithRawResponse(self._orgs.codespaces)

    @cached_property
    def copilot(self) -> CopilotResourceWithRawResponse:
        return CopilotResourceWithRawResponse(self._orgs.copilot)

    @cached_property
    def dependabot(self) -> DependabotResourceWithRawResponse:
        return DependabotResourceWithRawResponse(self._orgs.dependabot)

    @cached_property
    def docker(self) -> DockerResourceWithRawResponse:
        return DockerResourceWithRawResponse(self._orgs.docker)

    @cached_property
    def hooks(self) -> HooksResourceWithRawResponse:
        return HooksResourceWithRawResponse(self._orgs.hooks)

    @cached_property
    def insights(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self._orgs.insights)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResourceWithRawResponse:
        return InteractionLimitsResourceWithRawResponse(self._orgs.interaction_limits)

    @cached_property
    def invitations(self) -> InvitationsResourceWithRawResponse:
        return InvitationsResourceWithRawResponse(self._orgs.invitations)

    @cached_property
    def issue_types(self) -> IssueTypesResourceWithRawResponse:
        return IssueTypesResourceWithRawResponse(self._orgs.issue_types)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._orgs.members)

    @cached_property
    def memberships(self) -> MembershipsResourceWithRawResponse:
        return MembershipsResourceWithRawResponse(self._orgs.memberships)

    @cached_property
    def migrations(self) -> MigrationsResourceWithRawResponse:
        return MigrationsResourceWithRawResponse(self._orgs.migrations)

    @cached_property
    def organization_roles(self) -> OrganizationRolesResourceWithRawResponse:
        return OrganizationRolesResourceWithRawResponse(self._orgs.organization_roles)

    @cached_property
    def outside_collaborators(self) -> OutsideCollaboratorsResourceWithRawResponse:
        return OutsideCollaboratorsResourceWithRawResponse(self._orgs.outside_collaborators)

    @cached_property
    def packages(self) -> PackagesResourceWithRawResponse:
        return PackagesResourceWithRawResponse(self._orgs.packages)

    @cached_property
    def personal_access_token_requests(self) -> PersonalAccessTokenRequestsResourceWithRawResponse:
        return PersonalAccessTokenRequestsResourceWithRawResponse(self._orgs.personal_access_token_requests)

    @cached_property
    def personal_access_tokens(self) -> PersonalAccessTokensResourceWithRawResponse:
        return PersonalAccessTokensResourceWithRawResponse(self._orgs.personal_access_tokens)

    @cached_property
    def private_registries(self) -> PrivateRegistriesResourceWithRawResponse:
        return PrivateRegistriesResourceWithRawResponse(self._orgs.private_registries)

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._orgs.projects)

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        return PropertiesResourceWithRawResponse(self._orgs.properties)

    @cached_property
    def public_members(self) -> PublicMembersResourceWithRawResponse:
        return PublicMembersResourceWithRawResponse(self._orgs.public_members)

    @cached_property
    def repos(self) -> ReposResourceWithRawResponse:
        return ReposResourceWithRawResponse(self._orgs.repos)

    @cached_property
    def rulesets(self) -> RulesetsResourceWithRawResponse:
        return RulesetsResourceWithRawResponse(self._orgs.rulesets)

    @cached_property
    def secret_scanning(self) -> SecretScanningResourceWithRawResponse:
        return SecretScanningResourceWithRawResponse(self._orgs.secret_scanning)

    @cached_property
    def security_managers(self) -> SecurityManagersResourceWithRawResponse:
        return SecurityManagersResourceWithRawResponse(self._orgs.security_managers)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._orgs.settings)

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self._orgs.teams)


class AsyncOrgsResourceWithRawResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.retrieve = async_to_raw_response_wrapper(
            orgs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            orgs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            orgs.delete,
        )
        self.get_installation = async_to_raw_response_wrapper(
            orgs.get_installation,
        )
        self.list_attestations = async_to_raw_response_wrapper(
            orgs.list_attestations,
        )
        self.list_events = async_to_raw_response_wrapper(
            orgs.list_events,
        )
        self.list_failed_invitations = async_to_raw_response_wrapper(
            orgs.list_failed_invitations,
        )
        self.list_installations = async_to_raw_response_wrapper(
            orgs.list_installations,
        )
        self.list_issues = async_to_raw_response_wrapper(
            orgs.list_issues,
        )
        self.list_security_advisories = async_to_raw_response_wrapper(
            orgs.list_security_advisories,
        )
        self.set_security_feature = async_to_raw_response_wrapper(
            orgs.set_security_feature,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._orgs.actions)

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithRawResponse:
        return AsyncBlocksResourceWithRawResponse(self._orgs.blocks)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithRawResponse:
        return AsyncCampaignsResourceWithRawResponse(self._orgs.campaigns)

    @cached_property
    def code_scanning(self) -> AsyncCodeScanningResourceWithRawResponse:
        return AsyncCodeScanningResourceWithRawResponse(self._orgs.code_scanning)

    @cached_property
    def code_security(self) -> AsyncCodeSecurityResourceWithRawResponse:
        return AsyncCodeSecurityResourceWithRawResponse(self._orgs.code_security)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResourceWithRawResponse:
        return AsyncCodespacesResourceWithRawResponse(self._orgs.codespaces)

    @cached_property
    def copilot(self) -> AsyncCopilotResourceWithRawResponse:
        return AsyncCopilotResourceWithRawResponse(self._orgs.copilot)

    @cached_property
    def dependabot(self) -> AsyncDependabotResourceWithRawResponse:
        return AsyncDependabotResourceWithRawResponse(self._orgs.dependabot)

    @cached_property
    def docker(self) -> AsyncDockerResourceWithRawResponse:
        return AsyncDockerResourceWithRawResponse(self._orgs.docker)

    @cached_property
    def hooks(self) -> AsyncHooksResourceWithRawResponse:
        return AsyncHooksResourceWithRawResponse(self._orgs.hooks)

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self._orgs.insights)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResourceWithRawResponse:
        return AsyncInteractionLimitsResourceWithRawResponse(self._orgs.interaction_limits)

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithRawResponse:
        return AsyncInvitationsResourceWithRawResponse(self._orgs.invitations)

    @cached_property
    def issue_types(self) -> AsyncIssueTypesResourceWithRawResponse:
        return AsyncIssueTypesResourceWithRawResponse(self._orgs.issue_types)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._orgs.members)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithRawResponse:
        return AsyncMembershipsResourceWithRawResponse(self._orgs.memberships)

    @cached_property
    def migrations(self) -> AsyncMigrationsResourceWithRawResponse:
        return AsyncMigrationsResourceWithRawResponse(self._orgs.migrations)

    @cached_property
    def organization_roles(self) -> AsyncOrganizationRolesResourceWithRawResponse:
        return AsyncOrganizationRolesResourceWithRawResponse(self._orgs.organization_roles)

    @cached_property
    def outside_collaborators(self) -> AsyncOutsideCollaboratorsResourceWithRawResponse:
        return AsyncOutsideCollaboratorsResourceWithRawResponse(self._orgs.outside_collaborators)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithRawResponse:
        return AsyncPackagesResourceWithRawResponse(self._orgs.packages)

    @cached_property
    def personal_access_token_requests(self) -> AsyncPersonalAccessTokenRequestsResourceWithRawResponse:
        return AsyncPersonalAccessTokenRequestsResourceWithRawResponse(self._orgs.personal_access_token_requests)

    @cached_property
    def personal_access_tokens(self) -> AsyncPersonalAccessTokensResourceWithRawResponse:
        return AsyncPersonalAccessTokensResourceWithRawResponse(self._orgs.personal_access_tokens)

    @cached_property
    def private_registries(self) -> AsyncPrivateRegistriesResourceWithRawResponse:
        return AsyncPrivateRegistriesResourceWithRawResponse(self._orgs.private_registries)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._orgs.projects)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        return AsyncPropertiesResourceWithRawResponse(self._orgs.properties)

    @cached_property
    def public_members(self) -> AsyncPublicMembersResourceWithRawResponse:
        return AsyncPublicMembersResourceWithRawResponse(self._orgs.public_members)

    @cached_property
    def repos(self) -> AsyncReposResourceWithRawResponse:
        return AsyncReposResourceWithRawResponse(self._orgs.repos)

    @cached_property
    def rulesets(self) -> AsyncRulesetsResourceWithRawResponse:
        return AsyncRulesetsResourceWithRawResponse(self._orgs.rulesets)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResourceWithRawResponse:
        return AsyncSecretScanningResourceWithRawResponse(self._orgs.secret_scanning)

    @cached_property
    def security_managers(self) -> AsyncSecurityManagersResourceWithRawResponse:
        return AsyncSecurityManagersResourceWithRawResponse(self._orgs.security_managers)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._orgs.settings)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self._orgs.teams)


class OrgsResourceWithStreamingResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.retrieve = to_streamed_response_wrapper(
            orgs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            orgs.update,
        )
        self.delete = to_streamed_response_wrapper(
            orgs.delete,
        )
        self.get_installation = to_streamed_response_wrapper(
            orgs.get_installation,
        )
        self.list_attestations = to_streamed_response_wrapper(
            orgs.list_attestations,
        )
        self.list_events = to_streamed_response_wrapper(
            orgs.list_events,
        )
        self.list_failed_invitations = to_streamed_response_wrapper(
            orgs.list_failed_invitations,
        )
        self.list_installations = to_streamed_response_wrapper(
            orgs.list_installations,
        )
        self.list_issues = to_streamed_response_wrapper(
            orgs.list_issues,
        )
        self.list_security_advisories = to_streamed_response_wrapper(
            orgs.list_security_advisories,
        )
        self.set_security_feature = to_streamed_response_wrapper(
            orgs.set_security_feature,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._orgs.actions)

    @cached_property
    def blocks(self) -> BlocksResourceWithStreamingResponse:
        return BlocksResourceWithStreamingResponse(self._orgs.blocks)

    @cached_property
    def campaigns(self) -> CampaignsResourceWithStreamingResponse:
        return CampaignsResourceWithStreamingResponse(self._orgs.campaigns)

    @cached_property
    def code_scanning(self) -> CodeScanningResourceWithStreamingResponse:
        return CodeScanningResourceWithStreamingResponse(self._orgs.code_scanning)

    @cached_property
    def code_security(self) -> CodeSecurityResourceWithStreamingResponse:
        return CodeSecurityResourceWithStreamingResponse(self._orgs.code_security)

    @cached_property
    def codespaces(self) -> CodespacesResourceWithStreamingResponse:
        return CodespacesResourceWithStreamingResponse(self._orgs.codespaces)

    @cached_property
    def copilot(self) -> CopilotResourceWithStreamingResponse:
        return CopilotResourceWithStreamingResponse(self._orgs.copilot)

    @cached_property
    def dependabot(self) -> DependabotResourceWithStreamingResponse:
        return DependabotResourceWithStreamingResponse(self._orgs.dependabot)

    @cached_property
    def docker(self) -> DockerResourceWithStreamingResponse:
        return DockerResourceWithStreamingResponse(self._orgs.docker)

    @cached_property
    def hooks(self) -> HooksResourceWithStreamingResponse:
        return HooksResourceWithStreamingResponse(self._orgs.hooks)

    @cached_property
    def insights(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self._orgs.insights)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResourceWithStreamingResponse:
        return InteractionLimitsResourceWithStreamingResponse(self._orgs.interaction_limits)

    @cached_property
    def invitations(self) -> InvitationsResourceWithStreamingResponse:
        return InvitationsResourceWithStreamingResponse(self._orgs.invitations)

    @cached_property
    def issue_types(self) -> IssueTypesResourceWithStreamingResponse:
        return IssueTypesResourceWithStreamingResponse(self._orgs.issue_types)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._orgs.members)

    @cached_property
    def memberships(self) -> MembershipsResourceWithStreamingResponse:
        return MembershipsResourceWithStreamingResponse(self._orgs.memberships)

    @cached_property
    def migrations(self) -> MigrationsResourceWithStreamingResponse:
        return MigrationsResourceWithStreamingResponse(self._orgs.migrations)

    @cached_property
    def organization_roles(self) -> OrganizationRolesResourceWithStreamingResponse:
        return OrganizationRolesResourceWithStreamingResponse(self._orgs.organization_roles)

    @cached_property
    def outside_collaborators(self) -> OutsideCollaboratorsResourceWithStreamingResponse:
        return OutsideCollaboratorsResourceWithStreamingResponse(self._orgs.outside_collaborators)

    @cached_property
    def packages(self) -> PackagesResourceWithStreamingResponse:
        return PackagesResourceWithStreamingResponse(self._orgs.packages)

    @cached_property
    def personal_access_token_requests(self) -> PersonalAccessTokenRequestsResourceWithStreamingResponse:
        return PersonalAccessTokenRequestsResourceWithStreamingResponse(self._orgs.personal_access_token_requests)

    @cached_property
    def personal_access_tokens(self) -> PersonalAccessTokensResourceWithStreamingResponse:
        return PersonalAccessTokensResourceWithStreamingResponse(self._orgs.personal_access_tokens)

    @cached_property
    def private_registries(self) -> PrivateRegistriesResourceWithStreamingResponse:
        return PrivateRegistriesResourceWithStreamingResponse(self._orgs.private_registries)

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._orgs.projects)

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        return PropertiesResourceWithStreamingResponse(self._orgs.properties)

    @cached_property
    def public_members(self) -> PublicMembersResourceWithStreamingResponse:
        return PublicMembersResourceWithStreamingResponse(self._orgs.public_members)

    @cached_property
    def repos(self) -> ReposResourceWithStreamingResponse:
        return ReposResourceWithStreamingResponse(self._orgs.repos)

    @cached_property
    def rulesets(self) -> RulesetsResourceWithStreamingResponse:
        return RulesetsResourceWithStreamingResponse(self._orgs.rulesets)

    @cached_property
    def secret_scanning(self) -> SecretScanningResourceWithStreamingResponse:
        return SecretScanningResourceWithStreamingResponse(self._orgs.secret_scanning)

    @cached_property
    def security_managers(self) -> SecurityManagersResourceWithStreamingResponse:
        return SecurityManagersResourceWithStreamingResponse(self._orgs.security_managers)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._orgs.settings)

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self._orgs.teams)


class AsyncOrgsResourceWithStreamingResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.retrieve = async_to_streamed_response_wrapper(
            orgs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            orgs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            orgs.delete,
        )
        self.get_installation = async_to_streamed_response_wrapper(
            orgs.get_installation,
        )
        self.list_attestations = async_to_streamed_response_wrapper(
            orgs.list_attestations,
        )
        self.list_events = async_to_streamed_response_wrapper(
            orgs.list_events,
        )
        self.list_failed_invitations = async_to_streamed_response_wrapper(
            orgs.list_failed_invitations,
        )
        self.list_installations = async_to_streamed_response_wrapper(
            orgs.list_installations,
        )
        self.list_issues = async_to_streamed_response_wrapper(
            orgs.list_issues,
        )
        self.list_security_advisories = async_to_streamed_response_wrapper(
            orgs.list_security_advisories,
        )
        self.set_security_feature = async_to_streamed_response_wrapper(
            orgs.set_security_feature,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._orgs.actions)

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithStreamingResponse:
        return AsyncBlocksResourceWithStreamingResponse(self._orgs.blocks)

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithStreamingResponse:
        return AsyncCampaignsResourceWithStreamingResponse(self._orgs.campaigns)

    @cached_property
    def code_scanning(self) -> AsyncCodeScanningResourceWithStreamingResponse:
        return AsyncCodeScanningResourceWithStreamingResponse(self._orgs.code_scanning)

    @cached_property
    def code_security(self) -> AsyncCodeSecurityResourceWithStreamingResponse:
        return AsyncCodeSecurityResourceWithStreamingResponse(self._orgs.code_security)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResourceWithStreamingResponse:
        return AsyncCodespacesResourceWithStreamingResponse(self._orgs.codespaces)

    @cached_property
    def copilot(self) -> AsyncCopilotResourceWithStreamingResponse:
        return AsyncCopilotResourceWithStreamingResponse(self._orgs.copilot)

    @cached_property
    def dependabot(self) -> AsyncDependabotResourceWithStreamingResponse:
        return AsyncDependabotResourceWithStreamingResponse(self._orgs.dependabot)

    @cached_property
    def docker(self) -> AsyncDockerResourceWithStreamingResponse:
        return AsyncDockerResourceWithStreamingResponse(self._orgs.docker)

    @cached_property
    def hooks(self) -> AsyncHooksResourceWithStreamingResponse:
        return AsyncHooksResourceWithStreamingResponse(self._orgs.hooks)

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self._orgs.insights)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResourceWithStreamingResponse:
        return AsyncInteractionLimitsResourceWithStreamingResponse(self._orgs.interaction_limits)

    @cached_property
    def invitations(self) -> AsyncInvitationsResourceWithStreamingResponse:
        return AsyncInvitationsResourceWithStreamingResponse(self._orgs.invitations)

    @cached_property
    def issue_types(self) -> AsyncIssueTypesResourceWithStreamingResponse:
        return AsyncIssueTypesResourceWithStreamingResponse(self._orgs.issue_types)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._orgs.members)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self._orgs.memberships)

    @cached_property
    def migrations(self) -> AsyncMigrationsResourceWithStreamingResponse:
        return AsyncMigrationsResourceWithStreamingResponse(self._orgs.migrations)

    @cached_property
    def organization_roles(self) -> AsyncOrganizationRolesResourceWithStreamingResponse:
        return AsyncOrganizationRolesResourceWithStreamingResponse(self._orgs.organization_roles)

    @cached_property
    def outside_collaborators(self) -> AsyncOutsideCollaboratorsResourceWithStreamingResponse:
        return AsyncOutsideCollaboratorsResourceWithStreamingResponse(self._orgs.outside_collaborators)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithStreamingResponse:
        return AsyncPackagesResourceWithStreamingResponse(self._orgs.packages)

    @cached_property
    def personal_access_token_requests(self) -> AsyncPersonalAccessTokenRequestsResourceWithStreamingResponse:
        return AsyncPersonalAccessTokenRequestsResourceWithStreamingResponse(self._orgs.personal_access_token_requests)

    @cached_property
    def personal_access_tokens(self) -> AsyncPersonalAccessTokensResourceWithStreamingResponse:
        return AsyncPersonalAccessTokensResourceWithStreamingResponse(self._orgs.personal_access_tokens)

    @cached_property
    def private_registries(self) -> AsyncPrivateRegistriesResourceWithStreamingResponse:
        return AsyncPrivateRegistriesResourceWithStreamingResponse(self._orgs.private_registries)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._orgs.projects)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        return AsyncPropertiesResourceWithStreamingResponse(self._orgs.properties)

    @cached_property
    def public_members(self) -> AsyncPublicMembersResourceWithStreamingResponse:
        return AsyncPublicMembersResourceWithStreamingResponse(self._orgs.public_members)

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._orgs.repos)

    @cached_property
    def rulesets(self) -> AsyncRulesetsResourceWithStreamingResponse:
        return AsyncRulesetsResourceWithStreamingResponse(self._orgs.rulesets)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResourceWithStreamingResponse:
        return AsyncSecretScanningResourceWithStreamingResponse(self._orgs.secret_scanning)

    @cached_property
    def security_managers(self) -> AsyncSecurityManagersResourceWithStreamingResponse:
        return AsyncSecurityManagersResourceWithStreamingResponse(self._orgs.security_managers)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._orgs.settings)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self._orgs.teams)
