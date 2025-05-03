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
from ...types.orgs.teams.team_membership import TeamMembership
from ...types.teams import membership_add_or_update_params

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
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamMembership:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Get team membership for a user](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user)
        > endpoint.

        Team members will include the members of child teams.

        To get a user's membership with a team, the team must be visible to the
        authenticated user.

        **Note:** The response contains the `state` of the membership and the member's
        `role`.

        The `role` for organization owners is set to `maintainer`. For more information
        about `maintainer` roles, see
        [Create a team](https://docs.github.com/rest/teams/teams#create-a-team).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/teams/{team_id}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamMembership,
        )

    def add_or_update(
        self,
        username: str,
        *,
        team_id: int,
        role: Literal["member", "maintainer"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamMembership:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Add or update team membership for a user](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user)
        > endpoint.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        If the user is already a member of the team's organization, this endpoint will
        add the user to the team. To add a membership between an organization member and
        a team, the authenticated user must be an organization owner or a team
        maintainer.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        If the user is unaffiliated with the team's organization, this endpoint will
        send an invitation to the user via email. This newly-created membership will be
        in the "pending" state until the user accepts the invitation, at which point the
        membership will transition to the "active" state and the user will be added as a
        member of the team. To add a membership between an unaffiliated user and a team,
        the authenticated user must be an organization owner.

        If the user is already a member of the team, this endpoint will update the role
        of the team member's role. To update the membership of a team member, the
        authenticated user must be an organization owner or a team maintainer.

        Args:
          role: The role that this user should have in the team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._put(
            f"/teams/{team_id}/memberships/{username}",
            body=maybe_transform({"role": role}, membership_add_or_update_params.MembershipAddOrUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamMembership,
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
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Remove team membership for a user](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user)
        > endpoint.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To remove a membership between a user and a team, the authenticated user must
        have 'admin' permissions to the team or be an owner of the organization that the
        team is associated with. Removing team membership does not delete the user, it
        just removes their membership from the team.

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
            f"/teams/{team_id}/memberships/{username}",
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
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamMembership:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Get team membership for a user](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user)
        > endpoint.

        Team members will include the members of child teams.

        To get a user's membership with a team, the team must be visible to the
        authenticated user.

        **Note:** The response contains the `state` of the membership and the member's
        `role`.

        The `role` for organization owners is set to `maintainer`. For more information
        about `maintainer` roles, see
        [Create a team](https://docs.github.com/rest/teams/teams#create-a-team).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/teams/{team_id}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamMembership,
        )

    async def add_or_update(
        self,
        username: str,
        *,
        team_id: int,
        role: Literal["member", "maintainer"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamMembership:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Add or update team membership for a user](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user)
        > endpoint.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        If the user is already a member of the team's organization, this endpoint will
        add the user to the team. To add a membership between an organization member and
        a team, the authenticated user must be an organization owner or a team
        maintainer.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        If the user is unaffiliated with the team's organization, this endpoint will
        send an invitation to the user via email. This newly-created membership will be
        in the "pending" state until the user accepts the invitation, at which point the
        membership will transition to the "active" state and the user will be added as a
        member of the team. To add a membership between an unaffiliated user and a team,
        the authenticated user must be an organization owner.

        If the user is already a member of the team, this endpoint will update the role
        of the team member's role. To update the membership of a team member, the
        authenticated user must be an organization owner or a team maintainer.

        Args:
          role: The role that this user should have in the team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._put(
            f"/teams/{team_id}/memberships/{username}",
            body=await async_maybe_transform({"role": role}, membership_add_or_update_params.MembershipAddOrUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamMembership,
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
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Remove team membership for a user](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user)
        > endpoint.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To remove a membership between a user and a team, the authenticated user must
        have 'admin' permissions to the team or be an owner of the organization that the
        team is associated with. Removing team membership does not delete the user, it
        just removes their membership from the team.

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
            f"/teams/{team_id}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class MembershipsResourceWithRawResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.retrieve = to_raw_response_wrapper(
            memberships.retrieve,
        )
        self.add_or_update = to_raw_response_wrapper(
            memberships.add_or_update,
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
        self.add_or_update = async_to_raw_response_wrapper(
            memberships.add_or_update,
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
        self.add_or_update = to_streamed_response_wrapper(
            memberships.add_or_update,
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
        self.add_or_update = async_to_streamed_response_wrapper(
            memberships.add_or_update,
        )
        self.remove = async_to_streamed_response_wrapper(
            memberships.remove,
        )
