from __future__ import annotations

from typing import Iterable

import httpx
from typing_extensions import Literal

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
from ...types.repos import (
    check_suite_create_params,
    check_suite_list_check_runs_params,
    check_suite_update_preferences_params,
)
from ...types.repos.check_suite import CheckSuite
from ...types.repos.check_suite_list_check_runs_response import CheckSuiteListCheckRunsResponse
from ...types.repos.check_suite_update_preferences_response import CheckSuiteUpdatePreferencesResponse

__all__ = ["CheckSuitesResource", "AsyncCheckSuitesResource"]


class CheckSuitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckSuitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CheckSuitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckSuitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CheckSuitesResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        head_sha: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckSuite:
        """Creates a check suite manually.

        By default, check suites are automatically
        created when you create a [check run](https://docs.github.com/rest/checks/runs).
        You only need to use this endpoint for manually creating check suites when
        you've disabled automatic creation using
        "[Update repository preferences for check suites](https://docs.github.com/rest/checks/suites#update-repository-preferences-for-check-suites)".

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array and a `null` value for
        > `head_branch`.

        OAuth apps and personal access tokens (classic) cannot use this endpoint.

        Args:
          head_sha: The sha of the head commit.

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
            f"/repos/{owner}/{repo}/check-suites",
            body=maybe_transform({"head_sha": head_sha}, check_suite_create_params.CheckSuiteCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckSuite,
        )

    def retrieve(
        self,
        check_suite_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckSuite:
        """
        Gets a single check suite using its `id`.

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array and a `null` value for
        > `head_branch`.

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
            f"/repos/{owner}/{repo}/check-suites/{check_suite_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckSuite,
        )

    def list_check_runs(
        self,
        check_suite_id: int,
        *,
        owner: str,
        repo: str,
        check_name: str | NotGiven = NOT_GIVEN,
        filter: Literal["latest", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["queued", "in_progress", "completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckSuiteListCheckRunsResponse:
        """
        Lists check runs for a check suite using its `id`.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

        Args:
          check_name: Returns check runs with the specified `name`.

          filter: Filters check runs by their `completed_at` timestamp. `latest` returns the most
              recent check runs.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: Returns check runs with the specified `status`.

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
            f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "check_name": check_name,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    check_suite_list_check_runs_params.CheckSuiteListCheckRunsParams,
                ),
            ),
            cast_to=CheckSuiteListCheckRunsResponse,
        )

    def rerequest(
        self,
        check_suite_id: int,
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
        Triggers GitHub to rerequest an existing check suite, without pushing new code
        to a repository. This endpoint will trigger the
        [`check_suite` webhook](https://docs.github.com/webhooks/event-payloads/#check_suite)
        event with the action `rerequested`. When a check suite is `rerequested`, its
        `status` is reset to `queued` and the `conclusion` is cleared.

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
            f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def update_preferences(
        self,
        repo: str,
        *,
        owner: str,
        auto_trigger_checks: Iterable[check_suite_update_preferences_params.AutoTriggerCheck] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckSuiteUpdatePreferencesResponse:
        """Changes the default automatic flow when creating check suites.

        By default, a
        check suite is automatically created each time code is pushed to a repository.
        When you disable the automatic creation of check suites, you can manually
        [Create a check suite](https://docs.github.com/rest/checks/suites#create-a-check-suite).
        You must have admin permissions in the repository to set preferences for check
        suites.

        Args:
          auto_trigger_checks: Enables or disables automatic creation of CheckSuite events upon pushes to the
              repository. Enabled by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/check-suites/preferences",
            body=maybe_transform(
                {"auto_trigger_checks": auto_trigger_checks},
                check_suite_update_preferences_params.CheckSuiteUpdatePreferencesParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckSuiteUpdatePreferencesResponse,
        )


class AsyncCheckSuitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckSuitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckSuitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckSuitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCheckSuitesResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        head_sha: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckSuite:
        """Creates a check suite manually.

        By default, check suites are automatically
        created when you create a [check run](https://docs.github.com/rest/checks/runs).
        You only need to use this endpoint for manually creating check suites when
        you've disabled automatic creation using
        "[Update repository preferences for check suites](https://docs.github.com/rest/checks/suites#update-repository-preferences-for-check-suites)".

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array and a `null` value for
        > `head_branch`.

        OAuth apps and personal access tokens (classic) cannot use this endpoint.

        Args:
          head_sha: The sha of the head commit.

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
            f"/repos/{owner}/{repo}/check-suites",
            body=await async_maybe_transform({"head_sha": head_sha}, check_suite_create_params.CheckSuiteCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckSuite,
        )

    async def retrieve(
        self,
        check_suite_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckSuite:
        """
        Gets a single check suite using its `id`.

        > [!NOTE] The Checks API only looks for pushes in the repository where the check
        > suite or check run were created. Pushes to a branch in a forked repository are
        > not detected and return an empty `pull_requests` array and a `null` value for
        > `head_branch`.

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
            f"/repos/{owner}/{repo}/check-suites/{check_suite_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckSuite,
        )

    async def list_check_runs(
        self,
        check_suite_id: int,
        *,
        owner: str,
        repo: str,
        check_name: str | NotGiven = NOT_GIVEN,
        filter: Literal["latest", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["queued", "in_progress", "completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckSuiteListCheckRunsResponse:
        """
        Lists check runs for a check suite using its `id`.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

        Args:
          check_name: Returns check runs with the specified `name`.

          filter: Filters check runs by their `completed_at` timestamp. `latest` returns the most
              recent check runs.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: Returns check runs with the specified `status`.

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
            f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "check_name": check_name,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    check_suite_list_check_runs_params.CheckSuiteListCheckRunsParams,
                ),
            ),
            cast_to=CheckSuiteListCheckRunsResponse,
        )

    async def rerequest(
        self,
        check_suite_id: int,
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
        Triggers GitHub to rerequest an existing check suite, without pushing new code
        to a repository. This endpoint will trigger the
        [`check_suite` webhook](https://docs.github.com/webhooks/event-payloads/#check_suite)
        event with the action `rerequested`. When a check suite is `rerequested`, its
        `status` is reset to `queued` and the `conclusion` is cleared.

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
            f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def update_preferences(
        self,
        repo: str,
        *,
        owner: str,
        auto_trigger_checks: Iterable[check_suite_update_preferences_params.AutoTriggerCheck] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckSuiteUpdatePreferencesResponse:
        """Changes the default automatic flow when creating check suites.

        By default, a
        check suite is automatically created each time code is pushed to a repository.
        When you disable the automatic creation of check suites, you can manually
        [Create a check suite](https://docs.github.com/rest/checks/suites#create-a-check-suite).
        You must have admin permissions in the repository to set preferences for check
        suites.

        Args:
          auto_trigger_checks: Enables or disables automatic creation of CheckSuite events upon pushes to the
              repository. Enabled by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/check-suites/preferences",
            body=await async_maybe_transform(
                {"auto_trigger_checks": auto_trigger_checks},
                check_suite_update_preferences_params.CheckSuiteUpdatePreferencesParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CheckSuiteUpdatePreferencesResponse,
        )


class CheckSuitesResourceWithRawResponse:
    def __init__(self, check_suites: CheckSuitesResource) -> None:
        self._check_suites = check_suites

        self.create = to_raw_response_wrapper(
            check_suites.create,
        )
        self.retrieve = to_raw_response_wrapper(
            check_suites.retrieve,
        )
        self.list_check_runs = to_raw_response_wrapper(
            check_suites.list_check_runs,
        )
        self.rerequest = to_raw_response_wrapper(
            check_suites.rerequest,
        )
        self.update_preferences = to_raw_response_wrapper(
            check_suites.update_preferences,
        )


class AsyncCheckSuitesResourceWithRawResponse:
    def __init__(self, check_suites: AsyncCheckSuitesResource) -> None:
        self._check_suites = check_suites

        self.create = async_to_raw_response_wrapper(
            check_suites.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            check_suites.retrieve,
        )
        self.list_check_runs = async_to_raw_response_wrapper(
            check_suites.list_check_runs,
        )
        self.rerequest = async_to_raw_response_wrapper(
            check_suites.rerequest,
        )
        self.update_preferences = async_to_raw_response_wrapper(
            check_suites.update_preferences,
        )


class CheckSuitesResourceWithStreamingResponse:
    def __init__(self, check_suites: CheckSuitesResource) -> None:
        self._check_suites = check_suites

        self.create = to_streamed_response_wrapper(
            check_suites.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            check_suites.retrieve,
        )
        self.list_check_runs = to_streamed_response_wrapper(
            check_suites.list_check_runs,
        )
        self.rerequest = to_streamed_response_wrapper(
            check_suites.rerequest,
        )
        self.update_preferences = to_streamed_response_wrapper(
            check_suites.update_preferences,
        )


class AsyncCheckSuitesResourceWithStreamingResponse:
    def __init__(self, check_suites: AsyncCheckSuitesResource) -> None:
        self._check_suites = check_suites

        self.create = async_to_streamed_response_wrapper(
            check_suites.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            check_suites.retrieve,
        )
        self.list_check_runs = async_to_streamed_response_wrapper(
            check_suites.list_check_runs,
        )
        self.rerequest = async_to_streamed_response_wrapper(
            check_suites.rerequest,
        )
        self.update_preferences = async_to_streamed_response_wrapper(
            check_suites.update_preferences,
        )
