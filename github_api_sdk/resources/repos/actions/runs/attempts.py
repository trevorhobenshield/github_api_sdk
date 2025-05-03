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
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.repos.actions.runs import attempt_list_jobs_params, attempt_retrieve_params
from .....types.repos.actions.runs.attempt_list_jobs_response import AttemptListJobsResponse
from .....types.repos.actions.workflow_run import WorkflowRun

__all__ = ["AttemptsResource", "AsyncAttemptsResource"]


class AttemptsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AttemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AttemptsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        attempt_number: int,
        *,
        owner: str,
        repo: str,
        run_id: int,
        exclude_pull_requests: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowRun:
        """
        Gets a specific workflow run attempt.

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          exclude_pull_requests: If `true` pull requests are omitted from the response (empty array).

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"exclude_pull_requests": exclude_pull_requests}, attempt_retrieve_params.AttemptRetrieveParams),
            ),
            cast_to=WorkflowRun,
        )

    def download_logs(
        self,
        attempt_number: int,
        *,
        owner: str,
        repo: str,
        run_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Gets a redirect URL to download an archive of log files for a specific workflow
        run attempt. This link expires after 1 minute. Look for `Location:` in the
        response header to find the URL for the download.

        Anyone with read access to the repository can use this endpoint.

        If the repository is private, OAuth tokens and personal access tokens (classic)
        need the `repo` scope to use this endpoint.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_jobs(
        self,
        attempt_number: int,
        *,
        owner: str,
        repo: str,
        run_id: int,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttemptListJobsResponse:
        """Lists jobs for a specific workflow run attempt.

        You can use parameters to narrow
        the list of results. For more information about using parameters, see
        [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs",
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
                    attempt_list_jobs_params.AttemptListJobsParams,
                ),
            ),
            cast_to=AttemptListJobsResponse,
        )


class AsyncAttemptsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAttemptsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        attempt_number: int,
        *,
        owner: str,
        repo: str,
        run_id: int,
        exclude_pull_requests: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowRun:
        """
        Gets a specific workflow run attempt.

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          exclude_pull_requests: If `true` pull requests are omitted from the response (empty array).

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"exclude_pull_requests": exclude_pull_requests}, attempt_retrieve_params.AttemptRetrieveParams),
            ),
            cast_to=WorkflowRun,
        )

    async def download_logs(
        self,
        attempt_number: int,
        *,
        owner: str,
        repo: str,
        run_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Gets a redirect URL to download an archive of log files for a specific workflow
        run attempt. This link expires after 1 minute. Look for `Location:` in the
        response header to find the URL for the download.

        Anyone with read access to the repository can use this endpoint.

        If the repository is private, OAuth tokens and personal access tokens (classic)
        need the `repo` scope to use this endpoint.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_jobs(
        self,
        attempt_number: int,
        *,
        owner: str,
        repo: str,
        run_id: int,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttemptListJobsResponse:
        """Lists jobs for a specific workflow run attempt.

        You can use parameters to narrow
        the list of results. For more information about using parameters, see
        [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs",
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
                    attempt_list_jobs_params.AttemptListJobsParams,
                ),
            ),
            cast_to=AttemptListJobsResponse,
        )


class AttemptsResourceWithRawResponse:
    def __init__(self, attempts: AttemptsResource) -> None:
        self._attempts = attempts

        self.retrieve = to_raw_response_wrapper(
            attempts.retrieve,
        )
        self.download_logs = to_raw_response_wrapper(
            attempts.download_logs,
        )
        self.list_jobs = to_raw_response_wrapper(
            attempts.list_jobs,
        )


class AsyncAttemptsResourceWithRawResponse:
    def __init__(self, attempts: AsyncAttemptsResource) -> None:
        self._attempts = attempts

        self.retrieve = async_to_raw_response_wrapper(
            attempts.retrieve,
        )
        self.download_logs = async_to_raw_response_wrapper(
            attempts.download_logs,
        )
        self.list_jobs = async_to_raw_response_wrapper(
            attempts.list_jobs,
        )


class AttemptsResourceWithStreamingResponse:
    def __init__(self, attempts: AttemptsResource) -> None:
        self._attempts = attempts

        self.retrieve = to_streamed_response_wrapper(
            attempts.retrieve,
        )
        self.download_logs = to_streamed_response_wrapper(
            attempts.download_logs,
        )
        self.list_jobs = to_streamed_response_wrapper(
            attempts.list_jobs,
        )


class AsyncAttemptsResourceWithStreamingResponse:
    def __init__(self, attempts: AsyncAttemptsResource) -> None:
        self._attempts = attempts

        self.retrieve = async_to_streamed_response_wrapper(
            attempts.retrieve,
        )
        self.download_logs = async_to_streamed_response_wrapper(
            attempts.download_logs,
        )
        self.list_jobs = async_to_streamed_response_wrapper(
            attempts.list_jobs,
        )
