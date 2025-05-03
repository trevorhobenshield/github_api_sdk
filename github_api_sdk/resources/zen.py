from __future__ import annotations

import httpx

from .._base_client import make_request_options
from .._compat import cached_property
from .._resource import AsyncAPIResource, SyncAPIResource
from .._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query

__all__ = ["ZenResource", "AsyncZenResource"]


class ZenResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ZenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ZenResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Get a random sentence from the Zen of GitHub"""
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            "/zen",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )


class AsyncZenResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZenResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZenResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZenResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncZenResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """Get a random sentence from the Zen of GitHub"""
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            "/zen",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )


class ZenResourceWithRawResponse:
    def __init__(self, zen: ZenResource) -> None:
        self._zen = zen

        self.retrieve = to_raw_response_wrapper(
            zen.retrieve,
        )


class AsyncZenResourceWithRawResponse:
    def __init__(self, zen: AsyncZenResource) -> None:
        self._zen = zen

        self.retrieve = async_to_raw_response_wrapper(
            zen.retrieve,
        )


class ZenResourceWithStreamingResponse:
    def __init__(self, zen: ZenResource) -> None:
        self._zen = zen

        self.retrieve = to_streamed_response_wrapper(
            zen.retrieve,
        )


class AsyncZenResourceWithStreamingResponse:
    def __init__(self, zen: AsyncZenResource) -> None:
        self._zen = zen

        self.retrieve = async_to_streamed_response_wrapper(
            zen.retrieve,
        )
