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
from ....types.orgs.actions import cache_list_usage_by_repository_params
from ....types.orgs.actions.cache_get_usage_response import CacheGetUsageResponse
from ....types.orgs.actions.cache_list_usage_by_repository_response import CacheListUsageByRepositoryResponse

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

    def get_usage(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheGetUsageResponse:
        """Gets the total GitHub Actions cache usage for an organization.

        The data fetched
        using this API is refreshed approximately every 5 minutes, so values returned
        from this endpoint may take at least 5 minutes to get updated.

        OAuth tokens and personal access tokens (classic) need the `read:org` scope to
        use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/cache/usage",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CacheGetUsageResponse,
        )

    def list_usage_by_repository(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheListUsageByRepositoryResponse:
        """Lists repositories and their GitHub Actions cache usage for an organization.

        The
        data fetched using this API is refreshed approximately every 5 minutes, so
        values returned from this endpoint may take at least 5 minutes to get updated.

        OAuth tokens and personal access tokens (classic) need the `read:org` scope to
        use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/cache/usage-by-repository",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    cache_list_usage_by_repository_params.CacheListUsageByRepositoryParams,
                ),
            ),
            cast_to=CacheListUsageByRepositoryResponse,
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

    async def get_usage(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheGetUsageResponse:
        """Gets the total GitHub Actions cache usage for an organization.

        The data fetched
        using this API is refreshed approximately every 5 minutes, so values returned
        from this endpoint may take at least 5 minutes to get updated.

        OAuth tokens and personal access tokens (classic) need the `read:org` scope to
        use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/cache/usage",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CacheGetUsageResponse,
        )

    async def list_usage_by_repository(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CacheListUsageByRepositoryResponse:
        """Lists repositories and their GitHub Actions cache usage for an organization.

        The
        data fetched using this API is refreshed approximately every 5 minutes, so
        values returned from this endpoint may take at least 5 minutes to get updated.

        OAuth tokens and personal access tokens (classic) need the `read:org` scope to
        use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/cache/usage-by-repository",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    cache_list_usage_by_repository_params.CacheListUsageByRepositoryParams,
                ),
            ),
            cast_to=CacheListUsageByRepositoryResponse,
        )


class CacheResourceWithRawResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.get_usage = to_raw_response_wrapper(
            cache.get_usage,
        )
        self.list_usage_by_repository = to_raw_response_wrapper(
            cache.list_usage_by_repository,
        )


class AsyncCacheResourceWithRawResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.get_usage = async_to_raw_response_wrapper(
            cache.get_usage,
        )
        self.list_usage_by_repository = async_to_raw_response_wrapper(
            cache.list_usage_by_repository,
        )


class CacheResourceWithStreamingResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

        self.get_usage = to_streamed_response_wrapper(
            cache.get_usage,
        )
        self.list_usage_by_repository = to_streamed_response_wrapper(
            cache.list_usage_by_repository,
        )


class AsyncCacheResourceWithStreamingResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

        self.get_usage = async_to_streamed_response_wrapper(
            cache.get_usage,
        )
        self.list_usage_by_repository = async_to_streamed_response_wrapper(
            cache.list_usage_by_repository,
        )
