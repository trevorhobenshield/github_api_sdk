from __future__ import annotations

from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from .databases import (
    AsyncDatabasesResource,
    AsyncDatabasesResourceWithRawResponse,
    AsyncDatabasesResourceWithStreamingResponse,
    DatabasesResource,
    DatabasesResourceWithRawResponse,
    DatabasesResourceWithStreamingResponse,
)
from .variant_analyses import (
    AsyncVariantAnalysesResource,
    AsyncVariantAnalysesResourceWithRawResponse,
    AsyncVariantAnalysesResourceWithStreamingResponse,
    VariantAnalysesResource,
    VariantAnalysesResourceWithRawResponse,
    VariantAnalysesResourceWithStreamingResponse,
)

__all__ = ["CodeqlResource", "AsyncCodeqlResource"]


class CodeqlResource(SyncAPIResource):
    @cached_property
    def databases(self) -> DatabasesResource:
        return DatabasesResource(self._client)

    @cached_property
    def variant_analyses(self) -> VariantAnalysesResource:
        return VariantAnalysesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CodeqlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodeqlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeqlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodeqlResourceWithStreamingResponse(self)


class AsyncCodeqlResource(AsyncAPIResource):
    @cached_property
    def databases(self) -> AsyncDatabasesResource:
        return AsyncDatabasesResource(self._client)

    @cached_property
    def variant_analyses(self) -> AsyncVariantAnalysesResource:
        return AsyncVariantAnalysesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCodeqlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodeqlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeqlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodeqlResourceWithStreamingResponse(self)


class CodeqlResourceWithRawResponse:
    def __init__(self, codeql: CodeqlResource) -> None:
        self._codeql = codeql

    @cached_property
    def databases(self) -> DatabasesResourceWithRawResponse:
        return DatabasesResourceWithRawResponse(self._codeql.databases)

    @cached_property
    def variant_analyses(self) -> VariantAnalysesResourceWithRawResponse:
        return VariantAnalysesResourceWithRawResponse(self._codeql.variant_analyses)


class AsyncCodeqlResourceWithRawResponse:
    def __init__(self, codeql: AsyncCodeqlResource) -> None:
        self._codeql = codeql

    @cached_property
    def databases(self) -> AsyncDatabasesResourceWithRawResponse:
        return AsyncDatabasesResourceWithRawResponse(self._codeql.databases)

    @cached_property
    def variant_analyses(self) -> AsyncVariantAnalysesResourceWithRawResponse:
        return AsyncVariantAnalysesResourceWithRawResponse(self._codeql.variant_analyses)


class CodeqlResourceWithStreamingResponse:
    def __init__(self, codeql: CodeqlResource) -> None:
        self._codeql = codeql

    @cached_property
    def databases(self) -> DatabasesResourceWithStreamingResponse:
        return DatabasesResourceWithStreamingResponse(self._codeql.databases)

    @cached_property
    def variant_analyses(self) -> VariantAnalysesResourceWithStreamingResponse:
        return VariantAnalysesResourceWithStreamingResponse(self._codeql.variant_analyses)


class AsyncCodeqlResourceWithStreamingResponse:
    def __init__(self, codeql: AsyncCodeqlResource) -> None:
        self._codeql = codeql

    @cached_property
    def databases(self) -> AsyncDatabasesResourceWithStreamingResponse:
        return AsyncDatabasesResourceWithStreamingResponse(self._codeql.databases)

    @cached_property
    def variant_analyses(self) -> AsyncVariantAnalysesResourceWithStreamingResponse:
        return AsyncVariantAnalysesResourceWithStreamingResponse(self._codeql.variant_analyses)
