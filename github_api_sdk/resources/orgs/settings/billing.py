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
from ....types.orgs.settings.actions_billing_usage import ActionsBillingUsage
from ....types.orgs.settings.combined_billing_usage import CombinedBillingUsage
from ....types.orgs.settings.packages_billing_usage import PackagesBillingUsage

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

    def get_actions(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsBillingUsage:
        """
        Gets the summary of the free and paid GitHub Actions minutes used.

        Paid minutes only apply to workflows in private repositories that use
        GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner
        operating system. Any job re-runs are also included in the usage. The usage
        returned includes any minute multipliers for macOS and Windows runners, and is
        rounded up to the nearest whole minute. For more information, see
        "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `admin:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/settings/billing/actions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionsBillingUsage,
        )

    def get_packages(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackagesBillingUsage:
        """
        Gets the free and paid storage used for GitHub Packages in gigabytes.

        Paid minutes only apply to packages stored for private repositories. For more
        information, see
        "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `admin:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/settings/billing/packages",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PackagesBillingUsage,
        )

    def get_shared_storage(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CombinedBillingUsage:
        """
        Gets the estimated paid and estimated total storage used for GitHub Actions and
        GitHub Packages.

        Paid minutes only apply to packages stored for private repositories. For more
        information, see
        "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `admin:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/settings/billing/shared-storage",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CombinedBillingUsage,
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

    async def get_actions(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsBillingUsage:
        """
        Gets the summary of the free and paid GitHub Actions minutes used.

        Paid minutes only apply to workflows in private repositories that use
        GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner
        operating system. Any job re-runs are also included in the usage. The usage
        returned includes any minute multipliers for macOS and Windows runners, and is
        rounded up to the nearest whole minute. For more information, see
        "[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `admin:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/settings/billing/actions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionsBillingUsage,
        )

    async def get_packages(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackagesBillingUsage:
        """
        Gets the free and paid storage used for GitHub Packages in gigabytes.

        Paid minutes only apply to packages stored for private repositories. For more
        information, see
        "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `admin:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/settings/billing/packages",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PackagesBillingUsage,
        )

    async def get_shared_storage(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CombinedBillingUsage:
        """
        Gets the estimated paid and estimated total storage used for GitHub Actions and
        GitHub Packages.

        Paid minutes only apply to packages stored for private repositories. For more
        information, see
        "[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `admin:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/settings/billing/shared-storage",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CombinedBillingUsage,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_actions = to_raw_response_wrapper(
            billing.get_actions,
        )
        self.get_packages = to_raw_response_wrapper(
            billing.get_packages,
        )
        self.get_shared_storage = to_raw_response_wrapper(
            billing.get_shared_storage,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_actions = async_to_raw_response_wrapper(
            billing.get_actions,
        )
        self.get_packages = async_to_raw_response_wrapper(
            billing.get_packages,
        )
        self.get_shared_storage = async_to_raw_response_wrapper(
            billing.get_shared_storage,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_actions = to_streamed_response_wrapper(
            billing.get_actions,
        )
        self.get_packages = to_streamed_response_wrapper(
            billing.get_packages,
        )
        self.get_shared_storage = to_streamed_response_wrapper(
            billing.get_shared_storage,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_actions = async_to_streamed_response_wrapper(
            billing.get_actions,
        )
        self.get_packages = async_to_streamed_response_wrapper(
            billing.get_packages,
        )
        self.get_shared_storage = async_to_streamed_response_wrapper(
            billing.get_shared_storage,
        )
