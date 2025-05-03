from __future__ import annotations

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
from ...types.orgs import membership_update_params
from ...types.orgs.org_membership import OrgMembership

__all__ = ["MembershipsResource", "AsyncMembershipsResource"]


class MembershipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MembershipsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        username: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgMembership:
        """
        In order to get a user's membership with an organization, the authenticated user
        must be an organization member. The `state` parameter in the response can be
        used to identify the user's membership status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/orgs/{org}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgMembership,
        )

    def update(
        self,
        username: str,
        *,
        org: str,
        role: Literal["admin", "member"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgMembership:
        """
        Only authenticated organization owners can add a member to the organization or
        update the member's role.

        - If the authenticated user is _adding_ a member to the organization, the
          invited user will receive an email inviting them to the organization. The
          user's
          [membership status](https://docs.github.com/rest/orgs/members#get-organization-membership-for-a-user)
          will be `pending` until they accept the invitation.
        - Authenticated users can _update_ a user's membership by passing the `role`
          parameter. If the authenticated user changes a member's role to `admin`, the
          affected user will receive an email notifying them that they've been made an
          organization owner. If the authenticated user changes an owner's role to
          `member`, no email will be sent.

        **Rate limits**

        To prevent abuse, organization owners are limited to creating 50 organization
        invitations for an organization within a 24 hour period. If the organization is
        more than one month old or on a paid plan, the limit is 500 invitations per 24
        hour period.

        Args:
          role:
              The role to give the user in the organization. Can be one of:

              - `admin` - The user will become an owner of the organization.
              - `member` - The user will become a non-owner member of the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._put(
            f"/orgs/{org}/memberships/{username}",
            body=maybe_transform({"role": role}, membership_update_params.MembershipUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgMembership,
        )

    def remove(
        self,
        username: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        In order to remove a user's membership with an organization, the authenticated
        user must be an organization owner.

        If the specified user is an active member of the organization, this will remove
        them from the organization. If the specified user has been invited to the
        organization, this will cancel their invitation. The specified user will receive
        an email notification in both cases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncMembershipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMembershipsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        username: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgMembership:
        """
        In order to get a user's membership with an organization, the authenticated user
        must be an organization member. The `state` parameter in the response can be
        used to identify the user's membership status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/orgs/{org}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgMembership,
        )

    async def update(
        self,
        username: str,
        *,
        org: str,
        role: Literal["admin", "member"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgMembership:
        """
        Only authenticated organization owners can add a member to the organization or
        update the member's role.

        - If the authenticated user is _adding_ a member to the organization, the
          invited user will receive an email inviting them to the organization. The
          user's
          [membership status](https://docs.github.com/rest/orgs/members#get-organization-membership-for-a-user)
          will be `pending` until they accept the invitation.
        - Authenticated users can _update_ a user's membership by passing the `role`
          parameter. If the authenticated user changes a member's role to `admin`, the
          affected user will receive an email notifying them that they've been made an
          organization owner. If the authenticated user changes an owner's role to
          `member`, no email will be sent.

        **Rate limits**

        To prevent abuse, organization owners are limited to creating 50 organization
        invitations for an organization within a 24 hour period. If the organization is
        more than one month old or on a paid plan, the limit is 500 invitations per 24
        hour period.

        Args:
          role:
              The role to give the user in the organization. Can be one of:

              - `admin` - The user will become an owner of the organization.
              - `member` - The user will become a non-owner member of the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._put(
            f"/orgs/{org}/memberships/{username}",
            body=await async_maybe_transform({"role": role}, membership_update_params.MembershipUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgMembership,
        )

    async def remove(
        self,
        username: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        In order to remove a user's membership with an organization, the authenticated
        user must be an organization owner.

        If the specified user is an active member of the organization, this will remove
        them from the organization. If the specified user has been invited to the
        organization, this will cancel their invitation. The specified user will receive
        an email notification in both cases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class MembershipsResourceWithRawResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = to_raw_response_wrapper(
            memberships.retrieve,
        )
        self.update = to_raw_response_wrapper(
            memberships.update,
        )
        self.remove = to_raw_response_wrapper(
            memberships.remove,
        )


class AsyncMembershipsResourceWithRawResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = async_to_raw_response_wrapper(
            memberships.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            memberships.update,
        )
        self.remove = async_to_raw_response_wrapper(
            memberships.remove,
        )


class MembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = to_streamed_response_wrapper(
            memberships.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            memberships.update,
        )
        self.remove = to_streamed_response_wrapper(
            memberships.remove,
        )


class AsyncMembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = async_to_streamed_response_wrapper(
            memberships.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            memberships.update,
        )
        self.remove = async_to_streamed_response_wrapper(
            memberships.remove,
        )
