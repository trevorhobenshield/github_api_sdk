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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.orgs.teams import copilot_get_metrics_params
from ....types.orgs.teams.copilot_get_metrics_response import CopilotGetMetricsResponse

__all__ = ["CopilotResource", "AsyncCopilotResource"]


class CopilotResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CopilotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CopilotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CopilotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CopilotResourceWithStreamingResponse(self)

    def get_metrics(
        self,
        team_slug: str,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | NotGiven = NOT_GIVEN,
        until: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CopilotGetMetricsResponse:
        """
        Use this endpoint to see a breakdown of aggregated metrics for various GitHub
        Copilot features. See the response schema tab for detailed metrics definitions.

        > [!NOTE] This endpoint will only return results for a given day if the team had
        > **five or more members with active Copilot licenses** on that day, as
        > evaluated at the end of that day.

        The response contains metrics for up to 28 days prior. Metrics are processed
        once per day for the previous day, and the response will only include data up
        until yesterday. In order for an end user to be counted towards these metrics,
        they must have telemetry enabled in their IDE.

        To access this endpoint, the Copilot Metrics API access policy must be enabled
        for the organization containing the team within GitHub settings. Only
        organization owners for the organization that contains this team and owners and
        billing managers of the parent enterprise can view Copilot metrics for a team.

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot`, `read:org`, or `read:enterprise` scopes to use this
        endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of days of metrics to display per page (max 28). For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Show usage metrics since this date. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
              (`YYYY-MM-DDTHH:MM:SSZ`). Maximum value is 28 days ago.

          until: Show usage metrics until this date. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
              (`YYYY-MM-DDTHH:MM:SSZ`) and should not preceed the `since` date if it is
              passed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._get(
            f"/orgs/{org}/team/{team_slug}/copilot/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "until": until,
                    },
                    copilot_get_metrics_params.CopilotGetMetricsParams,
                ),
            ),
            cast_to=CopilotGetMetricsResponse,
        )


class AsyncCopilotResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCopilotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCopilotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCopilotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCopilotResourceWithStreamingResponse(self)

    async def get_metrics(
        self,
        team_slug: str,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | NotGiven = NOT_GIVEN,
        until: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CopilotGetMetricsResponse:
        """
        Use this endpoint to see a breakdown of aggregated metrics for various GitHub
        Copilot features. See the response schema tab for detailed metrics definitions.

        > [!NOTE] This endpoint will only return results for a given day if the team had
        > **five or more members with active Copilot licenses** on that day, as
        > evaluated at the end of that day.

        The response contains metrics for up to 28 days prior. Metrics are processed
        once per day for the previous day, and the response will only include data up
        until yesterday. In order for an end user to be counted towards these metrics,
        they must have telemetry enabled in their IDE.

        To access this endpoint, the Copilot Metrics API access policy must be enabled
        for the organization containing the team within GitHub settings. Only
        organization owners for the organization that contains this team and owners and
        billing managers of the parent enterprise can view Copilot metrics for a team.

        OAuth app tokens and personal access tokens (classic) need either the
        `manage_billing:copilot`, `read:org`, or `read:enterprise` scopes to use this
        endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of days of metrics to display per page (max 28). For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Show usage metrics since this date. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
              (`YYYY-MM-DDTHH:MM:SSZ`). Maximum value is 28 days ago.

          until: Show usage metrics until this date. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
              (`YYYY-MM-DDTHH:MM:SSZ`) and should not preceed the `since` date if it is
              passed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._get(
            f"/orgs/{org}/team/{team_slug}/copilot/metrics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "until": until,
                    },
                    copilot_get_metrics_params.CopilotGetMetricsParams,
                ),
            ),
            cast_to=CopilotGetMetricsResponse,
        )


class CopilotResourceWithRawResponse:
    def __init__(self, copilot: CopilotResource) -> None:
        self._copilot = copilot

        self.get_metrics = to_raw_response_wrapper(
            copilot.get_metrics,
        )


class AsyncCopilotResourceWithRawResponse:
    def __init__(self, copilot: AsyncCopilotResource) -> None:
        self._copilot = copilot

        self.get_metrics = async_to_raw_response_wrapper(
            copilot.get_metrics,
        )


class CopilotResourceWithStreamingResponse:
    def __init__(self, copilot: CopilotResource) -> None:
        self._copilot = copilot

        self.get_metrics = to_streamed_response_wrapper(
            copilot.get_metrics,
        )


class AsyncCopilotResourceWithStreamingResponse:
    def __init__(self, copilot: AsyncCopilotResource) -> None:
        self._copilot = copilot

        self.get_metrics = async_to_streamed_response_wrapper(
            copilot.get_metrics,
        )
