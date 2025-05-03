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
from ...types.teams import member_list_params
from ...types.teams.member_list_response import MemberListResponse

__all__ = ["MembersResource", "AsyncMembersResource"]


class MembersResource(SyncAPIResource):
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

    def retrieve(
        self,
        username: str,
        *,
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The "Get team member" endpoint (described below) is closing down.

        We recommend using the
        [Get team membership for a user](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user)
        endpoint instead. It allows you to get both active and pending memberships.

        To list members in a team, the team must be visible to the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/teams/{team_id}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        role: Literal["member", "maintainer", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemberListResponse:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`List team members`](https://docs.github.com/rest/teams/members#list-team-members)
        > endpoint.

        Team members will include the members of child teams.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          role: Filters members returned by their role in the team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/teams/{team_id}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "role": role,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    def add(
        self,
        username: str,
        *,
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The "Add team member" endpoint (described below) is closing down.

        We recommend using the
        [Add or update team membership for a user](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user)
        endpoint instead. It allows you to invite new organization members to your
        teams.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To add someone to a team, the authenticated user must be an organization owner
        or a team maintainer in the team they're changing. The person being added to the
        team must be a member of the team's organization.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        Note that you'll need to set `Content-Length` to zero when calling out to this
        endpoint. For more information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/teams/{team_id}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def remove(
        self,
        username: str,
        *,
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The "Remove team member" endpoint (described below) is closing down.

        We recommend using the
        [Remove team membership for a user](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user)
        endpoint instead. It allows you to remove both active and pending memberships.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To remove a team member, the authenticated user must have 'admin' permissions to
        the team or be an owner of the org that the team is associated with. Removing a
        team member does not delete the user, it just removes them from the team.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/teams/{team_id}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncMembersResource(AsyncAPIResource):
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

    async def retrieve(
        self,
        username: str,
        *,
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The "Get team member" endpoint (described below) is closing down.

        We recommend using the
        [Get team membership for a user](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user)
        endpoint instead. It allows you to get both active and pending memberships.

        To list members in a team, the team must be visible to the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/teams/{team_id}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        role: Literal["member", "maintainer", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemberListResponse:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`List team members`](https://docs.github.com/rest/teams/members#list-team-members)
        > endpoint.

        Team members will include the members of child teams.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          role: Filters members returned by their role in the team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/teams/{team_id}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "role": role,
                    },
                    member_list_params.MemberListParams,
                ),
            ),
            cast_to=MemberListResponse,
        )

    async def add(
        self,
        username: str,
        *,
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The "Add team member" endpoint (described below) is closing down.

        We recommend using the
        [Add or update team membership for a user](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user)
        endpoint instead. It allows you to invite new organization members to your
        teams.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To add someone to a team, the authenticated user must be an organization owner
        or a team maintainer in the team they're changing. The person being added to the
        team must be a member of the team's organization.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        Note that you'll need to set `Content-Length` to zero when calling out to this
        endpoint. For more information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/teams/{team_id}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def remove(
        self,
        username: str,
        *,
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        The "Remove team member" endpoint (described below) is closing down.

        We recommend using the
        [Remove team membership for a user](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user)
        endpoint instead. It allows you to remove both active and pending memberships.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To remove a team member, the authenticated user must have 'admin' permissions to
        the team or be an owner of the org that the team is associated with. Removing a
        team member does not delete the user, it just removes them from the team.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/teams/{team_id}/members/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class MembersResourceWithRawResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.retrieve = to_raw_response_wrapper(
            members.retrieve,
        )
        self.list = to_raw_response_wrapper(
            members.list,
        )
        self.add = to_raw_response_wrapper(
            members.add,
        )
        self.remove = to_raw_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithRawResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.retrieve = async_to_raw_response_wrapper(
            members.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            members.list,
        )
        self.add = async_to_raw_response_wrapper(
            members.add,
        )
        self.remove = async_to_raw_response_wrapper(
            members.remove,
        )


class MembersResourceWithStreamingResponse:
    def __init__(self, members: MembersResource) -> None:
        self._members = members

        self.retrieve = to_streamed_response_wrapper(
            members.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            members.list,
        )
        self.add = to_streamed_response_wrapper(
            members.add,
        )
        self.remove = to_streamed_response_wrapper(
            members.remove,
        )


class AsyncMembersResourceWithStreamingResponse:
    def __init__(self, members: AsyncMembersResource) -> None:
        self._members = members

        self.retrieve = async_to_streamed_response_wrapper(
            members.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            members.list,
        )
        self.add = async_to_streamed_response_wrapper(
            members.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            members.remove,
        )
