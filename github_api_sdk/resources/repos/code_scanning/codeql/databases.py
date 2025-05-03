from __future__ import annotations

import httpx

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from .....types.repos.code_scanning.codeql.code_scanning_codeql_database import CodeScanningCodeqlDatabase
from .....types.repos.code_scanning.codeql.database_list_response import DatabaseListResponse

__all__ = ["DatabasesResource", "AsyncDatabasesResource"]


class DatabasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatabasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DatabasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatabasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DatabasesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        language: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningCodeqlDatabase:
        """
        Gets a CodeQL database for a language in a repository.

        By default this endpoint returns JSON metadata about the CodeQL database. To
        download the CodeQL database binary content, set the `Accept` header of the
        request to
        [`application/zip`](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types),
        and make sure your HTTP client is configured to follow redirects or use the
        `Location` header to make a second request to get the redirect URL.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._get(
            f"/repos/{owner}/{repo}/code-scanning/codeql/databases/{language}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningCodeqlDatabase,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseListResponse:
        """
        Lists the CodeQL databases that are available in a repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
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
            f"/repos/{owner}/{repo}/code-scanning/codeql/databases",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DatabaseListResponse,
        )

    def delete(
        self,
        language: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a CodeQL database for a language in a repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/code-scanning/codeql/databases/{language}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncDatabasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatabasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatabasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatabasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDatabasesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        language: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningCodeqlDatabase:
        """
        Gets a CodeQL database for a language in a repository.

        By default this endpoint returns JSON metadata about the CodeQL database. To
        download the CodeQL database binary content, set the `Accept` header of the
        request to
        [`application/zip`](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types),
        and make sure your HTTP client is configured to follow redirects or use the
        `Location` header to make a second request to get the redirect URL.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/code-scanning/codeql/databases/{language}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningCodeqlDatabase,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DatabaseListResponse:
        """
        Lists the CodeQL databases that are available in a repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
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
            f"/repos/{owner}/{repo}/code-scanning/codeql/databases",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DatabaseListResponse,
        )

    async def delete(
        self,
        language: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a CodeQL database for a language in a repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with private or public repositories, or the `public_repo`
        scope to use this endpoint with only public repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/code-scanning/codeql/databases/{language}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class DatabasesResourceWithRawResponse:
    def __init__(self, databases: DatabasesResource) -> None:
        self._databases = databases

        self.retrieve = to_raw_response_wrapper(
            databases.retrieve,
        )
        self.list = to_raw_response_wrapper(
            databases.list,
        )
        self.delete = to_raw_response_wrapper(
            databases.delete,
        )


class AsyncDatabasesResourceWithRawResponse:
    def __init__(self, databases: AsyncDatabasesResource) -> None:
        self._databases = databases

        self.retrieve = async_to_raw_response_wrapper(
            databases.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            databases.list,
        )
        self.delete = async_to_raw_response_wrapper(
            databases.delete,
        )


class DatabasesResourceWithStreamingResponse:
    def __init__(self, databases: DatabasesResource) -> None:
        self._databases = databases

        self.retrieve = to_streamed_response_wrapper(
            databases.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            databases.list,
        )
        self.delete = to_streamed_response_wrapper(
            databases.delete,
        )


class AsyncDatabasesResourceWithStreamingResponse:
    def __init__(self, databases: AsyncDatabasesResource) -> None:
        self._databases = databases

        self.retrieve = async_to_streamed_response_wrapper(
            databases.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            databases.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            databases.delete,
        )
