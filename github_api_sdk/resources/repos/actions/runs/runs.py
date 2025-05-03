from __future__ import annotations

from datetime import datetime
from typing import Union

import httpx
from typing_extensions import Literal, overload

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
    required_args,
)
from .....types.repos.actions import (
    run_list_artifacts_params,
    run_list_jobs_params,
    run_list_params,
    run_rerun_failed_jobs_params,
    run_rerun_params,
    run_retrieve_params,
    run_review_deployment_protection_rule_params,
)
from .....types.repos.actions.run_get_approvals_response import RunGetApprovalsResponse
from .....types.repos.actions.run_get_timing_response import RunGetTimingResponse
from .....types.repos.actions.run_list_artifacts_response import RunListArtifactsResponse
from .....types.repos.actions.run_list_jobs_response import RunListJobsResponse
from .....types.repos.actions.run_list_response import RunListResponse
from .....types.repos.actions.workflow_run import WorkflowRun
from .attempts import (
    AsyncAttemptsResource,
    AsyncAttemptsResourceWithRawResponse,
    AsyncAttemptsResourceWithStreamingResponse,
    AttemptsResource,
    AttemptsResourceWithRawResponse,
    AttemptsResourceWithStreamingResponse,
)
from .logs import (
    AsyncLogsResource,
    AsyncLogsResourceWithRawResponse,
    AsyncLogsResourceWithStreamingResponse,
    LogsResource,
    LogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
)
from .pending_deployments import (
    AsyncPendingDeploymentsResource,
    AsyncPendingDeploymentsResourceWithRawResponse,
    AsyncPendingDeploymentsResourceWithStreamingResponse,
    PendingDeploymentsResource,
    PendingDeploymentsResourceWithRawResponse,
    PendingDeploymentsResourceWithStreamingResponse,
)

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def attempts(self) -> AttemptsResource:
        return AttemptsResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def pending_deployments(self) -> PendingDeploymentsResource:
        return PendingDeploymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        exclude_pull_requests: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowRun:
        """
        Gets a specific workflow run.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"exclude_pull_requests": exclude_pull_requests}, run_retrieve_params.RunRetrieveParams),
            ),
            cast_to=WorkflowRun,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        actor: str | NotGiven = NOT_GIVEN,
        branch: str | NotGiven = NOT_GIVEN,
        check_suite_id: int | NotGiven = NOT_GIVEN,
        created: str | datetime | NotGiven = NOT_GIVEN,
        event: str | NotGiven = NOT_GIVEN,
        exclude_pull_requests: bool | NotGiven = NOT_GIVEN,
        head_sha: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal[
            "completed",
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "skipped",
            "stale",
            "success",
            "timed_out",
            "in_progress",
            "queued",
            "requested",
            "waiting",
            "pending",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListResponse:
        """Lists all workflow runs for a repository.

        You can use parameters to narrow the
        list of results. For more information about using parameters, see
        [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        This endpoint will return up to 1,000 results for each search when using the
        following parameters: `actor`, `branch`, `check_suite_id`, `created`, `event`,
        `head_sha`, `status`.

        Args:
          actor: Returns someone's workflow runs. Use the login for the user who created the
              `push` associated with the check suite or workflow run.

          branch: Returns workflow runs associated with a branch. Use the name of the branch of
              the `push`.

          check_suite_id: Returns workflow runs with the `check_suite_id` that you specify.

          created: Returns workflow runs created within the given date-time range. For more
              information on the syntax, see
              "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."

          event: Returns workflow run triggered by the event you specify. For example, `push`,
              `pull_request` or `issue`. For more information, see
              "[Events that trigger workflows](https://docs.github.com/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows)."

          exclude_pull_requests: If `true` pull requests are omitted from the response (empty array).

          head_sha: Only returns workflow runs that are associated with the specified `head_sha`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: Returns workflow runs with the check run `status` or `conclusion` that you
              specify. For example, a conclusion can be `success` or a status can be
              `in_progress`. Only GitHub Actions can set a status of `waiting`, `pending`, or
              `requested`.

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
            f"/repos/{owner}/{repo}/actions/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "actor": actor,
                        "branch": branch,
                        "check_suite_id": check_suite_id,
                        "created": created,
                        "event": event,
                        "exclude_pull_requests": exclude_pull_requests,
                        "head_sha": head_sha,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    def delete(
        self,
        run_id: int,
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
        Deletes a specific workflow run.

        Anyone with write access to the repository can use this endpoint.

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
        return self._delete(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def approve(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Approves a workflow run for a pull request from a public fork of a first time
        contributor. For more information, see
        ["Approving workflow runs from public forks](https://docs.github.com/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks)."

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/approve",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def cancel(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Cancels a workflow run using its `id`.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def force_cancel(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Cancels a workflow run and bypasses conditions that would otherwise cause a
        workflow execution to continue, such as an `always()` condition on a job. You
        should only use this endpoint to cancel a workflow run when the workflow run is
        not responding to
        [`POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel`](/rest/actions/workflow-runs#cancel-a-workflow-run).

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/force-cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def get_approvals(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunGetApprovalsResponse:
        """
        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/approvals",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RunGetApprovalsResponse,
        )

    def get_timing(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunGetTimingResponse:
        """> [!WARNING]
        > This endpoint is in the process of closing down.

        Refer to
        > "[Actions Get workflow usage and Get workflow run usage endpoints closing down](https://github.blog/changelog/2025-02-02-actions-get-workflow-usage-and-get-workflow-run-usage-endpoints-closing-down/)"
        > for more information.

        Gets the number of billable minutes and total run time for a specific workflow
        run. Billable minutes only apply to workflows in private repositories that use
        GitHub-hosted runners. Usage is listed for each GitHub-hosted runner operating
        system in milliseconds. Any job re-runs are also included in the usage. The
        usage does not include the multiplier for macOS and Windows runners and is not
        rounded up to the nearest whole minute. For more information, see
        "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/timing",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RunGetTimingResponse,
        )

    def list_artifacts(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListArtifactsResponse:
        """
        Lists artifacts for a workflow run.

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          name: The name field of an artifact. When specified, only artifacts with this name
              will be returned.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    run_list_artifacts_params.RunListArtifactsParams,
                ),
            ),
            cast_to=RunListArtifactsResponse,
        )

    def list_jobs(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        filter: Literal["latest", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListJobsResponse:
        """Lists jobs for a workflow run.

        You can use parameters to narrow the list of
        results. For more information about using parameters, see
        [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          filter: Filters jobs by their `completed_at` timestamp. `latest` returns jobs from the
              most recent execution of the workflow run. `all` returns all jobs for a workflow
              run, including from old executions of the workflow run.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                    },
                    run_list_jobs_params.RunListJobsParams,
                ),
            ),
            cast_to=RunListJobsResponse,
        )

    def rerun(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        enable_debug_logging: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Re-runs your workflow run using its `id`.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          enable_debug_logging: Whether to enable debug logging for the re-run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun",
            body=maybe_transform({"enable_debug_logging": enable_debug_logging}, run_rerun_params.RunRerunParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def rerun_failed_jobs(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        enable_debug_logging: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Re-run all of the failed jobs and their dependent jobs in a workflow run using
        the `id` of the workflow run.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          enable_debug_logging: Whether to enable debug logging for the re-run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs",
            body=maybe_transform({"enable_debug_logging": enable_debug_logging}, run_rerun_failed_jobs_params.RunRerunFailedJobsParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    @overload
    def review_deployment_protection_rule(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        comment: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Approve or reject custom deployment protection rules provided by a GitHub App
        for a workflow run. For more information, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        > [!NOTE] GitHub Apps can only review their own custom deployment protection
        > rules. To approve or reject pending deployments that are waiting for review
        > from a specific person or team, see
        > [`POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments`](/rest/actions/workflow-runs#review-pending-deployments-for-a-workflow-run).

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          comment: Comment associated with the pending deployment protection rule. **Required when
              state is not provided.**

          environment_name: The name of the environment to approve or reject.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def review_deployment_protection_rule(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        state: Literal["approved", "rejected"],
        comment: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Approve or reject custom deployment protection rules provided by a GitHub App
        for a workflow run. For more information, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        > [!NOTE] GitHub Apps can only review their own custom deployment protection
        > rules. To approve or reject pending deployments that are waiting for review
        > from a specific person or team, see
        > [`POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments`](/rest/actions/workflow-runs#review-pending-deployments-for-a-workflow-run).

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          environment_name: The name of the environment to approve or reject.

          state: Whether to approve or reject deployment to the specified environments.

          comment: Optional comment to include with the review.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "repo", "comment", "environment_name"], ["owner", "repo", "environment_name", "state"])
    def review_deployment_protection_rule(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        comment: str | NotGiven = NOT_GIVEN,
        environment_name: str,
        state: Literal["approved", "rejected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule",
            body=maybe_transform(
                {
                    "comment": comment,
                    "environment_name": environment_name,
                    "state": state,
                },
                run_review_deployment_protection_rule_params.RunReviewDeploymentProtectionRuleParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def attempts(self) -> AsyncAttemptsResource:
        return AsyncAttemptsResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def pending_deployments(self) -> AsyncPendingDeploymentsResource:
        return AsyncPendingDeploymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        exclude_pull_requests: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowRun:
        """
        Gets a specific workflow run.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"exclude_pull_requests": exclude_pull_requests}, run_retrieve_params.RunRetrieveParams),
            ),
            cast_to=WorkflowRun,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        actor: str | NotGiven = NOT_GIVEN,
        branch: str | NotGiven = NOT_GIVEN,
        check_suite_id: int | NotGiven = NOT_GIVEN,
        created: str | datetime | NotGiven = NOT_GIVEN,
        event: str | NotGiven = NOT_GIVEN,
        exclude_pull_requests: bool | NotGiven = NOT_GIVEN,
        head_sha: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal[
            "completed",
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "skipped",
            "stale",
            "success",
            "timed_out",
            "in_progress",
            "queued",
            "requested",
            "waiting",
            "pending",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListResponse:
        """Lists all workflow runs for a repository.

        You can use parameters to narrow the
        list of results. For more information about using parameters, see
        [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        This endpoint will return up to 1,000 results for each search when using the
        following parameters: `actor`, `branch`, `check_suite_id`, `created`, `event`,
        `head_sha`, `status`.

        Args:
          actor: Returns someone's workflow runs. Use the login for the user who created the
              `push` associated with the check suite or workflow run.

          branch: Returns workflow runs associated with a branch. Use the name of the branch of
              the `push`.

          check_suite_id: Returns workflow runs with the `check_suite_id` that you specify.

          created: Returns workflow runs created within the given date-time range. For more
              information on the syntax, see
              "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."

          event: Returns workflow run triggered by the event you specify. For example, `push`,
              `pull_request` or `issue`. For more information, see
              "[Events that trigger workflows](https://docs.github.com/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows)."

          exclude_pull_requests: If `true` pull requests are omitted from the response (empty array).

          head_sha: Only returns workflow runs that are associated with the specified `head_sha`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: Returns workflow runs with the check run `status` or `conclusion` that you
              specify. For example, a conclusion can be `success` or a status can be
              `in_progress`. Only GitHub Actions can set a status of `waiting`, `pending`, or
              `requested`.

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
            f"/repos/{owner}/{repo}/actions/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "actor": actor,
                        "branch": branch,
                        "check_suite_id": check_suite_id,
                        "created": created,
                        "event": event,
                        "exclude_pull_requests": exclude_pull_requests,
                        "head_sha": head_sha,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            cast_to=RunListResponse,
        )

    async def delete(
        self,
        run_id: int,
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
        Deletes a specific workflow run.

        Anyone with write access to the repository can use this endpoint.

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
        return await self._delete(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def approve(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Approves a workflow run for a pull request from a public fork of a first time
        contributor. For more information, see
        ["Approving workflow runs from public forks](https://docs.github.com/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks)."

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return await self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/approve",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def cancel(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Cancels a workflow run using its `id`.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return await self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def force_cancel(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Cancels a workflow run and bypasses conditions that would otherwise cause a
        workflow execution to continue, such as an `always()` condition on a job. You
        should only use this endpoint to cancel a workflow run when the workflow run is
        not responding to
        [`POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel`](/rest/actions/workflow-runs#cancel-a-workflow-run).

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        return await self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/force-cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def get_approvals(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunGetApprovalsResponse:
        """
        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/approvals",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RunGetApprovalsResponse,
        )

    async def get_timing(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunGetTimingResponse:
        """> [!WARNING]
        > This endpoint is in the process of closing down.

        Refer to
        > "[Actions Get workflow usage and Get workflow run usage endpoints closing down](https://github.blog/changelog/2025-02-02-actions-get-workflow-usage-and-get-workflow-run-usage-endpoints-closing-down/)"
        > for more information.

        Gets the number of billable minutes and total run time for a specific workflow
        run. Billable minutes only apply to workflows in private repositories that use
        GitHub-hosted runners. Usage is listed for each GitHub-hosted runner operating
        system in milliseconds. Any job re-runs are also included in the usage. The
        usage does not include the multiplier for macOS and Windows runners and is not
        rounded up to the nearest whole minute. For more information, see
        "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/timing",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RunGetTimingResponse,
        )

    async def list_artifacts(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListArtifactsResponse:
        """
        Lists artifacts for a workflow run.

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          name: The name field of an artifact. When specified, only artifacts with this name
              will be returned.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "page": page,
                        "per_page": per_page,
                    },
                    run_list_artifacts_params.RunListArtifactsParams,
                ),
            ),
            cast_to=RunListArtifactsResponse,
        )

    async def list_jobs(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        filter: Literal["latest", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunListJobsResponse:
        """Lists jobs for a workflow run.

        You can use parameters to narrow the list of
        results. For more information about using parameters, see
        [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          filter: Filters jobs by their `completed_at` timestamp. `latest` returns jobs from the
              most recent execution of the workflow run. `all` returns all jobs for a workflow
              run, including from old executions of the workflow run.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                    },
                    run_list_jobs_params.RunListJobsParams,
                ),
            ),
            cast_to=RunListJobsResponse,
        )

    async def rerun(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        enable_debug_logging: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Re-runs your workflow run using its `id`.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          enable_debug_logging: Whether to enable debug logging for the re-run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun",
            body=await async_maybe_transform({"enable_debug_logging": enable_debug_logging}, run_rerun_params.RunRerunParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def rerun_failed_jobs(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        enable_debug_logging: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Re-run all of the failed jobs and their dependent jobs in a workflow run using
        the `id` of the workflow run.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          enable_debug_logging: Whether to enable debug logging for the re-run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs",
            body=await async_maybe_transform({"enable_debug_logging": enable_debug_logging}, run_rerun_failed_jobs_params.RunRerunFailedJobsParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    @overload
    async def review_deployment_protection_rule(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        comment: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Approve or reject custom deployment protection rules provided by a GitHub App
        for a workflow run. For more information, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        > [!NOTE] GitHub Apps can only review their own custom deployment protection
        > rules. To approve or reject pending deployments that are waiting for review
        > from a specific person or team, see
        > [`POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments`](/rest/actions/workflow-runs#review-pending-deployments-for-a-workflow-run).

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          comment: Comment associated with the pending deployment protection rule. **Required when
              state is not provided.**

          environment_name: The name of the environment to approve or reject.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def review_deployment_protection_rule(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        state: Literal["approved", "rejected"],
        comment: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Approve or reject custom deployment protection rules provided by a GitHub App
        for a workflow run. For more information, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        > [!NOTE] GitHub Apps can only review their own custom deployment protection
        > rules. To approve or reject pending deployments that are waiting for review
        > from a specific person or team, see
        > [`POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments`](/rest/actions/workflow-runs#review-pending-deployments-for-a-workflow-run).

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

        Args:
          environment_name: The name of the environment to approve or reject.

          state: Whether to approve or reject deployment to the specified environments.

          comment: Optional comment to include with the review.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "repo", "comment", "environment_name"], ["owner", "repo", "environment_name", "state"])
    async def review_deployment_protection_rule(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        comment: str | NotGiven = NOT_GIVEN,
        environment_name: str,
        state: Literal["approved", "rejected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "environment_name": environment_name,
                    "state": state,
                },
                run_review_deployment_protection_rule_params.RunReviewDeploymentProtectionRuleParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.delete = to_raw_response_wrapper(
            runs.delete,
        )
        self.approve = to_raw_response_wrapper(
            runs.approve,
        )
        self.cancel = to_raw_response_wrapper(
            runs.cancel,
        )
        self.force_cancel = to_raw_response_wrapper(
            runs.force_cancel,
        )
        self.get_approvals = to_raw_response_wrapper(
            runs.get_approvals,
        )
        self.get_timing = to_raw_response_wrapper(
            runs.get_timing,
        )
        self.list_artifacts = to_raw_response_wrapper(
            runs.list_artifacts,
        )
        self.list_jobs = to_raw_response_wrapper(
            runs.list_jobs,
        )
        self.rerun = to_raw_response_wrapper(
            runs.rerun,
        )
        self.rerun_failed_jobs = to_raw_response_wrapper(
            runs.rerun_failed_jobs,
        )
        self.review_deployment_protection_rule = to_raw_response_wrapper(
            runs.review_deployment_protection_rule,
        )

    @cached_property
    def attempts(self) -> AttemptsResourceWithRawResponse:
        return AttemptsResourceWithRawResponse(self._runs.attempts)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._runs.logs)

    @cached_property
    def pending_deployments(self) -> PendingDeploymentsResourceWithRawResponse:
        return PendingDeploymentsResourceWithRawResponse(self._runs.pending_deployments)


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            runs.delete,
        )
        self.approve = async_to_raw_response_wrapper(
            runs.approve,
        )
        self.cancel = async_to_raw_response_wrapper(
            runs.cancel,
        )
        self.force_cancel = async_to_raw_response_wrapper(
            runs.force_cancel,
        )
        self.get_approvals = async_to_raw_response_wrapper(
            runs.get_approvals,
        )
        self.get_timing = async_to_raw_response_wrapper(
            runs.get_timing,
        )
        self.list_artifacts = async_to_raw_response_wrapper(
            runs.list_artifacts,
        )
        self.list_jobs = async_to_raw_response_wrapper(
            runs.list_jobs,
        )
        self.rerun = async_to_raw_response_wrapper(
            runs.rerun,
        )
        self.rerun_failed_jobs = async_to_raw_response_wrapper(
            runs.rerun_failed_jobs,
        )
        self.review_deployment_protection_rule = async_to_raw_response_wrapper(
            runs.review_deployment_protection_rule,
        )

    @cached_property
    def attempts(self) -> AsyncAttemptsResourceWithRawResponse:
        return AsyncAttemptsResourceWithRawResponse(self._runs.attempts)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._runs.logs)

    @cached_property
    def pending_deployments(self) -> AsyncPendingDeploymentsResourceWithRawResponse:
        return AsyncPendingDeploymentsResourceWithRawResponse(self._runs.pending_deployments)


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.delete = to_streamed_response_wrapper(
            runs.delete,
        )
        self.approve = to_streamed_response_wrapper(
            runs.approve,
        )
        self.cancel = to_streamed_response_wrapper(
            runs.cancel,
        )
        self.force_cancel = to_streamed_response_wrapper(
            runs.force_cancel,
        )
        self.get_approvals = to_streamed_response_wrapper(
            runs.get_approvals,
        )
        self.get_timing = to_streamed_response_wrapper(
            runs.get_timing,
        )
        self.list_artifacts = to_streamed_response_wrapper(
            runs.list_artifacts,
        )
        self.list_jobs = to_streamed_response_wrapper(
            runs.list_jobs,
        )
        self.rerun = to_streamed_response_wrapper(
            runs.rerun,
        )
        self.rerun_failed_jobs = to_streamed_response_wrapper(
            runs.rerun_failed_jobs,
        )
        self.review_deployment_protection_rule = to_streamed_response_wrapper(
            runs.review_deployment_protection_rule,
        )

    @cached_property
    def attempts(self) -> AttemptsResourceWithStreamingResponse:
        return AttemptsResourceWithStreamingResponse(self._runs.attempts)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._runs.logs)

    @cached_property
    def pending_deployments(self) -> PendingDeploymentsResourceWithStreamingResponse:
        return PendingDeploymentsResourceWithStreamingResponse(self._runs.pending_deployments)


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            runs.delete,
        )
        self.approve = async_to_streamed_response_wrapper(
            runs.approve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            runs.cancel,
        )
        self.force_cancel = async_to_streamed_response_wrapper(
            runs.force_cancel,
        )
        self.get_approvals = async_to_streamed_response_wrapper(
            runs.get_approvals,
        )
        self.get_timing = async_to_streamed_response_wrapper(
            runs.get_timing,
        )
        self.list_artifacts = async_to_streamed_response_wrapper(
            runs.list_artifacts,
        )
        self.list_jobs = async_to_streamed_response_wrapper(
            runs.list_jobs,
        )
        self.rerun = async_to_streamed_response_wrapper(
            runs.rerun,
        )
        self.rerun_failed_jobs = async_to_streamed_response_wrapper(
            runs.rerun_failed_jobs,
        )
        self.review_deployment_protection_rule = async_to_streamed_response_wrapper(
            runs.review_deployment_protection_rule,
        )

    @cached_property
    def attempts(self) -> AsyncAttemptsResourceWithStreamingResponse:
        return AsyncAttemptsResourceWithStreamingResponse(self._runs.attempts)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._runs.logs)

    @cached_property
    def pending_deployments(self) -> AsyncPendingDeploymentsResourceWithStreamingResponse:
        return AsyncPendingDeploymentsResourceWithStreamingResponse(self._runs.pending_deployments)
