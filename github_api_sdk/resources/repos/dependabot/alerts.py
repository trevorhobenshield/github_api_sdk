from __future__ import annotations

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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.dependabot import alert_list_params, alert_update_params
from ....types.repos.dependabot.alert_list_response import AlertListResponse
from ....types.repos.dependabot.dependabot_alert import DependabotAlert

__all__ = ["AlertsResource", "AsyncAlertsResource"]


class AlertsResource(SyncAPIResource):
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
    ) -> DependabotAlert:
        """
        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint. If this endpoint is only used with public
        repositories, the token can use the `public_repo` scope instead.

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
            f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependabotAlert,
        )

    def update(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        state: Literal["dismissed", "open"],
        dismissed_comment: str | NotGiven = NOT_GIVEN,
        dismissed_reason: Literal["fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependabotAlert:
        """
        The authenticated user must have access to security alerts for the repository to
        use this endpoint. For more information, see
        "[Granting access to security alerts](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts)."

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint. If this endpoint is only used with public
        repositories, the token can use the `public_repo` scope instead.

        Args:
          alert_number: The security alert number.

          state: The state of the Dependabot alert. A `dismissed_reason` must be provided when
              setting the state to `dismissed`.

          dismissed_comment: An optional comment associated with dismissing the alert.

          dismissed_reason: **Required when `state` is `dismissed`.** A reason for dismissing the alert.

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
            f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}",
            body=maybe_transform(
                {
                    "state": state,
                    "dismissed_comment": dismissed_comment,
                    "dismissed_reason": dismissed_reason,
                },
                alert_update_params.AlertUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependabotAlert,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        ecosystem: str | NotGiven = NOT_GIVEN,
        epss_percentage: str | NotGiven = NOT_GIVEN,
        first: int | NotGiven = NOT_GIVEN,
        last: int | NotGiven = NOT_GIVEN,
        manifest: str | NotGiven = NOT_GIVEN,
        package: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        scope: Literal["development", "runtime"] | NotGiven = NOT_GIVEN,
        severity: str | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "epss_percentage"] | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertListResponse:
        """
        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint. If this endpoint is only used with public
        repositories, the token can use the `public_repo` scope instead.

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

          ecosystem: A comma-separated list of ecosystems. If specified, only alerts for these
              ecosystems will be returned.

              Can be: `composer`, `go`, `maven`, `npm`, `nuget`, `pip`, `pub`, `rubygems`,
              `rust`

          epss_percentage:
              CVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:

              - An exact number (`n`)
              - Comparators such as `>n`, `<n`, `>=n`, `<=n`
              - A range like `n..n`, where `n` is a number from 0.0 to 1.0

              Filters the list of alerts based on EPSS percentages. If specified, only alerts
              with the provided EPSS percentages will be returned.

          first: **Deprecated**. The number of results per page (max 100), starting from the
              first matching result. This parameter must not be used in combination with
              `last`. Instead, use `per_page` in combination with `after` to fetch the first
              page of results.

          last: **Deprecated**. The number of results per page (max 100), starting from the last
              matching result. This parameter must not be used in combination with `first`.
              Instead, use `per_page` in combination with `before` to fetch the last page of
              results.

          manifest: A comma-separated list of full manifest paths. If specified, only alerts for
              these manifests will be returned.

          package: A comma-separated list of package names. If specified, only alerts for these
              packages will be returned.

          page: **Closing down notice**. Page number of the results to fetch. Use cursor-based
              pagination with `before` or `after` instead.

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          scope: The scope of the vulnerable dependency. If specified, only alerts with this
              scope will be returned.

          severity: A comma-separated list of severities. If specified, only alerts with these
              severities will be returned.

              Can be: `low`, `medium`, `high`, `critical`

          sort: The property by which to sort the results. `created` means when the alert was
              created. `updated` means when the alert's state last changed. `epss_percentage`
              sorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.

          state: A comma-separated list of states. If specified, only alerts with these states
              will be returned.

              Can be: `auto_dismissed`, `dismissed`, `fixed`, `open`

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
            f"/repos/{owner}/{repo}/dependabot/alerts",
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
                        "ecosystem": ecosystem,
                        "epss_percentage": epss_percentage,
                        "first": first,
                        "last": last,
                        "manifest": manifest,
                        "package": package,
                        "page": page,
                        "per_page": per_page,
                        "scope": scope,
                        "severity": severity,
                        "sort": sort,
                        "state": state,
                    },
                    alert_list_params.AlertListParams,
                ),
            ),
            cast_to=AlertListResponse,
        )


class AsyncAlertsResource(AsyncAPIResource):
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
    ) -> DependabotAlert:
        """
        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint. If this endpoint is only used with public
        repositories, the token can use the `public_repo` scope instead.

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
            f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependabotAlert,
        )

    async def update(
        self,
        alert_number: int,
        *,
        owner: str,
        repo: str,
        state: Literal["dismissed", "open"],
        dismissed_comment: str | NotGiven = NOT_GIVEN,
        dismissed_reason: Literal["fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependabotAlert:
        """
        The authenticated user must have access to security alerts for the repository to
        use this endpoint. For more information, see
        "[Granting access to security alerts](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts)."

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint. If this endpoint is only used with public
        repositories, the token can use the `public_repo` scope instead.

        Args:
          alert_number: The security alert number.

          state: The state of the Dependabot alert. A `dismissed_reason` must be provided when
              setting the state to `dismissed`.

          dismissed_comment: An optional comment associated with dismissing the alert.

          dismissed_reason: **Required when `state` is `dismissed`.** A reason for dismissing the alert.

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
            f"/repos/{owner}/{repo}/dependabot/alerts/{alert_number}",
            body=await async_maybe_transform(
                {
                    "state": state,
                    "dismissed_comment": dismissed_comment,
                    "dismissed_reason": dismissed_reason,
                },
                alert_update_params.AlertUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependabotAlert,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        ecosystem: str | NotGiven = NOT_GIVEN,
        epss_percentage: str | NotGiven = NOT_GIVEN,
        first: int | NotGiven = NOT_GIVEN,
        last: int | NotGiven = NOT_GIVEN,
        manifest: str | NotGiven = NOT_GIVEN,
        package: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        scope: Literal["development", "runtime"] | NotGiven = NOT_GIVEN,
        severity: str | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "epss_percentage"] | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertListResponse:
        """
        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint. If this endpoint is only used with public
        repositories, the token can use the `public_repo` scope instead.

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

          ecosystem: A comma-separated list of ecosystems. If specified, only alerts for these
              ecosystems will be returned.

              Can be: `composer`, `go`, `maven`, `npm`, `nuget`, `pip`, `pub`, `rubygems`,
              `rust`

          epss_percentage:
              CVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:

              - An exact number (`n`)
              - Comparators such as `>n`, `<n`, `>=n`, `<=n`
              - A range like `n..n`, where `n` is a number from 0.0 to 1.0

              Filters the list of alerts based on EPSS percentages. If specified, only alerts
              with the provided EPSS percentages will be returned.

          first: **Deprecated**. The number of results per page (max 100), starting from the
              first matching result. This parameter must not be used in combination with
              `last`. Instead, use `per_page` in combination with `after` to fetch the first
              page of results.

          last: **Deprecated**. The number of results per page (max 100), starting from the last
              matching result. This parameter must not be used in combination with `first`.
              Instead, use `per_page` in combination with `before` to fetch the last page of
              results.

          manifest: A comma-separated list of full manifest paths. If specified, only alerts for
              these manifests will be returned.

          package: A comma-separated list of package names. If specified, only alerts for these
              packages will be returned.

          page: **Closing down notice**. Page number of the results to fetch. Use cursor-based
              pagination with `before` or `after` instead.

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          scope: The scope of the vulnerable dependency. If specified, only alerts with this
              scope will be returned.

          severity: A comma-separated list of severities. If specified, only alerts with these
              severities will be returned.

              Can be: `low`, `medium`, `high`, `critical`

          sort: The property by which to sort the results. `created` means when the alert was
              created. `updated` means when the alert's state last changed. `epss_percentage`
              sorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.

          state: A comma-separated list of states. If specified, only alerts with these states
              will be returned.

              Can be: `auto_dismissed`, `dismissed`, `fixed`, `open`

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
            f"/repos/{owner}/{repo}/dependabot/alerts",
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
                        "ecosystem": ecosystem,
                        "epss_percentage": epss_percentage,
                        "first": first,
                        "last": last,
                        "manifest": manifest,
                        "package": package,
                        "page": page,
                        "per_page": per_page,
                        "scope": scope,
                        "severity": severity,
                        "sort": sort,
                        "state": state,
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
