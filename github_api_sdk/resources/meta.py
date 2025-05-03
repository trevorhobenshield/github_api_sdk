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
from ..types.meta_retrieve_response import MetaRetrieveResponse

__all__ = ["MetaResource", "AsyncMetaResource"]


class MetaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MetaResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetaRetrieveResponse:
        """Returns meta information about GitHub, including a list of GitHub's IP
        addresses.

        For more information, see
        "[About GitHub's IP addresses](https://docs.github.com/articles/about-github-s-ip-addresses/)."

        The API's response also includes a list of GitHub's domain names.

        The values shown in the documentation's response are example values. You must
        always query the API directly to get the latest values.

        > [!NOTE] This endpoint returns both IPv4 and IPv6 addresses. However, not all
        > features support IPv6. You should refer to the specific documentation for each
        > feature to determine if IPv6 is supported.
        """
        return self._get(
            "/meta",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MetaRetrieveResponse,
        )


class AsyncMetaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMetaResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetaRetrieveResponse:
        """Returns meta information about GitHub, including a list of GitHub's IP
        addresses.

        For more information, see
        "[About GitHub's IP addresses](https://docs.github.com/articles/about-github-s-ip-addresses/)."

        The API's response also includes a list of GitHub's domain names.

        The values shown in the documentation's response are example values. You must
        always query the API directly to get the latest values.

        > [!NOTE] This endpoint returns both IPv4 and IPv6 addresses. However, not all
        > features support IPv6. You should refer to the specific documentation for each
        > feature to determine if IPv6 is supported.
        """
        return await self._get(
            "/meta",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MetaRetrieveResponse,
        )


class MetaResourceWithRawResponse:
    def __init__(self, meta: MetaResource) -> None:
        self._meta = meta

        self.retrieve = to_raw_response_wrapper(
            meta.retrieve,
        )


class AsyncMetaResourceWithRawResponse:
    def __init__(self, meta: AsyncMetaResource) -> None:
        self._meta = meta

        self.retrieve = async_to_raw_response_wrapper(
            meta.retrieve,
        )


class MetaResourceWithStreamingResponse:
    def __init__(self, meta: MetaResource) -> None:
        self._meta = meta

        self.retrieve = to_streamed_response_wrapper(
            meta.retrieve,
        )


class AsyncMetaResourceWithStreamingResponse:
    def __init__(self, meta: AsyncMetaResource) -> None:
        self._meta = meta

        self.retrieve = async_to_streamed_response_wrapper(
            meta.retrieve,
        )
