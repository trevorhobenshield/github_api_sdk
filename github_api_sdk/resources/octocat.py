from __future__ import annotations

import httpx

from .._base_client import make_request_options
from .._compat import cached_property
from .._resource import AsyncAPIResource, SyncAPIResource
from .._response import (
    AsyncBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    BinaryAPIResponse,
    StreamedBinaryAPIResponse,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
)
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from .._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ..types import octocat_retrieve_params

__all__ = ["OctocatResource", "AsyncOctocatResource"]


class OctocatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OctocatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return OctocatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OctocatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return OctocatResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        s: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Get the octocat as ASCII art

        Args:
          s: The words to show in Octocat's speech bubble

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octocat-stream", **(extra_headers or {})}
        return self._get(
            "/octocat",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"s": s}, octocat_retrieve_params.OctocatRetrieveParams),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncOctocatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOctocatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOctocatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOctocatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncOctocatResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        s: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Get the octocat as ASCII art

        Args:
          s: The words to show in Octocat's speech bubble

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octocat-stream", **(extra_headers or {})}
        return await self._get(
            "/octocat",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"s": s}, octocat_retrieve_params.OctocatRetrieveParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class OctocatResourceWithRawResponse:
    def __init__(self, octocat: OctocatResource) -> None:
        self._octocat = octocat

        self.retrieve = to_custom_raw_response_wrapper(
            octocat.retrieve,
            BinaryAPIResponse,
        )


class AsyncOctocatResourceWithRawResponse:
    def __init__(self, octocat: AsyncOctocatResource) -> None:
        self._octocat = octocat

        self.retrieve = async_to_custom_raw_response_wrapper(
            octocat.retrieve,
            AsyncBinaryAPIResponse,
        )


class OctocatResourceWithStreamingResponse:
    def __init__(self, octocat: OctocatResource) -> None:
        self._octocat = octocat

        self.retrieve = to_custom_streamed_response_wrapper(
            octocat.retrieve,
            StreamedBinaryAPIResponse,
        )


class AsyncOctocatResourceWithStreamingResponse:
    def __init__(self, octocat: AsyncOctocatResource) -> None:
        self._octocat = octocat

        self.retrieve = async_to_custom_streamed_response_wrapper(
            octocat.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
