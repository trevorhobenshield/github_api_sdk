from __future__ import annotations

from datetime import datetime
from typing import Dict, Union

import httpx
from typing_extensions import Literal

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
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.actions import workflow_dispatch_params, workflow_list_params, workflow_list_runs_params
from ....types.repos.actions.workflow import Workflow
from ....types.repos.actions.workflow_get_timing_response import WorkflowGetTimingResponse
from ....types.repos.actions.workflow_list_response import WorkflowListResponse
from ....types.repos.actions.workflow_list_runs_response import WorkflowListRunsResponse

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        workflow_id: int | str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """Gets a specific workflow.

        You can replace `workflow_id` with the workflow file
        name. For example, you could use `main.yaml`.

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
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Workflow,
        )

    def list(
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
    ) -> WorkflowListResponse:
        """
        Lists the workflows in a repository.

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
            f"/repos/{owner}/{repo}/actions/workflows",
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
                    workflow_list_params.WorkflowListParams,
                ),
            ),
            cast_to=WorkflowListResponse,
        )

    def disable(
        self,
        workflow_id: int | str,
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
        Disables a workflow and sets the `state` of the workflow to `disabled_manually`.
        You can replace `workflow_id` with the workflow file name. For example, you
        could use `main.yaml`.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def dispatch(
        self,
        workflow_id: int | str,
        *,
        owner: str,
        repo: str,
        ref: str,
        inputs: dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """You can use this endpoint to manually trigger a GitHub Actions workflow run.

        You
        can replace `workflow_id` with the workflow file name. For example, you could
        use `main.yaml`.

        You must configure your GitHub Actions workflow to run when the
        [`workflow_dispatch` webhook](/developers/webhooks-and-events/webhook-events-and-payloads#workflow_dispatch)
        event occurs. The `inputs` are configured in the workflow file. For more
        information about how to configure the `workflow_dispatch` event in the workflow
        file, see
        "[Events that trigger workflows](/actions/reference/events-that-trigger-workflows#workflow_dispatch)."

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
          ref: The git reference for the workflow. The reference can be a branch or tag name.

          inputs: Input keys and values configured in the workflow file. The maximum number of
              properties is 10. Any default properties configured in the workflow file will be
              used when `inputs` are omitted.

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
        return self._post(
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
            body=maybe_transform(
                {
                    "ref": ref,
                    "inputs": inputs,
                },
                workflow_dispatch_params.WorkflowDispatchParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def enable(
        self,
        workflow_id: int | str,
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
        """Enables a workflow and sets the `state` of the workflow to `active`.

        You can
        replace `workflow_id` with the workflow file name. For example, you could use
        `main.yaml`.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_timing(
        self,
        workflow_id: int | str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowGetTimingResponse:
        """> [!WARNING]
        > This endpoint is in the process of closing down.

        Refer to
        > "[Actions Get workflow usage and Get workflow run usage endpoints closing down](https://github.blog/changelog/2025-02-02-actions-get-workflow-usage-and-get-workflow-run-usage-endpoints-closing-down/)"
        > for more information.

        Gets the number of billable minutes used by a specific workflow during the
        current billing cycle. Billable minutes only apply to workflows in private
        repositories that use GitHub-hosted runners. Usage is listed for each
        GitHub-hosted runner operating system in milliseconds. Any job re-runs are also
        included in the usage. The usage does not include the multiplier for macOS and
        Windows runners and is not rounded up to the nearest whole minute. For more
        information, see
        "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        You can replace `workflow_id` with the workflow file name. For example, you
        could use `main.yaml`.

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
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkflowGetTimingResponse,
        )

    def list_runs(
        self,
        workflow_id: int | str,
        *,
        owner: str,
        repo: str,
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
    ) -> WorkflowListRunsResponse:
        """List all workflow runs for a workflow.

        You can replace `workflow_id` with the
        workflow file name. For example, you could use `main.yaml`. You can use
        parameters to narrow the list of results. For more information about using
        parameters, see
        [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).

        Anyone with read access to the repository can use this endpoint

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
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs",
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
                    workflow_list_runs_params.WorkflowListRunsParams,
                ),
            ),
            cast_to=WorkflowListRunsResponse,
        )


class AsyncWorkflowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        workflow_id: int | str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Workflow:
        """Gets a specific workflow.

        You can replace `workflow_id` with the workflow file
        name. For example, you could use `main.yaml`.

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
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Workflow,
        )

    async def list(
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
    ) -> WorkflowListResponse:
        """
        Lists the workflows in a repository.

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
            f"/repos/{owner}/{repo}/actions/workflows",
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
                    workflow_list_params.WorkflowListParams,
                ),
            ),
            cast_to=WorkflowListResponse,
        )

    async def disable(
        self,
        workflow_id: int | str,
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
        Disables a workflow and sets the `state` of the workflow to `disabled_manually`.
        You can replace `workflow_id` with the workflow file name. For example, you
        could use `main.yaml`.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def dispatch(
        self,
        workflow_id: int | str,
        *,
        owner: str,
        repo: str,
        ref: str,
        inputs: dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """You can use this endpoint to manually trigger a GitHub Actions workflow run.

        You
        can replace `workflow_id` with the workflow file name. For example, you could
        use `main.yaml`.

        You must configure your GitHub Actions workflow to run when the
        [`workflow_dispatch` webhook](/developers/webhooks-and-events/webhook-events-and-payloads#workflow_dispatch)
        event occurs. The `inputs` are configured in the workflow file. For more
        information about how to configure the `workflow_dispatch` event in the workflow
        file, see
        "[Events that trigger workflows](/actions/reference/events-that-trigger-workflows#workflow_dispatch)."

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
          ref: The git reference for the workflow. The reference can be a branch or tag name.

          inputs: Input keys and values configured in the workflow file. The maximum number of
              properties is 10. Any default properties configured in the workflow file will be
              used when `inputs` are omitted.

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
        return await self._post(
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
            body=await async_maybe_transform(
                {
                    "ref": ref,
                    "inputs": inputs,
                },
                workflow_dispatch_params.WorkflowDispatchParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def enable(
        self,
        workflow_id: int | str,
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
        """Enables a workflow and sets the `state` of the workflow to `active`.

        You can
        replace `workflow_id` with the workflow file name. For example, you could use
        `main.yaml`.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_timing(
        self,
        workflow_id: int | str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkflowGetTimingResponse:
        """> [!WARNING]
        > This endpoint is in the process of closing down.

        Refer to
        > "[Actions Get workflow usage and Get workflow run usage endpoints closing down](https://github.blog/changelog/2025-02-02-actions-get-workflow-usage-and-get-workflow-run-usage-endpoints-closing-down/)"
        > for more information.

        Gets the number of billable minutes used by a specific workflow during the
        current billing cycle. Billable minutes only apply to workflows in private
        repositories that use GitHub-hosted runners. Usage is listed for each
        GitHub-hosted runner operating system in milliseconds. Any job re-runs are also
        included in the usage. The usage does not include the multiplier for macOS and
        Windows runners and is not rounded up to the nearest whole minute. For more
        information, see
        "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        You can replace `workflow_id` with the workflow file name. For example, you
        could use `main.yaml`.

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
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=WorkflowGetTimingResponse,
        )

    async def list_runs(
        self,
        workflow_id: int | str,
        *,
        owner: str,
        repo: str,
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
    ) -> WorkflowListRunsResponse:
        """List all workflow runs for a workflow.

        You can replace `workflow_id` with the
        workflow file name. For example, you could use `main.yaml`. You can use
        parameters to narrow the list of results. For more information about using
        parameters, see
        [Parameters](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#parameters).

        Anyone with read access to the repository can use this endpoint

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
            f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs",
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
                    workflow_list_runs_params.WorkflowListRunsParams,
                ),
            ),
            cast_to=WorkflowListRunsResponse,
        )


class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.retrieve = to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.list = to_raw_response_wrapper(
            workflows.list,
        )
        self.disable = to_raw_response_wrapper(
            workflows.disable,
        )
        self.dispatch = to_raw_response_wrapper(
            workflows.dispatch,
        )
        self.enable = to_raw_response_wrapper(
            workflows.enable,
        )
        self.get_timing = to_raw_response_wrapper(
            workflows.get_timing,
        )
        self.list_runs = to_raw_response_wrapper(
            workflows.list_runs,
        )


class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.retrieve = async_to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            workflows.list,
        )
        self.disable = async_to_raw_response_wrapper(
            workflows.disable,
        )
        self.dispatch = async_to_raw_response_wrapper(
            workflows.dispatch,
        )
        self.enable = async_to_raw_response_wrapper(
            workflows.enable,
        )
        self.get_timing = async_to_raw_response_wrapper(
            workflows.get_timing,
        )
        self.list_runs = async_to_raw_response_wrapper(
            workflows.list_runs,
        )


class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.retrieve = to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            workflows.list,
        )
        self.disable = to_streamed_response_wrapper(
            workflows.disable,
        )
        self.dispatch = to_streamed_response_wrapper(
            workflows.dispatch,
        )
        self.enable = to_streamed_response_wrapper(
            workflows.enable,
        )
        self.get_timing = to_streamed_response_wrapper(
            workflows.get_timing,
        )
        self.list_runs = to_streamed_response_wrapper(
            workflows.list_runs,
        )


class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.retrieve = async_to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            workflows.list,
        )
        self.disable = async_to_streamed_response_wrapper(
            workflows.disable,
        )
        self.dispatch = async_to_streamed_response_wrapper(
            workflows.dispatch,
        )
        self.enable = async_to_streamed_response_wrapper(
            workflows.enable,
        )
        self.get_timing = async_to_streamed_response_wrapper(
            workflows.get_timing,
        )
        self.list_runs = async_to_streamed_response_wrapper(
            workflows.list_runs,
        )
