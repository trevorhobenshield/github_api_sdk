from __future__ import annotations

from typing import Iterable

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
from ...types.orgs import invitation_create_params, invitation_list_params, invitation_list_teams_params
from ...types.orgs.invitation import Invitation
from ...types.orgs.invitation_list_response import InvitationListResponse
from ...types.orgs.invitation_list_teams_response import InvitationListTeamsResponse

__all__ = ["InvitationsResource", "AsyncInvitationsResource"]


class InvitationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return InvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return InvitationsResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        email: str | NotGiven = NOT_GIVEN,
        invitee_id: int | NotGiven = NOT_GIVEN,
        role: Literal["admin", "direct_member", "billing_manager", "reinstate"] | NotGiven = NOT_GIVEN,
        team_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invitation:
        """
        Invite people to an organization by using their GitHub user ID or their email
        address. In order to create invitations in an organization, the authenticated
        user must be an organization owner.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Args:
          email: **Required unless you provide `invitee_id`**. Email address of the person you
              are inviting, which can be an existing GitHub user.

          invitee_id: **Required unless you provide `email`**. GitHub user ID for the person you are
              inviting.

          role: The role for the new member.

              - `admin` - Organization owners with full administrative rights to the
                organization and complete access to all repositories and teams.
              - `direct_member` - Non-owner organization members with ability to see other
                members and join teams by invitation.
              - `billing_manager` - Non-owner organization members with ability to manage the
                billing settings of your organization.
              - `reinstate` - The previous role assigned to the invitee before they were
                removed from your organization. Can be one of the roles listed above. Only
                works if the invitee was previously part of your organization.

          team_ids: Specify IDs for the teams you want to invite new members to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/invitations",
            body=maybe_transform(
                {
                    "email": email,
                    "invitee_id": invitee_id,
                    "role": role,
                    "team_ids": team_ids,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Invitation,
        )

    def list(
        self,
        org: str,
        *,
        invitation_source: Literal["all", "member", "scim"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        role: Literal["all", "admin", "direct_member", "billing_manager", "hiring_manager"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvitationListResponse:
        """
        The return hash contains a `role` field which refers to the Organization
        Invitation role and will be one of the following values: `direct_member`,
        `admin`, `billing_manager`, or `hiring_manager`. If the invitee is not a GitHub
        member, the `login` field in the return hash will be `null`.

        Args:
          invitation_source: Filter invitations by their invitation source.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          role: Filter invitations by their member role.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/invitations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "invitation_source": invitation_source,
                        "page": page,
                        "per_page": per_page,
                        "role": role,
                    },
                    invitation_list_params.InvitationListParams,
                ),
            ),
            cast_to=InvitationListResponse,
        )

    def cancel(
        self,
        invitation_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Cancel an organization invitation.

        In order to cancel an organization
        invitation, the authenticated user must be an organization owner.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/invitations/{invitation_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_teams(
        self,
        invitation_id: int,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvitationListTeamsResponse:
        """List all teams associated with an invitation.

        In order to see invitations in an
        organization, the authenticated user must be an organization owner.

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
            f"/orgs/{org}/invitations/{invitation_id}/teams",
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
                    invitation_list_teams_params.InvitationListTeamsParams,
                ),
            ),
            cast_to=InvitationListTeamsResponse,
        )


class AsyncInvitationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncInvitationsResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        email: str | NotGiven = NOT_GIVEN,
        invitee_id: int | NotGiven = NOT_GIVEN,
        role: Literal["admin", "direct_member", "billing_manager", "reinstate"] | NotGiven = NOT_GIVEN,
        team_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invitation:
        """
        Invite people to an organization by using their GitHub user ID or their email
        address. In order to create invitations in an organization, the authenticated
        user must be an organization owner.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Args:
          email: **Required unless you provide `invitee_id`**. Email address of the person you
              are inviting, which can be an existing GitHub user.

          invitee_id: **Required unless you provide `email`**. GitHub user ID for the person you are
              inviting.

          role: The role for the new member.

              - `admin` - Organization owners with full administrative rights to the
                organization and complete access to all repositories and teams.
              - `direct_member` - Non-owner organization members with ability to see other
                members and join teams by invitation.
              - `billing_manager` - Non-owner organization members with ability to manage the
                billing settings of your organization.
              - `reinstate` - The previous role assigned to the invitee before they were
                removed from your organization. Can be one of the roles listed above. Only
                works if the invitee was previously part of your organization.

          team_ids: Specify IDs for the teams you want to invite new members to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/invitations",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "invitee_id": invitee_id,
                    "role": role,
                    "team_ids": team_ids,
                },
                invitation_create_params.InvitationCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Invitation,
        )

    async def list(
        self,
        org: str,
        *,
        invitation_source: Literal["all", "member", "scim"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        role: Literal["all", "admin", "direct_member", "billing_manager", "hiring_manager"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvitationListResponse:
        """
        The return hash contains a `role` field which refers to the Organization
        Invitation role and will be one of the following values: `direct_member`,
        `admin`, `billing_manager`, or `hiring_manager`. If the invitee is not a GitHub
        member, the `login` field in the return hash will be `null`.

        Args:
          invitation_source: Filter invitations by their invitation source.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          role: Filter invitations by their member role.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/invitations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "invitation_source": invitation_source,
                        "page": page,
                        "per_page": per_page,
                        "role": role,
                    },
                    invitation_list_params.InvitationListParams,
                ),
            ),
            cast_to=InvitationListResponse,
        )

    async def cancel(
        self,
        invitation_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Cancel an organization invitation.

        In order to cancel an organization
        invitation, the authenticated user must be an organization owner.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/invitations/{invitation_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_teams(
        self,
        invitation_id: int,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvitationListTeamsResponse:
        """List all teams associated with an invitation.

        In order to see invitations in an
        organization, the authenticated user must be an organization owner.

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
            f"/orgs/{org}/invitations/{invitation_id}/teams",
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
                    invitation_list_teams_params.InvitationListTeamsParams,
                ),
            ),
            cast_to=InvitationListTeamsResponse,
        )


class InvitationsResourceWithRawResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.create = to_raw_response_wrapper(
            invitations.create,
        )
        self.list = to_raw_response_wrapper(
            invitations.list,
        )
        self.cancel = to_raw_response_wrapper(
            invitations.cancel,
        )
        self.list_teams = to_raw_response_wrapper(
            invitations.list_teams,
        )


class AsyncInvitationsResourceWithRawResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.create = async_to_raw_response_wrapper(
            invitations.create,
        )
        self.list = async_to_raw_response_wrapper(
            invitations.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            invitations.cancel,
        )
        self.list_teams = async_to_raw_response_wrapper(
            invitations.list_teams,
        )


class InvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: InvitationsResource) -> None:
        self._invitations = invitations

        self.create = to_streamed_response_wrapper(
            invitations.create,
        )
        self.list = to_streamed_response_wrapper(
            invitations.list,
        )
        self.cancel = to_streamed_response_wrapper(
            invitations.cancel,
        )
        self.list_teams = to_streamed_response_wrapper(
            invitations.list_teams,
        )


class AsyncInvitationsResourceWithStreamingResponse:
    def __init__(self, invitations: AsyncInvitationsResource) -> None:
        self._invitations = invitations

        self.create = async_to_streamed_response_wrapper(
            invitations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            invitations.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            invitations.cancel,
        )
        self.list_teams = async_to_streamed_response_wrapper(
            invitations.list_teams,
        )
