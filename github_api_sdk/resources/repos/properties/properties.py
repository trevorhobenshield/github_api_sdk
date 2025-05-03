from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .values import (
    AsyncValuesResource,
    AsyncValuesResourceWithRawResponse,
    AsyncValuesResourceWithStreamingResponse,
    ValuesResource,
    ValuesResourceWithRawResponse,
    ValuesResourceWithStreamingResponse,
)

__all__ = ["PropertiesResource", "AsyncPropertiesResource"]


class PropertiesResource(SyncAPIResource):
    @cached_property
    def values(self) -> ValuesResource:
        return ValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PropertiesResourceWithStreamingResponse(self)


class AsyncPropertiesResource(AsyncAPIResource):
    @cached_property
    def values(self) -> AsyncValuesResource:
        return AsyncValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPropertiesResourceWithStreamingResponse(self)


class PropertiesResourceWithRawResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

    @cached_property
    def values(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self._properties.values)


class AsyncPropertiesResourceWithRawResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

    @cached_property
    def values(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self._properties.values)


class PropertiesResourceWithStreamingResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

    @cached_property
    def values(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self._properties.values)


class AsyncPropertiesResourceWithStreamingResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

    @cached_property
    def values(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self._properties.values)
