from __future__ import annotations

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.applications.hook.delivery import Delivery
from ....types.orgs.hooks import delivery_list_params
from ....types.orgs.hooks.delivery_list_response import DeliveryListResponse

__all__ = ["DeliveriesResource", "AsyncDeliveriesResource"]


class DeliveriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DeliveriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        delivery_id: int,
        *,
        org: str,
        hook_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Delivery:
        """
        Returns a delivery for a webhook configured in an organization.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Delivery,
        )

    def list(
        self,
        hook_id: int,
        *,
        org: str,
        cursor: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeliveryListResponse:
        """
        Returns a list of webhook deliveries for a webhook configured in an
        organization.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          cursor: Used for pagination: the starting delivery from which the page of deliveries is
              fetched. Refer to the `link` header for the next and previous page cursors.

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
            f"/orgs/{org}/hooks/{hook_id}/deliveries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                    },
                    delivery_list_params.DeliveryListParams,
                ),
            ),
            cast_to=DeliveryListResponse,
        )

    def redeliver(
        self,
        delivery_id: int,
        *,
        org: str,
        hook_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Redeliver a delivery for a webhook configured in an organization.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class AsyncDeliveriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDeliveriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        delivery_id: int,
        *,
        org: str,
        hook_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Delivery:
        """
        Returns a delivery for a webhook configured in an organization.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Delivery,
        )

    async def list(
        self,
        hook_id: int,
        *,
        org: str,
        cursor: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeliveryListResponse:
        """
        Returns a list of webhook deliveries for a webhook configured in an
        organization.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          cursor: Used for pagination: the starting delivery from which the page of deliveries is
              fetched. Refer to the `link` header for the next and previous page cursors.

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
            f"/orgs/{org}/hooks/{hook_id}/deliveries",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "per_page": per_page,
                    },
                    delivery_list_params.DeliveryListParams,
                ),
            ),
            cast_to=DeliveryListResponse,
        )

    async def redeliver(
        self,
        delivery_id: int,
        *,
        org: str,
        hook_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Redeliver a delivery for a webhook configured in an organization.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class DeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.retrieve = to_raw_response_wrapper(
            deliveries.retrieve,
        )
        self.list = to_raw_response_wrapper(
            deliveries.list,
        )
        self.redeliver = to_raw_response_wrapper(
            deliveries.redeliver,
        )


class AsyncDeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.retrieve = async_to_raw_response_wrapper(
            deliveries.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            deliveries.list,
        )
        self.redeliver = async_to_raw_response_wrapper(
            deliveries.redeliver,
        )


class DeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.retrieve = to_streamed_response_wrapper(
            deliveries.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            deliveries.list,
        )
        self.redeliver = to_streamed_response_wrapper(
            deliveries.redeliver,
        )


class AsyncDeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.retrieve = async_to_streamed_response_wrapper(
            deliveries.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            deliveries.list,
        )
        self.redeliver = async_to_streamed_response_wrapper(
            deliveries.redeliver,
        )
