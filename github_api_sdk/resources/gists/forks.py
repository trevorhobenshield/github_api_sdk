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
from ...types.gists import fork_list_params
from ...types.gists.base_gist import BaseGist
from ...types.gists.fork_list_response import ForkListResponse

__all__ = ["ForksResource", "AsyncForksResource"]


class ForksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ForksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ForksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ForksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ForksResourceWithStreamingResponse(self)

    def create(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BaseGist:
        """
        Fork a gist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return self._post(
            f"/gists/{gist_id}/forks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BaseGist,
        )

    def list(
        self,
        gist_id: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ForkListResponse:
        """List gist forks

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
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return self._get(
            f"/gists/{gist_id}/forks",
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
                    fork_list_params.ForkListParams,
                ),
            ),
            cast_to=ForkListResponse,
        )


class AsyncForksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncForksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncForksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncForksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncForksResourceWithStreamingResponse(self)

    async def create(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BaseGist:
        """
        Fork a gist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return await self._post(
            f"/gists/{gist_id}/forks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BaseGist,
        )

    async def list(
        self,
        gist_id: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ForkListResponse:
        """List gist forks

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
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return await self._get(
            f"/gists/{gist_id}/forks",
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
                    fork_list_params.ForkListParams,
                ),
            ),
            cast_to=ForkListResponse,
        )


class ForksResourceWithRawResponse:
    def __init__(self, forks: ForksResource) -> None:
        self._forks = forks

        self.create = to_raw_response_wrapper(
            forks.create,
        )
        self.list = to_raw_response_wrapper(
            forks.list,
        )


class AsyncForksResourceWithRawResponse:
    def __init__(self, forks: AsyncForksResource) -> None:
        self._forks = forks

        self.create = async_to_raw_response_wrapper(
            forks.create,
        )
        self.list = async_to_raw_response_wrapper(
            forks.list,
        )


class ForksResourceWithStreamingResponse:
    def __init__(self, forks: ForksResource) -> None:
        self._forks = forks

        self.create = to_streamed_response_wrapper(
            forks.create,
        )
        self.list = to_streamed_response_wrapper(
            forks.list,
        )


class AsyncForksResourceWithStreamingResponse:
    def __init__(self, forks: AsyncForksResource) -> None:
        self._forks = forks

        self.create = async_to_streamed_response_wrapper(
            forks.create,
        )
        self.list = async_to_streamed_response_wrapper(
            forks.list,
        )
