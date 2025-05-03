from __future__ import annotations

import httpx
from typing_extensions import Literal

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.orgs import member_list_params
from ....types.orgs.copilot_seat_details import CopilotSeatDetails
from ....types.orgs.member_list_response import MemberListResponse
from .codespaces import (
    AsyncCodespacesResource,
    AsyncCodespacesResourceWithRawResponse,
    AsyncCodespacesResourceWithStreamingResponse,
    CodespacesResource,
    CodespacesResourceWithRawResponse,
    CodespacesResourceWithStreamingResponse,
)

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
    @cached_property
    def codespaces(self) -> CodespacesResource:
        return CodespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> MembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MembersResourceWithStreamingResponse(self)

    def list(
        self,
        org: str,
        *,
        filter: Literal["2fa_disabled", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        role: Literal["all", "admin", "member"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemberListResponse:
        """List all users who are members of an organization.

        If the authenticated user is
        also a member of this organization then both concealed and public members will
        be returned.

        Args:
          filter: Filter members returned in the list. `2fa_disabled` means that only members
              without
              [two-factor authentication](https://github.com/blog/1614-two-factor-authentication)
              enabled will be returned. This options is only available for organization
              owners.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          role: Filter members returned by their role.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "role": role,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    def check_membership(
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
        Check if a user is, publicly or privately, a member of the organization.

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
        return self._get(
            f"/orgs/{org}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_copilot_details(
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
    ) -> CopilotSeatDetails:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Gets the GitHub Copilot seat details for a member of an organization who
        currently has access to GitHub Copilot.

        The seat object contains information about the user's most recent Copilot
        activity. Users must have telemetry enabled in their IDE for Copilot in the IDE
        activity to be reflected in `last_activity_at`. For more information about
        activity data, see
        "[Reviewing user activity data for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization)."

        Only organization owners can view Copilot seat assignment details for members of
        their organization.

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot` or `read:org` scopes to use this endpoint.

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
            f"/orgs/{org}/members/{username}/copilot",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CopilotSeatDetails,
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
        Removing a user from this list will remove them from all teams and they will no
        longer have any access to the organization's repositories.

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
            f"/orgs/{org}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncMembersResource(AsyncAPIResource):
    @cached_property
    def codespaces(self) -> AsyncCodespacesResource:
        return AsyncCodespacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMembersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMembersResourceWithStreamingResponse(self)

    async def list(
        self,
        org: str,
        *,
        filter: Literal["2fa_disabled", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        role: Literal["all", "admin", "member"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemberListResponse:
        """List all users who are members of an organization.

        If the authenticated user is
        also a member of this organization then both concealed and public members will
        be returned.

        Args:
          filter: Filter members returned in the list. `2fa_disabled` means that only members
              without
              [two-factor authentication](https://github.com/blog/1614-two-factor-authentication)
              enabled will be returned. This options is only available for organization
              owners.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          role: Filter members returned by their role.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "role": role,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    async def check_membership(
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
        Check if a user is, publicly or privately, a member of the organization.

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
        return await self._get(
            f"/orgs/{org}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_copilot_details(
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
    ) -> CopilotSeatDetails:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Gets the GitHub Copilot seat details for a member of an organization who
        currently has access to GitHub Copilot.

        The seat object contains information about the user's most recent Copilot
        activity. Users must have telemetry enabled in their IDE for Copilot in the IDE
        activity to be reflected in `last_activity_at`. For more information about
        activity data, see
        "[Reviewing user activity data for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization)."

        Only organization owners can view Copilot seat assignment details for members of
        their organization.

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot` or `read:org` scopes to use this endpoint.

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
            f"/orgs/{org}/members/{username}/copilot",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CopilotSeatDetails,
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
        Removing a user from this list will remove them from all teams and they will no
        longer have any access to the organization's repositories.

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
            f"/orgs/{org}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.check_membership = to_raw_response_wrapper(
            members.check_membership,
        )
        self.get_copilot_details = to_raw_response_wrapper(
            members.get_copilot_details,
        )
        self.remove = to_raw_response_wrapper(
            members.remove,
        )

    @cached_property
    def codespaces(self) -> CodespacesResourceWithRawResponse:
        return CodespacesResourceWithRawResponse(self._members.codespaces)


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.check_membership = async_to_raw_response_wrapper(
            members.check_membership,
        )
        self.get_copilot_details = async_to_raw_response_wrapper(
            members.get_copilot_details,
        )
        self.remove = async_to_raw_response_wrapper(
            members.remove,
        )

    @cached_property
    def codespaces(self) -> AsyncCodespacesResourceWithRawResponse:
        return AsyncCodespacesResourceWithRawResponse(self._members.codespaces)


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.check_membership = to_streamed_response_wrapper(
            members.check_membership,
        )
        self.get_copilot_details = to_streamed_response_wrapper(
            members.get_copilot_details,
        )
        self.remove = to_streamed_response_wrapper(
            members.remove,
        )

    @cached_property
    def codespaces(self) -> CodespacesResourceWithStreamingResponse:
        return CodespacesResourceWithStreamingResponse(self._members.codespaces)


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.check_membership = async_to_streamed_response_wrapper(
            members.check_membership,
        )
        self.get_copilot_details = async_to_streamed_response_wrapper(
            members.get_copilot_details,
        )
        self.remove = async_to_streamed_response_wrapper(
            members.remove,
        )

    @cached_property
    def codespaces(self) -> AsyncCodespacesResourceWithStreamingResponse:
        return AsyncCodespacesResourceWithStreamingResponse(self._members.codespaces)
