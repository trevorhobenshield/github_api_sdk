from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .alerts.alerts import (
    AlertsResource,
    AlertsResourceWithRawResponse,
    AlertsResourceWithStreamingResponse,
    AsyncAlertsResource,
    AsyncAlertsResourceWithRawResponse,
    AsyncAlertsResourceWithStreamingResponse,
)
from .analyses import (
    AnalysesResource,
    AnalysesResourceWithRawResponse,
    AnalysesResourceWithStreamingResponse,
    AsyncAnalysesResource,
    AsyncAnalysesResourceWithRawResponse,
    AsyncAnalysesResourceWithStreamingResponse,
)
from .codeql.codeql import (
    AsyncCodeqlResource,
    AsyncCodeqlResourceWithRawResponse,
    AsyncCodeqlResourceWithStreamingResponse,
    CodeqlResource,
    CodeqlResourceWithRawResponse,
    CodeqlResourceWithStreamingResponse,
)
from .default_setup import (
    AsyncDefaultSetupResource,
    AsyncDefaultSetupResourceWithRawResponse,
    AsyncDefaultSetupResourceWithStreamingResponse,
    DefaultSetupResource,
    DefaultSetupResourceWithRawResponse,
    DefaultSetupResourceWithStreamingResponse,
)
from .sarifs import (
    AsyncSarifsResource,
    AsyncSarifsResourceWithRawResponse,
    AsyncSarifsResourceWithStreamingResponse,
    SarifsResource,
    SarifsResourceWithRawResponse,
    SarifsResourceWithStreamingResponse,
)

__all__ = ["CodeScanningResource", "AsyncCodeScanningResource"]


class CodeScanningResource(SyncAPIResource):
    @cached_property
    def alerts(self) -> AlertsResource:
        return AlertsResource(self._client)

    @cached_property
    def analyses(self) -> AnalysesResource:
        return AnalysesResource(self._client)

    @cached_property
    def codeql(self) -> CodeqlResource:
        return CodeqlResource(self._client)

    @cached_property
    def default_setup(self) -> DefaultSetupResource:
        return DefaultSetupResource(self._client)

    @cached_property
    def sarifs(self) -> SarifsResource:
        return SarifsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CodeScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodeScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodeScanningResourceWithStreamingResponse(self)


class AsyncCodeScanningResource(AsyncAPIResource):
    @cached_property
    def alerts(self) -> AsyncAlertsResource:
        return AsyncAlertsResource(self._client)

    @cached_property
    def analyses(self) -> AsyncAnalysesResource:
        return AsyncAnalysesResource(self._client)

    @cached_property
    def codeql(self) -> AsyncCodeqlResource:
        return AsyncCodeqlResource(self._client)

    @cached_property
    def default_setup(self) -> AsyncDefaultSetupResource:
        return AsyncDefaultSetupResource(self._client)

    @cached_property
    def sarifs(self) -> AsyncSarifsResource:
        return AsyncSarifsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCodeScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodeScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodeScanningResourceWithStreamingResponse(self)


class CodeScanningResourceWithRawResponse:
    def __init__(self, code_scanning: CodeScanningResource) -> None:
        self._code_scanning = code_scanning

    @cached_property
    def alerts(self) -> AlertsResourceWithRawResponse:
        return AlertsResourceWithRawResponse(self._code_scanning.alerts)

    @cached_property
    def analyses(self) -> AnalysesResourceWithRawResponse:
        return AnalysesResourceWithRawResponse(self._code_scanning.analyses)

    @cached_property
    def codeql(self) -> CodeqlResourceWithRawResponse:
        return CodeqlResourceWithRawResponse(self._code_scanning.codeql)

    @cached_property
    def default_setup(self) -> DefaultSetupResourceWithRawResponse:
        return DefaultSetupResourceWithRawResponse(self._code_scanning.default_setup)

    @cached_property
    def sarifs(self) -> SarifsResourceWithRawResponse:
        return SarifsResourceWithRawResponse(self._code_scanning.sarifs)


class AsyncCodeScanningResourceWithRawResponse:
    def __init__(self, code_scanning: AsyncCodeScanningResource) -> None:
        self._code_scanning = code_scanning

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithRawResponse:
        return AsyncAlertsResourceWithRawResponse(self._code_scanning.alerts)

    @cached_property
    def analyses(self) -> AsyncAnalysesResourceWithRawResponse:
        return AsyncAnalysesResourceWithRawResponse(self._code_scanning.analyses)

    @cached_property
    def codeql(self) -> AsyncCodeqlResourceWithRawResponse:
        return AsyncCodeqlResourceWithRawResponse(self._code_scanning.codeql)

    @cached_property
    def default_setup(self) -> AsyncDefaultSetupResourceWithRawResponse:
        return AsyncDefaultSetupResourceWithRawResponse(self._code_scanning.default_setup)

    @cached_property
    def sarifs(self) -> AsyncSarifsResourceWithRawResponse:
        return AsyncSarifsResourceWithRawResponse(self._code_scanning.sarifs)


class CodeScanningResourceWithStreamingResponse:
    def __init__(self, code_scanning: CodeScanningResource) -> None:
        self._code_scanning = code_scanning

    @cached_property
    def alerts(self) -> AlertsResourceWithStreamingResponse:
        return AlertsResourceWithStreamingResponse(self._code_scanning.alerts)

    @cached_property
    def analyses(self) -> AnalysesResourceWithStreamingResponse:
        return AnalysesResourceWithStreamingResponse(self._code_scanning.analyses)

    @cached_property
    def codeql(self) -> CodeqlResourceWithStreamingResponse:
        return CodeqlResourceWithStreamingResponse(self._code_scanning.codeql)

    @cached_property
    def default_setup(self) -> DefaultSetupResourceWithStreamingResponse:
        return DefaultSetupResourceWithStreamingResponse(self._code_scanning.default_setup)

    @cached_property
    def sarifs(self) -> SarifsResourceWithStreamingResponse:
        return SarifsResourceWithStreamingResponse(self._code_scanning.sarifs)


class AsyncCodeScanningResourceWithStreamingResponse:
    def __init__(self, code_scanning: AsyncCodeScanningResource) -> None:
        self._code_scanning = code_scanning

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithStreamingResponse:
        return AsyncAlertsResourceWithStreamingResponse(self._code_scanning.alerts)

    @cached_property
    def analyses(self) -> AsyncAnalysesResourceWithStreamingResponse:
        return AsyncAnalysesResourceWithStreamingResponse(self._code_scanning.analyses)

    @cached_property
    def codeql(self) -> AsyncCodeqlResourceWithStreamingResponse:
        return AsyncCodeqlResourceWithStreamingResponse(self._code_scanning.codeql)

    @cached_property
    def default_setup(self) -> AsyncDefaultSetupResourceWithStreamingResponse:
        return AsyncDefaultSetupResourceWithStreamingResponse(self._code_scanning.default_setup)

    @cached_property
    def sarifs(self) -> AsyncSarifsResourceWithStreamingResponse:
        return AsyncSarifsResourceWithStreamingResponse(self._code_scanning.sarifs)
