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
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.orgs.members import codespace_list_params
from ....types.orgs.members.codespace import Codespace
from ....types.orgs.members.codespace_list_response import CodespaceListResponse

__all__ = ["CodespacesResource", "AsyncCodespacesResource"]


class CodespacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CodespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodespacesResourceWithStreamingResponse(self)

    def list(
        self,
        username: str,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListResponse:
        """
        Lists the codespaces that a member of an organization has for repositories in
        that organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/orgs/{org}/members/{username}/codespaces",
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
                    codespace_list_params.CodespaceListParams,
                ),
            ),
            cast_to=CodespaceListResponse,
        )

    def delete(
        self,
        codespace_name: str,
        *,
        org: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._delete(
            f"/orgs/{org}/members/{username}/codespaces/{codespace_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def stop(
        self,
        codespace_name: str,
        *,
        org: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Stops a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._post(
            f"/orgs/{org}/members/{username}/codespaces/{codespace_name}/stop",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )


class AsyncCodespacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCodespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodespacesResourceWithStreamingResponse(self)

    async def list(
        self,
        username: str,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListResponse:
        """
        Lists the codespaces that a member of an organization has for repositories in
        that organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/orgs/{org}/members/{username}/codespaces",
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
                    codespace_list_params.CodespaceListParams,
                ),
            ),
            cast_to=CodespaceListResponse,
        )

    async def delete(
        self,
        codespace_name: str,
        *,
        org: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._delete(
            f"/orgs/{org}/members/{username}/codespaces/{codespace_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def stop(
        self,
        codespace_name: str,
        *,
        org: str,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Stops a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._post(
            f"/orgs/{org}/members/{username}/codespaces/{codespace_name}/stop",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )


class CodespacesResourceWithRawResponse:
    def __init__(self, codespaces: CodespacesResource) -> None:
        self._codespaces = codespaces

        self.list = to_raw_response_wrapper(
            codespaces.list,
        )
        self.delete = to_raw_response_wrapper(
            codespaces.delete,
        )
        self.stop = to_raw_response_wrapper(
            codespaces.stop,
        )


class AsyncCodespacesResourceWithRawResponse:
    def __init__(self, codespaces: AsyncCodespacesResource) -> None:
        self._codespaces = codespaces

        self.list = async_to_raw_response_wrapper(
            codespaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            codespaces.delete,
        )
        self.stop = async_to_raw_response_wrapper(
            codespaces.stop,
        )


class CodespacesResourceWithStreamingResponse:
    def __init__(self, codespaces: CodespacesResource) -> None:
        self._codespaces = codespaces

        self.list = to_streamed_response_wrapper(
            codespaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            codespaces.delete,
        )
        self.stop = to_streamed_response_wrapper(
            codespaces.stop,
        )


class AsyncCodespacesResourceWithStreamingResponse:
    def __init__(self, codespaces: AsyncCodespacesResource) -> None:
        self._codespaces = codespaces

        self.list = async_to_streamed_response_wrapper(
            codespaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            codespaces.delete,
        )
        self.stop = async_to_streamed_response_wrapper(
            codespaces.stop,
        )
