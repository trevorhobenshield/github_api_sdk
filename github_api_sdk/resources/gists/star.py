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
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query

__all__ = ["StarResource", "AsyncStarResource"]


class StarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return StarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return StarResourceWithStreamingResponse(self)

    def create(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Note that you'll need to set `Content-Length` to zero when calling out to this
        endpoint. For more information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/gists/{gist_id}/star",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def delete(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Unstar a gist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/gists/{gist_id}/star",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def check(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Check if a gist is starred

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/gists/{gist_id}/star",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncStarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncStarResourceWithStreamingResponse(self)

    async def create(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Note that you'll need to set `Content-Length` to zero when calling out to this
        endpoint. For more information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/gists/{gist_id}/star",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def delete(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Unstar a gist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/gists/{gist_id}/star",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def check(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Check if a gist is starred

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/gists/{gist_id}/star",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class StarResourceWithRawResponse:
    def __init__(self, star: StarResource) -> None:
        self._star = star

        self.create = to_raw_response_wrapper(
            star.create,
        )
        self.delete = to_raw_response_wrapper(
            star.delete,
        )
        self.check = to_raw_response_wrapper(
            star.check,
        )


class AsyncStarResourceWithRawResponse:
    def __init__(self, star: AsyncStarResource) -> None:
        self._star = star

        self.create = async_to_raw_response_wrapper(
            star.create,
        )
        self.delete = async_to_raw_response_wrapper(
            star.delete,
        )
        self.check = async_to_raw_response_wrapper(
            star.check,
        )


class StarResourceWithStreamingResponse:
    def __init__(self, star: StarResource) -> None:
        self._star = star

        self.create = to_streamed_response_wrapper(
            star.create,
        )
        self.delete = to_streamed_response_wrapper(
            star.delete,
        )
        self.check = to_streamed_response_wrapper(
            star.check,
        )


class AsyncStarResourceWithStreamingResponse:
    def __init__(self, star: AsyncStarResource) -> None:
        self._star = star

        self.create = async_to_streamed_response_wrapper(
            star.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            star.delete,
        )
        self.check = async_to_streamed_response_wrapper(
            star.check,
        )
