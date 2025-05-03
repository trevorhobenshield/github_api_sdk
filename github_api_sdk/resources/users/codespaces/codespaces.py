from __future__ import annotations

import builtins
from typing import List

import httpx
from typing_extensions import Literal, overload

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
    required_args,
)
from ....types.orgs.members.codespace import Codespace
from ....types.users import (
    codespace_create_params,
    codespace_list_params,
    codespace_publish_params,
    codespace_update_params,
)
from ....types.users.codespace_list_machines_response import CodespaceListMachinesResponse
from ....types.users.codespace_list_response import CodespaceListResponse
from ....types.users.codespace_publish_response import CodespacePublishResponse
from .exports import (
    AsyncExportsResource,
    AsyncExportsResourceWithRawResponse,
    AsyncExportsResourceWithStreamingResponse,
    ExportsResource,
    ExportsResourceWithRawResponse,
    ExportsResourceWithStreamingResponse,
)
from .secrets.secrets import (
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
    def exports(self) -> ExportsResource:
        return ExportsResource(self._client)

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

    @overload
    def create(
        self,
        *,
        repository_id: int,
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
        Creates a new codespace, owned by the authenticated user.

        This endpoint requires either a `repository_id` OR a `pull_request` but not
        both.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          repository_id: Repository id for this codespace

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
        ...

    @overload
    def create(
        self,
        *,
        pull_request: codespace_create_params.Variant1PullRequest,
        devcontainer_path: str | NotGiven = NOT_GIVEN,
        geo: Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"] | NotGiven = NOT_GIVEN,
        idle_timeout_minutes: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        machine: str | NotGiven = NOT_GIVEN,
        working_directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Creates a new codespace, owned by the authenticated user.

        This endpoint requires either a `repository_id` OR a `pull_request` but not
        both.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          pull_request: Pull request number for this codespace

          devcontainer_path: Path to devcontainer.json config to use for this codespace

          geo: The geographic area for this codespace. If not specified, the value is assigned
              by IP. This property replaces `location`, which is closing down.

          idle_timeout_minutes: Time in minutes before codespace stops from inactivity

          location: The requested location for a new codespace. Best efforts are made to respect
              this upon creation. Assigned by IP if not provided.

          machine: Machine type to use for this codespace

          working_directory: Working directory for this codespace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["repository_id"], ["pull_request"])
    def create(
        self,
        *,
        repository_id: int | NotGiven = NOT_GIVEN,
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
        pull_request: codespace_create_params.Variant1PullRequest | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        return self._post(
            "/user/codespaces",
            body=maybe_transform(
                {
                    "repository_id": repository_id,
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
                    "pull_request": pull_request,
                },
                codespace_create_params.CodespaceCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    def retrieve(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Gets information about a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._get(
            f"/user/codespaces/{codespace_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    def update(
        self,
        codespace_name: str,
        *,
        display_name: str | NotGiven = NOT_GIVEN,
        machine: str | NotGiven = NOT_GIVEN,
        recent_folders: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """Updates a codespace owned by the authenticated user.

        Currently only the
        codespace's machine type and recent folders can be modified using this endpoint.

        If you specify a new machine type it will be applied the next time your
        codespace is started.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          display_name: Display name for this codespace

          machine: A valid machine to transition this codespace to.

          recent_folders: Recently opened folders inside the codespace. It is currently used by the
              clients to determine the folder path to load the codespace in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._patch(
            f"/user/codespaces/{codespace_name}",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "machine": machine,
                    "recent_folders": recent_folders,
                },
                codespace_update_params.CodespaceUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        repository_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListResponse:
        """
        Lists the authenticated user's codespaces.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          repository_id: ID of the Repository to filter on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/codespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "repository_id": repository_id,
                    },
                    codespace_list_params.CodespaceListParams,
                ),
            ),
            cast_to=CodespaceListResponse,
        )

    def delete(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._delete(
            f"/user/codespaces/{codespace_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def list_machines(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListMachinesResponse:
        """
        List the machine types a codespace can transition to use.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._get(
            f"/user/codespaces/{codespace_name}/machines",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespaceListMachinesResponse,
        )

    def publish(
        self,
        codespace_name: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespacePublishResponse:
        """
        Publishes an unpublished codespace, creating a new repository and assigning it
        to the codespace.

        The codespace's token is granted write permissions to the repository, allowing
        the user to push their changes.

        This will fail for a codespace that is already published, meaning it has an
        associated repository.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          name: A name for the new repository.

          private: Whether the new repository should be private.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._post(
            f"/user/codespaces/{codespace_name}/publish",
            body=maybe_transform(
                {
                    "name": name,
                    "private": private,
                },
                codespace_publish_params.CodespacePublishParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespacePublishResponse,
        )

    def start(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Starts a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._post(
            f"/user/codespaces/{codespace_name}/start",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    def stop(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Stops a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return self._post(
            f"/user/codespaces/{codespace_name}/stop",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )


class AsyncCodespacesResource(AsyncAPIResource):
    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def exports(self) -> AsyncExportsResource:
        return AsyncExportsResource(self._client)

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

    @overload
    async def create(
        self,
        *,
        repository_id: int,
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
        Creates a new codespace, owned by the authenticated user.

        This endpoint requires either a `repository_id` OR a `pull_request` but not
        both.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          repository_id: Repository id for this codespace

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
        ...

    @overload
    async def create(
        self,
        *,
        pull_request: codespace_create_params.Variant1PullRequest,
        devcontainer_path: str | NotGiven = NOT_GIVEN,
        geo: Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"] | NotGiven = NOT_GIVEN,
        idle_timeout_minutes: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        machine: str | NotGiven = NOT_GIVEN,
        working_directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Creates a new codespace, owned by the authenticated user.

        This endpoint requires either a `repository_id` OR a `pull_request` but not
        both.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          pull_request: Pull request number for this codespace

          devcontainer_path: Path to devcontainer.json config to use for this codespace

          geo: The geographic area for this codespace. If not specified, the value is assigned
              by IP. This property replaces `location`, which is closing down.

          idle_timeout_minutes: Time in minutes before codespace stops from inactivity

          location: The requested location for a new codespace. Best efforts are made to respect
              this upon creation. Assigned by IP if not provided.

          machine: Machine type to use for this codespace

          working_directory: Working directory for this codespace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["repository_id"], ["pull_request"])
    async def create(
        self,
        *,
        repository_id: int | NotGiven = NOT_GIVEN,
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
        pull_request: codespace_create_params.Variant1PullRequest | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        return await self._post(
            "/user/codespaces",
            body=await async_maybe_transform(
                {
                    "repository_id": repository_id,
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
                    "pull_request": pull_request,
                },
                codespace_create_params.CodespaceCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    async def retrieve(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Gets information about a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._get(
            f"/user/codespaces/{codespace_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    async def update(
        self,
        codespace_name: str,
        *,
        display_name: str | NotGiven = NOT_GIVEN,
        machine: str | NotGiven = NOT_GIVEN,
        recent_folders: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """Updates a codespace owned by the authenticated user.

        Currently only the
        codespace's machine type and recent folders can be modified using this endpoint.

        If you specify a new machine type it will be applied the next time your
        codespace is started.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          display_name: Display name for this codespace

          machine: A valid machine to transition this codespace to.

          recent_folders: Recently opened folders inside the codespace. It is currently used by the
              clients to determine the folder path to load the codespace in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._patch(
            f"/user/codespaces/{codespace_name}",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "machine": machine,
                    "recent_folders": recent_folders,
                },
                codespace_update_params.CodespaceUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        repository_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListResponse:
        """
        Lists the authenticated user's codespaces.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          repository_id: ID of the Repository to filter on

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/codespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "repository_id": repository_id,
                    },
                    codespace_list_params.CodespaceListParams,
                ),
            ),
            cast_to=CodespaceListResponse,
        )

    async def delete(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._delete(
            f"/user/codespaces/{codespace_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def list_machines(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceListMachinesResponse:
        """
        List the machine types a codespace can transition to use.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._get(
            f"/user/codespaces/{codespace_name}/machines",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespaceListMachinesResponse,
        )

    async def publish(
        self,
        codespace_name: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespacePublishResponse:
        """
        Publishes an unpublished codespace, creating a new repository and assigning it
        to the codespace.

        The codespace's token is granted write permissions to the repository, allowing
        the user to push their changes.

        This will fail for a codespace that is already published, meaning it has an
        associated repository.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          name: A name for the new repository.

          private: Whether the new repository should be private.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._post(
            f"/user/codespaces/{codespace_name}/publish",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "private": private,
                },
                codespace_publish_params.CodespacePublishParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespacePublishResponse,
        )

    async def start(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Starts a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._post(
            f"/user/codespaces/{codespace_name}/start",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    async def stop(
        self,
        codespace_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Stops a user's codespace.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not codespace_name:
            raise ValueError(f"Expected a non-empty value for `codespace_name` but received {codespace_name!r}")
        return await self._post(
            f"/user/codespaces/{codespace_name}/stop",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )


class CodespacesResourceWithRawResponse:
    def __init__(self, codespaces: CodespacesResource) -> None:
        self._codespaces = codespaces

        self.create = to_raw_response_wrapper(
            codespaces.create,
        )
        self.retrieve = to_raw_response_wrapper(
            codespaces.retrieve,
        )
        self.update = to_raw_response_wrapper(
            codespaces.update,
        )
        self.list = to_raw_response_wrapper(
            codespaces.list,
        )
        self.delete = to_raw_response_wrapper(
            codespaces.delete,
        )
        self.list_machines = to_raw_response_wrapper(
            codespaces.list_machines,
        )
        self.publish = to_raw_response_wrapper(
            codespaces.publish,
        )
        self.start = to_raw_response_wrapper(
            codespaces.start,
        )
        self.stop = to_raw_response_wrapper(
            codespaces.stop,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._codespaces.secrets)

    @cached_property
    def exports(self) -> ExportsResourceWithRawResponse:
        return ExportsResourceWithRawResponse(self._codespaces.exports)


class AsyncCodespacesResourceWithRawResponse:
    def __init__(self, codespaces: AsyncCodespacesResource) -> None:
        self._codespaces = codespaces

        self.create = async_to_raw_response_wrapper(
            codespaces.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            codespaces.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            codespaces.update,
        )
        self.list = async_to_raw_response_wrapper(
            codespaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            codespaces.delete,
        )
        self.list_machines = async_to_raw_response_wrapper(
            codespaces.list_machines,
        )
        self.publish = async_to_raw_response_wrapper(
            codespaces.publish,
        )
        self.start = async_to_raw_response_wrapper(
            codespaces.start,
        )
        self.stop = async_to_raw_response_wrapper(
            codespaces.stop,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._codespaces.secrets)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithRawResponse:
        return AsyncExportsResourceWithRawResponse(self._codespaces.exports)


class CodespacesResourceWithStreamingResponse:
    def __init__(self, codespaces: CodespacesResource) -> None:
        self._codespaces = codespaces

        self.create = to_streamed_response_wrapper(
            codespaces.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            codespaces.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            codespaces.update,
        )
        self.list = to_streamed_response_wrapper(
            codespaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            codespaces.delete,
        )
        self.list_machines = to_streamed_response_wrapper(
            codespaces.list_machines,
        )
        self.publish = to_streamed_response_wrapper(
            codespaces.publish,
        )
        self.start = to_streamed_response_wrapper(
            codespaces.start,
        )
        self.stop = to_streamed_response_wrapper(
            codespaces.stop,
        )

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._codespaces.secrets)

    @cached_property
    def exports(self) -> ExportsResourceWithStreamingResponse:
        return ExportsResourceWithStreamingResponse(self._codespaces.exports)


class AsyncCodespacesResourceWithStreamingResponse:
    def __init__(self, codespaces: AsyncCodespacesResource) -> None:
        self._codespaces = codespaces

        self.create = async_to_streamed_response_wrapper(
            codespaces.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            codespaces.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            codespaces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            codespaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            codespaces.delete,
        )
        self.list_machines = async_to_streamed_response_wrapper(
            codespaces.list_machines,
        )
        self.publish = async_to_streamed_response_wrapper(
            codespaces.publish,
        )
        self.start = async_to_streamed_response_wrapper(
            codespaces.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            codespaces.stop,
        )

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._codespaces.secrets)

    @cached_property
    def exports(self) -> AsyncExportsResourceWithStreamingResponse:
        return AsyncExportsResourceWithStreamingResponse(self._codespaces.exports)
