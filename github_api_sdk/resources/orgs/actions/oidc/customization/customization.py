from __future__ import annotations

from ......_compat import cached_property
from ......_resource import AsyncAPIResource, SyncAPIResource
from .sub import (
    AsyncSubResource,
    AsyncSubResourceWithRawResponse,
    AsyncSubResourceWithStreamingResponse,
    SubResource,
    SubResourceWithRawResponse,
    SubResourceWithStreamingResponse,
)

__all__ = ["CustomizationResource", "AsyncCustomizationResource"]


class CustomizationResource(SyncAPIResource):
    @cached_property
    def sub(self) -> SubResource:
        return SubResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CustomizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CustomizationResourceWithStreamingResponse(self)


class AsyncCustomizationResource(AsyncAPIResource):
    @cached_property
    def sub(self) -> AsyncSubResource:
        return AsyncSubResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCustomizationResourceWithStreamingResponse(self)


class CustomizationResourceWithRawResponse:
    def __init__(self, customization: CustomizationResource) -> None:
        self._customization = customization

    @cached_property
    def sub(self) -> SubResourceWithRawResponse:
        return SubResourceWithRawResponse(self._customization.sub)


class AsyncCustomizationResourceWithRawResponse:
    def __init__(self, customization: AsyncCustomizationResource) -> None:
        self._customization = customization

    @cached_property
    def sub(self) -> AsyncSubResourceWithRawResponse:
        return AsyncSubResourceWithRawResponse(self._customization.sub)


class CustomizationResourceWithStreamingResponse:
    def __init__(self, customization: CustomizationResource) -> None:
        self._customization = customization

    @cached_property
    def sub(self) -> SubResourceWithStreamingResponse:
        return SubResourceWithStreamingResponse(self._customization.sub)


class AsyncCustomizationResourceWithStreamingResponse:
    def __init__(self, customization: AsyncCustomizationResource) -> None:
        self._customization = customization

    @cached_property
    def sub(self) -> AsyncSubResourceWithStreamingResponse:
        return AsyncSubResourceWithStreamingResponse(self._customization.sub)
