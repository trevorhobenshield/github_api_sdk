from __future__ import annotations

from datetime import datetime
from typing import Iterable, Union

import httpx
from typing_extensions import Literal, overload

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
    required_args,
)
from ...types.repos import check_run_create_params, check_run_list_annotations_params, check_run_update_params
from ...types.repos.check_run import CheckRun
from ...types.repos.check_run_list_annotations_response import CheckRunListAnnotationsResponse

__all__ = ["CheckRunsResource", "AsyncCheckRunsResource"]


class CheckRunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CheckRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CheckRunsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        repo: str,
        *,
        owner: str,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"],
        status: Literal["completed"],
        actions: Iterable[check_run_create_params.Variant0Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        head_sha: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_create_params.Variant0Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Creates a new check run for a specific commit in a repository.

        To create a check run, you must use a GitHub App. OAuth apps and authenticated
        users are not able to create a check suite.

        In a check suite, GitHub limits the number of check runs with the same name
        to 1000. Once these check runs exceed 1000, GitHub will start to automatically
        delete older check runs.

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array.

        Args:
          conclusion: **Required if you provide `completed_at` or a `status` of `completed`**. The
              final conclusion of the check. **Note:** Providing `conclusion` will
              automatically set the `status` parameter to `completed`. You cannot change a
              check run conclusion to `stale`, only GitHub can set this.

          actions: Displays a button on GitHub that can be clicked to alert your app to do
              additional tasks. For example, a code linting app can display a button that
              automatically fixes detected errors. The button created in this object is
              displayed after the check run completes. When a user clicks the button, GitHub
              sends the
              [`check_run.requested_action` webhook](https://docs.github.com/webhooks/event-payloads/#check_run)
              to your app. Each action includes a `label`, `identifier` and `description`. A
              maximum of three actions are accepted. To learn more about check runs and
              requested actions, see
              "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."

          completed_at: The time the check completed. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          details_url: The URL of the integrator's site that has the full details of the check. If the
              integrator does not provide this, then the homepage of the GitHub app is used.

          external_id: A reference for the run on the integrator's system.

          head_sha: The SHA of the commit.

          name: The name of the check. For example, "code-coverage".

          output: Check runs can accept a variety of data in the `output` object, including a
              `title` and `summary` and can optionally provide descriptive details about the
              run.

          started_at: The time that the check run began. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        repo: str,
        *,
        owner: str,
        actions: Iterable[check_run_create_params.Variant1Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"] | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        head_sha: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_create_params.Variant1Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        status: Literal["queued", "in_progress"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Creates a new check run for a specific commit in a repository.

        To create a check run, you must use a GitHub App. OAuth apps and authenticated
        users are not able to create a check suite.

        In a check suite, GitHub limits the number of check runs with the same name
        to 1000. Once these check runs exceed 1000, GitHub will start to automatically
        delete older check runs.

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array.

        Args:
          actions: Displays a button on GitHub that can be clicked to alert your app to do
              additional tasks. For example, a code linting app can display a button that
              automatically fixes detected errors. The button created in this object is
              displayed after the check run completes. When a user clicks the button, GitHub
              sends the
              [`check_run.requested_action` webhook](https://docs.github.com/webhooks/event-payloads/#check_run)
              to your app. Each action includes a `label`, `identifier` and `description`. A
              maximum of three actions are accepted. To learn more about check runs and
              requested actions, see
              "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."

          completed_at: The time the check completed. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          conclusion: **Required if you provide `completed_at` or a `status` of `completed`**. The
              final conclusion of the check. **Note:** Providing `conclusion` will
              automatically set the `status` parameter to `completed`. You cannot change a
              check run conclusion to `stale`, only GitHub can set this.

          details_url: The URL of the integrator's site that has the full details of the check. If the
              integrator does not provide this, then the homepage of the GitHub app is used.

          external_id: A reference for the run on the integrator's system.

          head_sha: The SHA of the commit.

          name: The name of the check. For example, "code-coverage".

          output: Check runs can accept a variety of data in the `output` object, including a
              `title` and `summary` and can optionally provide descriptive details about the
              run.

          started_at: The time that the check run began. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "conclusion", "status"], ["owner"])
    def create(
        self,
        repo: str,
        *,
        owner: str,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"] | NotGiven = NOT_GIVEN,
        status: Literal["completed", "queued", "in_progress"] | NotGiven = NOT_GIVEN,
        actions: Iterable[check_run_create_params.Variant0Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        head_sha: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_create_params.Variant0Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/check-runs",
            body=maybe_transform(
                {
                    "conclusion": conclusion,
                    "status": status,
                    "actions": actions,
                    "completed_at": completed_at,
                    "details_url": details_url,
                    "external_id": external_id,
                    "head_sha": head_sha,
                    "name": name,
                    "output": output,
                    "started_at": started_at,
                },
                check_run_create_params.CheckRunCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckRun,
        )

    def retrieve(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Gets a single check run using its `id`.

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

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
            f"/repos/{owner}/{repo}/check-runs/{check_run_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckRun,
        )

    @overload
    def update(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"],
        actions: Iterable[check_run_update_params.Variant0Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_update_params.Variant0Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        status: Literal["completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Updates a check run for a specific commit in a repository.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array.

        OAuth apps and personal access tokens (classic) cannot use this endpoint.

        Args:
          conclusion: **Required if you provide `completed_at` or a `status` of `completed`**. The
              final conclusion of the check. **Note:** Providing `conclusion` will
              automatically set the `status` parameter to `completed`. You cannot change a
              check run conclusion to `stale`, only GitHub can set this.

          actions: Possible further actions the integrator can perform, which a user may trigger.
              Each action includes a `label`, `identifier` and `description`. A maximum of
              three actions are accepted. To learn more about check runs and requested
              actions, see
              "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."

          completed_at: The time the check completed. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          details_url: The URL of the integrator's site that has the full details of the check.

          external_id: A reference for the run on the integrator's system.

          name: The name of the check. For example, "code-coverage".

          output: Check runs can accept a variety of data in the `output` object, including a
              `title` and `summary` and can optionally provide descriptive details about the
              run.

          started_at: This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
              format: `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        actions: Iterable[check_run_update_params.Variant1Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"] | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_update_params.Variant1Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        status: Literal["queued", "in_progress"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Updates a check run for a specific commit in a repository.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array.

        OAuth apps and personal access tokens (classic) cannot use this endpoint.

        Args:
          actions: Possible further actions the integrator can perform, which a user may trigger.
              Each action includes a `label`, `identifier` and `description`. A maximum of
              three actions are accepted. To learn more about check runs and requested
              actions, see
              "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."

          completed_at: The time the check completed. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          conclusion: **Required if you provide `completed_at` or a `status` of `completed`**. The
              final conclusion of the check. **Note:** Providing `conclusion` will
              automatically set the `status` parameter to `completed`. You cannot change a
              check run conclusion to `stale`, only GitHub can set this.

          details_url: The URL of the integrator's site that has the full details of the check.

          external_id: A reference for the run on the integrator's system.

          name: The name of the check. For example, "code-coverage".

          output: Check runs can accept a variety of data in the `output` object, including a
              `title` and `summary` and can optionally provide descriptive details about the
              run.

          started_at: This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
              format: `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "repo", "conclusion"], ["owner", "repo"])
    def update(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"] | NotGiven = NOT_GIVEN,
        actions: Iterable[check_run_update_params.Variant0Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_update_params.Variant0Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        status: Literal["completed", "queued", "in_progress"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/check-runs/{check_run_id}",
            body=maybe_transform(
                {
                    "conclusion": conclusion,
                    "actions": actions,
                    "completed_at": completed_at,
                    "details_url": details_url,
                    "external_id": external_id,
                    "name": name,
                    "output": output,
                    "started_at": started_at,
                    "status": status,
                },
                check_run_update_params.CheckRunUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckRun,
        )

    def list_annotations(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRunListAnnotationsResponse:
        """
        Lists annotations for a check run using the annotation `id`.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

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
            f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations",
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
                    check_run_list_annotations_params.CheckRunListAnnotationsParams,
                ),
            ),
            cast_to=CheckRunListAnnotationsResponse,
        )

    def rerequest(
        self,
        check_run_id: int,
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
        Triggers GitHub to rerequest an existing check run, without pushing new code to
        a repository. This endpoint will trigger the
        [`check_run` webhook](https://docs.github.com/webhooks/event-payloads/#check_run)
        event with the action `rerequested`. When a check run is `rerequested`, its
        `status` is reset to `queued` and the `conclusion` is cleared.

        For more information about how to re-run GitHub Actions jobs, see
        "[Re-run a job from a workflow run](https://docs.github.com/rest/actions/workflow-runs#re-run-a-job-from-a-workflow-run)".

        OAuth apps and personal access tokens (classic) cannot use this endpoint.

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
            f"/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class AsyncCheckRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCheckRunsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        repo: str,
        *,
        owner: str,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"],
        status: Literal["completed"],
        actions: Iterable[check_run_create_params.Variant0Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        head_sha: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_create_params.Variant0Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Creates a new check run for a specific commit in a repository.

        To create a check run, you must use a GitHub App. OAuth apps and authenticated
        users are not able to create a check suite.

        In a check suite, GitHub limits the number of check runs with the same name
        to 1000. Once these check runs exceed 1000, GitHub will start to automatically
        delete older check runs.

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array.

        Args:
          conclusion: **Required if you provide `completed_at` or a `status` of `completed`**. The
              final conclusion of the check. **Note:** Providing `conclusion` will
              automatically set the `status` parameter to `completed`. You cannot change a
              check run conclusion to `stale`, only GitHub can set this.

          actions: Displays a button on GitHub that can be clicked to alert your app to do
              additional tasks. For example, a code linting app can display a button that
              automatically fixes detected errors. The button created in this object is
              displayed after the check run completes. When a user clicks the button, GitHub
              sends the
              [`check_run.requested_action` webhook](https://docs.github.com/webhooks/event-payloads/#check_run)
              to your app. Each action includes a `label`, `identifier` and `description`. A
              maximum of three actions are accepted. To learn more about check runs and
              requested actions, see
              "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."

          completed_at: The time the check completed. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          details_url: The URL of the integrator's site that has the full details of the check. If the
              integrator does not provide this, then the homepage of the GitHub app is used.

          external_id: A reference for the run on the integrator's system.

          head_sha: The SHA of the commit.

          name: The name of the check. For example, "code-coverage".

          output: Check runs can accept a variety of data in the `output` object, including a
              `title` and `summary` and can optionally provide descriptive details about the
              run.

          started_at: The time that the check run began. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        repo: str,
        *,
        owner: str,
        actions: Iterable[check_run_create_params.Variant1Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"] | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        head_sha: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_create_params.Variant1Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        status: Literal["queued", "in_progress"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Creates a new check run for a specific commit in a repository.

        To create a check run, you must use a GitHub App. OAuth apps and authenticated
        users are not able to create a check suite.

        In a check suite, GitHub limits the number of check runs with the same name
        to 1000. Once these check runs exceed 1000, GitHub will start to automatically
        delete older check runs.

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array.

        Args:
          actions: Displays a button on GitHub that can be clicked to alert your app to do
              additional tasks. For example, a code linting app can display a button that
              automatically fixes detected errors. The button created in this object is
              displayed after the check run completes. When a user clicks the button, GitHub
              sends the
              [`check_run.requested_action` webhook](https://docs.github.com/webhooks/event-payloads/#check_run)
              to your app. Each action includes a `label`, `identifier` and `description`. A
              maximum of three actions are accepted. To learn more about check runs and
              requested actions, see
              "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."

          completed_at: The time the check completed. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          conclusion: **Required if you provide `completed_at` or a `status` of `completed`**. The
              final conclusion of the check. **Note:** Providing `conclusion` will
              automatically set the `status` parameter to `completed`. You cannot change a
              check run conclusion to `stale`, only GitHub can set this.

          details_url: The URL of the integrator's site that has the full details of the check. If the
              integrator does not provide this, then the homepage of the GitHub app is used.

          external_id: A reference for the run on the integrator's system.

          head_sha: The SHA of the commit.

          name: The name of the check. For example, "code-coverage".

          output: Check runs can accept a variety of data in the `output` object, including a
              `title` and `summary` and can optionally provide descriptive details about the
              run.

          started_at: The time that the check run began. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "conclusion", "status"], ["owner"])
    async def create(
        self,
        repo: str,
        *,
        owner: str,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"] | NotGiven = NOT_GIVEN,
        status: Literal["completed", "queued", "in_progress"] | NotGiven = NOT_GIVEN,
        actions: Iterable[check_run_create_params.Variant0Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        head_sha: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_create_params.Variant0Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/check-runs",
            body=await async_maybe_transform(
                {
                    "conclusion": conclusion,
                    "status": status,
                    "actions": actions,
                    "completed_at": completed_at,
                    "details_url": details_url,
                    "external_id": external_id,
                    "head_sha": head_sha,
                    "name": name,
                    "output": output,
                    "started_at": started_at,
                },
                check_run_create_params.CheckRunCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckRun,
        )

    async def retrieve(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Gets a single check run using its `id`.

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

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
            f"/repos/{owner}/{repo}/check-runs/{check_run_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckRun,
        )

    @overload
    async def update(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"],
        actions: Iterable[check_run_update_params.Variant0Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_update_params.Variant0Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        status: Literal["completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Updates a check run for a specific commit in a repository.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array.

        OAuth apps and personal access tokens (classic) cannot use this endpoint.

        Args:
          conclusion: **Required if you provide `completed_at` or a `status` of `completed`**. The
              final conclusion of the check. **Note:** Providing `conclusion` will
              automatically set the `status` parameter to `completed`. You cannot change a
              check run conclusion to `stale`, only GitHub can set this.

          actions: Possible further actions the integrator can perform, which a user may trigger.
              Each action includes a `label`, `identifier` and `description`. A maximum of
              three actions are accepted. To learn more about check runs and requested
              actions, see
              "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."

          completed_at: The time the check completed. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          details_url: The URL of the integrator's site that has the full details of the check.

          external_id: A reference for the run on the integrator's system.

          name: The name of the check. For example, "code-coverage".

          output: Check runs can accept a variety of data in the `output` object, including a
              `title` and `summary` and can optionally provide descriptive details about the
              run.

          started_at: This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
              format: `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        actions: Iterable[check_run_update_params.Variant1Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"] | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_update_params.Variant1Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        status: Literal["queued", "in_progress"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        """
        Updates a check run for a specific commit in a repository.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array.

        OAuth apps and personal access tokens (classic) cannot use this endpoint.

        Args:
          actions: Possible further actions the integrator can perform, which a user may trigger.
              Each action includes a `label`, `identifier` and `description`. A maximum of
              three actions are accepted. To learn more about check runs and requested
              actions, see
              "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."

          completed_at: The time the check completed. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          conclusion: **Required if you provide `completed_at` or a `status` of `completed`**. The
              final conclusion of the check. **Note:** Providing `conclusion` will
              automatically set the `status` parameter to `completed`. You cannot change a
              check run conclusion to `stale`, only GitHub can set this.

          details_url: The URL of the integrator's site that has the full details of the check.

          external_id: A reference for the run on the integrator's system.

          name: The name of the check. For example, "code-coverage".

          output: Check runs can accept a variety of data in the `output` object, including a
              `title` and `summary` and can optionally provide descriptive details about the
              run.

          started_at: This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
              format: `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "repo", "conclusion"], ["owner", "repo"])
    async def update(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        conclusion: Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"] | NotGiven = NOT_GIVEN,
        actions: Iterable[check_run_update_params.Variant0Action] | NotGiven = NOT_GIVEN,
        completed_at: str | datetime | NotGiven = NOT_GIVEN,
        details_url: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        output: check_run_update_params.Variant0Output | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        status: Literal["completed", "queued", "in_progress"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRun:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/check-runs/{check_run_id}",
            body=await async_maybe_transform(
                {
                    "conclusion": conclusion,
                    "actions": actions,
                    "completed_at": completed_at,
                    "details_url": details_url,
                    "external_id": external_id,
                    "name": name,
                    "output": output,
                    "started_at": started_at,
                    "status": status,
                },
                check_run_update_params.CheckRunUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckRun,
        )

    async def list_annotations(
        self,
        check_run_id: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckRunListAnnotationsResponse:
        """
        Lists annotations for a check run using the annotation `id`.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

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
            f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations",
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
                    check_run_list_annotations_params.CheckRunListAnnotationsParams,
                ),
            ),
            cast_to=CheckRunListAnnotationsResponse,
        )

    async def rerequest(
        self,
        check_run_id: int,
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
        Triggers GitHub to rerequest an existing check run, without pushing new code to
        a repository. This endpoint will trigger the
        [`check_run` webhook](https://docs.github.com/webhooks/event-payloads/#check_run)
        event with the action `rerequested`. When a check run is `rerequested`, its
        `status` is reset to `queued` and the `conclusion` is cleared.

        For more information about how to re-run GitHub Actions jobs, see
        "[Re-run a job from a workflow run](https://docs.github.com/rest/actions/workflow-runs#re-run-a-job-from-a-workflow-run)".

        OAuth apps and personal access tokens (classic) cannot use this endpoint.

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
            f"/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class CheckRunsResourceWithRawResponse:
    def __init__(self, check_runs: CheckRunsResource) -> None:
        self._check_runs = check_runs

        self.create = to_raw_response_wrapper(
            check_runs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            check_runs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            check_runs.update,
        )
        self.list_annotations = to_raw_response_wrapper(
            check_runs.list_annotations,
        )
        self.rerequest = to_raw_response_wrapper(
            check_runs.rerequest,
        )


class AsyncCheckRunsResourceWithRawResponse:
    def __init__(self, check_runs: AsyncCheckRunsResource) -> None:
        self._check_runs = check_runs

        self.create = async_to_raw_response_wrapper(
            check_runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            check_runs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            check_runs.update,
        )
        self.list_annotations = async_to_raw_response_wrapper(
            check_runs.list_annotations,
        )
        self.rerequest = async_to_raw_response_wrapper(
            check_runs.rerequest,
        )


class CheckRunsResourceWithStreamingResponse:
    def __init__(self, check_runs: CheckRunsResource) -> None:
        self._check_runs = check_runs

        self.create = to_streamed_response_wrapper(
            check_runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            check_runs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            check_runs.update,
        )
        self.list_annotations = to_streamed_response_wrapper(
            check_runs.list_annotations,
        )
        self.rerequest = to_streamed_response_wrapper(
            check_runs.rerequest,
        )


class AsyncCheckRunsResourceWithStreamingResponse:
    def __init__(self, check_runs: AsyncCheckRunsResource) -> None:
        self._check_runs = check_runs

        self.create = async_to_streamed_response_wrapper(
            check_runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            check_runs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            check_runs.update,
        )
        self.list_annotations = async_to_streamed_response_wrapper(
            check_runs.list_annotations,
        )
        self.rerequest = async_to_streamed_response_wrapper(
            check_runs.rerequest,
        )
