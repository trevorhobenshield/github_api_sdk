from __future__ import annotations

from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from .customization.customization import (
    AsyncCustomizationResource,
    AsyncCustomizationResourceWithRawResponse,
    AsyncCustomizationResourceWithStreamingResponse,
    CustomizationResource,
    CustomizationResourceWithRawResponse,
    CustomizationResourceWithStreamingResponse,
)

__all__ = ["OidcResource", "AsyncOidcResource"]


class OidcResource(SyncAPIResource):
    @cached_property
    def customization(self) -> CustomizationResource:
        return CustomizationResource(self._client)

    @cached_property
    def with_raw_response(self) -> OidcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return OidcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OidcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return OidcResourceWithStreamingResponse(self)


class AsyncOidcResource(AsyncAPIResource):
    @cached_property
    def customization(self) -> AsyncCustomizationResource:
        return AsyncCustomizationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOidcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOidcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOidcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncOidcResourceWithStreamingResponse(self)


class OidcResourceWithRawResponse:
    def __init__(self, oidc: OidcResource) -> None:
        self._oidc = oidc

    @cached_property
    def customization(self) -> CustomizationResourceWithRawResponse:
        return CustomizationResourceWithRawResponse(self._oidc.customization)


class AsyncOidcResourceWithRawResponse:
    def __init__(self, oidc: AsyncOidcResource) -> None:
        self._oidc = oidc

    @cached_property
    def customization(self) -> AsyncCustomizationResourceWithRawResponse:
        return AsyncCustomizationResourceWithRawResponse(self._oidc.customization)


class OidcResourceWithStreamingResponse:
    def __init__(self, oidc: OidcResource) -> None:
        self._oidc = oidc

    @cached_property
    def customization(self) -> CustomizationResourceWithStreamingResponse:
        return CustomizationResourceWithStreamingResponse(self._oidc.customization)


class AsyncOidcResourceWithStreamingResponse:
    def __init__(self, oidc: AsyncOidcResource) -> None:
        self._oidc = oidc

    @cached_property
    def customization(self) -> AsyncCustomizationResourceWithStreamingResponse:
        return AsyncCustomizationResourceWithStreamingResponse(self._oidc.customization)
