from __future__ import annotations

import httpx
from typing_extensions import Literal

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs.insights.api import time_stat_by_actor_params, time_stat_by_user_params, time_stat_retrieve_params
from .....types.orgs.insights.api.time_stat_by_actor_response import TimeStatByActorResponse
from .....types.orgs.insights.api.time_stat_by_user_response import TimeStatByUserResponse
from .....types.orgs.insights.api.time_stat_retrieve_response import TimeStatRetrieveResponse

__all__ = ["TimeStatsResource", "AsyncTimeStatsResource"]


class TimeStatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimeStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return TimeStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return TimeStatsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        org: str,
        *,
        min_timestamp: str,
        timestamp_increment: str,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeStatRetrieveResponse:
        """
        Get the number of API requests and rate-limited requests made within an
        organization over a specified time period.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          timestamp_increment: The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/insights/api/time-stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "timestamp_increment": timestamp_increment,
                        "max_timestamp": max_timestamp,
                    },
                    time_stat_retrieve_params.TimeStatRetrieveParams,
                ),
            ),
            cast_to=TimeStatRetrieveResponse,
        )

    def by_actor(
        self,
        actor_id: int,
        *,
        org: str,
        actor_type: Literal["installation", "classic_pat", "fine_grained_pat", "oauth_app", "github_app_user_to_server"],
        min_timestamp: str,
        timestamp_increment: str,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeStatByActorResponse:
        """
        Get the number of API requests and rate-limited requests made within an
        organization by a specific actor within a specified time period.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          timestamp_increment: The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not actor_type:
            raise ValueError(f"Expected a non-empty value for `actor_type` but received {actor_type!r}")
        return self._get(
            f"/orgs/{org}/insights/api/time-stats/{actor_type}/{actor_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "timestamp_increment": timestamp_increment,
                        "max_timestamp": max_timestamp,
                    },
                    time_stat_by_actor_params.TimeStatByActorParams,
                ),
            ),
            cast_to=TimeStatByActorResponse,
        )

    def by_user(
        self,
        user_id: str,
        *,
        org: str,
        min_timestamp: str,
        timestamp_increment: str,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeStatByUserResponse:
        """
        Get the number of API requests and rate-limited requests made within an
        organization by a specific user over a specified time period.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          timestamp_increment: The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/orgs/{org}/insights/api/time-stats/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "timestamp_increment": timestamp_increment,
                        "max_timestamp": max_timestamp,
                    },
                    time_stat_by_user_params.TimeStatByUserParams,
                ),
            ),
            cast_to=TimeStatByUserResponse,
        )


class AsyncTimeStatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimeStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimeStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncTimeStatsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        org: str,
        *,
        min_timestamp: str,
        timestamp_increment: str,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeStatRetrieveResponse:
        """
        Get the number of API requests and rate-limited requests made within an
        organization over a specified time period.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          timestamp_increment: The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/insights/api/time-stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "timestamp_increment": timestamp_increment,
                        "max_timestamp": max_timestamp,
                    },
                    time_stat_retrieve_params.TimeStatRetrieveParams,
                ),
            ),
            cast_to=TimeStatRetrieveResponse,
        )

    async def by_actor(
        self,
        actor_id: int,
        *,
        org: str,
        actor_type: Literal["installation", "classic_pat", "fine_grained_pat", "oauth_app", "github_app_user_to_server"],
        min_timestamp: str,
        timestamp_increment: str,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeStatByActorResponse:
        """
        Get the number of API requests and rate-limited requests made within an
        organization by a specific actor within a specified time period.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          timestamp_increment: The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not actor_type:
            raise ValueError(f"Expected a non-empty value for `actor_type` but received {actor_type!r}")
        return await self._get(
            f"/orgs/{org}/insights/api/time-stats/{actor_type}/{actor_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "timestamp_increment": timestamp_increment,
                        "max_timestamp": max_timestamp,
                    },
                    time_stat_by_actor_params.TimeStatByActorParams,
                ),
            ),
            cast_to=TimeStatByActorResponse,
        )

    async def by_user(
        self,
        user_id: str,
        *,
        org: str,
        min_timestamp: str,
        timestamp_increment: str,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimeStatByUserResponse:
        """
        Get the number of API requests and rate-limited requests made within an
        organization by a specific user over a specified time period.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          timestamp_increment: The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/orgs/{org}/insights/api/time-stats/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "timestamp_increment": timestamp_increment,
                        "max_timestamp": max_timestamp,
                    },
                    time_stat_by_user_params.TimeStatByUserParams,
                ),
            ),
            cast_to=TimeStatByUserResponse,
        )


class TimeStatsResourceWithRawResponse:
    def __init__(self, time_stats: TimeStatsResource) -> None:
        self._time_stats = time_stats

        self.retrieve = to_raw_response_wrapper(
            time_stats.retrieve,
        )
        self.by_actor = to_raw_response_wrapper(
            time_stats.by_actor,
        )
        self.by_user = to_raw_response_wrapper(
            time_stats.by_user,
        )


class AsyncTimeStatsResourceWithRawResponse:
    def __init__(self, time_stats: AsyncTimeStatsResource) -> None:
        self._time_stats = time_stats

        self.retrieve = async_to_raw_response_wrapper(
            time_stats.retrieve,
        )
        self.by_actor = async_to_raw_response_wrapper(
            time_stats.by_actor,
        )
        self.by_user = async_to_raw_response_wrapper(
            time_stats.by_user,
        )


class TimeStatsResourceWithStreamingResponse:
    def __init__(self, time_stats: TimeStatsResource) -> None:
        self._time_stats = time_stats

        self.retrieve = to_streamed_response_wrapper(
            time_stats.retrieve,
        )
        self.by_actor = to_streamed_response_wrapper(
            time_stats.by_actor,
        )
        self.by_user = to_streamed_response_wrapper(
            time_stats.by_user,
        )


class AsyncTimeStatsResourceWithStreamingResponse:
    def __init__(self, time_stats: AsyncTimeStatsResource) -> None:
        self._time_stats = time_stats

        self.retrieve = async_to_streamed_response_wrapper(
            time_stats.retrieve,
        )
        self.by_actor = async_to_streamed_response_wrapper(
            time_stats.by_actor,
        )
        self.by_user = async_to_streamed_response_wrapper(
            time_stats.by_user,
        )
