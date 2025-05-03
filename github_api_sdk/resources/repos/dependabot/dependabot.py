from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .alerts import (
    AlertsResource,
    AlertsResourceWithRawResponse,
    AlertsResourceWithStreamingResponse,
    AsyncAlertsResource,
    AsyncAlertsResourceWithRawResponse,
    AsyncAlertsResourceWithStreamingResponse,
)
from .secrets import (
    AsyncSecretsResource,
    AsyncSecretsResourceWithRawResponse,
    AsyncSecretsResourceWithStreamingResponse,
    SecretsResource,
    SecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
)

__all__ = ["DependabotResource", "AsyncDependabotResource"]


class DependabotResource(SyncAPIResource):
    @cached_property
    def alerts(self) -> AlertsResource:
        return AlertsResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DependabotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DependabotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DependabotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DependabotResourceWithStreamingResponse(self)


class AsyncDependabotResource(AsyncAPIResource):
    @cached_property
    def alerts(self) -> AsyncAlertsResource:
        return AsyncAlertsResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDependabotResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDependabotResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDependabotResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDependabotResourceWithStreamingResponse(self)


class DependabotResourceWithRawResponse:
    def __init__(self, dependabot: DependabotResource) -> None:
        self._dependabot = dependabot

    @cached_property
    def alerts(self) -> AlertsResourceWithRawResponse:
        return AlertsResourceWithRawResponse(self._dependabot.alerts)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._dependabot.secrets)


class AsyncDependabotResourceWithRawResponse:
    def __init__(self, dependabot: AsyncDependabotResource) -> None:
        self._dependabot = dependabot

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithRawResponse:
        return AsyncAlertsResourceWithRawResponse(self._dependabot.alerts)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._dependabot.secrets)


class DependabotResourceWithStreamingResponse:
    def __init__(self, dependabot: DependabotResource) -> None:
        self._dependabot = dependabot

    @cached_property
    def alerts(self) -> AlertsResourceWithStreamingResponse:
        return AlertsResourceWithStreamingResponse(self._dependabot.alerts)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._dependabot.secrets)


class AsyncDependabotResourceWithStreamingResponse:
    def __init__(self, dependabot: AsyncDependabotResource) -> None:
        self._dependabot = dependabot

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithStreamingResponse:
        return AsyncAlertsResourceWithStreamingResponse(self._dependabot.alerts)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._dependabot.secrets)
