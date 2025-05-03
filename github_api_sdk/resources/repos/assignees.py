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
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.repos import assignee_list_params
from ...types.repos.assignee_list_response import AssigneeListResponse

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

    def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssigneeListResponse:
        """
        Lists the
        [available assignees](https://docs.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/)
        for issues in a repository.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/assignees",
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
                    assignee_list_params.AssigneeListParams,
                ),
            ),
            cast_to=AssigneeListResponse,
        )

    def check(
        self,
        assignee: str,
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
        Checks if a user has permission to be assigned to an issue in this repository.

        If the `assignee` can be assigned to issues in the repository, a `204` header
        with no content is returned.

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
            f"/repos/{owner}/{repo}/assignees/{assignee}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
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

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssigneeListResponse:
        """
        Lists the
        [available assignees](https://docs.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/)
        for issues in a repository.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/assignees",
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
                    assignee_list_params.AssigneeListParams,
                ),
            ),
            cast_to=AssigneeListResponse,
        )

    async def check(
        self,
        assignee: str,
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
        Checks if a user has permission to be assigned to an issue in this repository.

        If the `assignee` can be assigned to issues in the repository, a `204` header
        with no content is returned.

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
            f"/repos/{owner}/{repo}/assignees/{assignee}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AssigneesResourceWithRawResponse:
    def __init__(self, assignees: AssigneesResource) -> None:
        self._assignees = assignees

        self.list = to_raw_response_wrapper(
            assignees.list,
        )
        self.check = to_raw_response_wrapper(
            assignees.check,
        )


class AsyncAssigneesResourceWithRawResponse:
    def __init__(self, assignees: AsyncAssigneesResource) -> None:
        self._assignees = assignees

        self.list = async_to_raw_response_wrapper(
            assignees.list,
        )
        self.check = async_to_raw_response_wrapper(
            assignees.check,
        )


class AssigneesResourceWithStreamingResponse:
    def __init__(self, assignees: AssigneesResource) -> None:
        self._assignees = assignees

        self.list = to_streamed_response_wrapper(
            assignees.list,
        )
        self.check = to_streamed_response_wrapper(
            assignees.check,
        )


class AsyncAssigneesResourceWithStreamingResponse:
    def __init__(self, assignees: AsyncAssigneesResource) -> None:
        self._assignees = assignees

        self.list = async_to_streamed_response_wrapper(
            assignees.list,
        )
        self.check = async_to_streamed_response_wrapper(
            assignees.check,
        )
