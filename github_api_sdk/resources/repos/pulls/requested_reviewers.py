from __future__ import annotations

import builtins
from typing import List

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
from ....types.repos.pulls import requested_reviewer_remove_params, requested_reviewer_request_params
from ....types.repos.pulls.pull_request_simple import PullRequestSimple
from ....types.repos.pulls.requested_reviewer_list_response import RequestedReviewerListResponse

__all__ = ["RequestedReviewersResource", "AsyncRequestedReviewersResource"]


class RequestedReviewersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequestedReviewersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RequestedReviewersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequestedReviewersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RequestedReviewersResourceWithStreamingResponse(self)

    def list(
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
    ) -> RequestedReviewerListResponse:
        """Gets the users or teams whose review is requested for a pull request.

        Once a
        requested reviewer submits a review, they are no longer considered a requested
        reviewer. Their review will instead be returned by the
        [List reviews for a pull request](https://docs.github.com/rest/pulls/reviews#list-reviews-for-a-pull-request)
        operation.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RequestedReviewerListResponse,
        )

    def remove(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        reviewers: builtins.list[str],
        team_reviewers: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestSimple:
        """
        Removes review requests from a pull request for a given set of users and/or
        teams.

        Args:
          reviewers: An array of user `login`s that will be removed.

          team_reviewers: An array of team `slug`s that will be removed.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
            body=maybe_transform(
                {
                    "reviewers": reviewers,
                    "team_reviewers": team_reviewers,
                },
                requested_reviewer_remove_params.RequestedReviewerRemoveParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestSimple,
        )

    def request(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        reviewers: builtins.list[str] | NotGiven = NOT_GIVEN,
        team_reviewers: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestSimple:
        """Requests reviews for a pull request from a given set of users and/or teams.

        This
        endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Args:
          reviewers: An array of user `login`s that will be requested.

          team_reviewers: An array of team `slug`s that will be requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
            body=maybe_transform(
                {
                    "reviewers": reviewers,
                    "team_reviewers": team_reviewers,
                },
                requested_reviewer_request_params.RequestedReviewerRequestParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestSimple,
        )


class AsyncRequestedReviewersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequestedReviewersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequestedReviewersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequestedReviewersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRequestedReviewersResourceWithStreamingResponse(self)

    async def list(
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
    ) -> RequestedReviewerListResponse:
        """Gets the users or teams whose review is requested for a pull request.

        Once a
        requested reviewer submits a review, they are no longer considered a requested
        reviewer. Their review will instead be returned by the
        [List reviews for a pull request](https://docs.github.com/rest/pulls/reviews#list-reviews-for-a-pull-request)
        operation.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RequestedReviewerListResponse,
        )

    async def remove(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        reviewers: builtins.list[str],
        team_reviewers: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestSimple:
        """
        Removes review requests from a pull request for a given set of users and/or
        teams.

        Args:
          reviewers: An array of user `login`s that will be removed.

          team_reviewers: An array of team `slug`s that will be removed.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
            body=await async_maybe_transform(
                {
                    "reviewers": reviewers,
                    "team_reviewers": team_reviewers,
                },
                requested_reviewer_remove_params.RequestedReviewerRemoveParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestSimple,
        )

    async def request(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        reviewers: builtins.list[str] | NotGiven = NOT_GIVEN,
        team_reviewers: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestSimple:
        """Requests reviews for a pull request from a given set of users and/or teams.

        This
        endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Args:
          reviewers: An array of user `login`s that will be requested.

          team_reviewers: An array of team `slug`s that will be requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
            body=await async_maybe_transform(
                {
                    "reviewers": reviewers,
                    "team_reviewers": team_reviewers,
                },
                requested_reviewer_request_params.RequestedReviewerRequestParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestSimple,
        )


class RequestedReviewersResourceWithRawResponse:
    def __init__(self, requested_reviewers: RequestedReviewersResource) -> None:
        self._requested_reviewers = requested_reviewers

        self.list = to_raw_response_wrapper(
            requested_reviewers.list,
        )
        self.remove = to_raw_response_wrapper(
            requested_reviewers.remove,
        )
        self.request = to_raw_response_wrapper(
            requested_reviewers.request,
        )


class AsyncRequestedReviewersResourceWithRawResponse:
    def __init__(self, requested_reviewers: AsyncRequestedReviewersResource) -> None:
        self._requested_reviewers = requested_reviewers

        self.list = async_to_raw_response_wrapper(
            requested_reviewers.list,
        )
        self.remove = async_to_raw_response_wrapper(
            requested_reviewers.remove,
        )
        self.request = async_to_raw_response_wrapper(
            requested_reviewers.request,
        )


class RequestedReviewersResourceWithStreamingResponse:
    def __init__(self, requested_reviewers: RequestedReviewersResource) -> None:
        self._requested_reviewers = requested_reviewers

        self.list = to_streamed_response_wrapper(
            requested_reviewers.list,
        )
        self.remove = to_streamed_response_wrapper(
            requested_reviewers.remove,
        )
        self.request = to_streamed_response_wrapper(
            requested_reviewers.request,
        )


class AsyncRequestedReviewersResourceWithStreamingResponse:
    def __init__(self, requested_reviewers: AsyncRequestedReviewersResource) -> None:
        self._requested_reviewers = requested_reviewers

        self.list = async_to_streamed_response_wrapper(
            requested_reviewers.list,
        )
        self.remove = async_to_streamed_response_wrapper(
            requested_reviewers.remove,
        )
        self.request = async_to_streamed_response_wrapper(
            requested_reviewers.request,
        )
