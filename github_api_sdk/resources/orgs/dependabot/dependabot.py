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
from ....types.orgs import dependabot_list_alerts_params
from ....types.orgs.dependabot_list_alerts_response import DependabotListAlertsResponse
from .secrets.secrets import (
    AsyncSecretsResource,
    AsyncSecretsResourceWithRawResponse,
    AsyncSecretsResourceWithStreamingResponse,
    SecretsResource,
    SecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
)

__all__ = ["DependabotResource", "AsyncDependabotResource"]


class DependabotResource(SyncAPIResource):
    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DependabotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DependabotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DependabotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DependabotResourceWithStreamingResponse(self)

    def list_alerts(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        ecosystem: str | NotGiven = NOT_GIVEN,
        epss_percentage: str | NotGiven = NOT_GIVEN,
        first: int | NotGiven = NOT_GIVEN,
        last: int | NotGiven = NOT_GIVEN,
        package: str | NotGiven = NOT_GIVEN,
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
    ) -> DependabotListAlertsResponse:
        """
        Lists Dependabot alerts for an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

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

          package: A comma-separated list of package names. If specified, only alerts for these
              packages will be returned.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/dependabot/alerts",
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
                        "package": package,
                        "per_page": per_page,
                        "scope": scope,
                        "severity": severity,
                        "sort": sort,
                        "state": state,
                    },
                    dependabot_list_alerts_params.DependabotListAlertsParams,
                ),
            ),
            cast_to=DependabotListAlertsResponse,
        )


class AsyncDependabotResource(AsyncAPIResource):
    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDependabotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDependabotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDependabotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDependabotResourceWithStreamingResponse(self)

    async def list_alerts(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        ecosystem: str | NotGiven = NOT_GIVEN,
        epss_percentage: str | NotGiven = NOT_GIVEN,
        first: int | NotGiven = NOT_GIVEN,
        last: int | NotGiven = NOT_GIVEN,
        package: str | NotGiven = NOT_GIVEN,
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
    ) -> DependabotListAlertsResponse:
        """
        Lists Dependabot alerts for an organization.

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

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

          package: A comma-separated list of package names. If specified, only alerts for these
              packages will be returned.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/dependabot/alerts",
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
                        "package": package,
                        "per_page": per_page,
                        "scope": scope,
                        "severity": severity,
                        "sort": sort,
                        "state": state,
                    },
                    dependabot_list_alerts_params.DependabotListAlertsParams,
                ),
            ),
            cast_to=DependabotListAlertsResponse,
        )


class DependabotResourceWithRawResponse:
    def __init__(self, dependabot: DependabotResource) -> None:
        self._dependabot = dependabot

        self.list_alerts = to_raw_response_wrapper(
            dependabot.list_alerts,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._dependabot.secrets)


class AsyncDependabotResourceWithRawResponse:
    def __init__(self, dependabot: AsyncDependabotResource) -> None:
        self._dependabot = dependabot

        self.list_alerts = async_to_raw_response_wrapper(
            dependabot.list_alerts,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._dependabot.secrets)


class DependabotResourceWithStreamingResponse:
    def __init__(self, dependabot: DependabotResource) -> None:
        self._dependabot = dependabot

        self.list_alerts = to_streamed_response_wrapper(
            dependabot.list_alerts,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._dependabot.secrets)


class AsyncDependabotResourceWithStreamingResponse:
    def __init__(self, dependabot: AsyncDependabotResource) -> None:
        self._dependabot = dependabot

        self.list_alerts = async_to_streamed_response_wrapper(
            dependabot.list_alerts,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._dependabot.secrets)
