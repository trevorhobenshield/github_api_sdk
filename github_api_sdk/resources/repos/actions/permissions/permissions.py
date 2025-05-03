from __future__ import annotations

import httpx

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
from .....types.orgs.actions import AllowedActions
from .....types.orgs.actions.allowed_actions import AllowedActions
from .....types.repos.actions import permission_update_params
from .....types.repos.actions.permission_retrieve_response import PermissionRetrieveResponse
from .access import (
    AccessResource,
    AccessResourceWithRawResponse,
    AccessResourceWithStreamingResponse,
    AsyncAccessResource,
    AsyncAccessResourceWithRawResponse,
    AsyncAccessResourceWithStreamingResponse,
)
from .selected_actions import (
    AsyncSelectedActionsResource,
    AsyncSelectedActionsResourceWithRawResponse,
    AsyncSelectedActionsResourceWithStreamingResponse,
    SelectedActionsResource,
    SelectedActionsResourceWithRawResponse,
    SelectedActionsResourceWithStreamingResponse,
)
from .workflow import (
    AsyncWorkflowResource,
    AsyncWorkflowResourceWithRawResponse,
    AsyncWorkflowResourceWithStreamingResponse,
    WorkflowResource,
    WorkflowResourceWithRawResponse,
    WorkflowResourceWithStreamingResponse,
)

__all__ = ["PermissionsResource", "AsyncPermissionsResource"]


class PermissionsResource(SyncAPIResource):
    @cached_property
    def access(self) -> AccessResource:
        return AccessResource(self._client)

    @cached_property
    def selected_actions(self) -> SelectedActionsResource:
        return SelectedActionsResource(self._client)

    @cached_property
    def workflow(self) -> WorkflowResource:
        return WorkflowResource(self._client)

    @cached_property
    def with_raw_response(self) -> PermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PermissionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PermissionRetrieveResponse:
        """
        Gets the GitHub Actions permissions policy for a repository, including whether
        GitHub Actions is enabled and the actions and reusable workflows allowed to run
        in the repository.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
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
            f"/repos/{owner}/{repo}/actions/permissions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PermissionRetrieveResponse,
        )

    def update(
        self,
        repo: str,
        *,
        owner: str,
        enabled: bool,
        allowed_actions: AllowedActions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Sets the GitHub Actions permissions policy for enabling GitHub Actions and
        allowed actions and reusable workflows in the repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          enabled: Whether GitHub Actions is enabled on the repository.

          allowed_actions: The permissions policy that controls the actions and reusable workflows that are
              allowed to run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/repos/{owner}/{repo}/actions/permissions",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "allowed_actions": allowed_actions,
                },
                permission_update_params.PermissionUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncPermissionsResource(AsyncAPIResource):
    @cached_property
    def access(self) -> AsyncAccessResource:
        return AsyncAccessResource(self._client)

    @cached_property
    def selected_actions(self) -> AsyncSelectedActionsResource:
        return AsyncSelectedActionsResource(self._client)

    @cached_property
    def workflow(self) -> AsyncWorkflowResource:
        return AsyncWorkflowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPermissionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPermissionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPermissionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPermissionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PermissionRetrieveResponse:
        """
        Gets the GitHub Actions permissions policy for a repository, including whether
        GitHub Actions is enabled and the actions and reusable workflows allowed to run
        in the repository.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
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
            f"/repos/{owner}/{repo}/actions/permissions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PermissionRetrieveResponse,
        )

    async def update(
        self,
        repo: str,
        *,
        owner: str,
        enabled: bool,
        allowed_actions: AllowedActions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Sets the GitHub Actions permissions policy for enabling GitHub Actions and
        allowed actions and reusable workflows in the repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          enabled: Whether GitHub Actions is enabled on the repository.

          allowed_actions: The permissions policy that controls the actions and reusable workflows that are
              allowed to run.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/repos/{owner}/{repo}/actions/permissions",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "allowed_actions": allowed_actions,
                },
                permission_update_params.PermissionUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class PermissionsResourceWithRawResponse:
    def __init__(self, permissions: PermissionsResource) -> None:
        self._permissions = permissions

        self.retrieve = to_raw_response_wrapper(
            permissions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            permissions.update,
        )

    @cached_property
    def access(self) -> AccessResourceWithRawResponse:
        return AccessResourceWithRawResponse(self._permissions.access)

    @cached_property
    def selected_actions(self) -> SelectedActionsResourceWithRawResponse:
        return SelectedActionsResourceWithRawResponse(self._permissions.selected_actions)

    @cached_property
    def workflow(self) -> WorkflowResourceWithRawResponse:
        return WorkflowResourceWithRawResponse(self._permissions.workflow)


class AsyncPermissionsResourceWithRawResponse:
    def __init__(self, permissions: AsyncPermissionsResource) -> None:
        self._permissions = permissions

        self.retrieve = async_to_raw_response_wrapper(
            permissions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            permissions.update,
        )

    @cached_property
    def access(self) -> AsyncAccessResourceWithRawResponse:
        return AsyncAccessResourceWithRawResponse(self._permissions.access)

    @cached_property
    def selected_actions(self) -> AsyncSelectedActionsResourceWithRawResponse:
        return AsyncSelectedActionsResourceWithRawResponse(self._permissions.selected_actions)

    @cached_property
    def workflow(self) -> AsyncWorkflowResourceWithRawResponse:
        return AsyncWorkflowResourceWithRawResponse(self._permissions.workflow)


class PermissionsResourceWithStreamingResponse:
    def __init__(self, permissions: PermissionsResource) -> None:
        self._permissions = permissions

        self.retrieve = to_streamed_response_wrapper(
            permissions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            permissions.update,
        )

    @cached_property
    def access(self) -> AccessResourceWithStreamingResponse:
        return AccessResourceWithStreamingResponse(self._permissions.access)

    @cached_property
    def selected_actions(self) -> SelectedActionsResourceWithStreamingResponse:
        return SelectedActionsResourceWithStreamingResponse(self._permissions.selected_actions)

    @cached_property
    def workflow(self) -> WorkflowResourceWithStreamingResponse:
        return WorkflowResourceWithStreamingResponse(self._permissions.workflow)


class AsyncPermissionsResourceWithStreamingResponse:
    def __init__(self, permissions: AsyncPermissionsResource) -> None:
        self._permissions = permissions

        self.retrieve = async_to_streamed_response_wrapper(
            permissions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            permissions.update,
        )

    @cached_property
    def access(self) -> AsyncAccessResourceWithStreamingResponse:
        return AsyncAccessResourceWithStreamingResponse(self._permissions.access)

    @cached_property
    def selected_actions(self) -> AsyncSelectedActionsResourceWithStreamingResponse:
        return AsyncSelectedActionsResourceWithStreamingResponse(self._permissions.selected_actions)

    @cached_property
    def workflow(self) -> AsyncWorkflowResourceWithStreamingResponse:
        return AsyncWorkflowResourceWithStreamingResponse(self._permissions.workflow)
