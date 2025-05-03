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
from ....types.organizations.settings import billing_get_usage_report_params
from ....types.organizations.settings.billing_get_usage_report_response import BillingGetUsageReportResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def get_usage_report(
        self,
        org: str,
        *,
        day: int | NotGiven = NOT_GIVEN,
        hour: int | NotGiven = NOT_GIVEN,
        month: int | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingGetUsageReportResponse:
        """Gets a report of the total usage for an organization.

        To use this endpoint, you
        must be an administrator of an organization within an enterprise or an
        organization account.

        **Note:** This endpoint is only available to organizations with access to the
        enhanced billing platform. For more information, see
        "[About the enhanced billing platform](https://docs.github.com/billing/using-the-new-billing-platform)."

        Args:
          day: If specified, only return results for a single day. The value of `day` is an
              integer between `1` and `31`. If no `year` or `month` is specified, the default
              `year` and `month` are used.

          hour: If specified, only return results for a single hour. The value of `hour` is an
              integer between `0` and `23`. If no `year`, `month`, or `day` is specified, the
              default `year`, `month`, and `day` are used.

          month: If specified, only return results for a single month. The value of `month` is an
              integer between `1` and `12`. If no year is specified the default `year` is
              used.

          year: If specified, only return results for a single year. The value of `year` is an
              integer with four digits representing a year. For example, `2025`. Default value
              is the current year.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/organizations/{org}/settings/billing/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "day": day,
                        "hour": hour,
                        "month": month,
                        "year": year,
                    },
                    billing_get_usage_report_params.BillingGetUsageReportParams,
                ),
            ),
            cast_to=BillingGetUsageReportResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def get_usage_report(
        self,
        org: str,
        *,
        day: int | NotGiven = NOT_GIVEN,
        hour: int | NotGiven = NOT_GIVEN,
        month: int | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingGetUsageReportResponse:
        """Gets a report of the total usage for an organization.

        To use this endpoint, you
        must be an administrator of an organization within an enterprise or an
        organization account.

        **Note:** This endpoint is only available to organizations with access to the
        enhanced billing platform. For more information, see
        "[About the enhanced billing platform](https://docs.github.com/billing/using-the-new-billing-platform)."

        Args:
          day: If specified, only return results for a single day. The value of `day` is an
              integer between `1` and `31`. If no `year` or `month` is specified, the default
              `year` and `month` are used.

          hour: If specified, only return results for a single hour. The value of `hour` is an
              integer between `0` and `23`. If no `year`, `month`, or `day` is specified, the
              default `year`, `month`, and `day` are used.

          month: If specified, only return results for a single month. The value of `month` is an
              integer between `1` and `12`. If no year is specified the default `year` is
              used.

          year: If specified, only return results for a single year. The value of `year` is an
              integer with four digits representing a year. For example, `2025`. Default value
              is the current year.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/organizations/{org}/settings/billing/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "day": day,
                        "hour": hour,
                        "month": month,
                        "year": year,
                    },
                    billing_get_usage_report_params.BillingGetUsageReportParams,
                ),
            ),
            cast_to=BillingGetUsageReportResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_usage_report = to_raw_response_wrapper(
            billing.get_usage_report,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_usage_report = async_to_raw_response_wrapper(
            billing.get_usage_report,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_usage_report = to_streamed_response_wrapper(
            billing.get_usage_report,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_usage_report = async_to_streamed_response_wrapper(
            billing.get_usage_report,
        )
