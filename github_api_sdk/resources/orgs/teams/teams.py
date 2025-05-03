from __future__ import annotations

import builtins
from typing import List, Optional

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
from ....types.orgs import (
    team_create_params,
    team_list_child_teams_params,
    team_list_invitations_params,
    team_list_members_params,
    team_list_params,
    team_update_params,
)
from ....types.orgs.team_full import TeamFull
from ....types.orgs.team_list_child_teams_response import TeamListChildTeamsResponse
from ....types.orgs.team_list_invitations_response import TeamListInvitationsResponse
from ....types.orgs.team_list_members_response import TeamListMembersResponse
from ....types.orgs.team_list_response import TeamListResponse
from .copilot import (
    AsyncCopilotResource,
    AsyncCopilotResourceWithRawResponse,
    AsyncCopilotResourceWithStreamingResponse,
    CopilotResource,
    CopilotResourceWithRawResponse,
    CopilotResourceWithStreamingResponse,
)
from .discussions.discussions import (
    AsyncDiscussionsResource,
    AsyncDiscussionsResourceWithRawResponse,
    AsyncDiscussionsResourceWithStreamingResponse,
    DiscussionsResource,
    DiscussionsResourceWithRawResponse,
    DiscussionsResourceWithStreamingResponse,
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
    def copilot(self) -> CopilotResource:
        return CopilotResource(self._client)

    @cached_property
    def discussions(self) -> DiscussionsResource:
        return DiscussionsResource(self._client)

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

    def create(
        self,
        org: str,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        maintainers: builtins.list[str] | NotGiven = NOT_GIVEN,
        notification_setting: Literal["notifications_enabled", "notifications_disabled"] | NotGiven = NOT_GIVEN,
        parent_team_id: int | NotGiven = NOT_GIVEN,
        permission: Literal["pull", "push"] | NotGiven = NOT_GIVEN,
        privacy: Literal["secret", "closed"] | NotGiven = NOT_GIVEN,
        repo_names: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamFull:
        """
        To create a team, the authenticated user must be a member or owner of `{org}`.
        By default, organization members can create teams. Organization owners can limit
        team creation to organization owners. For more information, see
        "[Setting team creation permissions](https://docs.github.com/articles/setting-team-creation-permissions-in-your-organization)."

        When you create a new team, you automatically become a team maintainer without
        explicitly adding yourself to the optional array of `maintainers`. For more
        information, see
        "[About teams](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/about-teams)".

        Args:
          name: The name of the team.

          description: The description of the team.

          maintainers: List GitHub IDs for organization members who will become team maintainers.

          notification_setting:
              The notification setting the team has chosen. The options are:

              - `notifications_enabled` - team members receive notifications when the team is
                @mentioned.
              - `notifications_disabled` - no one receives notifications.
                Default: `notifications_enabled`

          parent_team_id: The ID of a team to set as the parent team.

          permission: **Closing down notice**. The permission that new repositories will be added to
              the team with when none is specified.

          privacy:
              The level of privacy this team should have. The options are:
              **For a non-nested team:**

              - `secret` - only visible to organization owners and members of this team.
              - `closed` - visible to all members of this organization.
                Default: `secret`
                **For a parent or child team:**
              - `closed` - visible to all members of this organization.
                Default for child team: `closed`

          repo_names: The full name (e.g., "organization-name/repository-name") of repositories to add
              the team to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/teams",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "maintainers": maintainers,
                    "notification_setting": notification_setting,
                    "parent_team_id": parent_team_id,
                    "permission": permission,
                    "privacy": privacy,
                    "repo_names": repo_names,
                },
                team_create_params.TeamCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamFull,
        )

    def retrieve(
        self,
        team_slug: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamFull:
        """Gets a team using the team's `slug`.

        To create the `slug`, GitHub replaces
        special characters in the `name` string, changes all words to lowercase, and
        replaces spaces with a `-` separator. For example, `"My TEam Näme"` would become
        `my-team-name`.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}`.

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
        return self._get(
            f"/orgs/{org}/teams/{team_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamFull,
        )

    def update(
        self,
        team_slug: str,
        *,
        org: str,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
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
        To edit a team, the authenticated user must either be an organization owner or a
        team maintainer.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `PATCH /organizations/{org_id}/team/{team_id}`.

        Args:
          description: The description of the team.

          name: The name of the team.

          notification_setting: The notification setting the team has chosen. Editing teams without specifying
              this parameter leaves `notification_setting` intact. The options are:

              - `notifications_enabled` - team members receive notifications when the team is
                @mentioned.
              - `notifications_disabled` - no one receives notifications.

          parent_team_id: The ID of a team to set as the parent team.

          permission: **Closing down notice**. The permission that new repositories will be added to
              the team with when none is specified.

          privacy: The level of privacy this team should have. Editing teams without specifying
              this parameter leaves `privacy` intact. When a team is nested, the `privacy` for
              parent teams cannot be `secret`. The options are:
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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._patch(
            f"/orgs/{org}/teams/{team_slug}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
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

    def list(
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
    ) -> TeamListResponse:
        """
        Lists all teams in an organization that are visible to the authenticated user.

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
            f"/orgs/{org}/teams",
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
                    team_list_params.TeamListParams,
                ),
            ),
            cast_to=TeamListResponse,
        )

    def delete(
        self,
        team_slug: str,
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
        To delete a team, the authenticated user must be an organization owner or team
        maintainer.

        If you are an organization owner, deleting a parent team will delete all of its
        child teams as well.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `DELETE /organizations/{org_id}/team/{team_id}`.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/teams/{team_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_child_teams(
        self,
        team_slug: str,
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
    ) -> TeamListChildTeamsResponse:
        """
        Lists the child teams of the team specified by `{team_slug}`.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/teams`.

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
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._get(
            f"/orgs/{org}/teams/{team_slug}/teams",
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
        team_slug: str,
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
    ) -> TeamListInvitationsResponse:
        """
        The return hash contains a `role` field which refers to the Organization
        Invitation role and will be one of the following values: `direct_member`,
        `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is
        not a GitHub member, the `login` field in the return hash will be `null`.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/invitations`.

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
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._get(
            f"/orgs/{org}/teams/{team_slug}/invitations",
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

    def list_members(
        self,
        team_slug: str,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        role: Literal["member", "maintainer", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamListMembersResponse:
        """
        Team members will include the members of child teams.

        To list members in a team, the team must be visible to the authenticated user.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._get(
            f"/orgs/{org}/teams/{team_slug}/members",
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
                    team_list_members_params.TeamListMembersParams,
                ),
            ),
            cast_to=TeamListMembersResponse,
        )


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def copilot(self) -> AsyncCopilotResource:
        return AsyncCopilotResource(self._client)

    @cached_property
    def discussions(self) -> AsyncDiscussionsResource:
        return AsyncDiscussionsResource(self._client)

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

    async def create(
        self,
        org: str,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        maintainers: builtins.list[str] | NotGiven = NOT_GIVEN,
        notification_setting: Literal["notifications_enabled", "notifications_disabled"] | NotGiven = NOT_GIVEN,
        parent_team_id: int | NotGiven = NOT_GIVEN,
        permission: Literal["pull", "push"] | NotGiven = NOT_GIVEN,
        privacy: Literal["secret", "closed"] | NotGiven = NOT_GIVEN,
        repo_names: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamFull:
        """
        To create a team, the authenticated user must be a member or owner of `{org}`.
        By default, organization members can create teams. Organization owners can limit
        team creation to organization owners. For more information, see
        "[Setting team creation permissions](https://docs.github.com/articles/setting-team-creation-permissions-in-your-organization)."

        When you create a new team, you automatically become a team maintainer without
        explicitly adding yourself to the optional array of `maintainers`. For more
        information, see
        "[About teams](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/about-teams)".

        Args:
          name: The name of the team.

          description: The description of the team.

          maintainers: List GitHub IDs for organization members who will become team maintainers.

          notification_setting:
              The notification setting the team has chosen. The options are:

              - `notifications_enabled` - team members receive notifications when the team is
                @mentioned.
              - `notifications_disabled` - no one receives notifications.
                Default: `notifications_enabled`

          parent_team_id: The ID of a team to set as the parent team.

          permission: **Closing down notice**. The permission that new repositories will be added to
              the team with when none is specified.

          privacy:
              The level of privacy this team should have. The options are:
              **For a non-nested team:**

              - `secret` - only visible to organization owners and members of this team.
              - `closed` - visible to all members of this organization.
                Default: `secret`
                **For a parent or child team:**
              - `closed` - visible to all members of this organization.
                Default for child team: `closed`

          repo_names: The full name (e.g., "organization-name/repository-name") of repositories to add
              the team to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/teams",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "maintainers": maintainers,
                    "notification_setting": notification_setting,
                    "parent_team_id": parent_team_id,
                    "permission": permission,
                    "privacy": privacy,
                    "repo_names": repo_names,
                },
                team_create_params.TeamCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamFull,
        )

    async def retrieve(
        self,
        team_slug: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamFull:
        """Gets a team using the team's `slug`.

        To create the `slug`, GitHub replaces
        special characters in the `name` string, changes all words to lowercase, and
        replaces spaces with a `-` separator. For example, `"My TEam Näme"` would become
        `my-team-name`.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}`.

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
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamFull,
        )

    async def update(
        self,
        team_slug: str,
        *,
        org: str,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
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
        To edit a team, the authenticated user must either be an organization owner or a
        team maintainer.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `PATCH /organizations/{org_id}/team/{team_id}`.

        Args:
          description: The description of the team.

          name: The name of the team.

          notification_setting: The notification setting the team has chosen. Editing teams without specifying
              this parameter leaves `notification_setting` intact. The options are:

              - `notifications_enabled` - team members receive notifications when the team is
                @mentioned.
              - `notifications_disabled` - no one receives notifications.

          parent_team_id: The ID of a team to set as the parent team.

          permission: **Closing down notice**. The permission that new repositories will be added to
              the team with when none is specified.

          privacy: The level of privacy this team should have. Editing teams without specifying
              this parameter leaves `privacy` intact. When a team is nested, the `privacy` for
              parent teams cannot be `secret`. The options are:
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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._patch(
            f"/orgs/{org}/teams/{team_slug}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
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

    async def list(
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
    ) -> TeamListResponse:
        """
        Lists all teams in an organization that are visible to the authenticated user.

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
            f"/orgs/{org}/teams",
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
                    team_list_params.TeamListParams,
                ),
            ),
            cast_to=TeamListResponse,
        )

    async def delete(
        self,
        team_slug: str,
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
        To delete a team, the authenticated user must be an organization owner or team
        maintainer.

        If you are an organization owner, deleting a parent team will delete all of its
        child teams as well.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `DELETE /organizations/{org_id}/team/{team_id}`.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/teams/{team_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_child_teams(
        self,
        team_slug: str,
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
    ) -> TeamListChildTeamsResponse:
        """
        Lists the child teams of the team specified by `{team_slug}`.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/teams`.

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
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}/teams",
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
        team_slug: str,
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
    ) -> TeamListInvitationsResponse:
        """
        The return hash contains a `role` field which refers to the Organization
        Invitation role and will be one of the following values: `direct_member`,
        `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is
        not a GitHub member, the `login` field in the return hash will be `null`.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/invitations`.

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
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}/invitations",
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

    async def list_members(
        self,
        team_slug: str,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        role: Literal["member", "maintainer", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamListMembersResponse:
        """
        Team members will include the members of child teams.

        To list members in a team, the team must be visible to the authenticated user.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}/members",
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
                    team_list_members_params.TeamListMembersParams,
                ),
            ),
            cast_to=TeamListMembersResponse,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.create = to_raw_response_wrapper(
            teams.create,
        )
        self.retrieve = to_raw_response_wrapper(
            teams.retrieve,
        )
        self.update = to_raw_response_wrapper(
            teams.update,
        )
        self.list = to_raw_response_wrapper(
            teams.list,
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
        self.list_members = to_raw_response_wrapper(
            teams.list_members,
        )

    @cached_property
    def copilot(self) -> CopilotResourceWithRawResponse:
        return CopilotResourceWithRawResponse(self._teams.copilot)

    @cached_property
    def discussions(self) -> DiscussionsResourceWithRawResponse:
        return DiscussionsResourceWithRawResponse(self._teams.discussions)

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

        self.create = async_to_raw_response_wrapper(
            teams.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            teams.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            teams.update,
        )
        self.list = async_to_raw_response_wrapper(
            teams.list,
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
        self.list_members = async_to_raw_response_wrapper(
            teams.list_members,
        )

    @cached_property
    def copilot(self) -> AsyncCopilotResourceWithRawResponse:
        return AsyncCopilotResourceWithRawResponse(self._teams.copilot)

    @cached_property
    def discussions(self) -> AsyncDiscussionsResourceWithRawResponse:
        return AsyncDiscussionsResourceWithRawResponse(self._teams.discussions)

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

        self.create = to_streamed_response_wrapper(
            teams.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            teams.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            teams.update,
        )
        self.list = to_streamed_response_wrapper(
            teams.list,
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
        self.list_members = to_streamed_response_wrapper(
            teams.list_members,
        )

    @cached_property
    def copilot(self) -> CopilotResourceWithStreamingResponse:
        return CopilotResourceWithStreamingResponse(self._teams.copilot)

    @cached_property
    def discussions(self) -> DiscussionsResourceWithStreamingResponse:
        return DiscussionsResourceWithStreamingResponse(self._teams.discussions)

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

        self.create = async_to_streamed_response_wrapper(
            teams.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            teams.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            teams.update,
        )
        self.list = async_to_streamed_response_wrapper(
            teams.list,
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
        self.list_members = async_to_streamed_response_wrapper(
            teams.list_members,
        )

    @cached_property
    def copilot(self) -> AsyncCopilotResourceWithStreamingResponse:
        return AsyncCopilotResourceWithStreamingResponse(self._teams.copilot)

    @cached_property
    def discussions(self) -> AsyncDiscussionsResourceWithStreamingResponse:
        return AsyncDiscussionsResourceWithStreamingResponse(self._teams.discussions)

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self._teams.memberships)

    @cached_property
    def projects(self) -> AsyncProjectsResourceWithStreamingResponse:
        return AsyncProjectsResourceWithStreamingResponse(self._teams.projects)

    @cached_property
    def repos(self) -> AsyncReposResourceWithStreamingResponse:
        return AsyncReposResourceWithStreamingResponse(self._teams.repos)
