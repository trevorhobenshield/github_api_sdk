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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query

__all__ = ["ArchiveResource", "AsyncArchiveResource"]


class ArchiveResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArchiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ArchiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArchiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ArchiveResourceWithStreamingResponse(self)

    def delete(
        self,
        migration_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a previous migration archive.

        Migration archives are automatically
        deleted after seven days.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/migrations/{migration_id}/archive",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def download(
        self,
        migration_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Fetches the URL to a migration archive.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/orgs/{org}/migrations/{migration_id}/archive",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncArchiveResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArchiveResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArchiveResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArchiveResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncArchiveResourceWithStreamingResponse(self)

    async def delete(
        self,
        migration_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a previous migration archive.

        Migration archives are automatically
        deleted after seven days.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/migrations/{migration_id}/archive",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def download(
        self,
        migration_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Fetches the URL to a migration archive.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/orgs/{org}/migrations/{migration_id}/archive",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ArchiveResourceWithRawResponse:
    def __init__(self, archive: ArchiveResource) -> None:
        self._archive = archive

        self.delete = to_raw_response_wrapper(
            archive.delete,
        )
        self.download = to_raw_response_wrapper(
            archive.download,
        )


class AsyncArchiveResourceWithRawResponse:
    def __init__(self, archive: AsyncArchiveResource) -> None:
        self._archive = archive

        self.delete = async_to_raw_response_wrapper(
            archive.delete,
        )
        self.download = async_to_raw_response_wrapper(
            archive.download,
        )


class ArchiveResourceWithStreamingResponse:
    def __init__(self, archive: ArchiveResource) -> None:
        self._archive = archive

        self.delete = to_streamed_response_wrapper(
            archive.delete,
        )
        self.download = to_streamed_response_wrapper(
            archive.download,
        )


class AsyncArchiveResourceWithStreamingResponse:
    def __init__(self, archive: AsyncArchiveResource) -> None:
        self._archive = archive

        self.delete = async_to_streamed_response_wrapper(
            archive.delete,
        )
        self.download = async_to_streamed_response_wrapper(
            archive.download,
        )
