from __future__ import annotations

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.git import blob_create_params
from ....types.repos.git.blob_create_response import BlobCreateResponse
from ....types.repos.git.blob_retrieve_response import BlobRetrieveResponse

__all__ = ["BlobsResource", "AsyncBlobsResource"]


class BlobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return BlobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return BlobsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        content: str,
        encoding: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlobCreateResponse:
        """
        Create a blob

        Args:
          content: The new blob's content.

          encoding: The encoding used for `content`. Currently, `"utf-8"` and `"base64"` are
              supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/git/blobs",
            body=maybe_transform(
                {
                    "content": content,
                    "encoding": encoding,
                },
                blob_create_params.BlobCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BlobCreateResponse,
        )

    def retrieve(
        self,
        file_sha: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlobRetrieveResponse:
        """
        The `content` in the response will always be Base64 encoded.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw blob data.
        - **`application/vnd.github+json`**: Returns a JSON representation of the blob
          with `content` as a base64 encoded string. This is the default if no media
          type is specified.

        **Note** This endpoint supports blobs up to 100 megabytes in size.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not file_sha:
            raise ValueError(f"Expected a non-empty value for `file_sha` but received {file_sha!r}")
        return self._get(
            f"/repos/{owner}/{repo}/git/blobs/{file_sha}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BlobRetrieveResponse,
        )


class AsyncBlobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncBlobsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        content: str,
        encoding: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlobCreateResponse:
        """
        Create a blob

        Args:
          content: The new blob's content.

          encoding: The encoding used for `content`. Currently, `"utf-8"` and `"base64"` are
              supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/git/blobs",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "encoding": encoding,
                },
                blob_create_params.BlobCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BlobCreateResponse,
        )

    async def retrieve(
        self,
        file_sha: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlobRetrieveResponse:
        """
        The `content` in the response will always be Base64 encoded.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw blob data.
        - **`application/vnd.github+json`**: Returns a JSON representation of the blob
          with `content` as a base64 encoded string. This is the default if no media
          type is specified.

        **Note** This endpoint supports blobs up to 100 megabytes in size.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not file_sha:
            raise ValueError(f"Expected a non-empty value for `file_sha` but received {file_sha!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/git/blobs/{file_sha}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BlobRetrieveResponse,
        )


class BlobsResourceWithRawResponse:
    def __init__(self, blobs: BlobsResource) -> None:
        self._blobs = blobs

        self.create = to_raw_response_wrapper(
            blobs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            blobs.retrieve,
        )


class AsyncBlobsResourceWithRawResponse:
    def __init__(self, blobs: AsyncBlobsResource) -> None:
        self._blobs = blobs

        self.create = async_to_raw_response_wrapper(
            blobs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            blobs.retrieve,
        )


class BlobsResourceWithStreamingResponse:
    def __init__(self, blobs: BlobsResource) -> None:
        self._blobs = blobs

        self.create = to_streamed_response_wrapper(
            blobs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            blobs.retrieve,
        )


class AsyncBlobsResourceWithStreamingResponse:
    def __init__(self, blobs: AsyncBlobsResource) -> None:
        self._blobs = blobs

        self.create = async_to_streamed_response_wrapper(
            blobs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            blobs.retrieve,
        )
