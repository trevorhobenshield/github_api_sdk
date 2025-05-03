from __future__ import annotations

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....types.orgs.organization_role import OrganizationRole
from ....types.orgs.organization_role_list_response import OrganizationRoleListResponse
from .teams import (
    AsyncTeamsResource,
    AsyncTeamsResourceWithRawResponse,
    AsyncTeamsResourceWithStreamingResponse,
    TeamsResource,
    TeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
)
from .users import (
    AsyncUsersResource,
    AsyncUsersResourceWithRawResponse,
    AsyncUsersResourceWithStreamingResponse,
    UsersResource,
    UsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
)

__all__ = ["OrganizationRolesResource", "AsyncOrganizationRolesResource"]


class OrganizationRolesResource(SyncAPIResource):
    @cached_property
    def teams(self) -> TeamsResource:
        return TeamsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return OrganizationRolesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        role_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRole:
        """Gets an organization role that is available to this organization.

        For more
        information on organization roles, see
        "[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles)."

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permissions of
          `read_organization_custom_org_role` in the organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/organization-roles/{role_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationRole,
        )

    def list(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRoleListResponse:
        """Lists the organization roles available in this organization.

        For more
        information on organization roles, see
        "[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles)."

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permissions of
          `read_organization_custom_org_role` in the organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/organization-roles",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationRoleListResponse,
        )


class AsyncOrganizationRolesResource(AsyncAPIResource):
    @cached_property
    def teams(self) -> AsyncTeamsResource:
        return AsyncTeamsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationRolesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationRolesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationRolesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncOrganizationRolesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        role_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRole:
        """Gets an organization role that is available to this organization.

        For more
        information on organization roles, see
        "[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles)."

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permissions of
          `read_organization_custom_org_role` in the organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/organization-roles/{role_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationRole,
        )

    async def list(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRoleListResponse:
        """Lists the organization roles available in this organization.

        For more
        information on organization roles, see
        "[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles)."

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permissions of
          `read_organization_custom_org_role` in the organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/organization-roles",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationRoleListResponse,
        )


class OrganizationRolesResourceWithRawResponse:
    def __init__(self, organization_roles: OrganizationRolesResource) -> None:
        self._organization_roles = organization_roles

        self.retrieve = to_raw_response_wrapper(
            organization_roles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            organization_roles.list,
        )

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self._organization_roles.teams)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._organization_roles.users)


class AsyncOrganizationRolesResourceWithRawResponse:
    def __init__(self, organization_roles: AsyncOrganizationRolesResource) -> None:
        self._organization_roles = organization_roles

        self.retrieve = async_to_raw_response_wrapper(
            organization_roles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            organization_roles.list,
        )

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self._organization_roles.teams)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._organization_roles.users)


class OrganizationRolesResourceWithStreamingResponse:
    def __init__(self, organization_roles: OrganizationRolesResource) -> None:
        self._organization_roles = organization_roles

        self.retrieve = to_streamed_response_wrapper(
            organization_roles.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            organization_roles.list,
        )

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self._organization_roles.teams)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._organization_roles.users)


class AsyncOrganizationRolesResourceWithStreamingResponse:
    def __init__(self, organization_roles: AsyncOrganizationRolesResource) -> None:
        self._organization_roles = organization_roles

        self.retrieve = async_to_streamed_response_wrapper(
            organization_roles.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            organization_roles.list,
        )

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self._organization_roles.teams)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._organization_roles.users)
