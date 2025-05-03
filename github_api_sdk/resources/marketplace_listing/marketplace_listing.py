from __future__ import annotations

from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from .account import (
    AccountResource,
    AccountResourceWithRawResponse,
    AccountResourceWithStreamingResponse,
    AsyncAccountResource,
    AsyncAccountResourceWithRawResponse,
    AsyncAccountResourceWithStreamingResponse,
)
from .plans.plans import (
    AsyncPlansResource,
    AsyncPlansResourceWithRawResponse,
    AsyncPlansResourceWithStreamingResponse,
    PlansResource,
    PlansResourceWithRawResponse,
    PlansResourceWithStreamingResponse,
)
from .stubbed.stubbed import (
    AsyncStubbedResource,
    AsyncStubbedResourceWithRawResponse,
    AsyncStubbedResourceWithStreamingResponse,
    StubbedResource,
    StubbedResourceWithRawResponse,
    StubbedResourceWithStreamingResponse,
)

__all__ = ["MarketplaceListingResource", "AsyncMarketplaceListingResource"]


class MarketplaceListingResource(SyncAPIResource):
    @cached_property
    def account(self) -> AccountResource:
        return AccountResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def stubbed(self) -> StubbedResource:
        return StubbedResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketplaceListingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MarketplaceListingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketplaceListingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MarketplaceListingResourceWithStreamingResponse(self)


class AsyncMarketplaceListingResource(AsyncAPIResource):
    @cached_property
    def account(self) -> AsyncAccountResource:
        return AsyncAccountResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def stubbed(self) -> AsyncStubbedResource:
        return AsyncStubbedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketplaceListingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketplaceListingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketplaceListingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMarketplaceListingResourceWithStreamingResponse(self)


class MarketplaceListingResourceWithRawResponse:
    def __init__(self, marketplace_listing: MarketplaceListingResource) -> None:
        self._marketplace_listing = marketplace_listing

    @cached_property
    def account(self) -> AccountResourceWithRawResponse:
        return AccountResourceWithRawResponse(self._marketplace_listing.account)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._marketplace_listing.plans)

    @cached_property
    def stubbed(self) -> StubbedResourceWithRawResponse:
        return StubbedResourceWithRawResponse(self._marketplace_listing.stubbed)


class AsyncMarketplaceListingResourceWithRawResponse:
    def __init__(self, marketplace_listing: AsyncMarketplaceListingResource) -> None:
        self._marketplace_listing = marketplace_listing

    @cached_property
    def account(self) -> AsyncAccountResourceWithRawResponse:
        return AsyncAccountResourceWithRawResponse(self._marketplace_listing.account)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._marketplace_listing.plans)

    @cached_property
    def stubbed(self) -> AsyncStubbedResourceWithRawResponse:
        return AsyncStubbedResourceWithRawResponse(self._marketplace_listing.stubbed)


class MarketplaceListingResourceWithStreamingResponse:
    def __init__(self, marketplace_listing: MarketplaceListingResource) -> None:
        self._marketplace_listing = marketplace_listing

    @cached_property
    def account(self) -> AccountResourceWithStreamingResponse:
        return AccountResourceWithStreamingResponse(self._marketplace_listing.account)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._marketplace_listing.plans)

    @cached_property
    def stubbed(self) -> StubbedResourceWithStreamingResponse:
        return StubbedResourceWithStreamingResponse(self._marketplace_listing.stubbed)


class AsyncMarketplaceListingResourceWithStreamingResponse:
    def __init__(self, marketplace_listing: AsyncMarketplaceListingResource) -> None:
        self._marketplace_listing = marketplace_listing

    @cached_property
    def account(self) -> AsyncAccountResourceWithStreamingResponse:
        return AsyncAccountResourceWithStreamingResponse(self._marketplace_listing.account)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._marketplace_listing.plans)

    @cached_property
    def stubbed(self) -> AsyncStubbedResourceWithStreamingResponse:
        return AsyncStubbedResourceWithStreamingResponse(self._marketplace_listing.stubbed)
