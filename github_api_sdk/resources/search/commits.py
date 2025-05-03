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
from ...types.search import commit_search_params
from ...types.search.commit_search_response import CommitSearchResponse

__all__ = ["CommitsResource", "AsyncCommitsResource"]


class CommitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CommitsResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["author-date", "committer-date"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitSearchResponse:
        """Find commits via various criteria on the default branch (usually `main`).

        This
        method returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).

        When searching for commits, you can get text match metadata for the **message**
        field when you provide the `text-match` media type. For more details about how
        to receive highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you want to find commits related to CSS in the
        [octocat/Spoon-Knife](https://github.com/octocat/Spoon-Knife) repository. Your
        query would look something like this:

        `q=repo:octocat/Spoon-Knife+css`

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching commits](https://docs.github.com/search-github/searching-on-github/searching-commits)"
              for a detailed list of qualifiers.

          order: Determines whether the first search result returned is the highest number of
              matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
              unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort:
              Sorts the results of your query by `author-date` or `committer-date`. Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/commits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    commit_search_params.CommitSearchParams,
                ),
            ),
            cast_to=CommitSearchResponse,
        )


class AsyncCommitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCommitsResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["author-date", "committer-date"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitSearchResponse:
        """Find commits via various criteria on the default branch (usually `main`).

        This
        method returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).

        When searching for commits, you can get text match metadata for the **message**
        field when you provide the `text-match` media type. For more details about how
        to receive highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you want to find commits related to CSS in the
        [octocat/Spoon-Knife](https://github.com/octocat/Spoon-Knife) repository. Your
        query would look something like this:

        `q=repo:octocat/Spoon-Knife+css`

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching commits](https://docs.github.com/search-github/searching-on-github/searching-commits)"
              for a detailed list of qualifiers.

          order: Determines whether the first search result returned is the highest number of
              matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
              unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort:
              Sorts the results of your query by `author-date` or `committer-date`. Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/commits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    commit_search_params.CommitSearchParams,
                ),
            ),
            cast_to=CommitSearchResponse,
        )


class CommitsResourceWithRawResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.search = to_raw_response_wrapper(
            commits.search,
        )


class AsyncCommitsResourceWithRawResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.search = async_to_raw_response_wrapper(
            commits.search,
        )


class CommitsResourceWithStreamingResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.search = to_streamed_response_wrapper(
            commits.search,
        )


class AsyncCommitsResourceWithStreamingResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.search = async_to_streamed_response_wrapper(
            commits.search,
        )
