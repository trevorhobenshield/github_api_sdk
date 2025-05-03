from __future__ import annotations

from typing import Optional

import httpx
from typing_extensions import Literal

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs import AlertSeverity, AlertStateQuery
from .....types.orgs.alert_severity import AlertSeverity
from .....types.orgs.alert_state_query import AlertStateQuery
from .....types.repos.code_scanning import CodeScanningAlertDismissedReason, alert_list_params, alert_update_params
from .....types.repos.code_scanning.alert_list_response import AlertListResponse
from .....types.repos.code_scanning.code_scanning_alert import CodeScanningAlert
from .....types.repos.code_scanning.code_scanning_alert_dismissed_reason import CodeScanningAlertDismissedReason
from .autofix import (
    AsyncAutofixResource,
    AsyncAutofixResourceWithRawResponse,
    AsyncAutofixResourceWithStreamingResponse,
    AutofixResource,
    AutofixResourceWithRawResponse,
    AutofixResourceWithStreamingResponse,
)
from .instances import (
    AsyncInstancesResource,
    AsyncInstancesResourceWithRawResponse,
    AsyncInstancesResourceWithStreamingResponse,
    InstancesResource,
    InstancesResourceWithRawResponse,
    InstancesResourceWithStreamingResponse,
)

__all__ = ["AlertsResource", "AsyncAlertsResource"]


class AlertsResource(SyncAPIResource):
    @cached_property
    def autofix(self) -> AutofixResource:
        return AutofixResource(self._client)

    @cached_property
    def instances(self) -> InstancesResource:
        return InstancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AlertsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningAlert:
        """
        Gets a single code scanning alert.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningAlert,
        )

    def update(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        state: Literal["open", "dismissed"],
        create_request: bool | NotGiven = NOT_GIVEN,
        dismissed_comment: str | None | NotGiven = NOT_GIVEN,
        dismissed_reason: CodeScanningAlertDismissedReason | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningAlert:
        """Updates the status of a single code scanning alert.

        OAuth app tokens and
        personal access tokens (classic) need the `security_events` scope to use this
        endpoint with private or public repositories, or the `public_repo` scope to use
        this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

          state: Sets the state of the code scanning alert. You must provide `dismissed_reason`
              when you set the state to `dismissed`.

          create_request: If `true`, attempt to create an alert dismissal request.

          dismissed_comment: The dismissal comment associated with the dismissal of the alert.

          dismissed_reason: **Required when the state is dismissed.** The reason for dismissing or closing
              the alert.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
            body=maybe_transform(
                {
                    "state": state,
                    "create_request": create_request,
                    "dismissed_comment": dismissed_comment,
                    "dismissed_reason": dismissed_reason,
                },
                alert_update_params.AlertUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningAlert,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        pr: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        severity: AlertSeverity | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        state: AlertStateQuery | NotGiven = NOT_GIVEN,
        tool_guid: str | None | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertListResponse:
        """
        Lists code scanning alerts.

        The response includes a `most_recent_instance` object. This provides details of
        the most recent instance of this alert for the default branch (or for the
        specified Git reference if you used `ref` in the request).

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          pr: The number of the pull request for the results you want to list.

          ref: The Git reference for the results you want to list. The `ref` for a branch can
              be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To
              reference a pull request use `refs/pull/<number>/merge`.

          severity: If specified, only code scanning alerts with this severity will be returned.

          sort: The property by which to sort the results.

          state: If specified, only code scanning alerts with this state will be returned.

          tool_guid: The GUID of a code scanning tool. Only results by this tool will be listed. Note
              that some code scanning tools may not include a GUID in their analysis data. You
              can specify the tool by using either `tool_guid` or `tool_name`, but not both.

          tool_name: The name of a code scanning tool. Only results by this tool will be listed. You
              can specify the tool by using either `tool_name` or `tool_guid`, but not both.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "pr": pr,
                        "ref": ref,
                        "severity": severity,
                        "sort": sort,
                        "state": state,
                        "tool_guid": tool_guid,
                        "tool_name": tool_name,
                    },
                    alert_list_params.AlertListParams,
                ),
            ),
            cast_to=AlertListResponse,
        )


class AsyncAlertsResource(AsyncAPIResource):
    @cached_property
    def autofix(self) -> AsyncAutofixResource:
        return AsyncAutofixResource(self._client)

    @cached_property
    def instances(self) -> AsyncInstancesResource:
        return AsyncInstancesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAlertsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningAlert:
        """
        Gets a single code scanning alert.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningAlert,
        )

    async def update(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        state: Literal["open", "dismissed"],
        create_request: bool | NotGiven = NOT_GIVEN,
        dismissed_comment: str | None | NotGiven = NOT_GIVEN,
        dismissed_reason: CodeScanningAlertDismissedReason | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningAlert:
        """Updates the status of a single code scanning alert.

        OAuth app tokens and
        personal access tokens (classic) need the `security_events` scope to use this
        endpoint with private or public repositories, or the `public_repo` scope to use
        this endpoint with only public repositories.

        Args:
          alert_number: The security alert number.

          state: Sets the state of the code scanning alert. You must provide `dismissed_reason`
              when you set the state to `dismissed`.

          create_request: If `true`, attempt to create an alert dismissal request.

          dismissed_comment: The dismissal comment associated with the dismissal of the alert.

          dismissed_reason: **Required when the state is dismissed.** The reason for dismissing or closing
              the alert.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
            body=await async_maybe_transform(
                {
                    "state": state,
                    "create_request": create_request,
                    "dismissed_comment": dismissed_comment,
                    "dismissed_reason": dismissed_reason,
                },
                alert_update_params.AlertUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningAlert,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        pr: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        severity: AlertSeverity | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        state: AlertStateQuery | NotGiven = NOT_GIVEN,
        tool_guid: str | None | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertListResponse:
        """
        Lists code scanning alerts.

        The response includes a `most_recent_instance` object. This provides details of
        the most recent instance of this alert for the default branch (or for the
        specified Git reference if you used `ref` in the request).

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          pr: The number of the pull request for the results you want to list.

          ref: The Git reference for the results you want to list. The `ref` for a branch can
              be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To
              reference a pull request use `refs/pull/<number>/merge`.

          severity: If specified, only code scanning alerts with this severity will be returned.

          sort: The property by which to sort the results.

          state: If specified, only code scanning alerts with this state will be returned.

          tool_guid: The GUID of a code scanning tool. Only results by this tool will be listed. Note
              that some code scanning tools may not include a GUID in their analysis data. You
              can specify the tool by using either `tool_guid` or `tool_name`, but not both.

          tool_name: The name of a code scanning tool. Only results by this tool will be listed. You
              can specify the tool by using either `tool_name` or `tool_guid`, but not both.

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
            f"/repos/{owner}/{repo}/code-scanning/alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "pr": pr,
                        "ref": ref,
                        "severity": severity,
                        "sort": sort,
                        "state": state,
                        "tool_guid": tool_guid,
                        "tool_name": tool_name,
                    },
                    alert_list_params.AlertListParams,
                ),
            ),
            cast_to=AlertListResponse,
        )


class AlertsResourceWithRawResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = to_raw_response_wrapper(
            alerts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            alerts.update,
        )
        self.list = to_raw_response_wrapper(
            alerts.list,
        )

    @cached_property
    def autofix(self) -> AutofixResourceWithRawResponse:
        return AutofixResourceWithRawResponse(self._alerts.autofix)

    @cached_property
    def instances(self) -> InstancesResourceWithRawResponse:
        return InstancesResourceWithRawResponse(self._alerts.instances)


class AsyncAlertsResourceWithRawResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = async_to_raw_response_wrapper(
            alerts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            alerts.update,
        )
        self.list = async_to_raw_response_wrapper(
            alerts.list,
        )

    @cached_property
    def autofix(self) -> AsyncAutofixResourceWithRawResponse:
        return AsyncAutofixResourceWithRawResponse(self._alerts.autofix)

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithRawResponse:
        return AsyncInstancesResourceWithRawResponse(self._alerts.instances)


class AlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = to_streamed_response_wrapper(
            alerts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            alerts.update,
        )
        self.list = to_streamed_response_wrapper(
            alerts.list,
        )

    @cached_property
    def autofix(self) -> AutofixResourceWithStreamingResponse:
        return AutofixResourceWithStreamingResponse(self._alerts.autofix)

    @cached_property
    def instances(self) -> InstancesResourceWithStreamingResponse:
        return InstancesResourceWithStreamingResponse(self._alerts.instances)


class AsyncAlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = async_to_streamed_response_wrapper(
            alerts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            alerts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            alerts.list,
        )

    @cached_property
    def autofix(self) -> AsyncAutofixResourceWithStreamingResponse:
        return AsyncAutofixResourceWithStreamingResponse(self._alerts.autofix)

    @cached_property
    def instances(self) -> AsyncInstancesResourceWithStreamingResponse:
        return AsyncInstancesResourceWithStreamingResponse(self._alerts.instances)
