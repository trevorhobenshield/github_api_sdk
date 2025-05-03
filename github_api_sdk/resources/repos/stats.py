from __future__ import annotations

import httpx

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...types.repos.stat_get_code_frequency_response import StatGetCodeFrequencyResponse
from ...types.repos.stat_get_commit_activity_response import StatGetCommitActivityResponse
from ...types.repos.stat_get_contributors_response import StatGetContributorsResponse
from ...types.repos.stat_get_participation_response import StatGetParticipationResponse
from ...types.repos.stat_get_punch_card_response import StatGetPunchCardResponse

__all__ = ["StatsResource", "AsyncStatsResource"]


class StatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return StatsResourceWithStreamingResponse(self)

    def get_code_frequency(
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
    ) -> StatGetCodeFrequencyResponse:
        """
        Returns a weekly aggregate of the number of additions and deletions pushed to a
        repository.

        > [!NOTE] This endpoint can only be used for repositories with fewer than 10,000
        > commits. If the repository contains 10,000 or more commits, a 422 status code
        > will be returned.

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
            f"/repos/{owner}/{repo}/stats/code_frequency",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetCodeFrequencyResponse,
        )

    def get_commit_activity(
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
    ) -> StatGetCommitActivityResponse:
        """Returns the last year of commit activity grouped by week.

        The `days` array is a
        group of commits per day, starting on `Sunday`.

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
            f"/repos/{owner}/{repo}/stats/commit_activity",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetCommitActivityResponse,
        )

    def get_contributors(
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
    ) -> StatGetContributorsResponse:
        """Returns the `total` number of commits authored by the contributor.

        In addition,
        the response includes a Weekly Hash (`weeks` array) with the following
        information:

        - `w` - Start of the week, given as a
          [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time).
        - `a` - Number of additions
        - `d` - Number of deletions
        - `c` - Number of commits

        > [!NOTE] This endpoint will return `0` values for all addition and deletion
        > counts in repositories with 10,000 or more commits.

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
            f"/repos/{owner}/{repo}/stats/contributors",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetContributorsResponse,
        )

    def get_participation(
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
    ) -> StatGetParticipationResponse:
        """Returns the total commit counts for the `owner` and total commit counts in
        `all`.

        `all` is everyone combined, including the `owner` in the last 52 weeks.
        If you'd like to get the commit counts for non-owners, you can subtract `owner`
        from `all`.

        The array order is oldest week (index 0) to most recent week.

        The most recent week is seven days ago at UTC midnight to today at UTC midnight.

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
            f"/repos/{owner}/{repo}/stats/participation",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetParticipationResponse,
        )

    def get_punch_card(
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
    ) -> StatGetPunchCardResponse:
        """
        Each array contains the day number, hour number, and number of commits:

        - `0-6`: Sunday - Saturday
        - `0-23`: Hour of day
        - Number of commits

        For example, `[2, 14, 25]` indicates that there were 25 total commits, during
        the 2:00pm hour on Tuesdays. All times are based on the time zone of individual
        commits.

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
            f"/repos/{owner}/{repo}/stats/punch_card",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetPunchCardResponse,
        )


class AsyncStatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncStatsResourceWithStreamingResponse(self)

    async def get_code_frequency(
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
    ) -> StatGetCodeFrequencyResponse:
        """
        Returns a weekly aggregate of the number of additions and deletions pushed to a
        repository.

        > [!NOTE] This endpoint can only be used for repositories with fewer than 10,000
        > commits. If the repository contains 10,000 or more commits, a 422 status code
        > will be returned.

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
            f"/repos/{owner}/{repo}/stats/code_frequency",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetCodeFrequencyResponse,
        )

    async def get_commit_activity(
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
    ) -> StatGetCommitActivityResponse:
        """Returns the last year of commit activity grouped by week.

        The `days` array is a
        group of commits per day, starting on `Sunday`.

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
            f"/repos/{owner}/{repo}/stats/commit_activity",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetCommitActivityResponse,
        )

    async def get_contributors(
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
    ) -> StatGetContributorsResponse:
        """Returns the `total` number of commits authored by the contributor.

        In addition,
        the response includes a Weekly Hash (`weeks` array) with the following
        information:

        - `w` - Start of the week, given as a
          [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time).
        - `a` - Number of additions
        - `d` - Number of deletions
        - `c` - Number of commits

        > [!NOTE] This endpoint will return `0` values for all addition and deletion
        > counts in repositories with 10,000 or more commits.

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
            f"/repos/{owner}/{repo}/stats/contributors",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetContributorsResponse,
        )

    async def get_participation(
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
    ) -> StatGetParticipationResponse:
        """Returns the total commit counts for the `owner` and total commit counts in
        `all`.

        `all` is everyone combined, including the `owner` in the last 52 weeks.
        If you'd like to get the commit counts for non-owners, you can subtract `owner`
        from `all`.

        The array order is oldest week (index 0) to most recent week.

        The most recent week is seven days ago at UTC midnight to today at UTC midnight.

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
            f"/repos/{owner}/{repo}/stats/participation",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetParticipationResponse,
        )

    async def get_punch_card(
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
    ) -> StatGetPunchCardResponse:
        """
        Each array contains the day number, hour number, and number of commits:

        - `0-6`: Sunday - Saturday
        - `0-23`: Hour of day
        - Number of commits

        For example, `[2, 14, 25]` indicates that there were 25 total commits, during
        the 2:00pm hour on Tuesdays. All times are based on the time zone of individual
        commits.

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
            f"/repos/{owner}/{repo}/stats/punch_card",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=StatGetPunchCardResponse,
        )


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.get_code_frequency = to_raw_response_wrapper(
            stats.get_code_frequency,
        )
        self.get_commit_activity = to_raw_response_wrapper(
            stats.get_commit_activity,
        )
        self.get_contributors = to_raw_response_wrapper(
            stats.get_contributors,
        )
        self.get_participation = to_raw_response_wrapper(
            stats.get_participation,
        )
        self.get_punch_card = to_raw_response_wrapper(
            stats.get_punch_card,
        )


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.get_code_frequency = async_to_raw_response_wrapper(
            stats.get_code_frequency,
        )
        self.get_commit_activity = async_to_raw_response_wrapper(
            stats.get_commit_activity,
        )
        self.get_contributors = async_to_raw_response_wrapper(
            stats.get_contributors,
        )
        self.get_participation = async_to_raw_response_wrapper(
            stats.get_participation,
        )
        self.get_punch_card = async_to_raw_response_wrapper(
            stats.get_punch_card,
        )


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

        self.get_code_frequency = to_streamed_response_wrapper(
            stats.get_code_frequency,
        )
        self.get_commit_activity = to_streamed_response_wrapper(
            stats.get_commit_activity,
        )
        self.get_contributors = to_streamed_response_wrapper(
            stats.get_contributors,
        )
        self.get_participation = to_streamed_response_wrapper(
            stats.get_participation,
        )
        self.get_punch_card = to_streamed_response_wrapper(
            stats.get_punch_card,
        )


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

        self.get_code_frequency = async_to_streamed_response_wrapper(
            stats.get_code_frequency,
        )
        self.get_commit_activity = async_to_streamed_response_wrapper(
            stats.get_commit_activity,
        )
        self.get_contributors = async_to_streamed_response_wrapper(
            stats.get_contributors,
        )
        self.get_participation = async_to_streamed_response_wrapper(
            stats.get_participation,
        )
        self.get_punch_card = async_to_streamed_response_wrapper(
            stats.get_punch_card,
        )
