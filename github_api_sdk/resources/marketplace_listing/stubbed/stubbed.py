from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
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

__all__ = ["StubbedResource", "AsyncStubbedResource"]


class StubbedResource(SyncAPIResource):
    @cached_property
    def account(self) -> AccountResource:
        return AccountResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> StubbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return StubbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StubbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return StubbedResourceWithStreamingResponse(self)


class AsyncStubbedResource(AsyncAPIResource):
    @cached_property
    def account(self) -> AsyncAccountResource:
        return AsyncAccountResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStubbedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStubbedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStubbedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncStubbedResourceWithStreamingResponse(self)


class StubbedResourceWithRawResponse:
    def __init__(self, stubbed: StubbedResource) -> None:
        self._stubbed = stubbed

    @cached_property
    def account(self) -> AccountResourceWithRawResponse:
        return AccountResourceWithRawResponse(self._stubbed.account)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._stubbed.plans)


class AsyncStubbedResourceWithRawResponse:
    def __init__(self, stubbed: AsyncStubbedResource) -> None:
        self._stubbed = stubbed

    @cached_property
    def account(self) -> AsyncAccountResourceWithRawResponse:
        return AsyncAccountResourceWithRawResponse(self._stubbed.account)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._stubbed.plans)


class StubbedResourceWithStreamingResponse:
    def __init__(self, stubbed: StubbedResource) -> None:
        self._stubbed = stubbed

    @cached_property
    def account(self) -> AccountResourceWithStreamingResponse:
        return AccountResourceWithStreamingResponse(self._stubbed.account)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._stubbed.plans)


class AsyncStubbedResourceWithStreamingResponse:
    def __init__(self, stubbed: AsyncStubbedResource) -> None:
        self._stubbed = stubbed

    @cached_property
    def account(self) -> AsyncAccountResourceWithStreamingResponse:
        return AsyncAccountResourceWithStreamingResponse(self._stubbed.account)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._stubbed.plans)
