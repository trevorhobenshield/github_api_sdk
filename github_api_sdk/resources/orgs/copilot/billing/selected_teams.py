from __future__ import annotations

from typing import List

import httpx

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs.copilot.billing import selected_team_add_params, selected_team_remove_params
from .....types.orgs.copilot.billing.selected_team_add_response import SelectedTeamAddResponse
from .....types.orgs.copilot.billing.selected_team_remove_response import SelectedTeamRemoveResponse

__all__ = ["SelectedTeamsResource", "AsyncSelectedTeamsResource"]


class SelectedTeamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SelectedTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SelectedTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SelectedTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SelectedTeamsResourceWithStreamingResponse(self)

    def add(
        self,
        org: str,
        *,
        selected_teams: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelectedTeamAddResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Purchases a GitHub Copilot seat for all users within each specified team. The
        organization will be billed for each seat based on the organization's Copilot
        plan. For more information about Copilot pricing, see
        "[About billing for GitHub Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/about-billing-for-github-copilot-in-your-organization)."

        Only organization owners can purchase Copilot seats for their organization
        members. The organization must have a Copilot Business or Copilot Enterprise
        subscription and a configured suggestion matching policy. For more information
        about setting up a Copilot subscription, see
        "[Subscribing to Copilot for your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/subscribing-to-copilot-for-your-organization)."
        For more information about setting a suggestion matching policy, see
        "[Managing policies for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#policies-for-suggestion-matching)."

        The response contains the total number of new seats that were created and
        existing seats that were refreshed.

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot` or `admin:org` scopes to use this endpoint.

        Args:
          selected_teams: List of team names within the organization to which to grant access to GitHub
              Copilot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/copilot/billing/selected_teams",
            body=maybe_transform({"selected_teams": selected_teams}, selected_team_add_params.SelectedTeamAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SelectedTeamAddResponse,
        )

    def remove(
        self,
        org: str,
        *,
        selected_teams: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelectedTeamRemoveResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Sets seats for all members of each team specified to "pending cancellation".
        This will cause the members of the specified team(s) to lose access to GitHub
        Copilot at the end of the current billing cycle unless they retain access
        through another team. For more information about disabling access to Copilot,
        see
        "[Revoking access to Copilot for members of your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization)."

        Only organization owners can cancel Copilot seats for their organization
        members.

        The response contains the total number of seats set to "pending cancellation".

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot` or `admin:org` scopes to use this endpoint.

        Args:
          selected_teams: The names of teams from which to revoke access to GitHub Copilot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._delete(
            f"/orgs/{org}/copilot/billing/selected_teams",
            body=maybe_transform({"selected_teams": selected_teams}, selected_team_remove_params.SelectedTeamRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SelectedTeamRemoveResponse,
        )


class AsyncSelectedTeamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSelectedTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSelectedTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSelectedTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSelectedTeamsResourceWithStreamingResponse(self)

    async def add(
        self,
        org: str,
        *,
        selected_teams: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelectedTeamAddResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Purchases a GitHub Copilot seat for all users within each specified team. The
        organization will be billed for each seat based on the organization's Copilot
        plan. For more information about Copilot pricing, see
        "[About billing for GitHub Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/about-billing-for-github-copilot-in-your-organization)."

        Only organization owners can purchase Copilot seats for their organization
        members. The organization must have a Copilot Business or Copilot Enterprise
        subscription and a configured suggestion matching policy. For more information
        about setting up a Copilot subscription, see
        "[Subscribing to Copilot for your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/subscribing-to-copilot-for-your-organization)."
        For more information about setting a suggestion matching policy, see
        "[Managing policies for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#policies-for-suggestion-matching)."

        The response contains the total number of new seats that were created and
        existing seats that were refreshed.

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot` or `admin:org` scopes to use this endpoint.

        Args:
          selected_teams: List of team names within the organization to which to grant access to GitHub
              Copilot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/copilot/billing/selected_teams",
            body=await async_maybe_transform({"selected_teams": selected_teams}, selected_team_add_params.SelectedTeamAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SelectedTeamAddResponse,
        )

    async def remove(
        self,
        org: str,
        *,
        selected_teams: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SelectedTeamRemoveResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Sets seats for all members of each team specified to "pending cancellation".
        This will cause the members of the specified team(s) to lose access to GitHub
        Copilot at the end of the current billing cycle unless they retain access
        through another team. For more information about disabling access to Copilot,
        see
        "[Revoking access to Copilot for members of your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization)."

        Only organization owners can cancel Copilot seats for their organization
        members.

        The response contains the total number of seats set to "pending cancellation".

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot` or `admin:org` scopes to use this endpoint.

        Args:
          selected_teams: The names of teams from which to revoke access to GitHub Copilot.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._delete(
            f"/orgs/{org}/copilot/billing/selected_teams",
            body=await async_maybe_transform({"selected_teams": selected_teams}, selected_team_remove_params.SelectedTeamRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SelectedTeamRemoveResponse,
        )


class SelectedTeamsResourceWithRawResponse:
    def __init__(self, selected_teams: SelectedTeamsResource) -> None:
        self._selected_teams = selected_teams

        self.add = to_raw_response_wrapper(
            selected_teams.add,
        )
        self.remove = to_raw_response_wrapper(
            selected_teams.remove,
        )


class AsyncSelectedTeamsResourceWithRawResponse:
    def __init__(self, selected_teams: AsyncSelectedTeamsResource) -> None:
        self._selected_teams = selected_teams

        self.add = async_to_raw_response_wrapper(
            selected_teams.add,
        )
        self.remove = async_to_raw_response_wrapper(
            selected_teams.remove,
        )


class SelectedTeamsResourceWithStreamingResponse:
    def __init__(self, selected_teams: SelectedTeamsResource) -> None:
        self._selected_teams = selected_teams

        self.add = to_streamed_response_wrapper(
            selected_teams.add,
        )
        self.remove = to_streamed_response_wrapper(
            selected_teams.remove,
        )


class AsyncSelectedTeamsResourceWithStreamingResponse:
    def __init__(self, selected_teams: AsyncSelectedTeamsResource) -> None:
        self._selected_teams = selected_teams

        self.add = async_to_streamed_response_wrapper(
            selected_teams.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            selected_teams.remove,
        )
