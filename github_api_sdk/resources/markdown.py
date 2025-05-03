from __future__ import annotations

import httpx
from typing_extensions import Literal

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
from .._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ..types import markdown_render_params, markdown_render_raw_params

__all__ = ["MarkdownResource", "AsyncMarkdownResource"]


class MarkdownResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarkdownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MarkdownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarkdownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MarkdownResourceWithStreamingResponse(self)

    def render(
        self,
        *,
        text: str,
        context: str | NotGiven = NOT_GIVEN,
        mode: Literal["markdown", "gfm"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Render a Markdown document

        Args:
          text: The Markdown text to render in HTML.

          context: The repository context to use when creating references in `gfm` mode. For
              example, setting `context` to `octo-org/octo-repo` will change the text `#42`
              into an HTML link to issue 42 in the `octo-org/octo-repo` repository.

          mode: The rendering mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return self._post(
            "/markdown",
            body=maybe_transform(
                {
                    "text": text,
                    "context": context,
                    "mode": mode,
                },
                markdown_render_params.MarkdownRenderParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )

    def render_raw(
        self,
        *,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        You must send Markdown as plain text (using a `Content-Type` header of
        `text/plain` or `text/x-markdown`) to this endpoint, rather than using JSON
        format. In raw mode, [GitHub Flavored Markdown](https://github.github.com/gfm/)
        is not supported and Markdown will be rendered in plain format like a README.md
        file. Markdown content must be 400 KB or less.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return self._post(
            "/markdown/raw",
            body=maybe_transform(body, markdown_render_raw_params.MarkdownRenderRawParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )


class AsyncMarkdownResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarkdownResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarkdownResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarkdownResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMarkdownResourceWithStreamingResponse(self)

    async def render(
        self,
        *,
        text: str,
        context: str | NotGiven = NOT_GIVEN,
        mode: Literal["markdown", "gfm"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Render a Markdown document

        Args:
          text: The Markdown text to render in HTML.

          context: The repository context to use when creating references in `gfm` mode. For
              example, setting `context` to `octo-org/octo-repo` will change the text `#42`
              into an HTML link to issue 42 in the `octo-org/octo-repo` repository.

          mode: The rendering mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return await self._post(
            "/markdown",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "context": context,
                    "mode": mode,
                },
                markdown_render_params.MarkdownRenderParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )

    async def render_raw(
        self,
        *,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        You must send Markdown as plain text (using a `Content-Type` header of
        `text/plain` or `text/x-markdown`) to this endpoint, rather than using JSON
        format. In raw mode, [GitHub Flavored Markdown](https://github.github.com/gfm/)
        is not supported and Markdown will be rendered in plain format like a README.md
        file. Markdown content must be 400 KB or less.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return await self._post(
            "/markdown/raw",
            body=await async_maybe_transform(body, markdown_render_raw_params.MarkdownRenderRawParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=str,
        )


class MarkdownResourceWithRawResponse:
    def __init__(self, markdown: MarkdownResource) -> None:
        self._markdown = markdown

        self.render = to_raw_response_wrapper(
            markdown.render,
        )
        self.render_raw = to_raw_response_wrapper(
            markdown.render_raw,
        )


class AsyncMarkdownResourceWithRawResponse:
    def __init__(self, markdown: AsyncMarkdownResource) -> None:
        self._markdown = markdown

        self.render = async_to_raw_response_wrapper(
            markdown.render,
        )
        self.render_raw = async_to_raw_response_wrapper(
            markdown.render_raw,
        )


class MarkdownResourceWithStreamingResponse:
    def __init__(self, markdown: MarkdownResource) -> None:
        self._markdown = markdown

        self.render = to_streamed_response_wrapper(
            markdown.render,
        )
        self.render_raw = to_streamed_response_wrapper(
            markdown.render_raw,
        )


class AsyncMarkdownResourceWithStreamingResponse:
    def __init__(self, markdown: AsyncMarkdownResource) -> None:
        self._markdown = markdown

        self.render = async_to_streamed_response_wrapper(
            markdown.render,
        )
        self.render_raw = async_to_streamed_response_wrapper(
            markdown.render_raw,
        )
