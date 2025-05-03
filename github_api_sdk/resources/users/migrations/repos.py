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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query

__all__ = ["ReposResource", "AsyncReposResource"]


class ReposResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ReposResourceWithStreamingResponse(self)

    def unlock(
        self,
        repo_name: str,
        *,
        migration_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Unlocks a repository.

        You can lock repositories when you
        [start a user migration](https://docs.github.com/rest/migrations/users#start-a-user-migration).
        Once the migration is complete you can unlock each repository to begin using it
        again or
        [delete the repository](https://docs.github.com/rest/repos/repos#delete-a-repository)
        if you no longer need the source data. Returns a status of `404 Not Found` if
        the repository is not locked.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_name:
            raise ValueError(f"Expected a non-empty value for `repo_name` but received {repo_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/user/migrations/{migration_id}/repos/{repo_name}/lock",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncReposResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncReposResourceWithStreamingResponse(self)

    async def unlock(
        self,
        repo_name: str,
        *,
        migration_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Unlocks a repository.

        You can lock repositories when you
        [start a user migration](https://docs.github.com/rest/migrations/users#start-a-user-migration).
        Once the migration is complete you can unlock each repository to begin using it
        again or
        [delete the repository](https://docs.github.com/rest/repos/repos#delete-a-repository)
        if you no longer need the source data. Returns a status of `404 Not Found` if
        the repository is not locked.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not repo_name:
            raise ValueError(f"Expected a non-empty value for `repo_name` but received {repo_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/user/migrations/{migration_id}/repos/{repo_name}/lock",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ReposResourceWithRawResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.unlock = to_raw_response_wrapper(
            repos.unlock,
        )


class AsyncReposResourceWithRawResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.unlock = async_to_raw_response_wrapper(
            repos.unlock,
        )


class ReposResourceWithStreamingResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.unlock = to_streamed_response_wrapper(
            repos.unlock,
        )


class AsyncReposResourceWithStreamingResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.unlock = async_to_streamed_response_wrapper(
            repos.unlock,
        )
