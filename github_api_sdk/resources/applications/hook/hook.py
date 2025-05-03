from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .config import (
    AsyncConfigResource,
    AsyncConfigResourceWithRawResponse,
    AsyncConfigResourceWithStreamingResponse,
    ConfigResource,
    ConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
)
from .deliveries import (
    AsyncDeliveriesResource,
    AsyncDeliveriesResourceWithRawResponse,
    AsyncDeliveriesResourceWithStreamingResponse,
    DeliveriesResource,
    DeliveriesResourceWithRawResponse,
    DeliveriesResourceWithStreamingResponse,
)

__all__ = ["HookResource", "AsyncHookResource"]


class HookResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def deliveries(self) -> DeliveriesResource:
        return DeliveriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> HookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return HookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return HookResourceWithStreamingResponse(self)


class AsyncHookResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResource:
        return AsyncDeliveriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHookResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHookResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHookResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncHookResourceWithStreamingResponse(self)


class HookResourceWithRawResponse:
    def __init__(self, hook: HookResource) -> None:
        self._hook = hook

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._hook.config)

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithRawResponse:
        return DeliveriesResourceWithRawResponse(self._hook.deliveries)


class AsyncHookResourceWithRawResponse:
    def __init__(self, hook: AsyncHookResource) -> None:
        self._hook = hook

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._hook.config)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithRawResponse:
        return AsyncDeliveriesResourceWithRawResponse(self._hook.deliveries)


class HookResourceWithStreamingResponse:
    def __init__(self, hook: HookResource) -> None:
        self._hook = hook

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._hook.config)

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithStreamingResponse:
        return DeliveriesResourceWithStreamingResponse(self._hook.deliveries)


class AsyncHookResourceWithStreamingResponse:
    def __init__(self, hook: AsyncHookResource) -> None:
        self._hook = hook

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._hook.config)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        return AsyncDeliveriesResourceWithStreamingResponse(self._hook.deliveries)
