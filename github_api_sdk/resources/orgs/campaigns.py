from __future__ import annotations

import builtins
from datetime import datetime
from typing import Iterable, List, Optional, Union

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
from ...types.orgs import State, campaign_create_params, campaign_list_params, campaign_update_params
from ...types.orgs.campaign_list_response import CampaignListResponse
from ...types.orgs.state import State
from ...types.orgs.summary import Summary

__all__ = ["CampaignsResource", "AsyncCampaignsResource"]


class CampaignsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CampaignsResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        code_scanning_alerts: Iterable[campaign_create_params.CodeScanningAlert],
        description: str,
        ends_at: str | datetime,
        name: str,
        contact_link: str | None | NotGiven = NOT_GIVEN,
        generate_issues: bool | NotGiven = NOT_GIVEN,
        managers: builtins.list[str] | NotGiven = NOT_GIVEN,
        team_managers: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Summary:
        """
        Create a campaign for an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

        Fine-grained tokens must have the "Code scanning alerts" repository permissions
        (read) on all repositories included in the campaign.

        Args:
          code_scanning_alerts: The code scanning alerts to include in this campaign

          description: A description for the campaign

          ends_at: The end date and time of the campaign. The date must be in the future.

          name: The name of the campaign

          contact_link: The contact link of the campaign. Must be a URI.

          generate_issues: If true, will automatically generate issues for the campaign. The default is
              false.

          managers: The logins of the users to set as the campaign managers. At this time, only a
              single manager can be supplied.

          team_managers: The slugs of the teams to set as the campaign managers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/campaigns",
            body=maybe_transform(
                {
                    "code_scanning_alerts": code_scanning_alerts,
                    "description": description,
                    "ends_at": ends_at,
                    "name": name,
                    "contact_link": contact_link,
                    "generate_issues": generate_issues,
                    "managers": managers,
                    "team_managers": team_managers,
                },
                campaign_create_params.CampaignCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Summary,
        )

    def retrieve(
        self,
        campaign_number: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Summary:
        """
        Gets a campaign for an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/campaigns/{campaign_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Summary,
        )

    def update(
        self,
        campaign_number: int,
        *,
        org: str,
        contact_link: str | None | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ends_at: str | datetime | NotGiven = NOT_GIVEN,
        managers: builtins.list[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        state: State | NotGiven = NOT_GIVEN,
        team_managers: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Summary:
        """
        Updates a campaign in an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

        Args:
          contact_link: The contact link of the campaign. Must be a URI.

          description: A description for the campaign

          ends_at: The end date and time of the campaign, in ISO 8601 format':'
              YYYY-MM-DDTHH:MM:SSZ.

          managers: The logins of the users to set as the campaign managers. At this time, only a
              single manager can be supplied.

          name: The name of the campaign

          state: Indicates whether a campaign is open or closed

          team_managers: The slugs of the teams to set as the campaign managers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._patch(
            f"/orgs/{org}/campaigns/{campaign_number}",
            body=maybe_transform(
                {
                    "contact_link": contact_link,
                    "description": description,
                    "ends_at": ends_at,
                    "managers": managers,
                    "name": name,
                    "state": state,
                    "team_managers": team_managers,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Summary,
        )

    def list(
        self,
        org: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "ends_at", "published"] | NotGiven = NOT_GIVEN,
        state: State | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignListResponse:
        """
        Lists campaigns in an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

        Args:
          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property by which to sort the results.

          state: If specified, only campaigns with this state will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/campaigns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    campaign_list_params.CampaignListParams,
                ),
            ),
            cast_to=CampaignListResponse,
        )

    def delete(
        self,
        campaign_number: int,
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
        Deletes a campaign in an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

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
            f"/orgs/{org}/campaigns/{campaign_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncCampaignsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCampaignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCampaignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCampaignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCampaignsResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        code_scanning_alerts: Iterable[campaign_create_params.CodeScanningAlert],
        description: str,
        ends_at: str | datetime,
        name: str,
        contact_link: str | None | NotGiven = NOT_GIVEN,
        generate_issues: bool | NotGiven = NOT_GIVEN,
        managers: builtins.list[str] | NotGiven = NOT_GIVEN,
        team_managers: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Summary:
        """
        Create a campaign for an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

        Fine-grained tokens must have the "Code scanning alerts" repository permissions
        (read) on all repositories included in the campaign.

        Args:
          code_scanning_alerts: The code scanning alerts to include in this campaign

          description: A description for the campaign

          ends_at: The end date and time of the campaign. The date must be in the future.

          name: The name of the campaign

          contact_link: The contact link of the campaign. Must be a URI.

          generate_issues: If true, will automatically generate issues for the campaign. The default is
              false.

          managers: The logins of the users to set as the campaign managers. At this time, only a
              single manager can be supplied.

          team_managers: The slugs of the teams to set as the campaign managers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/campaigns",
            body=await async_maybe_transform(
                {
                    "code_scanning_alerts": code_scanning_alerts,
                    "description": description,
                    "ends_at": ends_at,
                    "name": name,
                    "contact_link": contact_link,
                    "generate_issues": generate_issues,
                    "managers": managers,
                    "team_managers": team_managers,
                },
                campaign_create_params.CampaignCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Summary,
        )

    async def retrieve(
        self,
        campaign_number: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Summary:
        """
        Gets a campaign for an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/campaigns/{campaign_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Summary,
        )

    async def update(
        self,
        campaign_number: int,
        *,
        org: str,
        contact_link: str | None | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        ends_at: str | datetime | NotGiven = NOT_GIVEN,
        managers: builtins.list[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        state: State | NotGiven = NOT_GIVEN,
        team_managers: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Summary:
        """
        Updates a campaign in an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

        Args:
          contact_link: The contact link of the campaign. Must be a URI.

          description: A description for the campaign

          ends_at: The end date and time of the campaign, in ISO 8601 format':'
              YYYY-MM-DDTHH:MM:SSZ.

          managers: The logins of the users to set as the campaign managers. At this time, only a
              single manager can be supplied.

          name: The name of the campaign

          state: Indicates whether a campaign is open or closed

          team_managers: The slugs of the teams to set as the campaign managers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._patch(
            f"/orgs/{org}/campaigns/{campaign_number}",
            body=await async_maybe_transform(
                {
                    "contact_link": contact_link,
                    "description": description,
                    "ends_at": ends_at,
                    "managers": managers,
                    "name": name,
                    "state": state,
                    "team_managers": team_managers,
                },
                campaign_update_params.CampaignUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Summary,
        )

    async def list(
        self,
        org: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "ends_at", "published"] | NotGiven = NOT_GIVEN,
        state: State | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CampaignListResponse:
        """
        Lists campaigns in an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

        Args:
          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property by which to sort the results.

          state: If specified, only campaigns with this state will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/campaigns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    campaign_list_params.CampaignListParams,
                ),
            ),
            cast_to=CampaignListResponse,
        )

    async def delete(
        self,
        campaign_number: int,
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
        Deletes a campaign in an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint.

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
            f"/orgs/{org}/campaigns/{campaign_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class CampaignsResourceWithRawResponse:
    def __init__(self, campaigns: CampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = to_raw_response_wrapper(
            campaigns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            campaigns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            campaigns.update,
        )
        self.list = to_raw_response_wrapper(
            campaigns.list,
        )
        self.delete = to_raw_response_wrapper(
            campaigns.delete,
        )


class AsyncCampaignsResourceWithRawResponse:
    def __init__(self, campaigns: AsyncCampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = async_to_raw_response_wrapper(
            campaigns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            campaigns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            campaigns.update,
        )
        self.list = async_to_raw_response_wrapper(
            campaigns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            campaigns.delete,
        )


class CampaignsResourceWithStreamingResponse:
    def __init__(self, campaigns: CampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = to_streamed_response_wrapper(
            campaigns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            campaigns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            campaigns.update,
        )
        self.list = to_streamed_response_wrapper(
            campaigns.list,
        )
        self.delete = to_streamed_response_wrapper(
            campaigns.delete,
        )


class AsyncCampaignsResourceWithStreamingResponse:
    def __init__(self, campaigns: AsyncCampaignsResource) -> None:
        self._campaigns = campaigns

        self.create = async_to_streamed_response_wrapper(
            campaigns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            campaigns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            campaigns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            campaigns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            campaigns.delete,
        )
