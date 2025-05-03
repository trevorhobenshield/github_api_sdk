from __future__ import annotations

import httpx
from typing_extensions import Literal

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
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.actions import cach_delete_params, cach_list_params
from ....types.repos.actions.actions_cache_list import ActionsCacheList

__all__ = ["CachesResource", "AsyncCachesResource"]


class CachesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CachesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CachesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CachesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CachesResourceWithStreamingResponse(self)

    def list(
        self,
        repo: str,
        *,
        owner: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "last_accessed_at", "size_in_bytes"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsCacheList:
        """
        Lists the GitHub Actions caches for a repository.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
          direction: The direction to sort the results by.

          key: An explicit key or prefix for identifying the cache

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          ref: The full Git reference for narrowing down the cache. The `ref` for a branch
              should be formatted as `refs/heads/<branch name>`. To reference a pull request
              use `refs/pull/<number>/merge`.

          sort: The property to sort the results by. `created_at` means when the cache was
              created. `last_accessed_at` means when the cache was last accessed.
              `size_in_bytes` is the size of the cache in bytes.

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
            f"/repos/{owner}/{repo}/actions/caches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "key": key,
                        "page": page,
                        "per_page": per_page,
                        "ref": ref,
                        "sort": sort,
                    },
                    cach_list_params.CachListParams,
                ),
            ),
            cast_to=ActionsCacheList,
        )

    def delete(
        self,
        repo: str,
        *,
        owner: str,
        key: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsCacheList:
        """
        Deletes one or more GitHub Actions caches for a repository, using a complete
        cache key. By default, all caches that match the provided key are deleted, but
        you can optionally provide a Git ref to restrict deletions to caches that match
        both the provided key and the Git ref.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
          key: A key for identifying the cache.

          ref: The full Git reference for narrowing down the cache. The `ref` for a branch
              should be formatted as `refs/heads/<branch name>`. To reference a pull request
              use `refs/pull/<number>/merge`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._delete(
            f"/repos/{owner}/{repo}/actions/caches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "key": key,
                        "ref": ref,
                    },
                    cach_delete_params.CachDeleteParams,
                ),
            ),
            cast_to=ActionsCacheList,
        )

    def delete_by_id(
        self,
        cache_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a GitHub Actions cache for a repository, using a cache ID.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/actions/caches/{cache_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncCachesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCachesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCachesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCachesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCachesResourceWithStreamingResponse(self)

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        key: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "last_accessed_at", "size_in_bytes"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsCacheList:
        """
        Lists the GitHub Actions caches for a repository.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
          direction: The direction to sort the results by.

          key: An explicit key or prefix for identifying the cache

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          ref: The full Git reference for narrowing down the cache. The `ref` for a branch
              should be formatted as `refs/heads/<branch name>`. To reference a pull request
              use `refs/pull/<number>/merge`.

          sort: The property to sort the results by. `created_at` means when the cache was
              created. `last_accessed_at` means when the cache was last accessed.
              `size_in_bytes` is the size of the cache in bytes.

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
            f"/repos/{owner}/{repo}/actions/caches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "key": key,
                        "page": page,
                        "per_page": per_page,
                        "ref": ref,
                        "sort": sort,
                    },
                    cach_list_params.CachListParams,
                ),
            ),
            cast_to=ActionsCacheList,
        )

    async def delete(
        self,
        repo: str,
        *,
        owner: str,
        key: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsCacheList:
        """
        Deletes one or more GitHub Actions caches for a repository, using a complete
        cache key. By default, all caches that match the provided key are deleted, but
        you can optionally provide a Git ref to restrict deletions to caches that match
        both the provided key and the Git ref.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
          key: A key for identifying the cache.

          ref: The full Git reference for narrowing down the cache. The `ref` for a branch
              should be formatted as `refs/heads/<branch name>`. To reference a pull request
              use `refs/pull/<number>/merge`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._delete(
            f"/repos/{owner}/{repo}/actions/caches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "key": key,
                        "ref": ref,
                    },
                    cach_delete_params.CachDeleteParams,
                ),
            ),
            cast_to=ActionsCacheList,
        )

    async def delete_by_id(
        self,
        cache_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a GitHub Actions cache for a repository, using a cache ID.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/actions/caches/{cache_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class CachesResourceWithRawResponse:
    def __init__(self, caches: CachesResource) -> None:
        self._caches = caches

        self.list = to_raw_response_wrapper(
            caches.list,
        )
        self.delete = to_raw_response_wrapper(
            caches.delete,
        )
        self.delete_by_id = to_raw_response_wrapper(
            caches.delete_by_id,
        )


class AsyncCachesResourceWithRawResponse:
    def __init__(self, caches: AsyncCachesResource) -> None:
        self._caches = caches

        self.list = async_to_raw_response_wrapper(
            caches.list,
        )
        self.delete = async_to_raw_response_wrapper(
            caches.delete,
        )
        self.delete_by_id = async_to_raw_response_wrapper(
            caches.delete_by_id,
        )


class CachesResourceWithStreamingResponse:
    def __init__(self, caches: CachesResource) -> None:
        self._caches = caches

        self.list = to_streamed_response_wrapper(
            caches.list,
        )
        self.delete = to_streamed_response_wrapper(
            caches.delete,
        )
        self.delete_by_id = to_streamed_response_wrapper(
            caches.delete_by_id,
        )


class AsyncCachesResourceWithStreamingResponse:
    def __init__(self, caches: AsyncCachesResource) -> None:
        self._caches = caches

        self.list = async_to_streamed_response_wrapper(
            caches.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            caches.delete,
        )
        self.delete_by_id = async_to_streamed_response_wrapper(
            caches.delete_by_id,
        )
