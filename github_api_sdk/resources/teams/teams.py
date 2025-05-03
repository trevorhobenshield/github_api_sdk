from __future__ import annotations

from typing import Optional

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
from ...types import team_list_child_teams_params, team_list_invitations_params, team_update_params
from ...types.orgs.team_full import TeamFull
from ...types.team_list_child_teams_response import TeamListChildTeamsResponse
from ...types.team_list_invitations_response import TeamListInvitationsResponse
from .discussions.discussions import (
    AsyncDiscussionsResource,
    AsyncDiscussionsResourceWithRawResponse,
    AsyncDiscussionsResourceWithStreamingResponse,
    DiscussionsResource,
    DiscussionsResourceWithRawResponse,
    DiscussionsResourceWithStreamingResponse,
)
from .members import (
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
from .projects import (
    AsyncProjectsResource,
    AsyncProjectsResourceWithRawResponse,
    AsyncProjectsResourceWithStreamingResponse,
    ProjectsResource,
    ProjectsResourceWithRawResponse,
    ProjectsResourceWithStreamingResponse,
)
from .repos import (
    AsyncReposResource,
    AsyncReposResourceWithRawResponse,
    AsyncReposResourceWithStreamingResponse,
    ReposResource,
    ReposResourceWithRawResponse,
    ReposResourceWithStreamingResponse,
)

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    @cached_property
    def discussions(self) -> DiscussionsResource:
        return DiscussionsResource(self._client)

    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def memberships(self) -> MembershipsResource:
        return MembershipsResource(self._client)

    @cached_property
    def projects(self) -> ProjectsResource:
        return ProjectsResource(self._client)

    @cached_property
    def repos(self) -> ReposResource:
        return ReposResource(self._client)

    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return TeamsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        team_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamFull:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the
        > [Get a team by name](https://docs.github.com/rest/teams/teams#get-a-team-by-name)
        > endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/teams/{team_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamFull,
        )

    def update(
        self,
        team_id: int,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        notification_setting: Literal["notifications_enabled", "notifications_disabled"] | NotGiven = NOT_GIVEN,
        parent_team_id: int | None | NotGiven = NOT_GIVEN,
        permission: Literal["pull", "push", "admin"] | NotGiven = NOT_GIVEN,
        privacy: Literal["secret", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamFull:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Update a team](https://docs.github.com/rest/teams/teams#update-a-team)
        > endpoint.

        To edit a team, the authenticated user must either be an organization owner or a
        team maintainer.

        > [!NOTE] With nested teams, the `privacy` for parent teams cannot be `secret`.

        Args:
          name: The name of the team.

          description: The description of the team.

          notification_setting: The notification setting the team has chosen. Editing teams without specifying
              this parameter leaves `notification_setting` intact. The options are:

              - `notifications_enabled` - team members receive notifications when the team is
                @mentioned.
              - `notifications_disabled` - no one receives notifications.

          parent_team_id: The ID of a team to set as the parent team.

          permission: **Closing down notice**. The permission that new repositories will be added to
              the team with when none is specified.

          privacy: The level of privacy this team should have. Editing teams without specifying
              this parameter leaves `privacy` intact. The options are:
              **For a non-nested team:**

              - `secret` - only visible to organization owners and members of this team.
              - `closed` - visible to all members of this organization.
                **For a parent or child team:**
              - `closed` - visible to all members of this organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/teams/{team_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "notification_setting": notification_setting,
                    "parent_team_id": parent_team_id,
                    "permission": permission,
                    "privacy": privacy,
                },
                team_update_params.TeamUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamFull,
        )

    def delete(
        self,
        team_id: int,
        *,
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
        > [Delete a team](https://docs.github.com/rest/teams/teams#delete-a-team)
        > endpoint.

        To delete a team, the authenticated user must be an organization owner or team
        maintainer.

        If you are an organization owner, deleting a parent team will delete all of its
        child teams as well.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/teams/{team_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_child_teams(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamListChildTeamsResponse:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`List child teams`](https://docs.github.com/rest/teams/teams#list-child-teams)
        > endpoint.

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
            f"/teams/{team_id}/teams",
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
                    team_list_child_teams_params.TeamListChildTeamsParams,
                ),
            ),
            cast_to=TeamListChildTeamsResponse,
        )

    def list_invitations(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamListInvitationsResponse:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`List pending team invitations`](https://docs.github.com/rest/teams/members#list-pending-team-invitations)
        > endpoint.

        The return hash contains a `role` field which refers to the Organization
        Invitation role and will be one of the following values: `direct_member`,
        `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is
        not a GitHub member, the `login` field in the return hash will be `null`.

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
            f"/teams/{team_id}/invitations",
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
                    team_list_invitations_params.TeamListInvitationsParams,
                ),
            ),
            cast_to=TeamListInvitationsResponse,
        )


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def discussions(self) -> AsyncDiscussionsResource:
        return AsyncDiscussionsResource(self._client)

    @cached_property
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        return AsyncMembershipsResource(self._client)

    @cached_property
    def projects(self) -> AsyncProjectsResource:
        return AsyncProjectsResource(self._client)

    @cached_property
    def repos(self) -> AsyncReposResource:
        return AsyncReposResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncTeamsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        team_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamFull:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the
        > [Get a team by name](https://docs.github.com/rest/teams/teams#get-a-team-by-name)
        > endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/teams/{team_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamFull,
        )

    async def update(
        self,
        team_id: int,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        notification_setting: Literal["notifications_enabled", "notifications_disabled"] | NotGiven = NOT_GIVEN,
        parent_team_id: int | None | NotGiven = NOT_GIVEN,
        permission: Literal["pull", "push", "admin"] | NotGiven = NOT_GIVEN,
        privacy: Literal["secret", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamFull:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Update a team](https://docs.github.com/rest/teams/teams#update-a-team)
        > endpoint.

        To edit a team, the authenticated user must either be an organization owner or a
        team maintainer.

        > [!NOTE] With nested teams, the `privacy` for parent teams cannot be `secret`.

        Args:
          name: The name of the team.

          description: The description of the team.

          notification_setting: The notification setting the team has chosen. Editing teams without specifying
              this parameter leaves `notification_setting` intact. The options are:

              - `notifications_enabled` - team members receive notifications when the team is
                @mentioned.
              - `notifications_disabled` - no one receives notifications.

          parent_team_id: The ID of a team to set as the parent team.

          permission: **Closing down notice**. The permission that new repositories will be added to
              the team with when none is specified.

          privacy: The level of privacy this team should have. Editing teams without specifying
              this parameter leaves `privacy` intact. The options are:
              **For a non-nested team:**

              - `secret` - only visible to organization owners and members of this team.
              - `closed` - visible to all members of this organization.
                **For a parent or child team:**
              - `closed` - visible to all members of this organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/teams/{team_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "notification_setting": notification_setting,
                    "parent_team_id": parent_team_id,
                    "permission": permission,
                    "privacy": privacy,
                },
                team_update_params.TeamUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamFull,
        )

    async def delete(
        self,
        team_id: int,
        *,
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
        > [Delete a team](https://docs.github.com/rest/teams/teams#delete-a-team)
        > endpoint.

        To delete a team, the authenticated user must be an organization owner or team
        maintainer.

        If you are an organization owner, deleting a parent team will delete all of its
        child teams as well.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/teams/{team_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_child_teams(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamListChildTeamsResponse:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`List child teams`](https://docs.github.com/rest/teams/teams#list-child-teams)
        > endpoint.

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
            f"/teams/{team_id}/teams",
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
                    team_list_child_teams_params.TeamListChildTeamsParams,
                ),
            ),
            cast_to=TeamListChildTeamsResponse,
        )

    async def list_invitations(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamListInvitationsResponse:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`List pending team invitations`](https://docs.github.com/rest/teams/members#list-pending-team-invitations)
        > endpoint.

        The return hash contains a `role` field which refers to the Organization
        Invitation role and will be one of the following values: `direct_member`,
        `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is
        not a GitHub member, the `login` field in the return hash will be `null`.

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
            f"/teams/{team_id}/invitations",
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
                    team_list_invitations_params.TeamListInvitationsParams,
                ),
            ),
            cast_to=TeamListInvitationsResponse,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.retrieve = to_raw_response_wrapper(
            teams.retrieve,
        )
        self.update = to_raw_response_wrapper(
            teams.update,
        )
        self.delete = to_raw_response_wrapper(
            teams.delete,
        )
        self.list_child_teams = to_raw_response_wrapper(
            teams.list_child_teams,
        )
        self.list_invitations = to_raw_response_wrapper(
            teams.list_invitations,
        )

    @cached_property
    def discussions(self) -> DiscussionsResourceWithRawResponse:
        return DiscussionsResourceWithRawResponse(self._teams.discussions)

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._teams.members)

    @cached_property
    def memberships(self) -> MembershipsResourceWithRawResponse:
        return MembershipsResourceWithRawResponse(self._teams.memberships)

    @cached_property
    def projects(self) -> ProjectsResourceWithRawResponse:
        return ProjectsResourceWithRawResponse(self._teams.projects)

    @cached_property
    def repos(self) -> ReposResourceWithRawResponse:
        return ReposResourceWithRawResponse(self._teams.repos)


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.retrieve = async_to_raw_response_wrapper(
            teams.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            teams.update,
        )
        self.delete = async_to_raw_response_wrapper(
            teams.delete,
        )
        self.list_child_teams = async_to_raw_response_wrapper(
            teams.list_child_teams,
        )
        self.list_invitations = async_to_raw_response_wrapper(
            teams.list_invitations,
        )

    @cached_property
    def discussions(self) -> AsyncDiscussionsResourceWithRawResponse:
        return AsyncDiscussionsResourceWithRawResponse(self._teams.discussions)

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._teams.members)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithRawResponse:
        return AsyncMembershipsResourceWithRawResponse(self._teams.memberships)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithRawResponse:
        return AsyncProjectsResourceWithRawResponse(self._teams.projects)

    @cached_property
    def repos(self) -> AsyncReposResourceWithRawResponse:
        return AsyncReposResourceWithRawResponse(self._teams.repos)


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.retrieve = to_streamed_response_wrapper(
            teams.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            teams.update,
        )
        self.delete = to_streamed_response_wrapper(
            teams.delete,
        )
        self.list_child_teams = to_streamed_response_wrapper(
            teams.list_child_teams,
        )
        self.list_invitations = to_streamed_response_wrapper(
            teams.list_invitations,
        )

    @cached_property
    def discussions(self) -> DiscussionsResourceWithStreamingResponse:
        return DiscussionsResourceWithStreamingResponse(self._teams.discussions)

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._teams.members)

    @cached_property
    def memberships(self) -> MembershipsResourceWithStreamingResponse:
        return MembershipsResourceWithStreamingResponse(self._teams.memberships)

    @cached_property
    def projects(self) -> ProjectsResourceWithStreamingResponse:
        return ProjectsResourceWithStreamingResponse(self._teams.projects)

    @cached_property
    def repos(self) -> ReposResourceWithStreamingResponse:
        return ReposResourceWithStreamingResponse(self._teams.repos)


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.retrieve = async_to_streamed_response_wrapper(
            teams.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            teams.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            teams.delete,
        )
        self.list_child_teams = async_to_streamed_response_wrapper(
            teams.list_child_teams,
        )
        self.list_invitations = async_to_streamed_response_wrapper(
            teams.list_invitations,
        )

    @cached_property
    def discussions(self) -> AsyncDiscussionsResourceWithStreamingResponse:
        return AsyncDiscussionsResourceWithStreamingResponse(self._teams.discussions)

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._teams.members)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self._teams.memberships)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._teams.projects)

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._teams.repos)
