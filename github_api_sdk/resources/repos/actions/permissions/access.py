from __future__ import annotations

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
from .....types.repos.actions.permissions import access_update_params
from .....types.repos.actions.permissions.actions_workflow_access import ActionsWorkflowAccess

__all__ = ["AccessResource", "AsyncAccessResource"]


class AccessResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AccessResourceWithStreamingResponse(self)

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
    ) -> ActionsWorkflowAccess:
        """
        Gets the level of access that workflows outside of the repository have to
        actions and reusable workflows in the repository. This endpoint only applies to
        private repositories. For more information, see
        "[Allowing access to components in a private repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository)."

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/actions/permissions/access",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionsWorkflowAccess,
        )

    def update(
        self,
        repo: str,
        *,
        owner: str,
        access_level: Literal["none", "user", "organization"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Sets the level of access that workflows outside of the repository have to
        actions and reusable workflows in the repository. This endpoint only applies to
        private repositories. For more information, see
        "[Allowing access to components in a private repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository)".

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          access_level: Defines the level of access that workflows outside of the repository have to
              actions and reusable workflows within the repository.

              `none` means the access is only possible from workflows in this repository.
              `user` level access allows sharing across user owned private repositories only.
              `organization` level access allows sharing across the organization.

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
            f"/repos/{owner}/{repo}/actions/permissions/access",
            body=maybe_transform({"access_level": access_level}, access_update_params.AccessUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncAccessResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAccessResourceWithStreamingResponse(self)

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
    ) -> ActionsWorkflowAccess:
        """
        Gets the level of access that workflows outside of the repository have to
        actions and reusable workflows in the repository. This endpoint only applies to
        private repositories. For more information, see
        "[Allowing access to components in a private repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository)."

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/actions/permissions/access",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionsWorkflowAccess,
        )

    async def update(
        self,
        repo: str,
        *,
        owner: str,
        access_level: Literal["none", "user", "organization"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Sets the level of access that workflows outside of the repository have to
        actions and reusable workflows in the repository. This endpoint only applies to
        private repositories. For more information, see
        "[Allowing access to components in a private repository](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository)".

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          access_level: Defines the level of access that workflows outside of the repository have to
              actions and reusable workflows within the repository.

              `none` means the access is only possible from workflows in this repository.
              `user` level access allows sharing across user owned private repositories only.
              `organization` level access allows sharing across the organization.

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
            f"/repos/{owner}/{repo}/actions/permissions/access",
            body=await async_maybe_transform({"access_level": access_level}, access_update_params.AccessUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AccessResourceWithRawResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

        self.retrieve = to_raw_response_wrapper(
            access.retrieve,
        )
        self.update = to_raw_response_wrapper(
            access.update,
        )


class AsyncAccessResourceWithRawResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

        self.retrieve = async_to_raw_response_wrapper(
            access.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            access.update,
        )


class AccessResourceWithStreamingResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

        self.retrieve = to_streamed_response_wrapper(
            access.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            access.update,
        )


class AsyncAccessResourceWithStreamingResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

        self.retrieve = async_to_streamed_response_wrapper(
            access.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            access.update,
        )
