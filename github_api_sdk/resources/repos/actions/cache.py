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
from ....types.repos.actions.actions_cache_usage import ActionsCacheUsage

__all__ = ["CacheResource", "AsyncCacheResource"]


class CacheResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CacheResourceWithStreamingResponse(self)

    def usage(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsCacheUsage:
        """Gets GitHub Actions cache usage for a repository.

        The data fetched using this
        API is refreshed approximately every 5 minutes, so values returned from this
        endpoint may take at least 5 minutes to get updated.

        Anyone with read access to the repository can use this endpoint.

        If the repository is private, OAuth tokens and personal access tokens (classic)
        need the `repo` scope to use this endpoint.

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
        return self._get(
            f"/repos/{owner}/{repo}/actions/cache/usage",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionsCacheUsage,
        )


class AsyncCacheResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCacheResourceWithStreamingResponse(self)

    async def usage(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsCacheUsage:
        """Gets GitHub Actions cache usage for a repository.

        The data fetched using this
        API is refreshed approximately every 5 minutes, so values returned from this
        endpoint may take at least 5 minutes to get updated.

        Anyone with read access to the repository can use this endpoint.

        If the repository is private, OAuth tokens and personal access tokens (classic)
        need the `repo` scope to use this endpoint.

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
        return await self._get(
            f"/repos/{owner}/{repo}/actions/cache/usage",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionsCacheUsage,
        )


class CacheResourceWithRawResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.usage = to_raw_response_wrapper(
            cache.usage,
        )


class AsyncCacheResourceWithRawResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.usage = async_to_raw_response_wrapper(
            cache.usage,
        )


class CacheResourceWithStreamingResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.usage = to_streamed_response_wrapper(
            cache.usage,
        )


class AsyncCacheResourceWithStreamingResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.usage = async_to_streamed_response_wrapper(
            cache.usage,
        )
