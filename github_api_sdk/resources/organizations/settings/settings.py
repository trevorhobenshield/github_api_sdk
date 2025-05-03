from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .billing import (
    AsyncBillingResource,
    AsyncBillingResourceWithRawResponse,
    AsyncBillingResourceWithStreamingResponse,
    BillingResource,
    BillingResourceWithRawResponse,
    BillingResourceWithStreamingResponse,
)

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def billing(self) -> BillingResource:
        return BillingResource(self._client)

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


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def billing(self) -> AsyncBillingResource:
        return AsyncBillingResource(self._client)

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


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def billing(self) -> BillingResourceWithRawResponse:
        return BillingResourceWithRawResponse(self._settings.billing)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def billing(self) -> AsyncBillingResourceWithRawResponse:
        return AsyncBillingResourceWithRawResponse(self._settings.billing)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def billing(self) -> BillingResourceWithStreamingResponse:
        return BillingResourceWithStreamingResponse(self._settings.billing)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def billing(self) -> AsyncBillingResourceWithStreamingResponse:
        return AsyncBillingResourceWithStreamingResponse(self._settings.billing)
