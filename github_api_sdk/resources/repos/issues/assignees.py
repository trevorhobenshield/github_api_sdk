from __future__ import annotations

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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.issue import Issue
from ....types.repos.issues import assignee_add_params, assignee_remove_params

__all__ = ["AssigneesResource", "AsyncAssigneesResource"]


class AssigneesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssigneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssigneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssigneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AssigneesResourceWithStreamingResponse(self)

    def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        assignees: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """Adds up to 10 assignees to an issue.

        Users already assigned to an issue are not
        replaced.

        Args:
          assignees: Usernames of people to assign this issue to. _NOTE: Only users with push access
              can add assignees to an issue. Assignees are silently ignored otherwise._

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/assignees",
            body=maybe_transform({"assignees": assignees}, assignee_add_params.AssigneeAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    def check(
        self,
        assignee: str,
        *,
        owner: str,
        repo: str,
        issue_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Checks if a user has permission to be assigned to a specific issue.

        If the `assignee` can be assigned to this issue, a `204` status code with no
        content is returned.

        Otherwise a `404` status code is returned.

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
        if not assignee:
            raise ValueError(f"Expected a non-empty value for `assignee` but received {assignee!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def remove(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        assignees: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        Removes one or more assignees from an issue.

        Args:
          assignees: Usernames of assignees to remove from an issue. _NOTE: Only users with push
              access can remove assignees from an issue. Assignees are silently ignored
              otherwise._

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/assignees",
            body=maybe_transform({"assignees": assignees}, assignee_remove_params.AssigneeRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )


class AsyncAssigneesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssigneesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssigneesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssigneesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAssigneesResourceWithStreamingResponse(self)

    async def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        assignees: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """Adds up to 10 assignees to an issue.

        Users already assigned to an issue are not
        replaced.

        Args:
          assignees: Usernames of people to assign this issue to. _NOTE: Only users with push access
              can add assignees to an issue. Assignees are silently ignored otherwise._

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/assignees",
            body=await async_maybe_transform({"assignees": assignees}, assignee_add_params.AssigneeAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    async def check(
        self,
        assignee: str,
        *,
        owner: str,
        repo: str,
        issue_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Checks if a user has permission to be assigned to a specific issue.

        If the `assignee` can be assigned to this issue, a `204` status code with no
        content is returned.

        Otherwise a `404` status code is returned.

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
        if not assignee:
            raise ValueError(f"Expected a non-empty value for `assignee` but received {assignee!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def remove(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        assignees: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        Removes one or more assignees from an issue.

        Args:
          assignees: Usernames of assignees to remove from an issue. _NOTE: Only users with push
              access can remove assignees from an issue. Assignees are silently ignored
              otherwise._

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/assignees",
            body=await async_maybe_transform({"assignees": assignees}, assignee_remove_params.AssigneeRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )


class AssigneesResourceWithRawResponse:
    def __init__(self, assignees: AssigneesResource) -> None:
        self._assignees = assignees

        self.add = to_raw_response_wrapper(
            assignees.add,
        )
        self.check = to_raw_response_wrapper(
            assignees.check,
        )
        self.remove = to_raw_response_wrapper(
            assignees.remove,
        )


class AsyncAssigneesResourceWithRawResponse:
    def __init__(self, assignees: AsyncAssigneesResource) -> None:
        self._assignees = assignees

        self.add = async_to_raw_response_wrapper(
            assignees.add,
        )
        self.check = async_to_raw_response_wrapper(
            assignees.check,
        )
        self.remove = async_to_raw_response_wrapper(
            assignees.remove,
        )


class AssigneesResourceWithStreamingResponse:
    def __init__(self, assignees: AssigneesResource) -> None:
        self._assignees = assignees

        self.add = to_streamed_response_wrapper(
            assignees.add,
        )
        self.check = to_streamed_response_wrapper(
            assignees.check,
        )
        self.remove = to_streamed_response_wrapper(
            assignees.remove,
        )


class AsyncAssigneesResourceWithStreamingResponse:
    def __init__(self, assignees: AsyncAssigneesResource) -> None:
        self._assignees = assignees

        self.add = async_to_streamed_response_wrapper(
            assignees.add,
        )
        self.check = async_to_streamed_response_wrapper(
            assignees.check,
        )
        self.remove = async_to_streamed_response_wrapper(
            assignees.remove,
        )
