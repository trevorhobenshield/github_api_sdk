from __future__ import annotations

from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from .cache import (
    AsyncCacheResource,
    AsyncCacheResourceWithRawResponse,
    AsyncCacheResourceWithStreamingResponse,
    CacheResource,
    CacheResourceWithRawResponse,
    CacheResourceWithStreamingResponse,
)
from .hosted_runners.hosted_runners import (
    AsyncHostedRunnersResource,
    AsyncHostedRunnersResourceWithRawResponse,
    AsyncHostedRunnersResourceWithStreamingResponse,
    HostedRunnersResource,
    HostedRunnersResourceWithRawResponse,
    HostedRunnersResourceWithStreamingResponse,
)
from .oidc.oidc import (
    AsyncOidcResource,
    AsyncOidcResourceWithRawResponse,
    AsyncOidcResourceWithStreamingResponse,
    OidcResource,
    OidcResourceWithRawResponse,
    OidcResourceWithStreamingResponse,
)
from .permissions.permissions import (
    AsyncPermissionsResource,
    AsyncPermissionsResourceWithRawResponse,
    AsyncPermissionsResourceWithStreamingResponse,
    PermissionsResource,
    PermissionsResourceWithRawResponse,
    PermissionsResourceWithStreamingResponse,
)
from .runner_groups.runner_groups import (
    AsyncRunnerGroupsResource,
    AsyncRunnerGroupsResourceWithRawResponse,
    AsyncRunnerGroupsResourceWithStreamingResponse,
    RunnerGroupsResource,
    RunnerGroupsResourceWithRawResponse,
    RunnerGroupsResourceWithStreamingResponse,
)
from .runners.runners import (
    AsyncRunnersResource,
    AsyncRunnersResourceWithRawResponse,
    AsyncRunnersResourceWithStreamingResponse,
    RunnersResource,
    RunnersResourceWithRawResponse,
    RunnersResourceWithStreamingResponse,
)
from .secrets.secrets import (
    AsyncSecretsResource,
    AsyncSecretsResourceWithRawResponse,
    AsyncSecretsResourceWithStreamingResponse,
    SecretsResource,
    SecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
)
from .variables.variables import (
    AsyncVariablesResource,
    AsyncVariablesResourceWithRawResponse,
    AsyncVariablesResourceWithStreamingResponse,
    VariablesResource,
    VariablesResourceWithRawResponse,
    VariablesResourceWithStreamingResponse,
)

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def cache(self) -> CacheResource:
        return CacheResource(self._client)

    @cached_property
    def hosted_runners(self) -> HostedRunnersResource:
        return HostedRunnersResource(self._client)

    @cached_property
    def oidc(self) -> OidcResource:
        return OidcResource(self._client)

    @cached_property
    def permissions(self) -> PermissionsResource:
        return PermissionsResource(self._client)

    @cached_property
    def runner_groups(self) -> RunnerGroupsResource:
        return RunnerGroupsResource(self._client)

    @cached_property
    def runners(self) -> RunnersResource:
        return RunnersResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def variables(self) -> VariablesResource:
        return VariablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def cache(self) -> AsyncCacheResource:
        return AsyncCacheResource(self._client)

    @cached_property
    def hosted_runners(self) -> AsyncHostedRunnersResource:
        return AsyncHostedRunnersResource(self._client)

    @cached_property
    def oidc(self) -> AsyncOidcResource:
        return AsyncOidcResource(self._client)

    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        return AsyncPermissionsResource(self._client)

    @cached_property
    def runner_groups(self) -> AsyncRunnerGroupsResource:
        return AsyncRunnerGroupsResource(self._client)

    @cached_property
    def runners(self) -> AsyncRunnersResource:
        return AsyncRunnersResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def variables(self) -> AsyncVariablesResource:
        return AsyncVariablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

    @cached_property
    def cache(self) -> CacheResourceWithRawResponse:
        return CacheResourceWithRawResponse(self._actions.cache)

    @cached_property
    def hosted_runners(self) -> HostedRunnersResourceWithRawResponse:
        return HostedRunnersResourceWithRawResponse(self._actions.hosted_runners)

    @cached_property
    def oidc(self) -> OidcResourceWithRawResponse:
        return OidcResourceWithRawResponse(self._actions.oidc)

    @cached_property
    def permissions(self) -> PermissionsResourceWithRawResponse:
        return PermissionsResourceWithRawResponse(self._actions.permissions)

    @cached_property
    def runner_groups(self) -> RunnerGroupsResourceWithRawResponse:
        return RunnerGroupsResourceWithRawResponse(self._actions.runner_groups)

    @cached_property
    def runners(self) -> RunnersResourceWithRawResponse:
        return RunnersResourceWithRawResponse(self._actions.runners)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._actions.secrets)

    @cached_property
    def variables(self) -> VariablesResourceWithRawResponse:
        return VariablesResourceWithRawResponse(self._actions.variables)


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

    @cached_property
    def cache(self) -> AsyncCacheResourceWithRawResponse:
        return AsyncCacheResourceWithRawResponse(self._actions.cache)

    @cached_property
    def hosted_runners(self) -> AsyncHostedRunnersResourceWithRawResponse:
        return AsyncHostedRunnersResourceWithRawResponse(self._actions.hosted_runners)

    @cached_property
    def oidc(self) -> AsyncOidcResourceWithRawResponse:
        return AsyncOidcResourceWithRawResponse(self._actions.oidc)

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithRawResponse:
        return AsyncPermissionsResourceWithRawResponse(self._actions.permissions)

    @cached_property
    def runner_groups(self) -> AsyncRunnerGroupsResourceWithRawResponse:
        return AsyncRunnerGroupsResourceWithRawResponse(self._actions.runner_groups)

    @cached_property
    def runners(self) -> AsyncRunnersResourceWithRawResponse:
        return AsyncRunnersResourceWithRawResponse(self._actions.runners)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._actions.secrets)

    @cached_property
    def variables(self) -> AsyncVariablesResourceWithRawResponse:
        return AsyncVariablesResourceWithRawResponse(self._actions.variables)


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

    @cached_property
    def cache(self) -> CacheResourceWithStreamingResponse:
        return CacheResourceWithStreamingResponse(self._actions.cache)

    @cached_property
    def hosted_runners(self) -> HostedRunnersResourceWithStreamingResponse:
        return HostedRunnersResourceWithStreamingResponse(self._actions.hosted_runners)

    @cached_property
    def oidc(self) -> OidcResourceWithStreamingResponse:
        return OidcResourceWithStreamingResponse(self._actions.oidc)

    @cached_property
    def permissions(self) -> PermissionsResourceWithStreamingResponse:
        return PermissionsResourceWithStreamingResponse(self._actions.permissions)

    @cached_property
    def runner_groups(self) -> RunnerGroupsResourceWithStreamingResponse:
        return RunnerGroupsResourceWithStreamingResponse(self._actions.runner_groups)

    @cached_property
    def runners(self) -> RunnersResourceWithStreamingResponse:
        return RunnersResourceWithStreamingResponse(self._actions.runners)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._actions.secrets)

    @cached_property
    def variables(self) -> VariablesResourceWithStreamingResponse:
        return VariablesResourceWithStreamingResponse(self._actions.variables)


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

    @cached_property
    def cache(self) -> AsyncCacheResourceWithStreamingResponse:
        return AsyncCacheResourceWithStreamingResponse(self._actions.cache)

    @cached_property
    def hosted_runners(self) -> AsyncHostedRunnersResourceWithStreamingResponse:
        return AsyncHostedRunnersResourceWithStreamingResponse(self._actions.hosted_runners)

    @cached_property
    def oidc(self) -> AsyncOidcResourceWithStreamingResponse:
        return AsyncOidcResourceWithStreamingResponse(self._actions.oidc)

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithStreamingResponse:
        return AsyncPermissionsResourceWithStreamingResponse(self._actions.permissions)

    @cached_property
    def runner_groups(self) -> AsyncRunnerGroupsResourceWithStreamingResponse:
        return AsyncRunnerGroupsResourceWithStreamingResponse(self._actions.runner_groups)

    @cached_property
    def runners(self) -> AsyncRunnersResourceWithStreamingResponse:
        return AsyncRunnersResourceWithStreamingResponse(self._actions.runners)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._actions.secrets)

    @cached_property
    def variables(self) -> AsyncVariablesResourceWithStreamingResponse:
        return AsyncVariablesResourceWithStreamingResponse(self._actions.variables)
