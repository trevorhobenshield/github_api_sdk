from __future__ import annotations

import httpx
from typing_extensions import Literal

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
from ....types.orgs.members.codespace import Codespace
from ....types.repos import (
    codespace_check_permissions_params,
    codespace_create_params,
    codespace_get_default_attributes_params,
    codespace_list_devcontainers_params,
    codespace_list_machines_params,
    codespace_list_params,
)
from ....types.repos.codespace_check_permissions_response import CodespaceCheckPermissionsResponse
from ....types.repos.codespace_get_default_attributes_response import CodespaceGetDefaultAttributesResponse
from ....types.repos.codespace_list_devcontainers_response import CodespaceListDevcontainersResponse
from ....types.repos.codespace_list_machines_response import CodespaceListMachinesResponse
from ....types.repos.codespace_list_response import CodespaceListResponse
from .secrets import (
    AsyncSecretsResource,
    AsyncSecretsResourceWithRawResponse,
    AsyncSecretsResourceWithStreamingResponse,
    SecretsResource,
    SecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
)

__all__ = ["CodespacesResource", "AsyncCodespacesResource"]


class CodespacesResource(SyncAPIResource):
    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CodespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodespacesResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        client_ip: str | NotGiven = NOT_GIVEN,
        devcontainer_path: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        geo: Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"] | NotGiven = NOT_GIVEN,
        idle_timeout_minutes: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        machine: str | NotGiven = NOT_GIVEN,
        multi_repo_permissions_opt_out: bool | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        retention_period_minutes: int | NotGiven = NOT_GIVEN,
        working_directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Creates a codespace owned by the authenticated user in the specified repository.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          client_ip: IP for location auto-detection when proxying a request

          devcontainer_path: Path to devcontainer.json config to use for this codespace

          display_name: Display name for this codespace

          geo: The geographic area for this codespace. If not specified, the value is assigned
              by IP. This property replaces `location`, which is closing down.

          idle_timeout_minutes: Time in minutes before codespace stops from inactivity

          location: The requested location for a new codespace. Best efforts are made to respect
              this upon creation. Assigned by IP if not provided.

          machine: Machine type to use for this codespace

          multi_repo_permissions_opt_out: Whether to authorize requested permissions from devcontainer.json

          ref: Git ref (typically a branch name) for this codespace

          retention_period_minutes: Duration in minutes after codespace has gone idle in which it will be deleted.
              Must be integer minutes between 0 and 43200 (30 days).

          working_directory: Working directory for this codespace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/codespaces",
            body=maybe_transform(
                {
                    "client_ip": client_ip,
                    "devcontainer_path": devcontainer_path,
                    "display_name": display_name,
                    "geo": geo,
                    "idle_timeout_minutes": idle_timeout_minutes,
                    "location": location,
                    "machine": machine,
                    "multi_repo_permissions_opt_out": multi_repo_permissions_opt_out,
                    "ref": ref,
                    "retention_period_minutes": retention_period_minutes,
                    "working_directory": working_directory,
                },
                codespace_create_params.CodespaceCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    def list(
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
    ) -> CodespaceListResponse:
        """
        Lists the codespaces associated to a specified repository and the authenticated
        user.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

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
            f"/repos/{owner}/{repo}/codespaces",
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
                    codespace_list_params.CodespaceListParams,
                ),
            ),
            cast_to=CodespaceListResponse,
        )

    def check_permissions(
        self,
        repo: str,
        *,
        owner: str,
        devcontainer_path: str,
        ref: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceCheckPermissionsResponse:
        """
        Checks whether the permissions defined by a given devcontainer configuration
        have been accepted by the authenticated user.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          devcontainer_path: Path to the devcontainer.json configuration to use for the permission check.

          ref: The git reference that points to the location of the devcontainer configuration
              to use for the permission check. The value of `ref` will typically be a branch
              name (`heads/BRANCH_NAME`). For more information, see
              "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
              in the Git documentation.

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
            f"/repos/{owner}/{repo}/codespaces/permissions_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "devcontainer_path": devcontainer_path,
                        "ref": ref,
                    },
                    codespace_check_permissions_params.CodespaceCheckPermissionsParams,
                ),
            ),
            cast_to=CodespaceCheckPermissionsResponse,
        )

    def get_default_attributes(
        self,
        repo: str,
        *,
        owner: str,
        client_ip: str | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceGetDefaultAttributesResponse:
        """
        Gets the default attributes for codespaces created by the user with the
        repository.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          client_ip: An alternative IP for default location auto-detection, such as when proxying a
              request.

          ref: The branch or commit to check for a default devcontainer path. If not specified,
              the default branch will be checked.

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
            f"/repos/{owner}/{repo}/codespaces/new",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_ip": client_ip,
                        "ref": ref,
                    },
                    codespace_get_default_attributes_params.CodespaceGetDefaultAttributesParams,
                ),
            ),
            cast_to=CodespaceGetDefaultAttributesResponse,
        )

    def list_devcontainers(
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
    ) -> CodespaceListDevcontainersResponse:
        """
        Lists the devcontainer.json files associated with a specified repository and the
        authenticated user. These files specify launchpoint configurations for
        codespaces created within the repository.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

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
            f"/repos/{owner}/{repo}/codespaces/devcontainers",
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
                    codespace_list_devcontainers_params.CodespaceListDevcontainersParams,
                ),
            ),
            cast_to=CodespaceListDevcontainersResponse,
        )

    def list_machines(
        self,
        repo: str,
        *,
        owner: str,
        client_ip: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListMachinesResponse:
        """
        List the machine types available for a given repository based on its
        configuration.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          client_ip: IP for location auto-detection when proxying a request

          location: The location to check for available machines. Assigned by IP if not provided.

          ref: The branch or commit to check for prebuild availability and devcontainer
              restrictions.

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
            f"/repos/{owner}/{repo}/codespaces/machines",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client_ip": client_ip,
                        "location": location,
                        "ref": ref,
                    },
                    codespace_list_machines_params.CodespaceListMachinesParams,
                ),
            ),
            cast_to=CodespaceListMachinesResponse,
        )


class AsyncCodespacesResource(AsyncAPIResource):
    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCodespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodespacesResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        client_ip: str | NotGiven = NOT_GIVEN,
        devcontainer_path: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        geo: Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"] | NotGiven = NOT_GIVEN,
        idle_timeout_minutes: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        machine: str | NotGiven = NOT_GIVEN,
        multi_repo_permissions_opt_out: bool | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        retention_period_minutes: int | NotGiven = NOT_GIVEN,
        working_directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Creates a codespace owned by the authenticated user in the specified repository.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          client_ip: IP for location auto-detection when proxying a request

          devcontainer_path: Path to devcontainer.json config to use for this codespace

          display_name: Display name for this codespace

          geo: The geographic area for this codespace. If not specified, the value is assigned
              by IP. This property replaces `location`, which is closing down.

          idle_timeout_minutes: Time in minutes before codespace stops from inactivity

          location: The requested location for a new codespace. Best efforts are made to respect
              this upon creation. Assigned by IP if not provided.

          machine: Machine type to use for this codespace

          multi_repo_permissions_opt_out: Whether to authorize requested permissions from devcontainer.json

          ref: Git ref (typically a branch name) for this codespace

          retention_period_minutes: Duration in minutes after codespace has gone idle in which it will be deleted.
              Must be integer minutes between 0 and 43200 (30 days).

          working_directory: Working directory for this codespace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/codespaces",
            body=await async_maybe_transform(
                {
                    "client_ip": client_ip,
                    "devcontainer_path": devcontainer_path,
                    "display_name": display_name,
                    "geo": geo,
                    "idle_timeout_minutes": idle_timeout_minutes,
                    "location": location,
                    "machine": machine,
                    "multi_repo_permissions_opt_out": multi_repo_permissions_opt_out,
                    "ref": ref,
                    "retention_period_minutes": retention_period_minutes,
                    "working_directory": working_directory,
                },
                codespace_create_params.CodespaceCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    async def list(
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
    ) -> CodespaceListResponse:
        """
        Lists the codespaces associated to a specified repository and the authenticated
        user.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

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
            f"/repos/{owner}/{repo}/codespaces",
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
                    codespace_list_params.CodespaceListParams,
                ),
            ),
            cast_to=CodespaceListResponse,
        )

    async def check_permissions(
        self,
        repo: str,
        *,
        owner: str,
        devcontainer_path: str,
        ref: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceCheckPermissionsResponse:
        """
        Checks whether the permissions defined by a given devcontainer configuration
        have been accepted by the authenticated user.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          devcontainer_path: Path to the devcontainer.json configuration to use for the permission check.

          ref: The git reference that points to the location of the devcontainer configuration
              to use for the permission check. The value of `ref` will typically be a branch
              name (`heads/BRANCH_NAME`). For more information, see
              "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
              in the Git documentation.

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
            f"/repos/{owner}/{repo}/codespaces/permissions_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "devcontainer_path": devcontainer_path,
                        "ref": ref,
                    },
                    codespace_check_permissions_params.CodespaceCheckPermissionsParams,
                ),
            ),
            cast_to=CodespaceCheckPermissionsResponse,
        )

    async def get_default_attributes(
        self,
        repo: str,
        *,
        owner: str,
        client_ip: str | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceGetDefaultAttributesResponse:
        """
        Gets the default attributes for codespaces created by the user with the
        repository.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          client_ip: An alternative IP for default location auto-detection, such as when proxying a
              request.

          ref: The branch or commit to check for a default devcontainer path. If not specified,
              the default branch will be checked.

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
            f"/repos/{owner}/{repo}/codespaces/new",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_ip": client_ip,
                        "ref": ref,
                    },
                    codespace_get_default_attributes_params.CodespaceGetDefaultAttributesParams,
                ),
            ),
            cast_to=CodespaceGetDefaultAttributesResponse,
        )

    async def list_devcontainers(
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
    ) -> CodespaceListDevcontainersResponse:
        """
        Lists the devcontainer.json files associated with a specified repository and the
        authenticated user. These files specify launchpoint configurations for
        codespaces created within the repository.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

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
            f"/repos/{owner}/{repo}/codespaces/devcontainers",
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
                    codespace_list_devcontainers_params.CodespaceListDevcontainersParams,
                ),
            ),
            cast_to=CodespaceListDevcontainersResponse,
        )

    async def list_machines(
        self,
        repo: str,
        *,
        owner: str,
        client_ip: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListMachinesResponse:
        """
        List the machine types available for a given repository based on its
        configuration.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          client_ip: IP for location auto-detection when proxying a request

          location: The location to check for available machines. Assigned by IP if not provided.

          ref: The branch or commit to check for prebuild availability and devcontainer
              restrictions.

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
            f"/repos/{owner}/{repo}/codespaces/machines",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client_ip": client_ip,
                        "location": location,
                        "ref": ref,
                    },
                    codespace_list_machines_params.CodespaceListMachinesParams,
                ),
            ),
            cast_to=CodespaceListMachinesResponse,
        )


class CodespacesResourceWithRawResponse:
    def __init__(self, codespaces: CodespacesResource) -> None:
        self._codespaces = codespaces

        self.create = to_raw_response_wrapper(
            codespaces.create,
        )
        self.list = to_raw_response_wrapper(
            codespaces.list,
        )
        self.check_permissions = to_raw_response_wrapper(
            codespaces.check_permissions,
        )
        self.get_default_attributes = to_raw_response_wrapper(
            codespaces.get_default_attributes,
        )
        self.list_devcontainers = to_raw_response_wrapper(
            codespaces.list_devcontainers,
        )
        self.list_machines = to_raw_response_wrapper(
            codespaces.list_machines,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._codespaces.secrets)


class AsyncCodespacesResourceWithRawResponse:
    def __init__(self, codespaces: AsyncCodespacesResource) -> None:
        self._codespaces = codespaces

        self.create = async_to_raw_response_wrapper(
            codespaces.create,
        )
        self.list = async_to_raw_response_wrapper(
            codespaces.list,
        )
        self.check_permissions = async_to_raw_response_wrapper(
            codespaces.check_permissions,
        )
        self.get_default_attributes = async_to_raw_response_wrapper(
            codespaces.get_default_attributes,
        )
        self.list_devcontainers = async_to_raw_response_wrapper(
            codespaces.list_devcontainers,
        )
        self.list_machines = async_to_raw_response_wrapper(
            codespaces.list_machines,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._codespaces.secrets)


class CodespacesResourceWithStreamingResponse:
    def __init__(self, codespaces: CodespacesResource) -> None:
        self._codespaces = codespaces

        self.create = to_streamed_response_wrapper(
            codespaces.create,
        )
        self.list = to_streamed_response_wrapper(
            codespaces.list,
        )
        self.check_permissions = to_streamed_response_wrapper(
            codespaces.check_permissions,
        )
        self.get_default_attributes = to_streamed_response_wrapper(
            codespaces.get_default_attributes,
        )
        self.list_devcontainers = to_streamed_response_wrapper(
            codespaces.list_devcontainers,
        )
        self.list_machines = to_streamed_response_wrapper(
            codespaces.list_machines,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._codespaces.secrets)


class AsyncCodespacesResourceWithStreamingResponse:
    def __init__(self, codespaces: AsyncCodespacesResource) -> None:
        self._codespaces = codespaces

        self.create = async_to_streamed_response_wrapper(
            codespaces.create,
        )
        self.list = async_to_streamed_response_wrapper(
            codespaces.list,
        )
        self.check_permissions = async_to_streamed_response_wrapper(
            codespaces.check_permissions,
        )
        self.get_default_attributes = async_to_streamed_response_wrapper(
            codespaces.get_default_attributes,
        )
        self.list_devcontainers = async_to_streamed_response_wrapper(
            codespaces.list_devcontainers,
        )
        self.list_machines = async_to_streamed_response_wrapper(
            codespaces.list_machines,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._codespaces.secrets)
