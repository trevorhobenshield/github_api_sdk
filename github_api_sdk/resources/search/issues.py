from __future__ import annotations

import httpx
from typing_extensions import Literal

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
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.search import issue_search_params
from ...types.search.issue_search_response import IssueSearchResponse

__all__ = ["IssuesResource", "AsyncIssuesResource"]


class IssuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IssuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return IssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IssuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return IssuesResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str,
        advanced_search: str | NotGiven = NOT_GIVEN,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "comments",
            "reactions",
            "reactions-+1",
            "reactions--1",
            "reactions-smile",
            "reactions-thinking_face",
            "reactions-heart",
            "reactions-tada",
            "interactions",
            "created",
            "updated",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueSearchResponse:
        """
        > [!WARNING] > **Notice:** Search for issues and pull requests will be
        > overridden by advanced search on September 4, 2025. You can read more about
        > this change on
        > [the GitHub blog](https://github.blog/changelog/2025-03-06-github-issues-projects-api-support-for-issues-advanced-search-and-more/).

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching issues and pull requests](https://docs.github.com/search-github/searching-on-github/searching-issues-and-pull-requests)"
              for a detailed list of qualifiers.

          advanced_search:
              Set to `true` to use advanced search. Example:
              `http://api.github.com/search/issues?q={query}&advanced_search=true`

          order: Determines whether the first search result returned is the highest number of
              matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
              unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: Sorts the results of your query by the number of `comments`, `reactions`,
              `reactions-+1`, `reactions--1`, `reactions-smile`, `reactions-thinking_face`,
              `reactions-heart`, `reactions-tada`, or `interactions`. You can also sort
              results by how recently the items were `created` or `updated`, Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/issues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "advanced_search": advanced_search,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    issue_search_params.IssueSearchParams,
                ),
            ),
            cast_to=IssueSearchResponse,
        )


class AsyncIssuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIssuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIssuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncIssuesResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str,
        advanced_search: str | NotGiven = NOT_GIVEN,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "comments",
            "reactions",
            "reactions-+1",
            "reactions--1",
            "reactions-smile",
            "reactions-thinking_face",
            "reactions-heart",
            "reactions-tada",
            "interactions",
            "created",
            "updated",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueSearchResponse:
        """
        > [!WARNING] > **Notice:** Search for issues and pull requests will be
        > overridden by advanced search on September 4, 2025. You can read more about
        > this change on
        > [the GitHub blog](https://github.blog/changelog/2025-03-06-github-issues-projects-api-support-for-issues-advanced-search-and-more/).

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching issues and pull requests](https://docs.github.com/search-github/searching-on-github/searching-issues-and-pull-requests)"
              for a detailed list of qualifiers.

          advanced_search:
              Set to `true` to use advanced search. Example:
              `http://api.github.com/search/issues?q={query}&advanced_search=true`

          order: Determines whether the first search result returned is the highest number of
              matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
              unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: Sorts the results of your query by the number of `comments`, `reactions`,
              `reactions-+1`, `reactions--1`, `reactions-smile`, `reactions-thinking_face`,
              `reactions-heart`, `reactions-tada`, or `interactions`. You can also sort
              results by how recently the items were `created` or `updated`, Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/issues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "advanced_search": advanced_search,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    issue_search_params.IssueSearchParams,
                ),
            ),
            cast_to=IssueSearchResponse,
        )


class IssuesResourceWithRawResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.search = to_raw_response_wrapper(
            issues.search,
        )


class AsyncIssuesResourceWithRawResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.search = async_to_raw_response_wrapper(
            issues.search,
        )


class IssuesResourceWithStreamingResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.search = to_streamed_response_wrapper(
            issues.search,
        )


class AsyncIssuesResourceWithStreamingResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.search = async_to_streamed_response_wrapper(
            issues.search,
        )
