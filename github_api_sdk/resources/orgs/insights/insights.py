from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .api.api import (
    APIResource,
    APIResourceWithRawResponse,
    APIResourceWithStreamingResponse,
    AsyncAPIResource,
    AsyncAPIResourceWithRawResponse,
    AsyncAPIResourceWithStreamingResponse,
)

__all__ = ["InsightsResource", "AsyncInsightsResource"]


class InsightsResource(SyncAPIResource):
    @cached_property
    def api(self) -> APIResource:
        return APIResource(self._client)

    @cached_property
    def with_raw_response(self) -> InsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return InsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return InsightsResourceWithStreamingResponse(self)


class AsyncInsightsResource(AsyncAPIResource):
    @cached_property
    def api(self) -> AsyncAPIResource:
        return AsyncAPIResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncInsightsResourceWithStreamingResponse(self)


class InsightsResourceWithRawResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

    @cached_property
    def api(self) -> APIResourceWithRawResponse:
        return APIResourceWithRawResponse(self._insights.api)


class AsyncInsightsResourceWithRawResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

    @cached_property
    def api(self) -> AsyncAPIResourceWithRawResponse:
        return AsyncAPIResourceWithRawResponse(self._insights.api)


class InsightsResourceWithStreamingResponse:
    def __init__(self, insights: InsightsResource) -> None:
        self._insights = insights

    @cached_property
    def api(self) -> APIResourceWithStreamingResponse:
        return APIResourceWithStreamingResponse(self._insights.api)


class AsyncInsightsResourceWithStreamingResponse:
    def __init__(self, insights: AsyncInsightsResource) -> None:
        self._insights = insights

    @cached_property
    def api(self) -> AsyncAPIResourceWithStreamingResponse:
        return AsyncAPIResourceWithStreamingResponse(self._insights.api)
