from __future__ import annotations

import httpx

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.users import marketplace_purchase_list_params, marketplace_purchase_list_stubbed_params
from ...types.users.marketplace_purchase_list_response import MarketplacePurchaseListResponse
from ...types.users.marketplace_purchase_list_stubbed_response import MarketplacePurchaseListStubbedResponse

__all__ = ["MarketplacePurchasesResource", "AsyncMarketplacePurchasesResource"]


class MarketplacePurchasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarketplacePurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MarketplacePurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketplacePurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MarketplacePurchasesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketplacePurchaseListResponse:
        """
        Lists the active subscriptions for the authenticated user.

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
            "/user/marketplace_purchases",
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
                    marketplace_purchase_list_params.MarketplacePurchaseListParams,
                ),
            ),
            cast_to=MarketplacePurchaseListResponse,
        )

    def list_stubbed(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketplacePurchaseListStubbedResponse:
        """
        Lists the active subscriptions for the authenticated user.

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
            "/user/marketplace_purchases/stubbed",
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
                    marketplace_purchase_list_stubbed_params.MarketplacePurchaseListStubbedParams,
                ),
            ),
            cast_to=MarketplacePurchaseListStubbedResponse,
        )


class AsyncMarketplacePurchasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarketplacePurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketplacePurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketplacePurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMarketplacePurchasesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketplacePurchaseListResponse:
        """
        Lists the active subscriptions for the authenticated user.

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
            "/user/marketplace_purchases",
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
                    marketplace_purchase_list_params.MarketplacePurchaseListParams,
                ),
            ),
            cast_to=MarketplacePurchaseListResponse,
        )

    async def list_stubbed(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MarketplacePurchaseListStubbedResponse:
        """
        Lists the active subscriptions for the authenticated user.

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
            "/user/marketplace_purchases/stubbed",
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
                    marketplace_purchase_list_stubbed_params.MarketplacePurchaseListStubbedParams,
                ),
            ),
            cast_to=MarketplacePurchaseListStubbedResponse,
        )


class MarketplacePurchasesResourceWithRawResponse:
    def __init__(self, marketplace_purchases: MarketplacePurchasesResource) -> None:
        self._marketplace_purchases = marketplace_purchases

        self.list = to_raw_response_wrapper(
            marketplace_purchases.list,
        )
        self.list_stubbed = to_raw_response_wrapper(
            marketplace_purchases.list_stubbed,
        )


class AsyncMarketplacePurchasesResourceWithRawResponse:
    def __init__(self, marketplace_purchases: AsyncMarketplacePurchasesResource) -> None:
        self._marketplace_purchases = marketplace_purchases

        self.list = async_to_raw_response_wrapper(
            marketplace_purchases.list,
        )
        self.list_stubbed = async_to_raw_response_wrapper(
            marketplace_purchases.list_stubbed,
        )


class MarketplacePurchasesResourceWithStreamingResponse:
    def __init__(self, marketplace_purchases: MarketplacePurchasesResource) -> None:
        self._marketplace_purchases = marketplace_purchases

        self.list = to_streamed_response_wrapper(
            marketplace_purchases.list,
        )
        self.list_stubbed = to_streamed_response_wrapper(
            marketplace_purchases.list_stubbed,
        )


class AsyncMarketplacePurchasesResourceWithStreamingResponse:
    def __init__(self, marketplace_purchases: AsyncMarketplacePurchasesResource) -> None:
        self._marketplace_purchases = marketplace_purchases

        self.list = async_to_streamed_response_wrapper(
            marketplace_purchases.list,
        )
        self.list_stubbed = async_to_streamed_response_wrapper(
            marketplace_purchases.list_stubbed,
        )
