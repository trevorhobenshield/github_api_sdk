from __future__ import annotations

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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....types.users.codespaces.codespace_export_details import CodespaceExportDetails

__all__ = ["ExportsResource", "AsyncExportsResource"]


class ExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ExportsResourceWithStreamingResponse(self)

    def create(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceExportDetails:
        """
        Triggers an export of the specified codespace and returns a URL and ID where the
        status of the export can be monitored.

        If changes cannot be pushed to the codespace's repository, they will be pushed
        to a new or previously-existing fork instead.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._post(
            f"/user/codespaces/{codespace_name}/exports",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespaceExportDetails,
        )

    def retrieve(
        self,
        export_id: str,
        *,
        codespace_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceExportDetails:
        """
        Gets information about an export of a codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return self._get(
            f"/user/codespaces/{codespace_name}/exports/{export_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespaceExportDetails,
        )


class AsyncExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncExportsResourceWithStreamingResponse(self)

    async def create(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceExportDetails:
        """
        Triggers an export of the specified codespace and returns a URL and ID where the
        status of the export can be monitored.

        If changes cannot be pushed to the codespace's repository, they will be pushed
        to a new or previously-existing fork instead.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._post(
            f"/user/codespaces/{codespace_name}/exports",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespaceExportDetails,
        )

    async def retrieve(
        self,
        export_id: str,
        *,
        codespace_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceExportDetails:
        """
        Gets information about an export of a codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        if not export_id:
            raise ValueError(f"Expected a non-empty value for `export_id` but received {export_id!r}")
        return await self._get(
            f"/user/codespaces/{codespace_name}/exports/{export_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespaceExportDetails,
        )


class ExportsResourceWithRawResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            exports.retrieve,
        )


class AsyncExportsResourceWithRawResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_raw_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            exports.retrieve,
        )


class ExportsResourceWithStreamingResponse:
    def __init__(self, exports: ExportsResource) -> None:
        self._exports = exports

        self.create = to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            exports.retrieve,
        )


class AsyncExportsResourceWithStreamingResponse:
    def __init__(self, exports: AsyncExportsResource) -> None:
        self._exports = exports

        self.create = async_to_streamed_response_wrapper(
            exports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            exports.retrieve,
        )
