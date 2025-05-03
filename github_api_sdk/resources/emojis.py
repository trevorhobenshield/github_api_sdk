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
from ..types.emoji_list_response import EmojiListResponse

__all__ = ["EmojisResource", "AsyncEmojisResource"]


class EmojisResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmojisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmojisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmojisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return EmojisResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmojiListResponse:
        """Lists all the emojis available to use on GitHub."""
        return self._get(
            "/emojis",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EmojiListResponse,
        )


class AsyncEmojisResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmojisResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmojisResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmojisResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncEmojisResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmojiListResponse:
        """Lists all the emojis available to use on GitHub."""
        return await self._get(
            "/emojis",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EmojiListResponse,
        )


class EmojisResourceWithRawResponse:
    def __init__(self, emojis: EmojisResource) -> None:
        self._emojis = emojis

        self.list = to_raw_response_wrapper(
            emojis.list,
        )


class AsyncEmojisResourceWithRawResponse:
    def __init__(self, emojis: AsyncEmojisResource) -> None:
        self._emojis = emojis

        self.list = async_to_raw_response_wrapper(
            emojis.list,
        )


class EmojisResourceWithStreamingResponse:
    def __init__(self, emojis: EmojisResource) -> None:
        self._emojis = emojis

        self.list = to_streamed_response_wrapper(
            emojis.list,
        )


class AsyncEmojisResourceWithStreamingResponse:
    def __init__(self, emojis: AsyncEmojisResource) -> None:
        self._emojis = emojis

        self.list = async_to_streamed_response_wrapper(
            emojis.list,
        )
