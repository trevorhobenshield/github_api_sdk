from __future__ import annotations

import httpx

from .._base_client import make_request_options
from .._compat import cached_property
from .._resource import AsyncAPIResource, SyncAPIResource
from .._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..types.code_of_conduct import CodeOfConduct
from ..types.codes_of_conduct_list_response import CodesOfConductListResponse

__all__ = ["CodesOfConductResource", "AsyncCodesOfConductResource"]


class CodesOfConductResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CodesOfConductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodesOfConductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodesOfConductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodesOfConductResourceWithStreamingResponse(self)

    def retrieve(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeOfConduct:
        """
        Returns information about the specified GitHub code of conduct.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return self._get(
            f"/codes_of_conduct/{key}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeOfConduct,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodesOfConductListResponse:
        """Returns array of all GitHub's codes of conduct."""
        return self._get(
            "/codes_of_conduct",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodesOfConductListResponse,
        )


class AsyncCodesOfConductResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCodesOfConductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodesOfConductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodesOfConductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodesOfConductResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        key: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeOfConduct:
        """
        Returns information about the specified GitHub code of conduct.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        return await self._get(
            f"/codes_of_conduct/{key}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeOfConduct,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodesOfConductListResponse:
        """Returns array of all GitHub's codes of conduct."""
        return await self._get(
            "/codes_of_conduct",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodesOfConductListResponse,
        )


class CodesOfConductResourceWithRawResponse:
    def __init__(self, codes_of_conduct: CodesOfConductResource) -> None:
        self._codes_of_conduct = codes_of_conduct

        self.retrieve = to_raw_response_wrapper(
            codes_of_conduct.retrieve,
        )
        self.list = to_raw_response_wrapper(
            codes_of_conduct.list,
        )


class AsyncCodesOfConductResourceWithRawResponse:
    def __init__(self, codes_of_conduct: AsyncCodesOfConductResource) -> None:
        self._codes_of_conduct = codes_of_conduct

        self.retrieve = async_to_raw_response_wrapper(
            codes_of_conduct.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            codes_of_conduct.list,
        )


class CodesOfConductResourceWithStreamingResponse:
    def __init__(self, codes_of_conduct: CodesOfConductResource) -> None:
        self._codes_of_conduct = codes_of_conduct

        self.retrieve = to_streamed_response_wrapper(
            codes_of_conduct.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            codes_of_conduct.list,
        )


class AsyncCodesOfConductResourceWithStreamingResponse:
    def __init__(self, codes_of_conduct: AsyncCodesOfConductResource) -> None:
        self._codes_of_conduct = codes_of_conduct

        self.retrieve = async_to_streamed_response_wrapper(
            codes_of_conduct.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            codes_of_conduct.list,
        )
