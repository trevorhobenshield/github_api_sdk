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
from ...types.search import code_search_params
from ...types.search.code_search_response import CodeSearchResponse

__all__ = ["CodeResource", "AsyncCodeResource"]


class CodeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodeResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["indexed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeSearchResponse:
        """Searches for query terms inside of a file.

        This method returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).

        When searching for code, you can get text match metadata for the file
        **content** and file **path** fields when you pass the `text-match` media type.
        For more details about how to receive highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you want to find the definition of the `addClass` function
        inside [jQuery](https://github.com/jquery/jquery) repository, your query would
        look something like this:

        `q=addClass+in:file+language:js+repo:jquery/jquery`

        This query searches for the keyword `addClass` within a file's contents. The
        query limits the search to files where the language is JavaScript in the
        `jquery/jquery` repository.

        Considerations for code search:

        Due to the complexity of searching code, there are a few restrictions on how
        searches are performed:

        - Only the _default branch_ is considered. In most cases, this will be the
          `master` branch.
        - Only files smaller than 384 KB are searchable.
        - You must always include at least one search term when searching source code.
          For example, searching for
          [`language:go`](https://github.com/search?utf8=%E2%9C%93&q=language%3Ago&type=Code)
          is not valid, while
          [`amazing language:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language%3Ago&type=Code)
          is.

        This endpoint requires you to authenticate and limits you to 10 requests per
        minute.

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching code](https://docs.github.com/search-github/searching-on-github/searching-code)"
              for a detailed list of qualifiers.

          order: **This field is closing down.** Determines whether the first search result
              returned is the highest number of matches (`desc`) or lowest number of matches
              (`asc`). This parameter is ignored unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: **This field is closing down.** Sorts the results of your query. Can only be
              `indexed`, which indicates how recently a file has been indexed by the GitHub
              search infrastructure. Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/code",
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
                    code_search_params.CodeSearchParams,
                ),
            ),
            cast_to=CodeSearchResponse,
        )


class AsyncCodeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodeResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["indexed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeSearchResponse:
        """Searches for query terms inside of a file.

        This method returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).

        When searching for code, you can get text match metadata for the file
        **content** and file **path** fields when you pass the `text-match` media type.
        For more details about how to receive highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you want to find the definition of the `addClass` function
        inside [jQuery](https://github.com/jquery/jquery) repository, your query would
        look something like this:

        `q=addClass+in:file+language:js+repo:jquery/jquery`

        This query searches for the keyword `addClass` within a file's contents. The
        query limits the search to files where the language is JavaScript in the
        `jquery/jquery` repository.

        Considerations for code search:

        Due to the complexity of searching code, there are a few restrictions on how
        searches are performed:

        - Only the _default branch_ is considered. In most cases, this will be the
          `master` branch.
        - Only files smaller than 384 KB are searchable.
        - You must always include at least one search term when searching source code.
          For example, searching for
          [`language:go`](https://github.com/search?utf8=%E2%9C%93&q=language%3Ago&type=Code)
          is not valid, while
          [`amazing language:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language%3Ago&type=Code)
          is.

        This endpoint requires you to authenticate and limits you to 10 requests per
        minute.

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching code](https://docs.github.com/search-github/searching-on-github/searching-code)"
              for a detailed list of qualifiers.

          order: **This field is closing down.** Determines whether the first search result
              returned is the highest number of matches (`desc`) or lowest number of matches
              (`asc`). This parameter is ignored unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: **This field is closing down.** Sorts the results of your query. Can only be
              `indexed`, which indicates how recently a file has been indexed by the GitHub
              search infrastructure. Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/code",
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
                    code_search_params.CodeSearchParams,
                ),
            ),
            cast_to=CodeSearchResponse,
        )


class CodeResourceWithRawResponse:
    def __init__(self, code: CodeResource) -> None:
        self._code = code

        self.search = to_raw_response_wrapper(
            code.search,
        )


class AsyncCodeResourceWithRawResponse:
    def __init__(self, code: AsyncCodeResource) -> None:
        self._code = code

        self.search = async_to_raw_response_wrapper(
            code.search,
        )


class CodeResourceWithStreamingResponse:
    def __init__(self, code: CodeResource) -> None:
        self._code = code

        self.search = to_streamed_response_wrapper(
            code.search,
        )


class AsyncCodeResourceWithStreamingResponse:
    def __init__(self, code: AsyncCodeResource) -> None:
        self._code = code

        self.search = async_to_streamed_response_wrapper(
            code.search,
        )
