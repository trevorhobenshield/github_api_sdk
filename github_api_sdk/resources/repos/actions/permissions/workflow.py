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
from .....types.orgs.actions.permissions import DefaultPermissions
from .....types.orgs.actions.permissions.default_permissions import DefaultPermissions
from .....types.orgs.actions.permissions.get_default_permissions import GetDefaultPermissions
from .....types.repos.actions.permissions import workflow_update_params

__all__ = ["WorkflowResource", "AsyncWorkflowResource"]


class WorkflowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return WorkflowResourceWithStreamingResponse(self)

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
    ) -> GetDefaultPermissions:
        """
        Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running
        workflows in a repository, as well as if GitHub Actions can submit approving
        pull request reviews. For more information, see
        "[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)."

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
            f"/repos/{owner}/{repo}/actions/permissions/workflow",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GetDefaultPermissions,
        )

    def update(
        self,
        repo: str,
        *,
        owner: str,
        can_approve_pull_request_reviews: bool | NotGiven = NOT_GIVEN,
        default_workflow_permissions: DefaultPermissions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running
        workflows in a repository, and sets if GitHub Actions can submit approving pull
        request reviews. For more information, see
        "[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)."

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          can_approve_pull_request_reviews: Whether GitHub Actions can approve pull requests. Enabling this can be a
              security risk.

          default_workflow_permissions: The default workflow permissions granted to the GITHUB_TOKEN when running
              workflows.

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
            f"/repos/{owner}/{repo}/actions/permissions/workflow",
            body=maybe_transform(
                {
                    "can_approve_pull_request_reviews": can_approve_pull_request_reviews,
                    "default_workflow_permissions": default_workflow_permissions,
                },
                workflow_update_params.WorkflowUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncWorkflowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncWorkflowResourceWithStreamingResponse(self)

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
    ) -> GetDefaultPermissions:
        """
        Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running
        workflows in a repository, as well as if GitHub Actions can submit approving
        pull request reviews. For more information, see
        "[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)."

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
            f"/repos/{owner}/{repo}/actions/permissions/workflow",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GetDefaultPermissions,
        )

    async def update(
        self,
        repo: str,
        *,
        owner: str,
        can_approve_pull_request_reviews: bool | NotGiven = NOT_GIVEN,
        default_workflow_permissions: DefaultPermissions | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Sets the default workflow permissions granted to the `GITHUB_TOKEN` when running
        workflows in a repository, and sets if GitHub Actions can submit approving pull
        request reviews. For more information, see
        "[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)."

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          can_approve_pull_request_reviews: Whether GitHub Actions can approve pull requests. Enabling this can be a
              security risk.

          default_workflow_permissions: The default workflow permissions granted to the GITHUB_TOKEN when running
              workflows.

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
            f"/repos/{owner}/{repo}/actions/permissions/workflow",
            body=await async_maybe_transform(
                {
                    "can_approve_pull_request_reviews": can_approve_pull_request_reviews,
                    "default_workflow_permissions": default_workflow_permissions,
                },
                workflow_update_params.WorkflowUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class WorkflowResourceWithRawResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.retrieve = to_raw_response_wrapper(
            workflow.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workflow.update,
        )


class AsyncWorkflowResourceWithRawResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.retrieve = async_to_raw_response_wrapper(
            workflow.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workflow.update,
        )


class WorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.retrieve = to_streamed_response_wrapper(
            workflow.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workflow.update,
        )


class AsyncWorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.retrieve = async_to_streamed_response_wrapper(
            workflow.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workflow.update,
        )
