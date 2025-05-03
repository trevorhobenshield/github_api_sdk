from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .configurations.configurations import (
    AsyncConfigurationsResource,
    AsyncConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
    ConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
)

__all__ = ["CodeSecurityResource", "AsyncCodeSecurityResource"]


class CodeSecurityResource(SyncAPIResource):
    @cached_property
    def configurations(self) -> ConfigurationsResource:
        return ConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CodeSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodeSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodeSecurityResourceWithStreamingResponse(self)


class AsyncCodeSecurityResource(AsyncAPIResource):
    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        return AsyncConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCodeSecurityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodeSecurityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeSecurityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodeSecurityResourceWithStreamingResponse(self)


class CodeSecurityResourceWithRawResponse:
    def __init__(self, code_security: CodeSecurityResource) -> None:
        self._code_security = code_security

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._code_security.configurations)


class AsyncCodeSecurityResourceWithRawResponse:
    def __init__(self, code_security: AsyncCodeSecurityResource) -> None:
        self._code_security = code_security

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._code_security.configurations)


class CodeSecurityResourceWithStreamingResponse:
    def __init__(self, code_security: CodeSecurityResource) -> None:
        self._code_security = code_security

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._code_security.configurations)


class AsyncCodeSecurityResourceWithStreamingResponse:
    def __init__(self, code_security: AsyncCodeSecurityResource) -> None:
        self._code_security = code_security

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._code_security.configurations)
