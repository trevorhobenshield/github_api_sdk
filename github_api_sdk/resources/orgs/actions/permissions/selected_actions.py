from __future__ import annotations

from typing import List

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
from .....types.orgs.actions.permissions import selected_action_set_params
from .....types.orgs.actions.permissions.actions import Actions

__all__ = ["SelectedActionsResource", "AsyncSelectedActionsResource"]


class SelectedActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SelectedActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SelectedActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SelectedActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SelectedActionsResourceWithStreamingResponse(self)

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
    ) -> Actions:
        """
        Gets the selected actions and reusable workflows that are allowed in an
        organization. To use this endpoint, the organization permission policy for
        `allowed_actions` must be configured to `selected`. For more information, see
        "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

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
            f"/orgs/{org}/actions/permissions/selected-actions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Actions,
        )

    def set(
        self,
        org: str,
        *,
        github_owned_allowed: bool | NotGiven = NOT_GIVEN,
        patterns_allowed: list[str] | NotGiven = NOT_GIVEN,
        verified_allowed: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Sets the actions and reusable workflows that are allowed in an organization.

        To
        use this endpoint, the organization permission policy for `allowed_actions` must
        be configured to `selected`. For more information, see
        "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          github_owned_allowed: Whether GitHub-owned actions are allowed. For example, this includes the actions
              in the `actions` organization.

          patterns_allowed: Specifies a list of string-matching patterns to allow specific action(s) and
              reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example,
              `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`.

              > [!NOTE] The `patterns_allowed` setting only applies to public repositories.

          verified_allowed: Whether actions from GitHub Marketplace verified creators are allowed. Set to
              `true` to allow all actions by GitHub Marketplace verified creators.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/orgs/{org}/actions/permissions/selected-actions",
            body=maybe_transform(
                {
                    "github_owned_allowed": github_owned_allowed,
                    "patterns_allowed": patterns_allowed,
                    "verified_allowed": verified_allowed,
                },
                selected_action_set_params.SelectedActionSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncSelectedActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSelectedActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSelectedActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSelectedActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSelectedActionsResourceWithStreamingResponse(self)

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
    ) -> Actions:
        """
        Gets the selected actions and reusable workflows that are allowed in an
        organization. To use this endpoint, the organization permission policy for
        `allowed_actions` must be configured to `selected`. For more information, see
        "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

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
            f"/orgs/{org}/actions/permissions/selected-actions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Actions,
        )

    async def set(
        self,
        org: str,
        *,
        github_owned_allowed: bool | NotGiven = NOT_GIVEN,
        patterns_allowed: list[str] | NotGiven = NOT_GIVEN,
        verified_allowed: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Sets the actions and reusable workflows that are allowed in an organization.

        To
        use this endpoint, the organization permission policy for `allowed_actions` must
        be configured to `selected`. For more information, see
        "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          github_owned_allowed: Whether GitHub-owned actions are allowed. For example, this includes the actions
              in the `actions` organization.

          patterns_allowed: Specifies a list of string-matching patterns to allow specific action(s) and
              reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example,
              `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`.

              > [!NOTE] The `patterns_allowed` setting only applies to public repositories.

          verified_allowed: Whether actions from GitHub Marketplace verified creators are allowed. Set to
              `true` to allow all actions by GitHub Marketplace verified creators.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/orgs/{org}/actions/permissions/selected-actions",
            body=await async_maybe_transform(
                {
                    "github_owned_allowed": github_owned_allowed,
                    "patterns_allowed": patterns_allowed,
                    "verified_allowed": verified_allowed,
                },
                selected_action_set_params.SelectedActionSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class SelectedActionsResourceWithRawResponse:
    def __init__(self, selected_actions: SelectedActionsResource) -> None:
        self._selected_actions = selected_actions

        self.get = to_raw_response_wrapper(
            selected_actions.get,
        )
        self.set = to_raw_response_wrapper(
            selected_actions.set,
        )


class AsyncSelectedActionsResourceWithRawResponse:
    def __init__(self, selected_actions: AsyncSelectedActionsResource) -> None:
        self._selected_actions = selected_actions

        self.get = async_to_raw_response_wrapper(
            selected_actions.get,
        )
        self.set = async_to_raw_response_wrapper(
            selected_actions.set,
        )


class SelectedActionsResourceWithStreamingResponse:
    def __init__(self, selected_actions: SelectedActionsResource) -> None:
        self._selected_actions = selected_actions

        self.get = to_streamed_response_wrapper(
            selected_actions.get,
        )
        self.set = to_streamed_response_wrapper(
            selected_actions.set,
        )


class AsyncSelectedActionsResourceWithStreamingResponse:
    def __init__(self, selected_actions: AsyncSelectedActionsResource) -> None:
        self._selected_actions = selected_actions

        self.get = async_to_streamed_response_wrapper(
            selected_actions.get,
        )
        self.set = async_to_streamed_response_wrapper(
            selected_actions.set,
        )
