from __future__ import annotations

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos import action_list_organization_secrets_params, action_list_organization_variables_params
from ....types.repos.action_list_organization_secrets_response import ActionListOrganizationSecretsResponse
from ....types.repos.action_list_organization_variables_response import ActionListOrganizationVariablesResponse
from .artifacts import (
    ArtifactsResource,
    ArtifactsResourceWithRawResponse,
    ArtifactsResourceWithStreamingResponse,
    AsyncArtifactsResource,
    AsyncArtifactsResourceWithRawResponse,
    AsyncArtifactsResourceWithStreamingResponse,
)
from .cache import (
    AsyncCacheResource,
    AsyncCacheResourceWithRawResponse,
    AsyncCacheResourceWithStreamingResponse,
    CacheResource,
    CacheResourceWithRawResponse,
    CacheResourceWithStreamingResponse,
)
from .caches import (
    AsyncCachesResource,
    AsyncCachesResourceWithRawResponse,
    AsyncCachesResourceWithStreamingResponse,
    CachesResource,
    CachesResourceWithRawResponse,
    CachesResourceWithStreamingResponse,
)
from .jobs import (
    AsyncJobsResource,
    AsyncJobsResourceWithRawResponse,
    AsyncJobsResourceWithStreamingResponse,
    JobsResource,
    JobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
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
from .runners.runners import (
    AsyncRunnersResource,
    AsyncRunnersResourceWithRawResponse,
    AsyncRunnersResourceWithStreamingResponse,
    RunnersResource,
    RunnersResourceWithRawResponse,
    RunnersResourceWithStreamingResponse,
)
from .runs.runs import (
    AsyncRunsResource,
    AsyncRunsResourceWithRawResponse,
    AsyncRunsResourceWithStreamingResponse,
    RunsResource,
    RunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
)
from .secrets import (
    AsyncSecretsResource,
    AsyncSecretsResourceWithRawResponse,
    AsyncSecretsResourceWithStreamingResponse,
    SecretsResource,
    SecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
)
from .variables import (
    AsyncVariablesResource,
    AsyncVariablesResourceWithRawResponse,
    AsyncVariablesResourceWithStreamingResponse,
    VariablesResource,
    VariablesResourceWithRawResponse,
    VariablesResourceWithStreamingResponse,
)
from .workflows import (
    AsyncWorkflowsResource,
    AsyncWorkflowsResourceWithRawResponse,
    AsyncWorkflowsResourceWithStreamingResponse,
    WorkflowsResource,
    WorkflowsResourceWithRawResponse,
    WorkflowsResourceWithStreamingResponse,
)

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def artifacts(self) -> ArtifactsResource:
        return ArtifactsResource(self._client)

    @cached_property
    def cache(self) -> CacheResource:
        return CacheResource(self._client)

    @cached_property
    def caches(self) -> CachesResource:
        return CachesResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def oidc(self) -> OidcResource:
        return OidcResource(self._client)

    @cached_property
    def permissions(self) -> PermissionsResource:
        return PermissionsResource(self._client)

    @cached_property
    def runners(self) -> RunnersResource:
        return RunnersResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def variables(self) -> VariablesResource:
        return VariablesResource(self._client)

    @cached_property
    def workflows(self) -> WorkflowsResource:
        return WorkflowsResource(self._client)

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

    def list_organization_secrets(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionListOrganizationSecretsResponse:
        """
        Lists all organization secrets shared with a repository without revealing their
        encrypted values.

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/actions/organization-secrets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    action_list_organization_secrets_params.ActionListOrganizationSecretsParams,
                ),
            ),
            cast_to=ActionListOrganizationSecretsResponse,
        )

    def list_organization_variables(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionListOrganizationVariablesResponse:
        """
        Lists all organization variables shared with a repository.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 30). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/actions/organization-variables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    action_list_organization_variables_params.ActionListOrganizationVariablesParams,
                ),
            ),
            cast_to=ActionListOrganizationVariablesResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def artifacts(self) -> AsyncArtifactsResource:
        return AsyncArtifactsResource(self._client)

    @cached_property
    def cache(self) -> AsyncCacheResource:
        return AsyncCacheResource(self._client)

    @cached_property
    def caches(self) -> AsyncCachesResource:
        return AsyncCachesResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def oidc(self) -> AsyncOidcResource:
        return AsyncOidcResource(self._client)

    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        return AsyncPermissionsResource(self._client)

    @cached_property
    def runners(self) -> AsyncRunnersResource:
        return AsyncRunnersResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def variables(self) -> AsyncVariablesResource:
        return AsyncVariablesResource(self._client)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResource:
        return AsyncWorkflowsResource(self._client)

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

    async def list_organization_secrets(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionListOrganizationSecretsResponse:
        """
        Lists all organization secrets shared with a repository without revealing their
        encrypted values.

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/actions/organization-secrets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    action_list_organization_secrets_params.ActionListOrganizationSecretsParams,
                ),
            ),
            cast_to=ActionListOrganizationSecretsResponse,
        )

    async def list_organization_variables(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionListOrganizationVariablesResponse:
        """
        Lists all organization variables shared with a repository.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 30). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/actions/organization-variables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    action_list_organization_variables_params.ActionListOrganizationVariablesParams,
                ),
            ),
            cast_to=ActionListOrganizationVariablesResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.list_organization_secrets = to_raw_response_wrapper(
            actions.list_organization_secrets,
        )
        self.list_organization_variables = to_raw_response_wrapper(
            actions.list_organization_variables,
        )

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithRawResponse:
        return ArtifactsResourceWithRawResponse(self._actions.artifacts)

    @cached_property
    def cache(self) -> CacheResourceWithRawResponse:
        return CacheResourceWithRawResponse(self._actions.cache)

    @cached_property
    def caches(self) -> CachesResourceWithRawResponse:
        return CachesResourceWithRawResponse(self._actions.caches)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._actions.jobs)

    @cached_property
    def oidc(self) -> OidcResourceWithRawResponse:
        return OidcResourceWithRawResponse(self._actions.oidc)

    @cached_property
    def permissions(self) -> PermissionsResourceWithRawResponse:
        return PermissionsResourceWithRawResponse(self._actions.permissions)

    @cached_property
    def runners(self) -> RunnersResourceWithRawResponse:
        return RunnersResourceWithRawResponse(self._actions.runners)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._actions.runs)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._actions.secrets)

    @cached_property
    def variables(self) -> VariablesResourceWithRawResponse:
        return VariablesResourceWithRawResponse(self._actions.variables)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithRawResponse:
        return WorkflowsResourceWithRawResponse(self._actions.workflows)


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.list_organization_secrets = async_to_raw_response_wrapper(
            actions.list_organization_secrets,
        )
        self.list_organization_variables = async_to_raw_response_wrapper(
            actions.list_organization_variables,
        )

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithRawResponse:
        return AsyncArtifactsResourceWithRawResponse(self._actions.artifacts)

    @cached_property
    def cache(self) -> AsyncCacheResourceWithRawResponse:
        return AsyncCacheResourceWithRawResponse(self._actions.cache)

    @cached_property
    def caches(self) -> AsyncCachesResourceWithRawResponse:
        return AsyncCachesResourceWithRawResponse(self._actions.caches)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._actions.jobs)

    @cached_property
    def oidc(self) -> AsyncOidcResourceWithRawResponse:
        return AsyncOidcResourceWithRawResponse(self._actions.oidc)

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithRawResponse:
        return AsyncPermissionsResourceWithRawResponse(self._actions.permissions)

    @cached_property
    def runners(self) -> AsyncRunnersResourceWithRawResponse:
        return AsyncRunnersResourceWithRawResponse(self._actions.runners)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._actions.runs)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._actions.secrets)

    @cached_property
    def variables(self) -> AsyncVariablesResourceWithRawResponse:
        return AsyncVariablesResourceWithRawResponse(self._actions.variables)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithRawResponse:
        return AsyncWorkflowsResourceWithRawResponse(self._actions.workflows)


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.list_organization_secrets = to_streamed_response_wrapper(
            actions.list_organization_secrets,
        )
        self.list_organization_variables = to_streamed_response_wrapper(
            actions.list_organization_variables,
        )

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithStreamingResponse:
        return ArtifactsResourceWithStreamingResponse(self._actions.artifacts)

    @cached_property
    def cache(self) -> CacheResourceWithStreamingResponse:
        return CacheResourceWithStreamingResponse(self._actions.cache)

    @cached_property
    def caches(self) -> CachesResourceWithStreamingResponse:
        return CachesResourceWithStreamingResponse(self._actions.caches)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._actions.jobs)

    @cached_property
    def oidc(self) -> OidcResourceWithStreamingResponse:
        return OidcResourceWithStreamingResponse(self._actions.oidc)

    @cached_property
    def permissions(self) -> PermissionsResourceWithStreamingResponse:
        return PermissionsResourceWithStreamingResponse(self._actions.permissions)

    @cached_property
    def runners(self) -> RunnersResourceWithStreamingResponse:
        return RunnersResourceWithStreamingResponse(self._actions.runners)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._actions.runs)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._actions.secrets)

    @cached_property
    def variables(self) -> VariablesResourceWithStreamingResponse:
        return VariablesResourceWithStreamingResponse(self._actions.variables)

    @cached_property
    def workflows(self) -> WorkflowsResourceWithStreamingResponse:
        return WorkflowsResourceWithStreamingResponse(self._actions.workflows)


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.list_organization_secrets = async_to_streamed_response_wrapper(
            actions.list_organization_secrets,
        )
        self.list_organization_variables = async_to_streamed_response_wrapper(
            actions.list_organization_variables,
        )

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithStreamingResponse:
        return AsyncArtifactsResourceWithStreamingResponse(self._actions.artifacts)

    @cached_property
    def cache(self) -> AsyncCacheResourceWithStreamingResponse:
        return AsyncCacheResourceWithStreamingResponse(self._actions.cache)

    @cached_property
    def caches(self) -> AsyncCachesResourceWithStreamingResponse:
        return AsyncCachesResourceWithStreamingResponse(self._actions.caches)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._actions.jobs)

    @cached_property
    def oidc(self) -> AsyncOidcResourceWithStreamingResponse:
        return AsyncOidcResourceWithStreamingResponse(self._actions.oidc)

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithStreamingResponse:
        return AsyncPermissionsResourceWithStreamingResponse(self._actions.permissions)

    @cached_property
    def runners(self) -> AsyncRunnersResourceWithStreamingResponse:
        return AsyncRunnersResourceWithStreamingResponse(self._actions.runners)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._actions.runs)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._actions.secrets)

    @cached_property
    def variables(self) -> AsyncVariablesResourceWithStreamingResponse:
        return AsyncVariablesResourceWithStreamingResponse(self._actions.variables)

    @cached_property
    def workflows(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        return AsyncWorkflowsResourceWithStreamingResponse(self._actions.workflows)
