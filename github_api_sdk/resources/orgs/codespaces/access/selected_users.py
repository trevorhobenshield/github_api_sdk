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
from .....types.orgs.codespaces.access import selected_user_add_params, selected_user_remove_params

__all__ = ["SelectedUsersResource", "AsyncSelectedUsersResource"]


class SelectedUsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SelectedUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SelectedUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SelectedUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SelectedUsersResourceWithStreamingResponse(self)

    def add(
        self,
        org: str,
        *,
        selected_usernames: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Codespaces for the specified users will be billed to the organization.

        To use this endpoint, the access settings for the organization must be set to
        `selected_members`. For information on how to change this setting, see
        "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          selected_usernames: The usernames of the organization members whose codespaces be billed to the
              organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/orgs/{org}/codespaces/access/selected_users",
            body=maybe_transform({"selected_usernames": selected_usernames}, selected_user_add_params.SelectedUserAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def remove(
        self,
        org: str,
        *,
        selected_usernames: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Codespaces for the specified users will no longer be billed to the organization.

        To use this endpoint, the access settings for the organization must be set to
        `selected_members`. For information on how to change this setting, see
        "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          selected_usernames: The usernames of the organization members whose codespaces should not be billed
              to the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/codespaces/access/selected_users",
            body=maybe_transform({"selected_usernames": selected_usernames}, selected_user_remove_params.SelectedUserRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncSelectedUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSelectedUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSelectedUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSelectedUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSelectedUsersResourceWithStreamingResponse(self)

    async def add(
        self,
        org: str,
        *,
        selected_usernames: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Codespaces for the specified users will be billed to the organization.

        To use this endpoint, the access settings for the organization must be set to
        `selected_members`. For information on how to change this setting, see
        "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          selected_usernames: The usernames of the organization members whose codespaces be billed to the
              organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/orgs/{org}/codespaces/access/selected_users",
            body=await async_maybe_transform({"selected_usernames": selected_usernames}, selected_user_add_params.SelectedUserAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def remove(
        self,
        org: str,
        *,
        selected_usernames: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Codespaces for the specified users will no longer be billed to the organization.

        To use this endpoint, the access settings for the organization must be set to
        `selected_members`. For information on how to change this setting, see
        "[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          selected_usernames: The usernames of the organization members whose codespaces should not be billed
              to the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/codespaces/access/selected_users",
            body=await async_maybe_transform({"selected_usernames": selected_usernames}, selected_user_remove_params.SelectedUserRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class SelectedUsersResourceWithRawResponse:
    def __init__(self, selected_users: SelectedUsersResource) -> None:
        self._selected_users = selected_users

        self.add = to_raw_response_wrapper(
            selected_users.add,
        )
        self.remove = to_raw_response_wrapper(
            selected_users.remove,
        )


class AsyncSelectedUsersResourceWithRawResponse:
    def __init__(self, selected_users: AsyncSelectedUsersResource) -> None:
        self._selected_users = selected_users

        self.add = async_to_raw_response_wrapper(
            selected_users.add,
        )
        self.remove = async_to_raw_response_wrapper(
            selected_users.remove,
        )


class SelectedUsersResourceWithStreamingResponse:
    def __init__(self, selected_users: SelectedUsersResource) -> None:
        self._selected_users = selected_users

        self.add = to_streamed_response_wrapper(
            selected_users.add,
        )
        self.remove = to_streamed_response_wrapper(
            selected_users.remove,
        )


class AsyncSelectedUsersResourceWithStreamingResponse:
    def __init__(self, selected_users: AsyncSelectedUsersResource) -> None:
        self._selected_users = selected_users

        self.add = async_to_streamed_response_wrapper(
            selected_users.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            selected_users.remove,
        )
