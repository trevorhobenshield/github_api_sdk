from __future__ import annotations

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
from .....types.orgs.copilot import billing_list_seats_params
from .....types.orgs.copilot.billing_list_seats_response import BillingListSeatsResponse
from .....types.orgs.copilot.billing_retrieve_response import BillingRetrieveResponse
from .selected_teams import (
    AsyncSelectedTeamsResource,
    AsyncSelectedTeamsResourceWithRawResponse,
    AsyncSelectedTeamsResourceWithStreamingResponse,
    SelectedTeamsResource,
    SelectedTeamsResourceWithRawResponse,
    SelectedTeamsResourceWithStreamingResponse,
)
from .selected_users import (
    AsyncSelectedUsersResource,
    AsyncSelectedUsersResourceWithRawResponse,
    AsyncSelectedUsersResourceWithStreamingResponse,
    SelectedUsersResource,
    SelectedUsersResourceWithRawResponse,
    SelectedUsersResourceWithStreamingResponse,
)

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def selected_teams(self) -> SelectedTeamsResource:
        return SelectedTeamsResource(self._client)

    @cached_property
    def selected_users(self) -> SelectedUsersResource:
        return SelectedUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingRetrieveResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Gets information about an organization's Copilot subscription, including seat
        breakdown and feature policies. To configure these settings, go to your
        organization's settings on GitHub.com. For more information, see
        "[Managing policies for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-policies-for-copilot-business-in-your-organization)."

        Only organization owners can view details about the organization's Copilot
        Business or Copilot Enterprise subscription.

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
        return self._get(
            f"/orgs/{org}/copilot/billing",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BillingRetrieveResponse,
        )

    def list_seats(
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
    ) -> BillingListSeatsResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Lists all Copilot seats for which an organization with a Copilot Business or
        Copilot Enterprise subscription is currently being billed. Only organization
        owners can view assigned seats.

        Each seat object contains information about the assigned user's most recent
        Copilot activity. Users must have telemetry enabled in their IDE for Copilot in
        the IDE activity to be reflected in `last_activity_at`. For more information
        about activity data, see
        "[Reviewing user activity data for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization)."

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot` or `read:org` scopes to use this endpoint.

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
            f"/orgs/{org}/copilot/billing/seats",
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
                    billing_list_seats_params.BillingListSeatsParams,
                ),
            ),
            cast_to=BillingListSeatsResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def selected_teams(self) -> AsyncSelectedTeamsResource:
        return AsyncSelectedTeamsResource(self._client)

    @cached_property
    def selected_users(self) -> AsyncSelectedUsersResource:
        return AsyncSelectedUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingRetrieveResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Gets information about an organization's Copilot subscription, including seat
        breakdown and feature policies. To configure these settings, go to your
        organization's settings on GitHub.com. For more information, see
        "[Managing policies for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-policies-for-copilot-business-in-your-organization)."

        Only organization owners can view details about the organization's Copilot
        Business or Copilot Enterprise subscription.

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
        return await self._get(
            f"/orgs/{org}/copilot/billing",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BillingRetrieveResponse,
        )

    async def list_seats(
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
    ) -> BillingListSeatsResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Lists all Copilot seats for which an organization with a Copilot Business or
        Copilot Enterprise subscription is currently being billed. Only organization
        owners can view assigned seats.

        Each seat object contains information about the assigned user's most recent
        Copilot activity. Users must have telemetry enabled in their IDE for Copilot in
        the IDE activity to be reflected in `last_activity_at`. For more information
        about activity data, see
        "[Reviewing user activity data for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization)."

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot` or `read:org` scopes to use this endpoint.

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
            f"/orgs/{org}/copilot/billing/seats",
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
                    billing_list_seats_params.BillingListSeatsParams,
                ),
            ),
            cast_to=BillingListSeatsResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.retrieve = to_raw_response_wrapper(
            billing.retrieve,
        )
        self.list_seats = to_raw_response_wrapper(
            billing.list_seats,
        )

    @cached_property
    def selected_teams(self) -> SelectedTeamsResourceWithRawResponse:
        return SelectedTeamsResourceWithRawResponse(self._billing.selected_teams)

    @cached_property
    def selected_users(self) -> SelectedUsersResourceWithRawResponse:
        return SelectedUsersResourceWithRawResponse(self._billing.selected_users)


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.retrieve = async_to_raw_response_wrapper(
            billing.retrieve,
        )
        self.list_seats = async_to_raw_response_wrapper(
            billing.list_seats,
        )

    @cached_property
    def selected_teams(self) -> AsyncSelectedTeamsResourceWithRawResponse:
        return AsyncSelectedTeamsResourceWithRawResponse(self._billing.selected_teams)

    @cached_property
    def selected_users(self) -> AsyncSelectedUsersResourceWithRawResponse:
        return AsyncSelectedUsersResourceWithRawResponse(self._billing.selected_users)


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.retrieve = to_streamed_response_wrapper(
            billing.retrieve,
        )
        self.list_seats = to_streamed_response_wrapper(
            billing.list_seats,
        )

    @cached_property
    def selected_teams(self) -> SelectedTeamsResourceWithStreamingResponse:
        return SelectedTeamsResourceWithStreamingResponse(self._billing.selected_teams)

    @cached_property
    def selected_users(self) -> SelectedUsersResourceWithStreamingResponse:
        return SelectedUsersResourceWithStreamingResponse(self._billing.selected_users)


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.retrieve = async_to_streamed_response_wrapper(
            billing.retrieve,
        )
        self.list_seats = async_to_streamed_response_wrapper(
            billing.list_seats,
        )

    @cached_property
    def selected_teams(self) -> AsyncSelectedTeamsResourceWithStreamingResponse:
        return AsyncSelectedTeamsResourceWithStreamingResponse(self._billing.selected_teams)

    @cached_property
    def selected_users(self) -> AsyncSelectedUsersResourceWithStreamingResponse:
        return AsyncSelectedUsersResourceWithStreamingResponse(self._billing.selected_users)
