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
from ....types.repos import PushProtectionBypassReason, secret_scanning_create_push_protection_bypass_params
from ....types.repos.push_protection_bypass_reason import PushProtectionBypassReason
from ....types.repos.secret_scanning_create_push_protection_bypass_response import (
    SecretScanningCreatePushProtectionBypassResponse,
)
from ....types.repos.secret_scanning_get_scan_history_response import SecretScanningGetScanHistoryResponse
from .alerts import (
    AlertsResource,
    AlertsResourceWithRawResponse,
    AlertsResourceWithStreamingResponse,
    AsyncAlertsResource,
    AsyncAlertsResourceWithRawResponse,
    AsyncAlertsResourceWithStreamingResponse,
)

__all__ = ["SecretScanningResource", "AsyncSecretScanningResource"]


class SecretScanningResource(SyncAPIResource):
    @cached_property
    def alerts(self) -> AlertsResource:
        return AlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecretScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SecretScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SecretScanningResourceWithStreamingResponse(self)

    def create_push_protection_bypass(
        self,
        repo: str,
        *,
        owner: str,
        placeholder_id: str,
        reason: PushProtectionBypassReason,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretScanningCreatePushProtectionBypassResponse:
        """
        Creates a bypass for a previously push protected secret.

        The authenticated user must be the original author of the committed secret.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          placeholder_id: The ID of the push protection bypass placeholder. This value is returned on any
              push protected routes.

          reason: The reason for bypassing push protection.

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
            f"/repos/{owner}/{repo}/secret-scanning/push-protection-bypasses",
            body=maybe_transform(
                {
                    "placeholder_id": placeholder_id,
                    "reason": reason,
                },
                secret_scanning_create_push_protection_bypass_params.SecretScanningCreatePushProtectionBypassParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SecretScanningCreatePushProtectionBypassResponse,
        )

    def get_scan_history(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretScanningGetScanHistoryResponse:
        """Lists the latest default incremental and backfill scans by type for a
        repository.

        Scans from Copilot Secret Scanning are not included.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `security_events` scope to use this endpoint. If this endpoint is only used with
        public repositories, the token can use the `public_repo` scope instead.

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
            f"/repos/{owner}/{repo}/secret-scanning/scan-history",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SecretScanningGetScanHistoryResponse,
        )


class AsyncSecretScanningResource(AsyncAPIResource):
    @cached_property
    def alerts(self) -> AsyncAlertsResource:
        return AsyncAlertsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecretScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSecretScanningResourceWithStreamingResponse(self)

    async def create_push_protection_bypass(
        self,
        repo: str,
        *,
        owner: str,
        placeholder_id: str,
        reason: PushProtectionBypassReason,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretScanningCreatePushProtectionBypassResponse:
        """
        Creates a bypass for a previously push protected secret.

        The authenticated user must be the original author of the committed secret.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          placeholder_id: The ID of the push protection bypass placeholder. This value is returned on any
              push protected routes.

          reason: The reason for bypassing push protection.

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
            f"/repos/{owner}/{repo}/secret-scanning/push-protection-bypasses",
            body=await async_maybe_transform(
                {
                    "placeholder_id": placeholder_id,
                    "reason": reason,
                },
                secret_scanning_create_push_protection_bypass_params.SecretScanningCreatePushProtectionBypassParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SecretScanningCreatePushProtectionBypassResponse,
        )

    async def get_scan_history(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretScanningGetScanHistoryResponse:
        """Lists the latest default incremental and backfill scans by type for a
        repository.

        Scans from Copilot Secret Scanning are not included.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `security_events` scope to use this endpoint. If this endpoint is only used with
        public repositories, the token can use the `public_repo` scope instead.

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
            f"/repos/{owner}/{repo}/secret-scanning/scan-history",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SecretScanningGetScanHistoryResponse,
        )


class SecretScanningResourceWithRawResponse:
    def __init__(self, secret_scanning: SecretScanningResource) -> None:
        self._secret_scanning = secret_scanning

        self.create_push_protection_bypass = to_raw_response_wrapper(
            secret_scanning.create_push_protection_bypass,
        )
        self.get_scan_history = to_raw_response_wrapper(
            secret_scanning.get_scan_history,
        )

    @cached_property
    def alerts(self) -> AlertsResourceWithRawResponse:
        return AlertsResourceWithRawResponse(self._secret_scanning.alerts)


class AsyncSecretScanningResourceWithRawResponse:
    def __init__(self, secret_scanning: AsyncSecretScanningResource) -> None:
        self._secret_scanning = secret_scanning

        self.create_push_protection_bypass = async_to_raw_response_wrapper(
            secret_scanning.create_push_protection_bypass,
        )
        self.get_scan_history = async_to_raw_response_wrapper(
            secret_scanning.get_scan_history,
        )

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithRawResponse:
        return AsyncAlertsResourceWithRawResponse(self._secret_scanning.alerts)


class SecretScanningResourceWithStreamingResponse:
    def __init__(self, secret_scanning: SecretScanningResource) -> None:
        self._secret_scanning = secret_scanning

        self.create_push_protection_bypass = to_streamed_response_wrapper(
            secret_scanning.create_push_protection_bypass,
        )
        self.get_scan_history = to_streamed_response_wrapper(
            secret_scanning.get_scan_history,
        )

    @cached_property
    def alerts(self) -> AlertsResourceWithStreamingResponse:
        return AlertsResourceWithStreamingResponse(self._secret_scanning.alerts)


class AsyncSecretScanningResourceWithStreamingResponse:
    def __init__(self, secret_scanning: AsyncSecretScanningResource) -> None:
        self._secret_scanning = secret_scanning

        self.create_push_protection_bypass = async_to_streamed_response_wrapper(
            secret_scanning.create_push_protection_bypass,
        )
        self.get_scan_history = async_to_streamed_response_wrapper(
            secret_scanning.get_scan_history,
        )

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithStreamingResponse:
        return AsyncAlertsResourceWithStreamingResponse(self._secret_scanning.alerts)
