from __future__ import annotations

from typing import List

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
from ...types.repos import topic_get_params, topic_replace_params
from ...types.repos.topic import Topic

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

    def get(
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
    ) -> Topic:
        """Get all repository topics

        Args:
          page: The page number of the results to fetch.

        For more information, see
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
            f"/repos/{owner}/{repo}/topics",
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
                    topic_get_params.TopicGetParams,
                ),
            ),
            cast_to=Topic,
        )

    def replace(
        self,
        repo: str,
        *,
        owner: str,
        names: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Topic:
        """
        Replace all repository topics

        Args:
          names: An array of topics to add to the repository. Pass one or more topics to
              _replace_ the set of existing topics. Send an empty array (`[]`) to clear all
              topics from the repository. **Note:** Topic `names` will be saved as lowercase.

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
            f"/repos/{owner}/{repo}/topics",
            body=maybe_transform({"names": names}, topic_replace_params.TopicReplaceParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Topic,
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

    async def get(
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
    ) -> Topic:
        """Get all repository topics

        Args:
          page: The page number of the results to fetch.

        For more information, see
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
            f"/repos/{owner}/{repo}/topics",
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
                    topic_get_params.TopicGetParams,
                ),
            ),
            cast_to=Topic,
        )

    async def replace(
        self,
        repo: str,
        *,
        owner: str,
        names: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Topic:
        """
        Replace all repository topics

        Args:
          names: An array of topics to add to the repository. Pass one or more topics to
              _replace_ the set of existing topics. Send an empty array (`[]`) to clear all
              topics from the repository. **Note:** Topic `names` will be saved as lowercase.

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
            f"/repos/{owner}/{repo}/topics",
            body=await async_maybe_transform({"names": names}, topic_replace_params.TopicReplaceParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Topic,
        )


class TopicsResourceWithRawResponse:
    def __init__(self, topics: TopicsResource) -> None:
        self._topics = topics

        self.get = to_raw_response_wrapper(
            topics.get,
        )
        self.replace = to_raw_response_wrapper(
            topics.replace,
        )


class AsyncTopicsResourceWithRawResponse:
    def __init__(self, topics: AsyncTopicsResource) -> None:
        self._topics = topics

        self.get = async_to_raw_response_wrapper(
            topics.get,
        )
        self.replace = async_to_raw_response_wrapper(
            topics.replace,
        )


class TopicsResourceWithStreamingResponse:
    def __init__(self, topics: TopicsResource) -> None:
        self._topics = topics

        self.get = to_streamed_response_wrapper(
            topics.get,
        )
        self.replace = to_streamed_response_wrapper(
            topics.replace,
        )


class AsyncTopicsResourceWithStreamingResponse:
    def __init__(self, topics: AsyncTopicsResource) -> None:
        self._topics = topics

        self.get = async_to_streamed_response_wrapper(
            topics.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            topics.replace,
        )
