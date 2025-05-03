from __future__ import annotations

from typing import List

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
from .....types.orgs.codespaces import access_update_params
from .selected_users import (
    AsyncSelectedUsersResource,
    AsyncSelectedUsersResourceWithRawResponse,
    AsyncSelectedUsersResourceWithStreamingResponse,
    SelectedUsersResource,
    SelectedUsersResourceWithRawResponse,
    SelectedUsersResourceWithStreamingResponse,
)

__all__ = ["AccessResource", "AsyncAccessResource"]


class AccessResource(SyncAPIResource):
    @cached_property
    def selected_users(self) -> SelectedUsersResource:
        return SelectedUsersResource(self._client)

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

    def update(
        self,
        org: str,
        *,
        visibility: Literal["disabled", "selected_members", "all_members", "all_members_and_outside_collaborators"],
        selected_usernames: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Sets which users can access codespaces in an organization.

        This is synonymous
        with granting or revoking codespaces access permissions for users according to
        the visibility. OAuth app tokens and personal access tokens (classic) need the
        `admin:org` scope to use this endpoint.

        Args:
          visibility: Which users can access codespaces in the organization. `disabled` means that no
              users can access codespaces in the organization.

          selected_usernames: The usernames of the organization members who should have access to codespaces
              in the organization. Required when `visibility` is `selected_members`. The
              provided list of usernames will replace any existing value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/orgs/{org}/codespaces/access",
            body=maybe_transform(
                {
                    "visibility": visibility,
                    "selected_usernames": selected_usernames,
                },
                access_update_params.AccessUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncAccessResource(AsyncAPIResource):
    @cached_property
    def selected_users(self) -> AsyncSelectedUsersResource:
        return AsyncSelectedUsersResource(self._client)

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

    async def update(
        self,
        org: str,
        *,
        visibility: Literal["disabled", "selected_members", "all_members", "all_members_and_outside_collaborators"],
        selected_usernames: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Sets which users can access codespaces in an organization.

        This is synonymous
        with granting or revoking codespaces access permissions for users according to
        the visibility. OAuth app tokens and personal access tokens (classic) need the
        `admin:org` scope to use this endpoint.

        Args:
          visibility: Which users can access codespaces in the organization. `disabled` means that no
              users can access codespaces in the organization.

          selected_usernames: The usernames of the organization members who should have access to codespaces
              in the organization. Required when `visibility` is `selected_members`. The
              provided list of usernames will replace any existing value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/orgs/{org}/codespaces/access",
            body=await async_maybe_transform(
                {
                    "visibility": visibility,
                    "selected_usernames": selected_usernames,
                },
                access_update_params.AccessUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AccessResourceWithRawResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

        self.update = to_raw_response_wrapper(
            access.update,
        )

    @cached_property
    def selected_users(self) -> SelectedUsersResourceWithRawResponse:
        return SelectedUsersResourceWithRawResponse(self._access.selected_users)


class AsyncAccessResourceWithRawResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

        self.update = async_to_raw_response_wrapper(
            access.update,
        )

    @cached_property
    def selected_users(self) -> AsyncSelectedUsersResourceWithRawResponse:
        return AsyncSelectedUsersResourceWithRawResponse(self._access.selected_users)


class AccessResourceWithStreamingResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

        self.update = to_streamed_response_wrapper(
            access.update,
        )

    @cached_property
    def selected_users(self) -> SelectedUsersResourceWithStreamingResponse:
        return SelectedUsersResourceWithStreamingResponse(self._access.selected_users)


class AsyncAccessResourceWithStreamingResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

        self.update = async_to_streamed_response_wrapper(
            access.update,
        )

    @cached_property
    def selected_users(self) -> AsyncSelectedUsersResourceWithStreamingResponse:
        return AsyncSelectedUsersResourceWithStreamingResponse(self._access.selected_users)
