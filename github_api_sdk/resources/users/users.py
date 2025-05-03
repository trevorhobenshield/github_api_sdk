from __future__ import annotations

from datetime import datetime
from typing import Any, Optional, Union, cast

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
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types import (
    user_create_project_params,
    user_list_attestations_params,
    user_list_followers_0_params,
    user_list_followers_1_params,
    user_list_gists_params,
    user_list_gpg_keys_params,
    user_list_issues_params,
    user_list_organizations_0_params,
    user_list_organizations_1_params,
    user_list_params,
    user_list_projects_params,
    user_list_public_emails_params,
    user_list_public_keys_params,
    user_list_repositories_params,
    user_list_social_accounts_params,
    user_list_ssh_signing_keys_params,
    user_list_starred_repositories_params,
    user_list_subscriptions_0_params,
    user_list_subscriptions_1_params,
    user_list_teams_params,
    user_retrieve_hovercard_params,
    user_update_params,
)
from ...types.applications.installation import Installation
from ...types.orgs.project import Project
from ...types.private_user import PrivateUser
from ...types.user_list_attestations_response import UserListAttestationsResponse
from ...types.user_list_followers_0_response import UserListFollowers0Response
from ...types.user_list_followers_1_response import UserListFollowers1Response
from ...types.user_list_gists_response import UserListGistsResponse
from ...types.user_list_gpg_keys_response import UserListGpgKeysResponse
from ...types.user_list_issues_response import UserListIssuesResponse
from ...types.user_list_organizations_0_response import UserListOrganizations0Response
from ...types.user_list_organizations_1_response import UserListOrganizations1Response
from ...types.user_list_projects_response import UserListProjectsResponse
from ...types.user_list_public_emails_response import UserListPublicEmailsResponse
from ...types.user_list_public_keys_response import UserListPublicKeysResponse
from ...types.user_list_repositories_response import UserListRepositoriesResponse
from ...types.user_list_response import UserListResponse
from ...types.user_list_social_accounts_response import UserListSocialAccountsResponse
from ...types.user_list_ssh_signing_keys_response import UserListSSHSigningKeysResponse
from ...types.user_list_starred_repositories_response import UserListStarredRepositoriesResponse
from ...types.user_list_subscriptions_0_response import UserListSubscriptions0Response
from ...types.user_list_subscriptions_1_response import UserListSubscriptions1Response
from ...types.user_list_teams_response import UserListTeamsResponse
from ...types.user_retrieve_0_response import UserRetrieve0Response
from ...types.user_retrieve_1_response import UserRetrieve1Response
from ...types.user_retrieve_by_id_response import UserRetrieveByIDResponse
from ...types.user_retrieve_hovercard_response import UserRetrieveHovercardResponse
from .blocks import (
    AsyncBlocksResource,
    AsyncBlocksResourceWithRawResponse,
    AsyncBlocksResourceWithStreamingResponse,
    BlocksResource,
    BlocksResourceWithRawResponse,
    BlocksResourceWithStreamingResponse,
)
from .codespaces.codespaces import (
    AsyncCodespacesResource,
    AsyncCodespacesResourceWithRawResponse,
    AsyncCodespacesResourceWithStreamingResponse,
    CodespacesResource,
    CodespacesResourceWithRawResponse,
    CodespacesResourceWithStreamingResponse,
)
from .docker import (
    AsyncDockerResource,
    AsyncDockerResourceWithRawResponse,
    AsyncDockerResourceWithStreamingResponse,
    DockerResource,
    DockerResourceWithRawResponse,
    DockerResourceWithStreamingResponse,
)
from .email import (
    AsyncEmailResource,
    AsyncEmailResourceWithRawResponse,
    AsyncEmailResourceWithStreamingResponse,
    EmailResource,
    EmailResourceWithRawResponse,
    EmailResourceWithStreamingResponse,
)
from .emails import (
    AsyncEmailsResource,
    AsyncEmailsResourceWithRawResponse,
    AsyncEmailsResourceWithStreamingResponse,
    EmailsResource,
    EmailsResourceWithRawResponse,
    EmailsResourceWithStreamingResponse,
)
from .events import (
    AsyncEventsResource,
    AsyncEventsResourceWithRawResponse,
    AsyncEventsResourceWithStreamingResponse,
    EventsResource,
    EventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
)
from .following import (
    AsyncFollowingResource,
    AsyncFollowingResourceWithRawResponse,
    AsyncFollowingResourceWithStreamingResponse,
    FollowingResource,
    FollowingResourceWithRawResponse,
    FollowingResourceWithStreamingResponse,
)
from .gpg_keys import (
    AsyncGpgKeysResource,
    AsyncGpgKeysResourceWithRawResponse,
    AsyncGpgKeysResourceWithStreamingResponse,
    GpgKeysResource,
    GpgKeysResourceWithRawResponse,
    GpgKeysResourceWithStreamingResponse,
)
from .installations.installations import (
    AsyncInstallationsResource,
    AsyncInstallationsResourceWithRawResponse,
    AsyncInstallationsResourceWithStreamingResponse,
    InstallationsResource,
    InstallationsResourceWithRawResponse,
    InstallationsResourceWithStreamingResponse,
)
from .interaction_limits import (
    AsyncInteractionLimitsResource,
    AsyncInteractionLimitsResourceWithRawResponse,
    AsyncInteractionLimitsResourceWithStreamingResponse,
    InteractionLimitsResource,
    InteractionLimitsResourceWithRawResponse,
    InteractionLimitsResourceWithStreamingResponse,
)
from .keys import (
    AsyncKeysResource,
    AsyncKeysResourceWithRawResponse,
    AsyncKeysResourceWithStreamingResponse,
    KeysResource,
    KeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
)
from .marketplace_purchases import (
    AsyncMarketplacePurchasesResource,
    AsyncMarketplacePurchasesResourceWithRawResponse,
    AsyncMarketplacePurchasesResourceWithStreamingResponse,
    MarketplacePurchasesResource,
    MarketplacePurchasesResourceWithRawResponse,
    MarketplacePurchasesResourceWithStreamingResponse,
)
from .memberships.memberships import (
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
from .packages.packages import (
    AsyncPackagesResource,
    AsyncPackagesResourceWithRawResponse,
    AsyncPackagesResourceWithStreamingResponse,
    PackagesResource,
    PackagesResourceWithRawResponse,
    PackagesResourceWithStreamingResponse,
)
from .received_events import (
    AsyncReceivedEventsResource,
    AsyncReceivedEventsResourceWithRawResponse,
    AsyncReceivedEventsResourceWithStreamingResponse,
    ReceivedEventsResource,
    ReceivedEventsResourceWithRawResponse,
    ReceivedEventsResourceWithStreamingResponse,
)
from .repos import (
    AsyncReposResource,
    AsyncReposResourceWithRawResponse,
    AsyncReposResourceWithStreamingResponse,
    ReposResource,
    ReposResourceWithRawResponse,
    ReposResourceWithStreamingResponse,
)
from .repository_invitations import (
    AsyncRepositoryInvitationsResource,
    AsyncRepositoryInvitationsResourceWithRawResponse,
    AsyncRepositoryInvitationsResourceWithStreamingResponse,
    RepositoryInvitationsResource,
    RepositoryInvitationsResourceWithRawResponse,
    RepositoryInvitationsResourceWithStreamingResponse,
)
from .settings.settings import (
    AsyncSettingsResource,
    AsyncSettingsResourceWithRawResponse,
    AsyncSettingsResourceWithStreamingResponse,
    SettingsResource,
    SettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
)
from .social_accounts import (
    AsyncSocialAccountsResource,
    AsyncSocialAccountsResourceWithRawResponse,
    AsyncSocialAccountsResourceWithStreamingResponse,
    SocialAccountsResource,
    SocialAccountsResourceWithRawResponse,
    SocialAccountsResourceWithStreamingResponse,
)
from .ssh_signing_keys import (
    AsyncSSHSigningKeysResource,
    AsyncSSHSigningKeysResourceWithRawResponse,
    AsyncSSHSigningKeysResourceWithStreamingResponse,
    SSHSigningKeysResource,
    SSHSigningKeysResourceWithRawResponse,
    SSHSigningKeysResourceWithStreamingResponse,
)
from .starred import (
    AsyncStarredResource,
    AsyncStarredResourceWithRawResponse,
    AsyncStarredResourceWithStreamingResponse,
    StarredResource,
    StarredResourceWithRawResponse,
    StarredResourceWithStreamingResponse,
)

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def blocks(self) -> BlocksResource:
        return BlocksResource(self._client)

    @cached_property
    def codespaces(self) -> CodespacesResource:
        return CodespacesResource(self._client)

    @cached_property
    def email(self) -> EmailResource:
        return EmailResource(self._client)

    @cached_property
    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    @cached_property
    def gpg_keys(self) -> GpgKeysResource:
        return GpgKeysResource(self._client)

    @cached_property
    def installations(self) -> InstallationsResource:
        return InstallationsResource(self._client)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResource:
        return InteractionLimitsResource(self._client)

    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def marketplace_purchases(self) -> MarketplacePurchasesResource:
        return MarketplacePurchasesResource(self._client)

    @cached_property
    def memberships(self) -> MembershipsResource:
        return MembershipsResource(self._client)

    @cached_property
    def migrations(self) -> MigrationsResource:
        return MigrationsResource(self._client)

    @cached_property
    def repos(self) -> ReposResource:
        return ReposResource(self._client)

    @cached_property
    def repository_invitations(self) -> RepositoryInvitationsResource:
        return RepositoryInvitationsResource(self._client)

    @cached_property
    def social_accounts(self) -> SocialAccountsResource:
        return SocialAccountsResource(self._client)

    @cached_property
    def ssh_signing_keys(self) -> SSHSigningKeysResource:
        return SSHSigningKeysResource(self._client)

    @cached_property
    def starred(self) -> StarredResource:
        return StarredResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def received_events(self) -> ReceivedEventsResource:
        return ReceivedEventsResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def docker(self) -> DockerResource:
        return DockerResource(self._client)

    @cached_property
    def following(self) -> FollowingResource:
        return FollowingResource(self._client)

    @cached_property
    def packages(self) -> PackagesResource:
        return PackagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        bio: str | NotGiven = NOT_GIVEN,
        blog: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        hireable: bool | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        twitter_username: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateUser:
        """
        **Note:** If your email is set to private and you send an `email` parameter as
        part of this request to update your profile, your privacy settings are still
        enforced: the email address will not be displayed on your public profile or via
        the API.

        Args:
          bio: The new short biography of the user.

          blog: The new blog URL of the user.

          company: The new company of the user.

          email: The publicly visible email address of the user.

          hireable: The new hiring availability of the user.

          location: The new location of the user.

          name: The new name of the user.

          twitter_username: The new Twitter username of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/user",
            body=maybe_transform(
                {
                    "bio": bio,
                    "blog": blog,
                    "company": company,
                    "email": email,
                    "hireable": hireable,
                    "location": location,
                    "name": name,
                    "twitter_username": twitter_username,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PrivateUser,
        )

    def list(
        self,
        *,
        per_page: int | NotGiven = NOT_GIVEN,
        since: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """Lists all users, in the order that they signed up on GitHub.

        This list includes
        personal user accounts and organization accounts.

        Note: Pagination is powered exclusively by the `since` parameter. Use the
        [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers)
        to get the URL for the next page of users.

        Args:
          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: A user ID. Only return users with an ID greater than this ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "per_page": per_page,
                        "since": since,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    def create_project(
        self,
        *,
        name: str,
        body: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          name: Name of the project

          body: Body of the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/projects",
            body=maybe_transform(
                {
                    "name": name,
                    "body": body,
                },
                user_create_project_params.UserCreateProjectParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    def list_attestations(
        self,
        subject_digest: str,
        *,
        username: str,
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
    ) -> UserListAttestationsResponse:
        """
        List a collection of artifact attestations with a given subject digest that are
        associated with repositories owned by a user.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not subject_digest:
            raise ValueError(f"Expected a non-empty value for `subject_digest` but received {subject_digest!r}")
        return self._get(
            f"/users/{username}/attestations/{subject_digest}",
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
                    user_list_attestations_params.UserListAttestationsParams,
                ),
            ),
            cast_to=UserListAttestationsResponse,
        )

    def list_followers_0(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListFollowers0Response:
        """
        Lists the people following the authenticated user.

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
        return self._get(
            "/user/followers",
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
                    user_list_followers_0_params.UserListFollowers0Params,
                ),
            ),
            cast_to=UserListFollowers0Response,
        )

    def list_followers_1(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListFollowers1Response:
        """
        Lists the people following the specified user.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/followers",
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
                    user_list_followers_1_params.UserListFollowers1Params,
                ),
            ),
            cast_to=UserListFollowers1Response,
        )

    def list_gists(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListGistsResponse:
        """
        Lists public gists for the specified user:

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/gists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                    },
                    user_list_gists_params.UserListGistsParams,
                ),
            ),
            cast_to=UserListGistsResponse,
        )

    def list_gpg_keys(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListGpgKeysResponse:
        """Lists the GPG keys for a user.

        This information is accessible by anyone.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/gpg_keys",
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
                    user_list_gpg_keys_params.UserListGpgKeysParams,
                ),
            ),
            cast_to=UserListGpgKeysResponse,
        )

    def list_issues(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        filter: Literal["assigned", "created", "mentioned", "subscribed", "repos", "all"] | NotGiven = NOT_GIVEN,
        labels: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "comments"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListIssuesResponse:
        """
        List issues across owned and member repositories assigned to the authenticated
        user.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/issues",
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
                    },
                    user_list_issues_params.UserListIssuesParams,
                ),
            ),
            cast_to=UserListIssuesResponse,
        )

    def list_organizations_0(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListOrganizations0Response:
        """
        List organizations for the authenticated user.

        For OAuth app tokens and personal access tokens (classic), this endpoint only
        lists organizations that your authorization allows you to operate on in some way
        (e.g., you can list teams with `read:org` scope, you can publicize your
        organization membership with `user` scope, etc.). Therefore, this API requires
        at least `user` or `read:org` scope for OAuth app tokens and personal access
        tokens (classic). Requests with insufficient scope will receive a
        `403 Forbidden` response.

        > [!NOTE] Requests using a fine-grained access token will receive a
        > `200 Success` response with an empty list.

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
        return self._get(
            "/user/orgs",
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
                    user_list_organizations_0_params.UserListOrganizations0Params,
                ),
            ),
            cast_to=UserListOrganizations0Response,
        )

    def list_organizations_1(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListOrganizations1Response:
        """
        List
        [public organization memberships](https://docs.github.com/articles/publicizing-or-concealing-organization-membership)
        for the specified user.

        This method only lists _public_ memberships, regardless of authentication. If
        you need to fetch all of the organization memberships (public and private) for
        the authenticated user, use the
        [List organizations for the authenticated user](https://docs.github.com/rest/orgs/orgs#list-organizations-for-the-authenticated-user)
        API instead.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/orgs",
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
                    user_list_organizations_1_params.UserListOrganizations1Params,
                ),
            ),
            cast_to=UserListOrganizations1Response,
        )

    def list_projects(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListProjectsResponse:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          state: Indicates the state of the projects to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    user_list_projects_params.UserListProjectsParams,
                ),
            ),
            cast_to=UserListProjectsResponse,
        )

    def list_public_emails(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListPublicEmailsResponse:
        """
        Lists your publicly visible email address, which you can set with the
        [Set primary email visibility for the authenticated user](https://docs.github.com/rest/users/emails#set-primary-email-visibility-for-the-authenticated-user)
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `user:email`
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
        return self._get(
            "/user/public_emails",
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
                    user_list_public_emails_params.UserListPublicEmailsParams,
                ),
            ),
            cast_to=UserListPublicEmailsResponse,
        )

    def list_public_keys(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListPublicKeysResponse:
        """Lists the _verified_ public SSH keys for a user.

        This is accessible by anyone.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/keys",
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
                    user_list_public_keys_params.UserListPublicKeysParams,
                ),
            ),
            cast_to=UserListPublicKeysResponse,
        )

    def list_repositories(
        self,
        username: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "pushed", "full_name"] | NotGiven = NOT_GIVEN,
        type: Literal["all", "owner", "member"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListRepositoriesResponse:
        """
        Lists public repositories for the specified user.

        Args:
          direction: The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          type: Limit results to repositories of the specified type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "type": type,
                    },
                    user_list_repositories_params.UserListRepositoriesParams,
                ),
            ),
            cast_to=UserListRepositoriesResponse,
        )

    def list_social_accounts(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListSocialAccountsResponse:
        """Lists social media accounts for a user.

        This endpoint is accessible by anyone.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/social_accounts",
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
                    user_list_social_accounts_params.UserListSocialAccountsParams,
                ),
            ),
            cast_to=UserListSocialAccountsResponse,
        )

    def list_ssh_signing_keys(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListSSHSigningKeysResponse:
        """Lists the SSH signing keys for a user.

        This operation is accessible by anyone.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/ssh_signing_keys",
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
                    user_list_ssh_signing_keys_params.UserListSSHSigningKeysParams,
                ),
            ),
            cast_to=UserListSSHSigningKeysResponse,
        )

    def list_starred_repositories(
        self,
        username: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListStarredRepositoriesResponse:
        """
        Lists repositories a user has starred.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.star+json`**: Includes a timestamp of when the star
          was created.

        Args:
          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by. `created` means when the repository was
              starred. `updated` means when the repository was last pushed to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return cast(
            UserListStarredRepositoriesResponse,
            self._get(
                f"/users/{username}/starred",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "direction": direction,
                            "page": page,
                            "per_page": per_page,
                            "sort": sort,
                        },
                        user_list_starred_repositories_params.UserListStarredRepositoriesParams,
                    ),
                ),
                cast_to=cast(Any, UserListStarredRepositoriesResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list_subscriptions_0(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListSubscriptions0Response:
        """
        Lists repositories the authenticated user is watching.

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
        return self._get(
            "/user/subscriptions",
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
                    user_list_subscriptions_0_params.UserListSubscriptions0Params,
                ),
            ),
            cast_to=UserListSubscriptions0Response,
        )

    def list_subscriptions_1(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListSubscriptions1Response:
        """
        Lists repositories a user is watching.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/subscriptions",
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
                    user_list_subscriptions_1_params.UserListSubscriptions1Params,
                ),
            ),
            cast_to=UserListSubscriptions1Response,
        )

    def list_teams(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListTeamsResponse:
        """
        List all of the teams across all of the organizations to which the authenticated
        user belongs.

        OAuth app tokens and personal access tokens (classic) need the `user`, `repo`,
        or `read:org` scope to use this endpoint.

        When using a fine-grained personal access token, the resource owner of the token
        must be a single organization, and the response will only include the teams from
        that organization.

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
        return self._get(
            "/user/teams",
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
                    user_list_teams_params.UserListTeamsParams,
                ),
            ),
            cast_to=UserListTeamsResponse,
        )

    def retrieve_0(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieve0Response:
        """
        OAuth app tokens and personal access tokens (classic) need the `user` scope in
        order for the response to include private profile information.
        """
        return cast(
            UserRetrieve0Response,
            self._get(
                "/user",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, UserRetrieve0Response),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_1(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieve1Response:
        """
        Provides publicly available information about someone with a GitHub account.

        If you are requesting information about an
        [Enterprise Managed User](https://docs.github.com/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users),
        or a GitHub App bot that is installed in an organization that uses Enterprise
        Managed Users, your requests must be authenticated as a user or GitHub App that
        has access to the organization to view that account's information. If you are
        not authorized, the request will return a `404 Not Found` status.

        The `email` key in the following response is the publicly visible email address
        from your GitHub [profile page](https://github.com/settings/profile). When
        setting up your profile, you can select a primary email address to be public
        which provides an email entry for this endpoint. If you do not set a public
        email address for `email`, then it will have a value of `null`. You only see
        publicly visible email addresses when authenticated with GitHub. For more
        information, see
        [Authentication](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#authentication).

        The Emails API enables you to list all of your email addresses, and toggle a
        primary email to be visible publicly. For more information, see
        [Emails API](https://docs.github.com/rest/users/emails).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return cast(
            UserRetrieve1Response,
            self._get(
                f"/users/{username}",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, UserRetrieve1Response),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_by_id(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveByIDResponse:
        """
        Provides publicly available information about someone with a GitHub account.
        This method takes their durable user `ID` instead of their `login`, which can
        change over time.

        If you are requesting information about an
        [Enterprise Managed User](https://docs.github.com/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users),
        or a GitHub App bot that is installed in an organization that uses Enterprise
        Managed Users, your requests must be authenticated as a user or GitHub App that
        has access to the organization to view that account's information. If you are
        not authorized, the request will return a `404 Not Found` status.

        The `email` key in the following response is the publicly visible email address
        from your GitHub [profile page](https://github.com/settings/profile). When
        setting up your profile, you can select a primary email address to be public
        which provides an email entry for this endpoint. If you do not set a public
        email address for `email`, then it will have a value of `null`. You only see
        publicly visible email addresses when authenticated with GitHub. For more
        information, see
        [Authentication](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#authentication).

        The Emails API enables you to list all of your email addresses, and toggle a
        primary email to be visible publicly. For more information, see
        [Emails API](https://docs.github.com/rest/users/emails).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            UserRetrieveByIDResponse,
            self._get(
                f"/user/{account_id}",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, UserRetrieveByIDResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_hovercard(
        self,
        username: str,
        *,
        subject_id: str | NotGiven = NOT_GIVEN,
        subject_type: Literal["organization", "repository", "issue", "pull_request"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveHovercardResponse:
        """Provides hovercard information.

        You can find out more about someone in relation
        to their pull requests, issues, repositories, and organizations.

        The `subject_type` and `subject_id` parameters provide context for the person's
        hovercard, which returns more information than without the parameters. For
        example, if you wanted to find out more about `octocat` who owns the
        `Spoon-Knife` repository, you would use a `subject_type` value of `repository`
        and a `subject_id` value of `1300192` (the ID of the `Spoon-Knife` repository).

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          subject_id: Uses the ID for the `subject_type` you specified. **Required** when using
              `subject_type`.

          subject_type: Identifies which additional information you'd like to receive about the person's
              hovercard. Can be `organization`, `repository`, `issue`, `pull_request`.
              **Required** when using `subject_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/hovercard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "subject_id": subject_id,
                        "subject_type": subject_type,
                    },
                    user_retrieve_hovercard_params.UserRetrieveHovercardParams,
                ),
            ),
            cast_to=UserRetrieveHovercardResponse,
        )

    def retrieve_installation(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Installation:
        """
        Enables an authenticated GitHub App to find the user’s installation information.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/installation",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Installation,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def blocks(self) -> AsyncBlocksResource:
        return AsyncBlocksResource(self._client)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResource:
        return AsyncCodespacesResource(self._client)

    @cached_property
    def email(self) -> AsyncEmailResource:
        return AsyncEmailResource(self._client)

    @cached_property
    def emails(self) -> AsyncEmailsResource:
        return AsyncEmailsResource(self._client)

    @cached_property
    def gpg_keys(self) -> AsyncGpgKeysResource:
        return AsyncGpgKeysResource(self._client)

    @cached_property
    def installations(self) -> AsyncInstallationsResource:
        return AsyncInstallationsResource(self._client)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResource:
        return AsyncInteractionLimitsResource(self._client)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def marketplace_purchases(self) -> AsyncMarketplacePurchasesResource:
        return AsyncMarketplacePurchasesResource(self._client)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        return AsyncMembershipsResource(self._client)

    @cached_property
    def migrations(self) -> AsyncMigrationsResource:
        return AsyncMigrationsResource(self._client)

    @cached_property
    def repos(self) -> AsyncReposResource:
        return AsyncReposResource(self._client)

    @cached_property
    def repository_invitations(self) -> AsyncRepositoryInvitationsResource:
        return AsyncRepositoryInvitationsResource(self._client)

    @cached_property
    def social_accounts(self) -> AsyncSocialAccountsResource:
        return AsyncSocialAccountsResource(self._client)

    @cached_property
    def ssh_signing_keys(self) -> AsyncSSHSigningKeysResource:
        return AsyncSSHSigningKeysResource(self._client)

    @cached_property
    def starred(self) -> AsyncStarredResource:
        return AsyncStarredResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def received_events(self) -> AsyncReceivedEventsResource:
        return AsyncReceivedEventsResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def docker(self) -> AsyncDockerResource:
        return AsyncDockerResource(self._client)

    @cached_property
    def following(self) -> AsyncFollowingResource:
        return AsyncFollowingResource(self._client)

    @cached_property
    def packages(self) -> AsyncPackagesResource:
        return AsyncPackagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        bio: str | NotGiven = NOT_GIVEN,
        blog: str | NotGiven = NOT_GIVEN,
        company: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        hireable: bool | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        twitter_username: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateUser:
        """
        **Note:** If your email is set to private and you send an `email` parameter as
        part of this request to update your profile, your privacy settings are still
        enforced: the email address will not be displayed on your public profile or via
        the API.

        Args:
          bio: The new short biography of the user.

          blog: The new blog URL of the user.

          company: The new company of the user.

          email: The publicly visible email address of the user.

          hireable: The new hiring availability of the user.

          location: The new location of the user.

          name: The new name of the user.

          twitter_username: The new Twitter username of the user.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/user",
            body=await async_maybe_transform(
                {
                    "bio": bio,
                    "blog": blog,
                    "company": company,
                    "email": email,
                    "hireable": hireable,
                    "location": location,
                    "name": name,
                    "twitter_username": twitter_username,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PrivateUser,
        )

    async def list(
        self,
        *,
        per_page: int | NotGiven = NOT_GIVEN,
        since: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListResponse:
        """Lists all users, in the order that they signed up on GitHub.

        This list includes
        personal user accounts and organization accounts.

        Note: Pagination is powered exclusively by the `since` parameter. Use the
        [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers)
        to get the URL for the next page of users.

        Args:
          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: A user ID. Only return users with an ID greater than this ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "per_page": per_page,
                        "since": since,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    async def create_project(
        self,
        *,
        name: str,
        body: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          name: Name of the project

          body: Body of the project

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/projects",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "body": body,
                },
                user_create_project_params.UserCreateProjectParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    async def list_attestations(
        self,
        subject_digest: str,
        *,
        username: str,
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
    ) -> UserListAttestationsResponse:
        """
        List a collection of artifact attestations with a given subject digest that are
        associated with repositories owned by a user.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not subject_digest:
            raise ValueError(f"Expected a non-empty value for `subject_digest` but received {subject_digest!r}")
        return await self._get(
            f"/users/{username}/attestations/{subject_digest}",
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
                    user_list_attestations_params.UserListAttestationsParams,
                ),
            ),
            cast_to=UserListAttestationsResponse,
        )

    async def list_followers_0(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListFollowers0Response:
        """
        Lists the people following the authenticated user.

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
        return await self._get(
            "/user/followers",
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
                    user_list_followers_0_params.UserListFollowers0Params,
                ),
            ),
            cast_to=UserListFollowers0Response,
        )

    async def list_followers_1(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListFollowers1Response:
        """
        Lists the people following the specified user.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/followers",
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
                    user_list_followers_1_params.UserListFollowers1Params,
                ),
            ),
            cast_to=UserListFollowers1Response,
        )

    async def list_gists(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListGistsResponse:
        """
        Lists public gists for the specified user:

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/gists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                    },
                    user_list_gists_params.UserListGistsParams,
                ),
            ),
            cast_to=UserListGistsResponse,
        )

    async def list_gpg_keys(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListGpgKeysResponse:
        """Lists the GPG keys for a user.

        This information is accessible by anyone.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/gpg_keys",
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
                    user_list_gpg_keys_params.UserListGpgKeysParams,
                ),
            ),
            cast_to=UserListGpgKeysResponse,
        )

    async def list_issues(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        filter: Literal["assigned", "created", "mentioned", "subscribed", "repos", "all"] | NotGiven = NOT_GIVEN,
        labels: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "comments"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListIssuesResponse:
        """
        List issues across owned and member repositories assigned to the authenticated
        user.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/issues",
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
                    },
                    user_list_issues_params.UserListIssuesParams,
                ),
            ),
            cast_to=UserListIssuesResponse,
        )

    async def list_organizations_0(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListOrganizations0Response:
        """
        List organizations for the authenticated user.

        For OAuth app tokens and personal access tokens (classic), this endpoint only
        lists organizations that your authorization allows you to operate on in some way
        (e.g., you can list teams with `read:org` scope, you can publicize your
        organization membership with `user` scope, etc.). Therefore, this API requires
        at least `user` or `read:org` scope for OAuth app tokens and personal access
        tokens (classic). Requests with insufficient scope will receive a
        `403 Forbidden` response.

        > [!NOTE] Requests using a fine-grained access token will receive a
        > `200 Success` response with an empty list.

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
        return await self._get(
            "/user/orgs",
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
                    user_list_organizations_0_params.UserListOrganizations0Params,
                ),
            ),
            cast_to=UserListOrganizations0Response,
        )

    async def list_organizations_1(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListOrganizations1Response:
        """
        List
        [public organization memberships](https://docs.github.com/articles/publicizing-or-concealing-organization-membership)
        for the specified user.

        This method only lists _public_ memberships, regardless of authentication. If
        you need to fetch all of the organization memberships (public and private) for
        the authenticated user, use the
        [List organizations for the authenticated user](https://docs.github.com/rest/orgs/orgs#list-organizations-for-the-authenticated-user)
        API instead.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/orgs",
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
                    user_list_organizations_1_params.UserListOrganizations1Params,
                ),
            ),
            cast_to=UserListOrganizations1Response,
        )

    async def list_projects(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListProjectsResponse:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          state: Indicates the state of the projects to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/projects",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    user_list_projects_params.UserListProjectsParams,
                ),
            ),
            cast_to=UserListProjectsResponse,
        )

    async def list_public_emails(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListPublicEmailsResponse:
        """
        Lists your publicly visible email address, which you can set with the
        [Set primary email visibility for the authenticated user](https://docs.github.com/rest/users/emails#set-primary-email-visibility-for-the-authenticated-user)
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `user:email`
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
        return await self._get(
            "/user/public_emails",
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
                    user_list_public_emails_params.UserListPublicEmailsParams,
                ),
            ),
            cast_to=UserListPublicEmailsResponse,
        )

    async def list_public_keys(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListPublicKeysResponse:
        """Lists the _verified_ public SSH keys for a user.

        This is accessible by anyone.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/keys",
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
                    user_list_public_keys_params.UserListPublicKeysParams,
                ),
            ),
            cast_to=UserListPublicKeysResponse,
        )

    async def list_repositories(
        self,
        username: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "pushed", "full_name"] | NotGiven = NOT_GIVEN,
        type: Literal["all", "owner", "member"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListRepositoriesResponse:
        """
        Lists public repositories for the specified user.

        Args:
          direction: The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          type: Limit results to repositories of the specified type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "type": type,
                    },
                    user_list_repositories_params.UserListRepositoriesParams,
                ),
            ),
            cast_to=UserListRepositoriesResponse,
        )

    async def list_social_accounts(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListSocialAccountsResponse:
        """Lists social media accounts for a user.

        This endpoint is accessible by anyone.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/social_accounts",
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
                    user_list_social_accounts_params.UserListSocialAccountsParams,
                ),
            ),
            cast_to=UserListSocialAccountsResponse,
        )

    async def list_ssh_signing_keys(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListSSHSigningKeysResponse:
        """Lists the SSH signing keys for a user.

        This operation is accessible by anyone.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/ssh_signing_keys",
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
                    user_list_ssh_signing_keys_params.UserListSSHSigningKeysParams,
                ),
            ),
            cast_to=UserListSSHSigningKeysResponse,
        )

    async def list_starred_repositories(
        self,
        username: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListStarredRepositoriesResponse:
        """
        Lists repositories a user has starred.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.star+json`**: Includes a timestamp of when the star
          was created.

        Args:
          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by. `created` means when the repository was
              starred. `updated` means when the repository was last pushed to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return cast(
            UserListStarredRepositoriesResponse,
            await self._get(
                f"/users/{username}/starred",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "direction": direction,
                            "page": page,
                            "per_page": per_page,
                            "sort": sort,
                        },
                        user_list_starred_repositories_params.UserListStarredRepositoriesParams,
                    ),
                ),
                cast_to=cast(Any, UserListStarredRepositoriesResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list_subscriptions_0(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListSubscriptions0Response:
        """
        Lists repositories the authenticated user is watching.

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
        return await self._get(
            "/user/subscriptions",
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
                    user_list_subscriptions_0_params.UserListSubscriptions0Params,
                ),
            ),
            cast_to=UserListSubscriptions0Response,
        )

    async def list_subscriptions_1(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListSubscriptions1Response:
        """
        Lists repositories a user is watching.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/subscriptions",
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
                    user_list_subscriptions_1_params.UserListSubscriptions1Params,
                ),
            ),
            cast_to=UserListSubscriptions1Response,
        )

    async def list_teams(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListTeamsResponse:
        """
        List all of the teams across all of the organizations to which the authenticated
        user belongs.

        OAuth app tokens and personal access tokens (classic) need the `user`, `repo`,
        or `read:org` scope to use this endpoint.

        When using a fine-grained personal access token, the resource owner of the token
        must be a single organization, and the response will only include the teams from
        that organization.

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
        return await self._get(
            "/user/teams",
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
                    user_list_teams_params.UserListTeamsParams,
                ),
            ),
            cast_to=UserListTeamsResponse,
        )

    async def retrieve_0(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieve0Response:
        """
        OAuth app tokens and personal access tokens (classic) need the `user` scope in
        order for the response to include private profile information.
        """
        return cast(
            UserRetrieve0Response,
            await self._get(
                "/user",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, UserRetrieve0Response),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_1(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieve1Response:
        """
        Provides publicly available information about someone with a GitHub account.

        If you are requesting information about an
        [Enterprise Managed User](https://docs.github.com/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users),
        or a GitHub App bot that is installed in an organization that uses Enterprise
        Managed Users, your requests must be authenticated as a user or GitHub App that
        has access to the organization to view that account's information. If you are
        not authorized, the request will return a `404 Not Found` status.

        The `email` key in the following response is the publicly visible email address
        from your GitHub [profile page](https://github.com/settings/profile). When
        setting up your profile, you can select a primary email address to be public
        which provides an email entry for this endpoint. If you do not set a public
        email address for `email`, then it will have a value of `null`. You only see
        publicly visible email addresses when authenticated with GitHub. For more
        information, see
        [Authentication](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#authentication).

        The Emails API enables you to list all of your email addresses, and toggle a
        primary email to be visible publicly. For more information, see
        [Emails API](https://docs.github.com/rest/users/emails).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return cast(
            UserRetrieve1Response,
            await self._get(
                f"/users/{username}",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, UserRetrieve1Response),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_by_id(
        self,
        account_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveByIDResponse:
        """
        Provides publicly available information about someone with a GitHub account.
        This method takes their durable user `ID` instead of their `login`, which can
        change over time.

        If you are requesting information about an
        [Enterprise Managed User](https://docs.github.com/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users),
        or a GitHub App bot that is installed in an organization that uses Enterprise
        Managed Users, your requests must be authenticated as a user or GitHub App that
        has access to the organization to view that account's information. If you are
        not authorized, the request will return a `404 Not Found` status.

        The `email` key in the following response is the publicly visible email address
        from your GitHub [profile page](https://github.com/settings/profile). When
        setting up your profile, you can select a primary email address to be public
        which provides an email entry for this endpoint. If you do not set a public
        email address for `email`, then it will have a value of `null`. You only see
        publicly visible email addresses when authenticated with GitHub. For more
        information, see
        [Authentication](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#authentication).

        The Emails API enables you to list all of your email addresses, and toggle a
        primary email to be visible publicly. For more information, see
        [Emails API](https://docs.github.com/rest/users/emails).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            UserRetrieveByIDResponse,
            await self._get(
                f"/user/{account_id}",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, UserRetrieveByIDResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_hovercard(
        self,
        username: str,
        *,
        subject_id: str | NotGiven = NOT_GIVEN,
        subject_type: Literal["organization", "repository", "issue", "pull_request"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveHovercardResponse:
        """Provides hovercard information.

        You can find out more about someone in relation
        to their pull requests, issues, repositories, and organizations.

        The `subject_type` and `subject_id` parameters provide context for the person's
        hovercard, which returns more information than without the parameters. For
        example, if you wanted to find out more about `octocat` who owns the
        `Spoon-Knife` repository, you would use a `subject_type` value of `repository`
        and a `subject_id` value of `1300192` (the ID of the `Spoon-Knife` repository).

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          subject_id: Uses the ID for the `subject_type` you specified. **Required** when using
              `subject_type`.

          subject_type: Identifies which additional information you'd like to receive about the person's
              hovercard. Can be `organization`, `repository`, `issue`, `pull_request`.
              **Required** when using `subject_id`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/hovercard",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "subject_id": subject_id,
                        "subject_type": subject_type,
                    },
                    user_retrieve_hovercard_params.UserRetrieveHovercardParams,
                ),
            ),
            cast_to=UserRetrieveHovercardResponse,
        )

    async def retrieve_installation(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Installation:
        """
        Enables an authenticated GitHub App to find the user’s installation information.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/installation",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Installation,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.create_project = to_raw_response_wrapper(
            users.create_project,
        )
        self.list_attestations = to_raw_response_wrapper(
            users.list_attestations,
        )
        self.list_followers_0 = to_raw_response_wrapper(
            users.list_followers_0,
        )
        self.list_followers_1 = to_raw_response_wrapper(
            users.list_followers_1,
        )
        self.list_gists = to_raw_response_wrapper(
            users.list_gists,
        )
        self.list_gpg_keys = to_raw_response_wrapper(
            users.list_gpg_keys,
        )
        self.list_issues = to_raw_response_wrapper(
            users.list_issues,
        )
        self.list_organizations_0 = to_raw_response_wrapper(
            users.list_organizations_0,
        )
        self.list_organizations_1 = to_raw_response_wrapper(
            users.list_organizations_1,
        )
        self.list_projects = to_raw_response_wrapper(
            users.list_projects,
        )
        self.list_public_emails = to_raw_response_wrapper(
            users.list_public_emails,
        )
        self.list_public_keys = to_raw_response_wrapper(
            users.list_public_keys,
        )
        self.list_repositories = to_raw_response_wrapper(
            users.list_repositories,
        )
        self.list_social_accounts = to_raw_response_wrapper(
            users.list_social_accounts,
        )
        self.list_ssh_signing_keys = to_raw_response_wrapper(
            users.list_ssh_signing_keys,
        )
        self.list_starred_repositories = to_raw_response_wrapper(
            users.list_starred_repositories,
        )
        self.list_subscriptions_0 = to_raw_response_wrapper(
            users.list_subscriptions_0,
        )
        self.list_subscriptions_1 = to_raw_response_wrapper(
            users.list_subscriptions_1,
        )
        self.list_teams = to_raw_response_wrapper(
            users.list_teams,
        )
        self.retrieve_0 = to_raw_response_wrapper(
            users.retrieve_0,
        )
        self.retrieve_1 = to_raw_response_wrapper(
            users.retrieve_1,
        )
        self.retrieve_by_id = to_raw_response_wrapper(
            users.retrieve_by_id,
        )
        self.retrieve_hovercard = to_raw_response_wrapper(
            users.retrieve_hovercard,
        )
        self.retrieve_installation = to_raw_response_wrapper(
            users.retrieve_installation,
        )

    @cached_property
    def blocks(self) -> BlocksResourceWithRawResponse:
        return BlocksResourceWithRawResponse(self._users.blocks)

    @cached_property
    def codespaces(self) -> CodespacesResourceWithRawResponse:
        return CodespacesResourceWithRawResponse(self._users.codespaces)

    @cached_property
    def email(self) -> EmailResourceWithRawResponse:
        return EmailResourceWithRawResponse(self._users.email)

    @cached_property
    def emails(self) -> EmailsResourceWithRawResponse:
        return EmailsResourceWithRawResponse(self._users.emails)

    @cached_property
    def gpg_keys(self) -> GpgKeysResourceWithRawResponse:
        return GpgKeysResourceWithRawResponse(self._users.gpg_keys)

    @cached_property
    def installations(self) -> InstallationsResourceWithRawResponse:
        return InstallationsResourceWithRawResponse(self._users.installations)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResourceWithRawResponse:
        return InteractionLimitsResourceWithRawResponse(self._users.interaction_limits)

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._users.keys)

    @cached_property
    def marketplace_purchases(self) -> MarketplacePurchasesResourceWithRawResponse:
        return MarketplacePurchasesResourceWithRawResponse(self._users.marketplace_purchases)

    @cached_property
    def memberships(self) -> MembershipsResourceWithRawResponse:
        return MembershipsResourceWithRawResponse(self._users.memberships)

    @cached_property
    def migrations(self) -> MigrationsResourceWithRawResponse:
        return MigrationsResourceWithRawResponse(self._users.migrations)

    @cached_property
    def repos(self) -> ReposResourceWithRawResponse:
        return ReposResourceWithRawResponse(self._users.repos)

    @cached_property
    def repository_invitations(self) -> RepositoryInvitationsResourceWithRawResponse:
        return RepositoryInvitationsResourceWithRawResponse(self._users.repository_invitations)

    @cached_property
    def social_accounts(self) -> SocialAccountsResourceWithRawResponse:
        return SocialAccountsResourceWithRawResponse(self._users.social_accounts)

    @cached_property
    def ssh_signing_keys(self) -> SSHSigningKeysResourceWithRawResponse:
        return SSHSigningKeysResourceWithRawResponse(self._users.ssh_signing_keys)

    @cached_property
    def starred(self) -> StarredResourceWithRawResponse:
        return StarredResourceWithRawResponse(self._users.starred)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._users.events)

    @cached_property
    def received_events(self) -> ReceivedEventsResourceWithRawResponse:
        return ReceivedEventsResourceWithRawResponse(self._users.received_events)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._users.settings)

    @cached_property
    def docker(self) -> DockerResourceWithRawResponse:
        return DockerResourceWithRawResponse(self._users.docker)

    @cached_property
    def following(self) -> FollowingResourceWithRawResponse:
        return FollowingResourceWithRawResponse(self._users.following)

    @cached_property
    def packages(self) -> PackagesResourceWithRawResponse:
        return PackagesResourceWithRawResponse(self._users.packages)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.create_project = async_to_raw_response_wrapper(
            users.create_project,
        )
        self.list_attestations = async_to_raw_response_wrapper(
            users.list_attestations,
        )
        self.list_followers_0 = async_to_raw_response_wrapper(
            users.list_followers_0,
        )
        self.list_followers_1 = async_to_raw_response_wrapper(
            users.list_followers_1,
        )
        self.list_gists = async_to_raw_response_wrapper(
            users.list_gists,
        )
        self.list_gpg_keys = async_to_raw_response_wrapper(
            users.list_gpg_keys,
        )
        self.list_issues = async_to_raw_response_wrapper(
            users.list_issues,
        )
        self.list_organizations_0 = async_to_raw_response_wrapper(
            users.list_organizations_0,
        )
        self.list_organizations_1 = async_to_raw_response_wrapper(
            users.list_organizations_1,
        )
        self.list_projects = async_to_raw_response_wrapper(
            users.list_projects,
        )
        self.list_public_emails = async_to_raw_response_wrapper(
            users.list_public_emails,
        )
        self.list_public_keys = async_to_raw_response_wrapper(
            users.list_public_keys,
        )
        self.list_repositories = async_to_raw_response_wrapper(
            users.list_repositories,
        )
        self.list_social_accounts = async_to_raw_response_wrapper(
            users.list_social_accounts,
        )
        self.list_ssh_signing_keys = async_to_raw_response_wrapper(
            users.list_ssh_signing_keys,
        )
        self.list_starred_repositories = async_to_raw_response_wrapper(
            users.list_starred_repositories,
        )
        self.list_subscriptions_0 = async_to_raw_response_wrapper(
            users.list_subscriptions_0,
        )
        self.list_subscriptions_1 = async_to_raw_response_wrapper(
            users.list_subscriptions_1,
        )
        self.list_teams = async_to_raw_response_wrapper(
            users.list_teams,
        )
        self.retrieve_0 = async_to_raw_response_wrapper(
            users.retrieve_0,
        )
        self.retrieve_1 = async_to_raw_response_wrapper(
            users.retrieve_1,
        )
        self.retrieve_by_id = async_to_raw_response_wrapper(
            users.retrieve_by_id,
        )
        self.retrieve_hovercard = async_to_raw_response_wrapper(
            users.retrieve_hovercard,
        )
        self.retrieve_installation = async_to_raw_response_wrapper(
            users.retrieve_installation,
        )

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithRawResponse:
        return AsyncBlocksResourceWithRawResponse(self._users.blocks)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResourceWithRawResponse:
        return AsyncCodespacesResourceWithRawResponse(self._users.codespaces)

    @cached_property
    def email(self) -> AsyncEmailResourceWithRawResponse:
        return AsyncEmailResourceWithRawResponse(self._users.email)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithRawResponse:
        return AsyncEmailsResourceWithRawResponse(self._users.emails)

    @cached_property
    def gpg_keys(self) -> AsyncGpgKeysResourceWithRawResponse:
        return AsyncGpgKeysResourceWithRawResponse(self._users.gpg_keys)

    @cached_property
    def installations(self) -> AsyncInstallationsResourceWithRawResponse:
        return AsyncInstallationsResourceWithRawResponse(self._users.installations)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResourceWithRawResponse:
        return AsyncInteractionLimitsResourceWithRawResponse(self._users.interaction_limits)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._users.keys)

    @cached_property
    def marketplace_purchases(self) -> AsyncMarketplacePurchasesResourceWithRawResponse:
        return AsyncMarketplacePurchasesResourceWithRawResponse(self._users.marketplace_purchases)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithRawResponse:
        return AsyncMembershipsResourceWithRawResponse(self._users.memberships)

    @cached_property
    def migrations(self) -> AsyncMigrationsResourceWithRawResponse:
        return AsyncMigrationsResourceWithRawResponse(self._users.migrations)

    @cached_property
    def repos(self) -> AsyncReposResourceWithRawResponse:
        return AsyncReposResourceWithRawResponse(self._users.repos)

    @cached_property
    def repository_invitations(self) -> AsyncRepositoryInvitationsResourceWithRawResponse:
        return AsyncRepositoryInvitationsResourceWithRawResponse(self._users.repository_invitations)

    @cached_property
    def social_accounts(self) -> AsyncSocialAccountsResourceWithRawResponse:
        return AsyncSocialAccountsResourceWithRawResponse(self._users.social_accounts)

    @cached_property
    def ssh_signing_keys(self) -> AsyncSSHSigningKeysResourceWithRawResponse:
        return AsyncSSHSigningKeysResourceWithRawResponse(self._users.ssh_signing_keys)

    @cached_property
    def starred(self) -> AsyncStarredResourceWithRawResponse:
        return AsyncStarredResourceWithRawResponse(self._users.starred)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._users.events)

    @cached_property
    def received_events(self) -> AsyncReceivedEventsResourceWithRawResponse:
        return AsyncReceivedEventsResourceWithRawResponse(self._users.received_events)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._users.settings)

    @cached_property
    def docker(self) -> AsyncDockerResourceWithRawResponse:
        return AsyncDockerResourceWithRawResponse(self._users.docker)

    @cached_property
    def following(self) -> AsyncFollowingResourceWithRawResponse:
        return AsyncFollowingResourceWithRawResponse(self._users.following)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithRawResponse:
        return AsyncPackagesResourceWithRawResponse(self._users.packages)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.create_project = to_streamed_response_wrapper(
            users.create_project,
        )
        self.list_attestations = to_streamed_response_wrapper(
            users.list_attestations,
        )
        self.list_followers_0 = to_streamed_response_wrapper(
            users.list_followers_0,
        )
        self.list_followers_1 = to_streamed_response_wrapper(
            users.list_followers_1,
        )
        self.list_gists = to_streamed_response_wrapper(
            users.list_gists,
        )
        self.list_gpg_keys = to_streamed_response_wrapper(
            users.list_gpg_keys,
        )
        self.list_issues = to_streamed_response_wrapper(
            users.list_issues,
        )
        self.list_organizations_0 = to_streamed_response_wrapper(
            users.list_organizations_0,
        )
        self.list_organizations_1 = to_streamed_response_wrapper(
            users.list_organizations_1,
        )
        self.list_projects = to_streamed_response_wrapper(
            users.list_projects,
        )
        self.list_public_emails = to_streamed_response_wrapper(
            users.list_public_emails,
        )
        self.list_public_keys = to_streamed_response_wrapper(
            users.list_public_keys,
        )
        self.list_repositories = to_streamed_response_wrapper(
            users.list_repositories,
        )
        self.list_social_accounts = to_streamed_response_wrapper(
            users.list_social_accounts,
        )
        self.list_ssh_signing_keys = to_streamed_response_wrapper(
            users.list_ssh_signing_keys,
        )
        self.list_starred_repositories = to_streamed_response_wrapper(
            users.list_starred_repositories,
        )
        self.list_subscriptions_0 = to_streamed_response_wrapper(
            users.list_subscriptions_0,
        )
        self.list_subscriptions_1 = to_streamed_response_wrapper(
            users.list_subscriptions_1,
        )
        self.list_teams = to_streamed_response_wrapper(
            users.list_teams,
        )
        self.retrieve_0 = to_streamed_response_wrapper(
            users.retrieve_0,
        )
        self.retrieve_1 = to_streamed_response_wrapper(
            users.retrieve_1,
        )
        self.retrieve_by_id = to_streamed_response_wrapper(
            users.retrieve_by_id,
        )
        self.retrieve_hovercard = to_streamed_response_wrapper(
            users.retrieve_hovercard,
        )
        self.retrieve_installation = to_streamed_response_wrapper(
            users.retrieve_installation,
        )

    @cached_property
    def blocks(self) -> BlocksResourceWithStreamingResponse:
        return BlocksResourceWithStreamingResponse(self._users.blocks)

    @cached_property
    def codespaces(self) -> CodespacesResourceWithStreamingResponse:
        return CodespacesResourceWithStreamingResponse(self._users.codespaces)

    @cached_property
    def email(self) -> EmailResourceWithStreamingResponse:
        return EmailResourceWithStreamingResponse(self._users.email)

    @cached_property
    def emails(self) -> EmailsResourceWithStreamingResponse:
        return EmailsResourceWithStreamingResponse(self._users.emails)

    @cached_property
    def gpg_keys(self) -> GpgKeysResourceWithStreamingResponse:
        return GpgKeysResourceWithStreamingResponse(self._users.gpg_keys)

    @cached_property
    def installations(self) -> InstallationsResourceWithStreamingResponse:
        return InstallationsResourceWithStreamingResponse(self._users.installations)

    @cached_property
    def interaction_limits(self) -> InteractionLimitsResourceWithStreamingResponse:
        return InteractionLimitsResourceWithStreamingResponse(self._users.interaction_limits)

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._users.keys)

    @cached_property
    def marketplace_purchases(self) -> MarketplacePurchasesResourceWithStreamingResponse:
        return MarketplacePurchasesResourceWithStreamingResponse(self._users.marketplace_purchases)

    @cached_property
    def memberships(self) -> MembershipsResourceWithStreamingResponse:
        return MembershipsResourceWithStreamingResponse(self._users.memberships)

    @cached_property
    def migrations(self) -> MigrationsResourceWithStreamingResponse:
        return MigrationsResourceWithStreamingResponse(self._users.migrations)

    @cached_property
    def repos(self) -> ReposResourceWithStreamingResponse:
        return ReposResourceWithStreamingResponse(self._users.repos)

    @cached_property
    def repository_invitations(self) -> RepositoryInvitationsResourceWithStreamingResponse:
        return RepositoryInvitationsResourceWithStreamingResponse(self._users.repository_invitations)

    @cached_property
    def social_accounts(self) -> SocialAccountsResourceWithStreamingResponse:
        return SocialAccountsResourceWithStreamingResponse(self._users.social_accounts)

    @cached_property
    def ssh_signing_keys(self) -> SSHSigningKeysResourceWithStreamingResponse:
        return SSHSigningKeysResourceWithStreamingResponse(self._users.ssh_signing_keys)

    @cached_property
    def starred(self) -> StarredResourceWithStreamingResponse:
        return StarredResourceWithStreamingResponse(self._users.starred)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._users.events)

    @cached_property
    def received_events(self) -> ReceivedEventsResourceWithStreamingResponse:
        return ReceivedEventsResourceWithStreamingResponse(self._users.received_events)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._users.settings)

    @cached_property
    def docker(self) -> DockerResourceWithStreamingResponse:
        return DockerResourceWithStreamingResponse(self._users.docker)

    @cached_property
    def following(self) -> FollowingResourceWithStreamingResponse:
        return FollowingResourceWithStreamingResponse(self._users.following)

    @cached_property
    def packages(self) -> PackagesResourceWithStreamingResponse:
        return PackagesResourceWithStreamingResponse(self._users.packages)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.create_project = async_to_streamed_response_wrapper(
            users.create_project,
        )
        self.list_attestations = async_to_streamed_response_wrapper(
            users.list_attestations,
        )
        self.list_followers_0 = async_to_streamed_response_wrapper(
            users.list_followers_0,
        )
        self.list_followers_1 = async_to_streamed_response_wrapper(
            users.list_followers_1,
        )
        self.list_gists = async_to_streamed_response_wrapper(
            users.list_gists,
        )
        self.list_gpg_keys = async_to_streamed_response_wrapper(
            users.list_gpg_keys,
        )
        self.list_issues = async_to_streamed_response_wrapper(
            users.list_issues,
        )
        self.list_organizations_0 = async_to_streamed_response_wrapper(
            users.list_organizations_0,
        )
        self.list_organizations_1 = async_to_streamed_response_wrapper(
            users.list_organizations_1,
        )
        self.list_projects = async_to_streamed_response_wrapper(
            users.list_projects,
        )
        self.list_public_emails = async_to_streamed_response_wrapper(
            users.list_public_emails,
        )
        self.list_public_keys = async_to_streamed_response_wrapper(
            users.list_public_keys,
        )
        self.list_repositories = async_to_streamed_response_wrapper(
            users.list_repositories,
        )
        self.list_social_accounts = async_to_streamed_response_wrapper(
            users.list_social_accounts,
        )
        self.list_ssh_signing_keys = async_to_streamed_response_wrapper(
            users.list_ssh_signing_keys,
        )
        self.list_starred_repositories = async_to_streamed_response_wrapper(
            users.list_starred_repositories,
        )
        self.list_subscriptions_0 = async_to_streamed_response_wrapper(
            users.list_subscriptions_0,
        )
        self.list_subscriptions_1 = async_to_streamed_response_wrapper(
            users.list_subscriptions_1,
        )
        self.list_teams = async_to_streamed_response_wrapper(
            users.list_teams,
        )
        self.retrieve_0 = async_to_streamed_response_wrapper(
            users.retrieve_0,
        )
        self.retrieve_1 = async_to_streamed_response_wrapper(
            users.retrieve_1,
        )
        self.retrieve_by_id = async_to_streamed_response_wrapper(
            users.retrieve_by_id,
        )
        self.retrieve_hovercard = async_to_streamed_response_wrapper(
            users.retrieve_hovercard,
        )
        self.retrieve_installation = async_to_streamed_response_wrapper(
            users.retrieve_installation,
        )

    @cached_property
    def blocks(self) -> AsyncBlocksResourceWithStreamingResponse:
        return AsyncBlocksResourceWithStreamingResponse(self._users.blocks)

    @cached_property
    def codespaces(self) -> AsyncCodespacesResourceWithStreamingResponse:
        return AsyncCodespacesResourceWithStreamingResponse(self._users.codespaces)

    @cached_property
    def email(self) -> AsyncEmailResourceWithStreamingResponse:
        return AsyncEmailResourceWithStreamingResponse(self._users.email)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithStreamingResponse:
        return AsyncEmailsResourceWithStreamingResponse(self._users.emails)

    @cached_property
    def gpg_keys(self) -> AsyncGpgKeysResourceWithStreamingResponse:
        return AsyncGpgKeysResourceWithStreamingResponse(self._users.gpg_keys)

    @cached_property
    def installations(self) -> AsyncInstallationsResourceWithStreamingResponse:
        return AsyncInstallationsResourceWithStreamingResponse(self._users.installations)

    @cached_property
    def interaction_limits(self) -> AsyncInteractionLimitsResourceWithStreamingResponse:
        return AsyncInteractionLimitsResourceWithStreamingResponse(self._users.interaction_limits)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._users.keys)

    @cached_property
    def marketplace_purchases(self) -> AsyncMarketplacePurchasesResourceWithStreamingResponse:
        return AsyncMarketplacePurchasesResourceWithStreamingResponse(self._users.marketplace_purchases)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self._users.memberships)

    @cached_property
    def migrations(self) -> AsyncMigrationsResourceWithStreamingResponse:
        return AsyncMigrationsResourceWithStreamingResponse(self._users.migrations)

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._users.repos)

    @cached_property
    def repository_invitations(self) -> AsyncRepositoryInvitationsResourceWithStreamingResponse:
        return AsyncRepositoryInvitationsResourceWithStreamingResponse(self._users.repository_invitations)

    @cached_property
    def social_accounts(self) -> AsyncSocialAccountsResourceWithStreamingResponse:
        return AsyncSocialAccountsResourceWithStreamingResponse(self._users.social_accounts)

    @cached_property
    def ssh_signing_keys(self) -> AsyncSSHSigningKeysResourceWithStreamingResponse:
        return AsyncSSHSigningKeysResourceWithStreamingResponse(self._users.ssh_signing_keys)

    @cached_property
    def starred(self) -> AsyncStarredResourceWithStreamingResponse:
        return AsyncStarredResourceWithStreamingResponse(self._users.starred)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._users.events)

    @cached_property
    def received_events(self) -> AsyncReceivedEventsResourceWithStreamingResponse:
        return AsyncReceivedEventsResourceWithStreamingResponse(self._users.received_events)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._users.settings)

    @cached_property
    def docker(self) -> AsyncDockerResourceWithStreamingResponse:
        return AsyncDockerResourceWithStreamingResponse(self._users.docker)

    @cached_property
    def following(self) -> AsyncFollowingResourceWithStreamingResponse:
        return AsyncFollowingResourceWithStreamingResponse(self._users.following)

    @cached_property
    def packages(self) -> AsyncPackagesResourceWithStreamingResponse:
        return AsyncPackagesResourceWithStreamingResponse(self._users.packages)
