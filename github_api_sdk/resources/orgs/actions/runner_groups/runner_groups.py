from __future__ import annotations

import builtins
from typing import Iterable, List, Optional

import httpx
from typing_extensions import Literal

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs.actions import (
    runner_group_create_params,
    runner_group_list_hosted_runners_params,
    runner_group_list_params,
    runner_group_update_params,
)
from .....types.orgs.actions.groups import Groups
from .....types.orgs.actions.runner_group_list_hosted_runners_response import RunnerGroupListHostedRunnersResponse
from .....types.orgs.actions.runner_group_list_response import RunnerGroupListResponse
from .repositories import (
    AsyncRepositoriesResource,
    AsyncRepositoriesResourceWithRawResponse,
    AsyncRepositoriesResourceWithStreamingResponse,
    RepositoriesResource,
    RepositoriesResourceWithRawResponse,
    RepositoriesResourceWithStreamingResponse,
)
from .runners import (
    AsyncRunnersResource,
    AsyncRunnersResourceWithRawResponse,
    AsyncRunnersResourceWithStreamingResponse,
    RunnersResource,
    RunnersResourceWithRawResponse,
    RunnersResourceWithStreamingResponse,
)

__all__ = ["RunnerGroupsResource", "AsyncRunnerGroupsResource"]


class RunnerGroupsResource(SyncAPIResource):
    @cached_property
    def repositories(self) -> RepositoriesResource:
        return RepositoriesResource(self._client)

    @cached_property
    def runners(self) -> RunnersResource:
        return RunnersResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunnerGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunnerGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunnerGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RunnerGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        name: str,
        allows_public_repositories: bool | NotGiven = NOT_GIVEN,
        network_configuration_id: str | NotGiven = NOT_GIVEN,
        restricted_to_workflows: bool | NotGiven = NOT_GIVEN,
        runners: Iterable[int] | NotGiven = NOT_GIVEN,
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        selected_workflows: builtins.list[str] | NotGiven = NOT_GIVEN,
        visibility: Literal["selected", "all", "private"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Groups:
        """
        Creates a new self-hosted runner group for an organization.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint.

        Args:
          name: Name of the runner group.

          allows_public_repositories: Whether the runner group can be used by `public` repositories.

          network_configuration_id: The identifier of a hosted compute network configuration.

          restricted_to_workflows: If `true`, the runner group will be restricted to running only the workflows
              specified in the `selected_workflows` array.

          runners: List of runner IDs to add to the runner group.

          selected_repository_ids: List of repository IDs that can access the runner group.

          selected_workflows: List of workflows the runner group should be allowed to run. This setting will
              be ignored unless `restricted_to_workflows` is set to `true`.

          visibility: Visibility of a runner group. You can select all repositories, select individual
              repositories, or limit access to private repositories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/actions/runner-groups",
            body=maybe_transform(
                {
                    "name": name,
                    "allows_public_repositories": allows_public_repositories,
                    "network_configuration_id": network_configuration_id,
                    "restricted_to_workflows": restricted_to_workflows,
                    "runners": runners,
                    "selected_repository_ids": selected_repository_ids,
                    "selected_workflows": selected_workflows,
                    "visibility": visibility,
                },
                runner_group_create_params.RunnerGroupCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Groups,
        )

    def retrieve(
        self,
        runner_group_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Groups:
        """
        Gets a specific self-hosted runner group for an organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/runner-groups/{runner_group_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Groups,
        )

    def update(
        self,
        runner_group_id: int,
        *,
        org: str,
        name: str,
        allows_public_repositories: bool | NotGiven = NOT_GIVEN,
        network_configuration_id: str | None | NotGiven = NOT_GIVEN,
        restricted_to_workflows: bool | NotGiven = NOT_GIVEN,
        selected_workflows: builtins.list[str] | NotGiven = NOT_GIVEN,
        visibility: Literal["selected", "all", "private"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Groups:
        """
        Updates the `name` and `visibility` of a self-hosted runner group in an
        organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          name: Name of the runner group.

          allows_public_repositories: Whether the runner group can be used by `public` repositories.

          network_configuration_id: The identifier of a hosted compute network configuration.

          restricted_to_workflows: If `true`, the runner group will be restricted to running only the workflows
              specified in the `selected_workflows` array.

          selected_workflows: List of workflows the runner group should be allowed to run. This setting will
              be ignored unless `restricted_to_workflows` is set to `true`.

          visibility: Visibility of a runner group. You can select all repositories, select individual
              repositories, or all private repositories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._patch(
            f"/orgs/{org}/actions/runner-groups/{runner_group_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "allows_public_repositories": allows_public_repositories,
                    "network_configuration_id": network_configuration_id,
                    "restricted_to_workflows": restricted_to_workflows,
                    "selected_workflows": selected_workflows,
                    "visibility": visibility,
                },
                runner_group_update_params.RunnerGroupUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Groups,
        )

    def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        visible_to_repository: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerGroupListResponse:
        """
        Lists all self-hosted runner groups configured in an organization and inherited
        from an enterprise.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          visible_to_repository: Only return runner groups that are allowed to be used by this repository.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/runner-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "visible_to_repository": visible_to_repository,
                    },
                    runner_group_list_params.RunnerGroupListParams,
                ),
            ),
            cast_to=RunnerGroupListResponse,
        )

    def delete(
        self,
        runner_group_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a self-hosted runner group for an organization.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/actions/runner-groups/{runner_group_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_hosted_runners(
        self,
        runner_group_id: int,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerGroupListHostedRunnersResponse:
        """
        Lists the GitHub-hosted runners in an organization group.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/runner-groups/{runner_group_id}/hosted-runners",
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
                    runner_group_list_hosted_runners_params.RunnerGroupListHostedRunnersParams,
                ),
            ),
            cast_to=RunnerGroupListHostedRunnersResponse,
        )


class AsyncRunnerGroupsResource(AsyncAPIResource):
    @cached_property
    def repositories(self) -> AsyncRepositoriesResource:
        return AsyncRepositoriesResource(self._client)

    @cached_property
    def runners(self) -> AsyncRunnersResource:
        return AsyncRunnersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunnerGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunnerGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunnerGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRunnerGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        name: str,
        allows_public_repositories: bool | NotGiven = NOT_GIVEN,
        network_configuration_id: str | NotGiven = NOT_GIVEN,
        restricted_to_workflows: bool | NotGiven = NOT_GIVEN,
        runners: Iterable[int] | NotGiven = NOT_GIVEN,
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        selected_workflows: builtins.list[str] | NotGiven = NOT_GIVEN,
        visibility: Literal["selected", "all", "private"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Groups:
        """
        Creates a new self-hosted runner group for an organization.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint.

        Args:
          name: Name of the runner group.

          allows_public_repositories: Whether the runner group can be used by `public` repositories.

          network_configuration_id: The identifier of a hosted compute network configuration.

          restricted_to_workflows: If `true`, the runner group will be restricted to running only the workflows
              specified in the `selected_workflows` array.

          runners: List of runner IDs to add to the runner group.

          selected_repository_ids: List of repository IDs that can access the runner group.

          selected_workflows: List of workflows the runner group should be allowed to run. This setting will
              be ignored unless `restricted_to_workflows` is set to `true`.

          visibility: Visibility of a runner group. You can select all repositories, select individual
              repositories, or limit access to private repositories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/actions/runner-groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "allows_public_repositories": allows_public_repositories,
                    "network_configuration_id": network_configuration_id,
                    "restricted_to_workflows": restricted_to_workflows,
                    "runners": runners,
                    "selected_repository_ids": selected_repository_ids,
                    "selected_workflows": selected_workflows,
                    "visibility": visibility,
                },
                runner_group_create_params.RunnerGroupCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Groups,
        )

    async def retrieve(
        self,
        runner_group_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Groups:
        """
        Gets a specific self-hosted runner group for an organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/runner-groups/{runner_group_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Groups,
        )

    async def update(
        self,
        runner_group_id: int,
        *,
        org: str,
        name: str,
        allows_public_repositories: bool | NotGiven = NOT_GIVEN,
        network_configuration_id: str | None | NotGiven = NOT_GIVEN,
        restricted_to_workflows: bool | NotGiven = NOT_GIVEN,
        selected_workflows: builtins.list[str] | NotGiven = NOT_GIVEN,
        visibility: Literal["selected", "all", "private"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Groups:
        """
        Updates the `name` and `visibility` of a self-hosted runner group in an
        organization.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          name: Name of the runner group.

          allows_public_repositories: Whether the runner group can be used by `public` repositories.

          network_configuration_id: The identifier of a hosted compute network configuration.

          restricted_to_workflows: If `true`, the runner group will be restricted to running only the workflows
              specified in the `selected_workflows` array.

          selected_workflows: List of workflows the runner group should be allowed to run. This setting will
              be ignored unless `restricted_to_workflows` is set to `true`.

          visibility: Visibility of a runner group. You can select all repositories, select individual
              repositories, or all private repositories.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._patch(
            f"/orgs/{org}/actions/runner-groups/{runner_group_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "allows_public_repositories": allows_public_repositories,
                    "network_configuration_id": network_configuration_id,
                    "restricted_to_workflows": restricted_to_workflows,
                    "selected_workflows": selected_workflows,
                    "visibility": visibility,
                },
                runner_group_update_params.RunnerGroupUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Groups,
        )

    async def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        visible_to_repository: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerGroupListResponse:
        """
        Lists all self-hosted runner groups configured in an organization and inherited
        from an enterprise.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          visible_to_repository: Only return runner groups that are allowed to be used by this repository.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/runner-groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "visible_to_repository": visible_to_repository,
                    },
                    runner_group_list_params.RunnerGroupListParams,
                ),
            ),
            cast_to=RunnerGroupListResponse,
        )

    async def delete(
        self,
        runner_group_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a self-hosted runner group for an organization.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/actions/runner-groups/{runner_group_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_hosted_runners(
        self,
        runner_group_id: int,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerGroupListHostedRunnersResponse:
        """
        Lists the GitHub-hosted runners in an organization group.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/runner-groups/{runner_group_id}/hosted-runners",
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
                    runner_group_list_hosted_runners_params.RunnerGroupListHostedRunnersParams,
                ),
            ),
            cast_to=RunnerGroupListHostedRunnersResponse,
        )


class RunnerGroupsResourceWithRawResponse:
    def __init__(self, runner_groups: RunnerGroupsResource) -> None:
        self._runner_groups = runner_groups

        self.create = to_raw_response_wrapper(
            runner_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            runner_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            runner_groups.update,
        )
        self.list = to_raw_response_wrapper(
            runner_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            runner_groups.delete,
        )
        self.list_hosted_runners = to_raw_response_wrapper(
            runner_groups.list_hosted_runners,
        )

    @cached_property
    def repositories(self) -> RepositoriesResourceWithRawResponse:
        return RepositoriesResourceWithRawResponse(self._runner_groups.repositories)

    @cached_property
    def runners(self) -> RunnersResourceWithRawResponse:
        return RunnersResourceWithRawResponse(self._runner_groups.runners)


class AsyncRunnerGroupsResourceWithRawResponse:
    def __init__(self, runner_groups: AsyncRunnerGroupsResource) -> None:
        self._runner_groups = runner_groups

        self.create = async_to_raw_response_wrapper(
            runner_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            runner_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            runner_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            runner_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            runner_groups.delete,
        )
        self.list_hosted_runners = async_to_raw_response_wrapper(
            runner_groups.list_hosted_runners,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithRawResponse:
        return AsyncRepositoriesResourceWithRawResponse(self._runner_groups.repositories)

    @cached_property
    def runners(self) -> AsyncRunnersResourceWithRawResponse:
        return AsyncRunnersResourceWithRawResponse(self._runner_groups.runners)


class RunnerGroupsResourceWithStreamingResponse:
    def __init__(self, runner_groups: RunnerGroupsResource) -> None:
        self._runner_groups = runner_groups

        self.create = to_streamed_response_wrapper(
            runner_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            runner_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            runner_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            runner_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            runner_groups.delete,
        )
        self.list_hosted_runners = to_streamed_response_wrapper(
            runner_groups.list_hosted_runners,
        )

    @cached_property
    def repositories(self) -> RepositoriesResourceWithStreamingResponse:
        return RepositoriesResourceWithStreamingResponse(self._runner_groups.repositories)

    @cached_property
    def runners(self) -> RunnersResourceWithStreamingResponse:
        return RunnersResourceWithStreamingResponse(self._runner_groups.runners)


class AsyncRunnerGroupsResourceWithStreamingResponse:
    def __init__(self, runner_groups: AsyncRunnerGroupsResource) -> None:
        self._runner_groups = runner_groups

        self.create = async_to_streamed_response_wrapper(
            runner_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            runner_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            runner_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            runner_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            runner_groups.delete,
        )
        self.list_hosted_runners = async_to_streamed_response_wrapper(
            runner_groups.list_hosted_runners,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self._runner_groups.repositories)

    @cached_property
    def runners(self) -> AsyncRunnersResourceWithStreamingResponse:
        return AsyncRunnersResourceWithStreamingResponse(self._runner_groups.runners)
