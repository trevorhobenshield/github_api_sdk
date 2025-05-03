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
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.search import topic_search_params
from ...types.search.topic_search_response import TopicSearchResponse

__all__ = ["TopicsResource", "AsyncTopicsResource"]


class TopicsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return TopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return TopicsResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopicSearchResponse:
        """Find topics via various criteria.

        Results are sorted by best match. This method
        returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).
        See "[Searching topics](https://docs.github.com/articles/searching-topics/)" for
        a detailed list of qualifiers.

        When searching for topics, you can get text match metadata for the topic's
        **short_description**, **description**, **name**, or **display_name** field when
        you pass the `text-match` media type. For more details about how to receive
        highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you want to search for topics related to Ruby that are featured
        on https://github.com/topics. Your query might look like this:

        `q=ruby+is:featured`

        This query searches for topics with the keyword `ruby` and limits the results to
        find only topics that are featured. The topics that are the best match for the
        query appear first in the search results.

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/topics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "page": page,
                        "per_page": per_page,
                    },
                    topic_search_params.TopicSearchParams,
                ),
            ),
            cast_to=TopicSearchResponse,
        )


class AsyncTopicsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncTopicsResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopicSearchResponse:
        """Find topics via various criteria.

        Results are sorted by best match. This method
        returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).
        See "[Searching topics](https://docs.github.com/articles/searching-topics/)" for
        a detailed list of qualifiers.

        When searching for topics, you can get text match metadata for the topic's
        **short_description**, **description**, **name**, or **display_name** field when
        you pass the `text-match` media type. For more details about how to receive
        highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you want to search for topics related to Ruby that are featured
        on https://github.com/topics. Your query might look like this:

        `q=ruby+is:featured`

        This query searches for topics with the keyword `ruby` and limits the results to
        find only topics that are featured. The topics that are the best match for the
        query appear first in the search results.

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/topics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "page": page,
                        "per_page": per_page,
                    },
                    topic_search_params.TopicSearchParams,
                ),
            ),
            cast_to=TopicSearchResponse,
        )


class TopicsResourceWithRawResponse:
    def __init__(self, topics: TopicsResource) -> None:
        self._topics = topics

        self.search = to_raw_response_wrapper(
            topics.search,
        )


class AsyncTopicsResourceWithRawResponse:
    def __init__(self, topics: AsyncTopicsResource) -> None:
        self._topics = topics

        self.search = async_to_raw_response_wrapper(
            topics.search,
        )


class TopicsResourceWithStreamingResponse:
    def __init__(self, topics: TopicsResource) -> None:
        self._topics = topics

        self.search = to_streamed_response_wrapper(
            topics.search,
        )


class AsyncTopicsResourceWithStreamingResponse:
    def __init__(self, topics: AsyncTopicsResource) -> None:
        self._topics = topics

        self.search = async_to_streamed_response_wrapper(
            topics.search,
        )
