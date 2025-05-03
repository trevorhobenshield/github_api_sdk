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
from ...types.search import label_search_params
from ...types.search.label_search_response import LabelSearchResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str,
        repository_id: int,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSearchResponse:
        """
        Find labels in a repository with names or descriptions that match search
        keywords. Returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).

        When searching for labels, you can get text match metadata for the label
        **name** and **description** fields when you pass the `text-match` media type.
        For more details about how to receive highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you want to find labels in the `linguist` repository that match
        `bug`, `defect`, or `enhancement`. Your query might look like this:

        `q=bug+defect+enhancement&repository_id=64778136`

        The labels that best match the query appear first in the search results.

        Args:
          q: The search keywords. This endpoint does not accept qualifiers in the query. To
              learn more about the format of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).

          repository_id: The id of the repository.

          order: Determines whether the first search result returned is the highest number of
              matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
              unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: Sorts the results of your query by when the label was `created` or `updated`.
              Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/labels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "repository_id": repository_id,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    label_search_params.LabelSearchParams,
                ),
            ),
            cast_to=LabelSearchResponse,
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str,
        repository_id: int,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSearchResponse:
        """
        Find labels in a repository with names or descriptions that match search
        keywords. Returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).

        When searching for labels, you can get text match metadata for the label
        **name** and **description** fields when you pass the `text-match` media type.
        For more details about how to receive highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you want to find labels in the `linguist` repository that match
        `bug`, `defect`, or `enhancement`. Your query might look like this:

        `q=bug+defect+enhancement&repository_id=64778136`

        The labels that best match the query appear first in the search results.

        Args:
          q: The search keywords. This endpoint does not accept qualifiers in the query. To
              learn more about the format of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).

          repository_id: The id of the repository.

          order: Determines whether the first search result returned is the highest number of
              matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
              unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: Sorts the results of your query by when the label was `created` or `updated`.
              Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/labels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "repository_id": repository_id,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    label_search_params.LabelSearchParams,
                ),
            ),
            cast_to=LabelSearchResponse,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.search = to_raw_response_wrapper(
            labels.search,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.search = async_to_raw_response_wrapper(
            labels.search,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.search = to_streamed_response_wrapper(
            labels.search,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.search = async_to_streamed_response_wrapper(
            labels.search,
        )
