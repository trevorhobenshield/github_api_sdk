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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos import traffic_get_clones_params, traffic_get_views_params
from ....types.repos.traffic_get_clones_response import TrafficGetClonesResponse
from ....types.repos.traffic_get_views_response import TrafficGetViewsResponse
from .popular import (
    AsyncPopularResource,
    AsyncPopularResourceWithRawResponse,
    AsyncPopularResourceWithStreamingResponse,
    PopularResource,
    PopularResourceWithRawResponse,
    PopularResourceWithStreamingResponse,
)

__all__ = ["TrafficResource", "AsyncTrafficResource"]


class TrafficResource(SyncAPIResource):
    @cached_property
    def popular(self) -> PopularResource:
        return PopularResource(self._client)

    @cached_property
    def with_raw_response(self) -> TrafficResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return TrafficResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrafficResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return TrafficResourceWithStreamingResponse(self)

    def get_clones(
        self,
        repo: str,
        *,
        owner: str,
        per: Literal["day", "week"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrafficGetClonesResponse:
        """
        Get the total number of clones and breakdown per day or week for the last 14
        days. Timestamps are aligned to UTC midnight of the beginning of the day or
        week. Week begins on Monday.

        Args:
          per: The time frame to display results for.

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
            f"/repos/{owner}/{repo}/traffic/clones",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"per": per}, traffic_get_clones_params.TrafficGetClonesParams),
            ),
            cast_to=TrafficGetClonesResponse,
        )

    def get_views(
        self,
        repo: str,
        *,
        owner: str,
        per: Literal["day", "week"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrafficGetViewsResponse:
        """Get the total number of views and breakdown per day or week for the last 14
        days.

        Timestamps are aligned to UTC midnight of the beginning of the day or
        week. Week begins on Monday.

        Args:
          per: The time frame to display results for.

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
            f"/repos/{owner}/{repo}/traffic/views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"per": per}, traffic_get_views_params.TrafficGetViewsParams),
            ),
            cast_to=TrafficGetViewsResponse,
        )


class AsyncTrafficResource(AsyncAPIResource):
    @cached_property
    def popular(self) -> AsyncPopularResource:
        return AsyncPopularResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTrafficResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrafficResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrafficResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncTrafficResourceWithStreamingResponse(self)

    async def get_clones(
        self,
        repo: str,
        *,
        owner: str,
        per: Literal["day", "week"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrafficGetClonesResponse:
        """
        Get the total number of clones and breakdown per day or week for the last 14
        days. Timestamps are aligned to UTC midnight of the beginning of the day or
        week. Week begins on Monday.

        Args:
          per: The time frame to display results for.

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
            f"/repos/{owner}/{repo}/traffic/clones",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"per": per}, traffic_get_clones_params.TrafficGetClonesParams),
            ),
            cast_to=TrafficGetClonesResponse,
        )

    async def get_views(
        self,
        repo: str,
        *,
        owner: str,
        per: Literal["day", "week"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrafficGetViewsResponse:
        """Get the total number of views and breakdown per day or week for the last 14
        days.

        Timestamps are aligned to UTC midnight of the beginning of the day or
        week. Week begins on Monday.

        Args:
          per: The time frame to display results for.

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
            f"/repos/{owner}/{repo}/traffic/views",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"per": per}, traffic_get_views_params.TrafficGetViewsParams),
            ),
            cast_to=TrafficGetViewsResponse,
        )


class TrafficResourceWithRawResponse:
    def __init__(self, traffic: TrafficResource) -> None:
        self._traffic = traffic

        self.get_clones = to_raw_response_wrapper(
            traffic.get_clones,
        )
        self.get_views = to_raw_response_wrapper(
            traffic.get_views,
        )

    @cached_property
    def popular(self) -> PopularResourceWithRawResponse:
        return PopularResourceWithRawResponse(self._traffic.popular)


class AsyncTrafficResourceWithRawResponse:
    def __init__(self, traffic: AsyncTrafficResource) -> None:
        self._traffic = traffic

        self.get_clones = async_to_raw_response_wrapper(
            traffic.get_clones,
        )
        self.get_views = async_to_raw_response_wrapper(
            traffic.get_views,
        )

    @cached_property
    def popular(self) -> AsyncPopularResourceWithRawResponse:
        return AsyncPopularResourceWithRawResponse(self._traffic.popular)


class TrafficResourceWithStreamingResponse:
    def __init__(self, traffic: TrafficResource) -> None:
        self._traffic = traffic

        self.get_clones = to_streamed_response_wrapper(
            traffic.get_clones,
        )
        self.get_views = to_streamed_response_wrapper(
            traffic.get_views,
        )

    @cached_property
    def popular(self) -> PopularResourceWithStreamingResponse:
        return PopularResourceWithStreamingResponse(self._traffic.popular)


class AsyncTrafficResourceWithStreamingResponse:
    def __init__(self, traffic: AsyncTrafficResource) -> None:
        self._traffic = traffic

        self.get_clones = async_to_streamed_response_wrapper(
            traffic.get_clones,
        )
        self.get_views = async_to_streamed_response_wrapper(
            traffic.get_views,
        )

    @cached_property
    def popular(self) -> AsyncPopularResourceWithStreamingResponse:
        return AsyncPopularResourceWithStreamingResponse(self._traffic.popular)
