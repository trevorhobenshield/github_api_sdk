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
from ....types.repos.pulls import merge_perform_params
from ....types.repos.pulls.merge_perform_response import MergePerformResponse

__all__ = ["MergeResource", "AsyncMergeResource"]


class MergeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MergeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MergeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MergeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MergeResourceWithStreamingResponse(self)

    def check(
        self,
        pull_number: int,
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
        """Checks if a pull request has been merged into the base branch.

        The HTTP status
        of the response indicates whether or not the pull request has been merged; the
        response body is empty.

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
        return self._get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/merge",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def perform(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        commit_message: str | NotGiven = NOT_GIVEN,
        commit_title: str | NotGiven = NOT_GIVEN,
        merge_method: Literal["merge", "squash", "rebase"] | NotGiven = NOT_GIVEN,
        sha: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MergePerformResponse:
        """Merges a pull request into the base branch.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Args:
          commit_message: Extra detail to append to automatic commit message.

          commit_title: Title for the automatic commit message.

          merge_method: The merge method to use.

          sha: SHA that pull request head must match to allow merge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._put(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/merge",
            body=maybe_transform(
                {
                    "commit_message": commit_message,
                    "commit_title": commit_title,
                    "merge_method": merge_method,
                    "sha": sha,
                },
                merge_perform_params.MergePerformParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MergePerformResponse,
        )


class AsyncMergeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMergeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMergeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMergeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMergeResourceWithStreamingResponse(self)

    async def check(
        self,
        pull_number: int,
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
        """Checks if a pull request has been merged into the base branch.

        The HTTP status
        of the response indicates whether or not the pull request has been merged; the
        response body is empty.

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
        return await self._get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/merge",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def perform(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        commit_message: str | NotGiven = NOT_GIVEN,
        commit_title: str | NotGiven = NOT_GIVEN,
        merge_method: Literal["merge", "squash", "rebase"] | NotGiven = NOT_GIVEN,
        sha: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MergePerformResponse:
        """Merges a pull request into the base branch.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Args:
          commit_message: Extra detail to append to automatic commit message.

          commit_title: Title for the automatic commit message.

          merge_method: The merge method to use.

          sha: SHA that pull request head must match to allow merge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/merge",
            body=await async_maybe_transform(
                {
                    "commit_message": commit_message,
                    "commit_title": commit_title,
                    "merge_method": merge_method,
                    "sha": sha,
                },
                merge_perform_params.MergePerformParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=MergePerformResponse,
        )


class MergeResourceWithRawResponse:
    def __init__(self, merge: MergeResource) -> None:
        self._merge = merge

        self.check = to_raw_response_wrapper(
            merge.check,
        )
        self.perform = to_raw_response_wrapper(
            merge.perform,
        )


class AsyncMergeResourceWithRawResponse:
    def __init__(self, merge: AsyncMergeResource) -> None:
        self._merge = merge

        self.check = async_to_raw_response_wrapper(
            merge.check,
        )
        self.perform = async_to_raw_response_wrapper(
            merge.perform,
        )


class MergeResourceWithStreamingResponse:
    def __init__(self, merge: MergeResource) -> None:
        self._merge = merge

        self.check = to_streamed_response_wrapper(
            merge.check,
        )
        self.perform = to_streamed_response_wrapper(
            merge.perform,
        )


class AsyncMergeResourceWithStreamingResponse:
    def __init__(self, merge: AsyncMergeResource) -> None:
        self._merge = merge

        self.check = async_to_streamed_response_wrapper(
            merge.check,
        )
        self.perform = async_to_streamed_response_wrapper(
            merge.perform,
        )
