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
from ....types.orgs.teams import membership_update_params
from ....types.orgs.teams.team_membership import TeamMembership

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
        team_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamMembership:
        """
        Team members will include the members of child teams.

        To get a user's membership with a team, the team must be visible to the
        authenticated user.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/memberships/{username}`.

        > [!NOTE] The response contains the `state` of the membership and the member's
        > `role`.

        The `role` for organization owners is set to `maintainer`. For more information
        about `maintainer` roles, see
        [Create a team](https://docs.github.com/rest/teams/teams#create-a-team).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/orgs/{org}/teams/{team_slug}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamMembership,
        )

    def update(
        self,
        username: str,
        *,
        org: str,
        team_slug: str,
        role: Literal["member", "maintainer"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamMembership:
        """Adds an organization member to a team.

        An authenticated organization owner or
        team maintainer can add organization members to a team.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        An organization owner can add someone who is not part of the team's organization
        to a team. When an organization owner adds someone to a team who is not an
        organization member, this endpoint will send an invitation to the person via
        email. This newly-created membership will be in the "pending" state until the
        person accepts the invitation, at which point the membership will transition to
        the "active" state and the user will be added as a member of the team.

        If the user is already a member of the team, this endpoint will update the role
        of the team member's role. To update the membership of a team member, the
        authenticated user must be an organization owner or a team maintainer.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `PUT /organizations/{org_id}/team/{team_id}/memberships/{username}`.

        Args:
          role: The role that this user should have in the team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._put(
            f"/orgs/{org}/teams/{team_slug}/memberships/{username}",
            body=maybe_transform({"role": role}, membership_update_params.MembershipUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamMembership,
        )

    def delete(
        self,
        username: str,
        *,
        org: str,
        team_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        To remove a membership between a user and a team, the authenticated user must
        have 'admin' permissions to the team or be an owner of the organization that the
        team is associated with. Removing team membership does not delete the user, it
        just removes their membership from the team.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `DELETE /organizations/{org_id}/team/{team_id}/memberships/{username}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/teams/{team_slug}/memberships/{username}",
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
        team_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamMembership:
        """
        Team members will include the members of child teams.

        To get a user's membership with a team, the team must be visible to the
        authenticated user.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/memberships/{username}`.

        > [!NOTE] The response contains the `state` of the membership and the member's
        > `role`.

        The `role` for organization owners is set to `maintainer`. For more information
        about `maintainer` roles, see
        [Create a team](https://docs.github.com/rest/teams/teams#create-a-team).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}/memberships/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamMembership,
        )

    async def update(
        self,
        username: str,
        *,
        org: str,
        team_slug: str,
        role: Literal["member", "maintainer"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamMembership:
        """Adds an organization member to a team.

        An authenticated organization owner or
        team maintainer can add organization members to a team.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        An organization owner can add someone who is not part of the team's organization
        to a team. When an organization owner adds someone to a team who is not an
        organization member, this endpoint will send an invitation to the person via
        email. This newly-created membership will be in the "pending" state until the
        person accepts the invitation, at which point the membership will transition to
        the "active" state and the user will be added as a member of the team.

        If the user is already a member of the team, this endpoint will update the role
        of the team member's role. To update the membership of a team member, the
        authenticated user must be an organization owner or a team maintainer.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `PUT /organizations/{org_id}/team/{team_id}/memberships/{username}`.

        Args:
          role: The role that this user should have in the team.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._put(
            f"/orgs/{org}/teams/{team_slug}/memberships/{username}",
            body=await async_maybe_transform({"role": role}, membership_update_params.MembershipUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamMembership,
        )

    async def delete(
        self,
        username: str,
        *,
        org: str,
        team_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        To remove a membership between a user and a team, the authenticated user must
        have 'admin' permissions to the team or be an owner of the organization that the
        team is associated with. Removing team membership does not delete the user, it
        just removes their membership from the team.

        Team synchronization is available for organizations using GitHub Enterprise
        Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        > [!NOTE] When you have team synchronization set up for a team with your
        > organization's identity provider (IdP), you will see an error if you attempt
        > to use the API for making changes to the team's membership. If you have access
        > to manage group membership in your IdP, you can manage GitHub team membership
        > through your identity provider, which automatically adds and removes team
        > members in an organization. For more information, see
        > "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `DELETE /organizations/{org_id}/team/{team_id}/memberships/{username}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/teams/{team_slug}/memberships/{username}",
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
        self.delete = to_raw_response_wrapper(
            memberships.delete,
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
        self.delete = async_to_raw_response_wrapper(
            memberships.delete,
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
        self.delete = to_streamed_response_wrapper(
            memberships.delete,
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
        self.delete = async_to_streamed_response_wrapper(
            memberships.delete,
        )
