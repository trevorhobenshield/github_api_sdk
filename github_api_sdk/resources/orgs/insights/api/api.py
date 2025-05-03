from __future__ import annotations

from typing import List

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
from .....types.orgs.insights import api_route_stats_params, api_subject_stats_params, api_user_stats_params
from .....types.orgs.insights.api_route_stats_response import APIRouteStatsResponse
from .....types.orgs.insights.api_subject_stats_response import APISubjectStatsResponse
from .....types.orgs.insights.api_user_stats_response import APIUserStatsResponse
from .summary_stats import (
    AsyncSummaryStatsResource,
    AsyncSummaryStatsResourceWithRawResponse,
    AsyncSummaryStatsResourceWithStreamingResponse,
    SummaryStatsResource,
    SummaryStatsResourceWithRawResponse,
    SummaryStatsResourceWithStreamingResponse,
)
from .time_stats import (
    AsyncTimeStatsResource,
    AsyncTimeStatsResourceWithRawResponse,
    AsyncTimeStatsResourceWithStreamingResponse,
    TimeStatsResource,
    TimeStatsResourceWithRawResponse,
    TimeStatsResourceWithStreamingResponse,
)

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(SyncAPIResource):
    @cached_property
    def summary_stats(self) -> SummaryStatsResource:
        return SummaryStatsResource(self._client)

    @cached_property
    def time_stats(self) -> TimeStatsResource:
        return TimeStatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return APIResourceWithStreamingResponse(self)

    def route_stats(
        self,
        actor_id: int,
        *,
        org: str,
        actor_type: Literal["installation", "classic_pat", "fine_grained_pat", "oauth_app", "github_app_user_to_server"],
        min_timestamp: str,
        api_route_substring: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: list[
            Literal[
                "last_rate_limited_timestamp",
                "last_request_timestamp",
                "rate_limited_request_count",
                "http_method",
                "api_route",
                "total_request_count",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIRouteStatsResponse:
        """
        Get API request count statistics for an actor broken down by route within a
        specified time frame.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          api_route_substring: Providing a substring will filter results where the API route contains the
              substring. This is a case-insensitive search.

          direction: The direction to sort the results by.

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

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
            f"/orgs/{org}/insights/api/route-stats/{actor_type}/{actor_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "api_route_substring": api_route_substring,
                        "direction": direction,
                        "max_timestamp": max_timestamp,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    api_route_stats_params.APIRouteStatsParams,
                ),
            ),
            cast_to=APIRouteStatsResponse,
        )

    def subject_stats(
        self,
        org: str,
        *,
        min_timestamp: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: list[
            Literal[
                "last_rate_limited_timestamp",
                "last_request_timestamp",
                "rate_limited_request_count",
                "subject_name",
                "total_request_count",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        subject_name_substring: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APISubjectStatsResponse:
        """
        Get API request statistics for all subjects within an organization within a
        specified time frame. Subjects can be users or GitHub Apps.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          direction: The direction to sort the results by.

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          subject_name_substring: Providing a substring will filter results where the subject name contains the
              substring. This is a case-insensitive search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/insights/api/subject-stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "direction": direction,
                        "max_timestamp": max_timestamp,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "subject_name_substring": subject_name_substring,
                    },
                    api_subject_stats_params.APISubjectStatsParams,
                ),
            ),
            cast_to=APISubjectStatsResponse,
        )

    def user_stats(
        self,
        user_id: str,
        *,
        org: str,
        min_timestamp: str,
        actor_name_substring: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: list[
            Literal[
                "last_rate_limited_timestamp",
                "last_request_timestamp",
                "rate_limited_request_count",
                "subject_name",
                "total_request_count",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIUserStatsResponse:
        """
        Get API usage statistics within an organization for a user broken down by the
        type of access.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          actor_name_substring: Providing a substring will filter results where the actor name contains the
              substring. This is a case-insensitive search.

          direction: The direction to sort the results by.

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

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
            f"/orgs/{org}/insights/api/user-stats/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "actor_name_substring": actor_name_substring,
                        "direction": direction,
                        "max_timestamp": max_timestamp,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    api_user_stats_params.APIUserStatsParams,
                ),
            ),
            cast_to=APIUserStatsResponse,
        )


class AsyncAPIResource(AsyncAPIResource):
    @cached_property
    def summary_stats(self) -> AsyncSummaryStatsResource:
        return AsyncSummaryStatsResource(self._client)

    @cached_property
    def time_stats(self) -> AsyncTimeStatsResource:
        return AsyncTimeStatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAPIResourceWithStreamingResponse(self)

    async def route_stats(
        self,
        actor_id: int,
        *,
        org: str,
        actor_type: Literal["installation", "classic_pat", "fine_grained_pat", "oauth_app", "github_app_user_to_server"],
        min_timestamp: str,
        api_route_substring: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: list[
            Literal[
                "last_rate_limited_timestamp",
                "last_request_timestamp",
                "rate_limited_request_count",
                "http_method",
                "api_route",
                "total_request_count",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIRouteStatsResponse:
        """
        Get API request count statistics for an actor broken down by route within a
        specified time frame.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          api_route_substring: Providing a substring will filter results where the API route contains the
              substring. This is a case-insensitive search.

          direction: The direction to sort the results by.

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

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
            f"/orgs/{org}/insights/api/route-stats/{actor_type}/{actor_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "api_route_substring": api_route_substring,
                        "direction": direction,
                        "max_timestamp": max_timestamp,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    api_route_stats_params.APIRouteStatsParams,
                ),
            ),
            cast_to=APIRouteStatsResponse,
        )

    async def subject_stats(
        self,
        org: str,
        *,
        min_timestamp: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: list[
            Literal[
                "last_rate_limited_timestamp",
                "last_request_timestamp",
                "rate_limited_request_count",
                "subject_name",
                "total_request_count",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        subject_name_substring: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APISubjectStatsResponse:
        """
        Get API request statistics for all subjects within an organization within a
        specified time frame. Subjects can be users or GitHub Apps.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          direction: The direction to sort the results by.

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          subject_name_substring: Providing a substring will filter results where the subject name contains the
              substring. This is a case-insensitive search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/insights/api/subject-stats",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "direction": direction,
                        "max_timestamp": max_timestamp,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "subject_name_substring": subject_name_substring,
                    },
                    api_subject_stats_params.APISubjectStatsParams,
                ),
            ),
            cast_to=APISubjectStatsResponse,
        )

    async def user_stats(
        self,
        user_id: str,
        *,
        org: str,
        min_timestamp: str,
        actor_name_substring: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        max_timestamp: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: list[
            Literal[
                "last_rate_limited_timestamp",
                "last_request_timestamp",
                "rate_limited_request_count",
                "subject_name",
                "total_request_count",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIUserStatsResponse:
        """
        Get API usage statistics within an organization for a user broken down by the
        type of access.

        Args:
          min_timestamp: The minimum timestamp to query for stats. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          actor_name_substring: Providing a substring will filter results where the actor name contains the
              substring. This is a case-insensitive search.

          direction: The direction to sort the results by.

          max_timestamp: The maximum timestamp to query for stats. Defaults to the time 30 days ago. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

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
            f"/orgs/{org}/insights/api/user-stats/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "min_timestamp": min_timestamp,
                        "actor_name_substring": actor_name_substring,
                        "direction": direction,
                        "max_timestamp": max_timestamp,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    api_user_stats_params.APIUserStatsParams,
                ),
            ),
            cast_to=APIUserStatsResponse,
        )


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.route_stats = to_raw_response_wrapper(
            api.route_stats,
        )
        self.subject_stats = to_raw_response_wrapper(
            api.subject_stats,
        )
        self.user_stats = to_raw_response_wrapper(
            api.user_stats,
        )

    @cached_property
    def summary_stats(self) -> SummaryStatsResourceWithRawResponse:
        return SummaryStatsResourceWithRawResponse(self._api.summary_stats)

    @cached_property
    def time_stats(self) -> TimeStatsResourceWithRawResponse:
        return TimeStatsResourceWithRawResponse(self._api.time_stats)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.route_stats = async_to_raw_response_wrapper(
            api.route_stats,
        )
        self.subject_stats = async_to_raw_response_wrapper(
            api.subject_stats,
        )
        self.user_stats = async_to_raw_response_wrapper(
            api.user_stats,
        )

    @cached_property
    def summary_stats(self) -> AsyncSummaryStatsResourceWithRawResponse:
        return AsyncSummaryStatsResourceWithRawResponse(self._api.summary_stats)

    @cached_property
    def time_stats(self) -> AsyncTimeStatsResourceWithRawResponse:
        return AsyncTimeStatsResourceWithRawResponse(self._api.time_stats)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

        self.route_stats = to_streamed_response_wrapper(
            api.route_stats,
        )
        self.subject_stats = to_streamed_response_wrapper(
            api.subject_stats,
        )
        self.user_stats = to_streamed_response_wrapper(
            api.user_stats,
        )

    @cached_property
    def summary_stats(self) -> SummaryStatsResourceWithStreamingResponse:
        return SummaryStatsResourceWithStreamingResponse(self._api.summary_stats)

    @cached_property
    def time_stats(self) -> TimeStatsResourceWithStreamingResponse:
        return TimeStatsResourceWithStreamingResponse(self._api.time_stats)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

        self.route_stats = async_to_streamed_response_wrapper(
            api.route_stats,
        )
        self.subject_stats = async_to_streamed_response_wrapper(
            api.subject_stats,
        )
        self.user_stats = async_to_streamed_response_wrapper(
            api.user_stats,
        )

    @cached_property
    def summary_stats(self) -> AsyncSummaryStatsResourceWithStreamingResponse:
        return AsyncSummaryStatsResourceWithStreamingResponse(self._api.summary_stats)

    @cached_property
    def time_stats(self) -> AsyncTimeStatsResourceWithStreamingResponse:
        return AsyncTimeStatsResourceWithStreamingResponse(self._api.time_stats)
