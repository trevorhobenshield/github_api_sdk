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
from ....types.orgs.setting_get_network_settings_response import SettingGetNetworkSettingsResponse
from .billing import (
    AsyncBillingResource,
    AsyncBillingResourceWithRawResponse,
    AsyncBillingResourceWithStreamingResponse,
    BillingResource,
    BillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
)
from .network_configurations import (
    AsyncNetworkConfigurationsResource,
    AsyncNetworkConfigurationsResourceWithRawResponse,
    AsyncNetworkConfigurationsResourceWithStreamingResponse,
    NetworkConfigurationsResource,
    NetworkConfigurationsResourceWithRawResponse,
    NetworkConfigurationsResourceWithStreamingResponse,
)

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

    @cached_property
    def network_configurations(self) -> NetworkConfigurationsResource:
        return NetworkConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def get_network_settings(
        self,
        network_settings_id: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingGetNetworkSettingsResponse:
        """
        Gets a hosted compute network settings resource configured for an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `read:network_configurations` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not network_settings_id:
            raise ValueError(f"Expected a non-empty value for `network_settings_id` but received {network_settings_id!r}")
        return self._get(
            f"/orgs/{org}/settings/network-settings/{network_settings_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SettingGetNetworkSettingsResponse,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

    @cached_property
    def network_configurations(self) -> AsyncNetworkConfigurationsResource:
        return AsyncNetworkConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def get_network_settings(
        self,
        network_settings_id: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettingGetNetworkSettingsResponse:
        """
        Gets a hosted compute network settings resource configured for an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `read:network_configurations` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not network_settings_id:
            raise ValueError(f"Expected a non-empty value for `network_settings_id` but received {network_settings_id!r}")
        return await self._get(
            f"/orgs/{org}/settings/network-settings/{network_settings_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SettingGetNetworkSettingsResponse,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.get_network_settings = to_raw_response_wrapper(
            settings.get_network_settings,
        )

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._settings.billing)

    @cached_property
    def network_configurations(self) -> NetworkConfigurationsResourceWithRawResponse:
        return NetworkConfigurationsResourceWithRawResponse(self._settings.network_configurations)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.get_network_settings = async_to_raw_response_wrapper(
            settings.get_network_settings,
        )

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._settings.billing)

    @cached_property
    def network_configurations(self) -> AsyncNetworkConfigurationsResourceWithRawResponse:
        return AsyncNetworkConfigurationsResourceWithRawResponse(self._settings.network_configurations)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.get_network_settings = to_streamed_response_wrapper(
            settings.get_network_settings,
        )

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._settings.billing)

    @cached_property
    def network_configurations(self) -> NetworkConfigurationsResourceWithStreamingResponse:
        return NetworkConfigurationsResourceWithStreamingResponse(self._settings.network_configurations)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.get_network_settings = async_to_streamed_response_wrapper(
            settings.get_network_settings,
        )

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._settings.billing)

    @cached_property
    def network_configurations(self) -> AsyncNetworkConfigurationsResourceWithStreamingResponse:
        return AsyncNetworkConfigurationsResourceWithStreamingResponse(self._settings.network_configurations)
