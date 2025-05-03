from __future__ import annotations

from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from .code_security.code_security import (
    AsyncCodeSecurityResource,
    AsyncCodeSecurityResourceWithRawResponse,
    AsyncCodeSecurityResourceWithStreamingResponse,
    CodeSecurityResource,
    CodeSecurityResourceWithRawResponse,
    CodeSecurityResourceWithStreamingResponse,
)
from .dependabot import (
    AsyncDependabotResource,
    AsyncDependabotResourceWithRawResponse,
    AsyncDependabotResourceWithStreamingResponse,
    DependabotResource,
    DependabotResourceWithRawResponse,
    DependabotResourceWithStreamingResponse,
)
from .secret_scanning import (
    AsyncSecretScanningResource,
    AsyncSecretScanningResourceWithRawResponse,
    AsyncSecretScanningResourceWithStreamingResponse,
    SecretScanningResource,
    SecretScanningResourceWithRawResponse,
    SecretScanningResourceWithStreamingResponse,
)

__all__ = ["EnterprisesResource", "AsyncEnterprisesResource"]


class EnterprisesResource(SyncAPIResource):
    @cached_property
    def code_security(self) -> CodeSecurityResource:
        return CodeSecurityResource(self._client)

    @cached_property
    def dependabot(self) -> DependabotResource:
        return DependabotResource(self._client)

    @cached_property
    def secret_scanning(self) -> SecretScanningResource:
        return SecretScanningResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnterprisesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnterprisesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnterprisesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return EnterprisesResourceWithStreamingResponse(self)


class AsyncEnterprisesResource(AsyncAPIResource):
    @cached_property
    def code_security(self) -> AsyncCodeSecurityResource:
        return AsyncCodeSecurityResource(self._client)

    @cached_property
    def dependabot(self) -> AsyncDependabotResource:
        return AsyncDependabotResource(self._client)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResource:
        return AsyncSecretScanningResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnterprisesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnterprisesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnterprisesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncEnterprisesResourceWithStreamingResponse(self)


class EnterprisesResourceWithRawResponse:
    def __init__(self, enterprises: EnterprisesResource) -> None:
        self._enterprises = enterprises

    @cached_property
    def code_security(self) -> CodeSecurityResourceWithRawResponse:
        return CodeSecurityResourceWithRawResponse(self._enterprises.code_security)

    @cached_property
    def dependabot(self) -> DependabotResourceWithRawResponse:
        return DependabotResourceWithRawResponse(self._enterprises.dependabot)

    @cached_property
    def secret_scanning(self) -> SecretScanningResourceWithRawResponse:
        return SecretScanningResourceWithRawResponse(self._enterprises.secret_scanning)


class AsyncEnterprisesResourceWithRawResponse:
    def __init__(self, enterprises: AsyncEnterprisesResource) -> None:
        self._enterprises = enterprises

    @cached_property
    def code_security(self) -> AsyncCodeSecurityResourceWithRawResponse:
        return AsyncCodeSecurityResourceWithRawResponse(self._enterprises.code_security)

    @cached_property
    def dependabot(self) -> AsyncDependabotResourceWithRawResponse:
        return AsyncDependabotResourceWithRawResponse(self._enterprises.dependabot)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResourceWithRawResponse:
        return AsyncSecretScanningResourceWithRawResponse(self._enterprises.secret_scanning)


class EnterprisesResourceWithStreamingResponse:
    def __init__(self, enterprises: EnterprisesResource) -> None:
        self._enterprises = enterprises

    @cached_property
    def code_security(self) -> CodeSecurityResourceWithStreamingResponse:
        return CodeSecurityResourceWithStreamingResponse(self._enterprises.code_security)

    @cached_property
    def dependabot(self) -> DependabotResourceWithStreamingResponse:
        return DependabotResourceWithStreamingResponse(self._enterprises.dependabot)

    @cached_property
    def secret_scanning(self) -> SecretScanningResourceWithStreamingResponse:
        return SecretScanningResourceWithStreamingResponse(self._enterprises.secret_scanning)


class AsyncEnterprisesResourceWithStreamingResponse:
    def __init__(self, enterprises: AsyncEnterprisesResource) -> None:
        self._enterprises = enterprises

    @cached_property
    def code_security(self) -> AsyncCodeSecurityResourceWithStreamingResponse:
        return AsyncCodeSecurityResourceWithStreamingResponse(self._enterprises.code_security)

    @cached_property
    def dependabot(self) -> AsyncDependabotResourceWithStreamingResponse:
        return AsyncDependabotResourceWithStreamingResponse(self._enterprises.dependabot)

    @cached_property
    def secret_scanning(self) -> AsyncSecretScanningResourceWithStreamingResponse:
        return AsyncSecretScanningResourceWithStreamingResponse(self._enterprises.secret_scanning)
