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
from .....types.orgs.actions.permissions import DefaultPermissions, workflow_set_params
from .....types.orgs.actions.permissions.default_permissions import DefaultPermissions
from .....types.orgs.actions.permissions.get_default_permissions import GetDefaultPermissions

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

    def get(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetDefaultPermissions:
        """
        Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running
        workflows in an organization, as well as whether GitHub Actions can submit
        approving pull request reviews. For more information, see
        "[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)."

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
        return self._get(
            f"/orgs/{org}/actions/permissions/workflow",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GetDefaultPermissions,
        )

    def set(
        self,
        org: str,
        *,
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
        workflows in an organization, and sets if GitHub Actions can submit approving
        pull request reviews. For more information, see
        "[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/orgs/{org}/actions/permissions/workflow",
            body=maybe_transform(
                {
                    "can_approve_pull_request_reviews": can_approve_pull_request_reviews,
                    "default_workflow_permissions": default_workflow_permissions,
                },
                workflow_set_params.WorkflowSetParams,
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

    async def get(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetDefaultPermissions:
        """
        Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running
        workflows in an organization, as well as whether GitHub Actions can submit
        approving pull request reviews. For more information, see
        "[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)."

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
        return await self._get(
            f"/orgs/{org}/actions/permissions/workflow",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GetDefaultPermissions,
        )

    async def set(
        self,
        org: str,
        *,
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
        workflows in an organization, and sets if GitHub Actions can submit approving
        pull request reviews. For more information, see
        "[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/orgs/{org}/actions/permissions/workflow",
            body=await async_maybe_transform(
                {
                    "can_approve_pull_request_reviews": can_approve_pull_request_reviews,
                    "default_workflow_permissions": default_workflow_permissions,
                },
                workflow_set_params.WorkflowSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class WorkflowResourceWithRawResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.get = to_raw_response_wrapper(
            workflow.get,
        )
        self.set = to_raw_response_wrapper(
            workflow.set,
        )


class AsyncWorkflowResourceWithRawResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.get = async_to_raw_response_wrapper(
            workflow.get,
        )
        self.set = async_to_raw_response_wrapper(
            workflow.set,
        )


class WorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.get = to_streamed_response_wrapper(
            workflow.get,
        )
        self.set = to_streamed_response_wrapper(
            workflow.set,
        )


class AsyncWorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.get = async_to_streamed_response_wrapper(
            workflow.get,
        )
        self.set = async_to_streamed_response_wrapper(
            workflow.set,
        )
