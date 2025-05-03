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
from ....types.repos.traffic.popular_get_top_paths_response import PopularGetTopPathsResponse
from ....types.repos.traffic.popular_get_top_referrers_response import PopularGetTopReferrersResponse

__all__ = ["PopularResource", "AsyncPopularResource"]


class PopularResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PopularResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PopularResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PopularResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PopularResourceWithStreamingResponse(self)

    def get_top_paths(
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
    ) -> PopularGetTopPathsResponse:
        """
        Get the top 10 popular contents over the last 14 days.

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
            f"/repos/{owner}/{repo}/traffic/popular/paths",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PopularGetTopPathsResponse,
        )

    def get_top_referrers(
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
    ) -> PopularGetTopReferrersResponse:
        """
        Get the top 10 referrers over the last 14 days.

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
            f"/repos/{owner}/{repo}/traffic/popular/referrers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PopularGetTopReferrersResponse,
        )


class AsyncPopularResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPopularResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPopularResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPopularResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPopularResourceWithStreamingResponse(self)

    async def get_top_paths(
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
    ) -> PopularGetTopPathsResponse:
        """
        Get the top 10 popular contents over the last 14 days.

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
            f"/repos/{owner}/{repo}/traffic/popular/paths",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PopularGetTopPathsResponse,
        )

    async def get_top_referrers(
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
    ) -> PopularGetTopReferrersResponse:
        """
        Get the top 10 referrers over the last 14 days.

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
            f"/repos/{owner}/{repo}/traffic/popular/referrers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PopularGetTopReferrersResponse,
        )


class PopularResourceWithRawResponse:
    def __init__(self, popular: PopularResource) -> None:
        self._popular = popular

        self.get_top_paths = to_raw_response_wrapper(
            popular.get_top_paths,
        )
        self.get_top_referrers = to_raw_response_wrapper(
            popular.get_top_referrers,
        )


class AsyncPopularResourceWithRawResponse:
    def __init__(self, popular: AsyncPopularResource) -> None:
        self._popular = popular

        self.get_top_paths = async_to_raw_response_wrapper(
            popular.get_top_paths,
        )
        self.get_top_referrers = async_to_raw_response_wrapper(
            popular.get_top_referrers,
        )


class PopularResourceWithStreamingResponse:
    def __init__(self, popular: PopularResource) -> None:
        self._popular = popular

        self.get_top_paths = to_streamed_response_wrapper(
            popular.get_top_paths,
        )
        self.get_top_referrers = to_streamed_response_wrapper(
            popular.get_top_referrers,
        )


class AsyncPopularResourceWithStreamingResponse:
    def __init__(self, popular: AsyncPopularResource) -> None:
        self._popular = popular

        self.get_top_paths = async_to_streamed_response_wrapper(
            popular.get_top_paths,
        )
        self.get_top_referrers = async_to_streamed_response_wrapper(
            popular.get_top_referrers,
        )
