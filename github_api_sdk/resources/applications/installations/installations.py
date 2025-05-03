from __future__ import annotations

import builtins
from datetime import datetime
from typing import Iterable, List, Union

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.applications import installation_create_access_token_params, installation_list_params
from ....types.applications.installation import Installation
from ....types.applications.installation_create_access_token_response import InstallationCreateAccessTokenResponse
from ....types.applications.installation_list_response import InstallationListResponse
from ....types.applications.permissions_param import PermissionsParam
from .suspended import (
    AsyncSuspendedResource,
    AsyncSuspendedResourceWithRawResponse,
    AsyncSuspendedResourceWithStreamingResponse,
    SuspendedResource,
    SuspendedResourceWithRawResponse,
    SuspendedResourceWithStreamingResponse,
)

__all__ = ["InstallationsResource", "AsyncInstallationsResource"]


class InstallationsResource(SyncAPIResource):
    @cached_property
    def suspended(self) -> SuspendedResource:
        return SuspendedResource(self._client)

    @cached_property
    def with_raw_response(self) -> InstallationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return InstallationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return InstallationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        installation_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Installation:
        """
        Enables an authenticated GitHub App to find an installation's information using
        the installation id.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/app/installations/{installation_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Installation,
        )

    def list(
        self,
        *,
        outdated: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstallationListResponse:
        """
        The permissions the installation has are included under the `permissions` key.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/app/installations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "outdated": outdated,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                    },
                    installation_list_params.InstallationListParams,
                ),
            ),
            cast_to=InstallationListResponse,
        )

    def delete(
        self,
        installation_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Uninstalls a GitHub App on a user, organization, or business account.

        If you
        prefer to temporarily suspend an app's access to your account's resources, then
        we recommend the
        "[Suspend an app installation](https://docs.github.com/rest/apps/apps#suspend-an-app-installation)"
        endpoint.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/app/installations/{installation_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_access_token(
        self,
        installation_id: int,
        *,
        permissions: PermissionsParam | NotGiven = NOT_GIVEN,
        repositories: builtins.list[str] | NotGiven = NOT_GIVEN,
        repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstallationCreateAccessTokenResponse:
        """
        Creates an installation access token that enables a GitHub App to make
        authenticated API requests for the app's installation on an organization or
        individual account. Installation tokens expire one hour from the time you create
        them. Using an expired token produces a status code of `401 - Unauthorized`, and
        requires creating a new installation token. By default the installation token
        has access to all repositories that the installation can access.

        Optionally, you can use the `repositories` or `repository_ids` body parameters
        to specify individual repositories that the installation access token can
        access. If you don't use `repositories` or `repository_ids` to grant access to
        specific repositories, the installation access token will have access to all
        repositories that the installation was granted access to. The installation
        access token cannot be granted access to repositories that the installation was
        not granted access to. Up to 500 repositories can be listed in this manner.

        Optionally, use the `permissions` body parameter to specify the permissions that
        the installation access token should have. If `permissions` is not specified,
        the installation access token will have all of the permissions that were granted
        to the app. The installation access token cannot be granted permissions that the
        app was not granted.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          permissions: The permissions granted to the user access token.

          repositories: List of repository names that the token should have access to

          repository_ids: List of repository IDs that the token should have access to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/app/installations/{installation_id}/access_tokens",
            body=maybe_transform(
                {
                    "permissions": permissions,
                    "repositories": repositories,
                    "repository_ids": repository_ids,
                },
                installation_create_access_token_params.InstallationCreateAccessTokenParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=InstallationCreateAccessTokenResponse,
        )


class AsyncInstallationsResource(AsyncAPIResource):
    @cached_property
    def suspended(self) -> AsyncSuspendedResource:
        return AsyncSuspendedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInstallationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstallationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncInstallationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        installation_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Installation:
        """
        Enables an authenticated GitHub App to find an installation's information using
        the installation id.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/app/installations/{installation_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Installation,
        )

    async def list(
        self,
        *,
        outdated: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstallationListResponse:
        """
        The permissions the installation has are included under the `permissions` key.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/app/installations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "outdated": outdated,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                    },
                    installation_list_params.InstallationListParams,
                ),
            ),
            cast_to=InstallationListResponse,
        )

    async def delete(
        self,
        installation_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Uninstalls a GitHub App on a user, organization, or business account.

        If you
        prefer to temporarily suspend an app's access to your account's resources, then
        we recommend the
        "[Suspend an app installation](https://docs.github.com/rest/apps/apps#suspend-an-app-installation)"
        endpoint.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/app/installations/{installation_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_access_token(
        self,
        installation_id: int,
        *,
        permissions: PermissionsParam | NotGiven = NOT_GIVEN,
        repositories: builtins.list[str] | NotGiven = NOT_GIVEN,
        repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstallationCreateAccessTokenResponse:
        """
        Creates an installation access token that enables a GitHub App to make
        authenticated API requests for the app's installation on an organization or
        individual account. Installation tokens expire one hour from the time you create
        them. Using an expired token produces a status code of `401 - Unauthorized`, and
        requires creating a new installation token. By default the installation token
        has access to all repositories that the installation can access.

        Optionally, you can use the `repositories` or `repository_ids` body parameters
        to specify individual repositories that the installation access token can
        access. If you don't use `repositories` or `repository_ids` to grant access to
        specific repositories, the installation access token will have access to all
        repositories that the installation was granted access to. The installation
        access token cannot be granted access to repositories that the installation was
        not granted access to. Up to 500 repositories can be listed in this manner.

        Optionally, use the `permissions` body parameter to specify the permissions that
        the installation access token should have. If `permissions` is not specified,
        the installation access token will have all of the permissions that were granted
        to the app. The installation access token cannot be granted permissions that the
        app was not granted.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          permissions: The permissions granted to the user access token.

          repositories: List of repository names that the token should have access to

          repository_ids: List of repository IDs that the token should have access to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/app/installations/{installation_id}/access_tokens",
            body=await async_maybe_transform(
                {
                    "permissions": permissions,
                    "repositories": repositories,
                    "repository_ids": repository_ids,
                },
                installation_create_access_token_params.InstallationCreateAccessTokenParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=InstallationCreateAccessTokenResponse,
        )


class InstallationsResourceWithRawResponse:
    def __init__(self, installations: InstallationsResource) -> None:
        self._installations = installations

        self.retrieve = to_raw_response_wrapper(
            installations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            installations.list,
        )
        self.delete = to_raw_response_wrapper(
            installations.delete,
        )
        self.create_access_token = to_raw_response_wrapper(
            installations.create_access_token,
        )

    @cached_property
    def suspended(self) -> SuspendedResourceWithRawResponse:
        return SuspendedResourceWithRawResponse(self._installations.suspended)


class AsyncInstallationsResourceWithRawResponse:
    def __init__(self, installations: AsyncInstallationsResource) -> None:
        self._installations = installations

        self.retrieve = async_to_raw_response_wrapper(
            installations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            installations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            installations.delete,
        )
        self.create_access_token = async_to_raw_response_wrapper(
            installations.create_access_token,
        )

    @cached_property
    def suspended(self) -> AsyncSuspendedResourceWithRawResponse:
        return AsyncSuspendedResourceWithRawResponse(self._installations.suspended)


class InstallationsResourceWithStreamingResponse:
    def __init__(self, installations: InstallationsResource) -> None:
        self._installations = installations

        self.retrieve = to_streamed_response_wrapper(
            installations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            installations.list,
        )
        self.delete = to_streamed_response_wrapper(
            installations.delete,
        )
        self.create_access_token = to_streamed_response_wrapper(
            installations.create_access_token,
        )

    @cached_property
    def suspended(self) -> SuspendedResourceWithStreamingResponse:
        return SuspendedResourceWithStreamingResponse(self._installations.suspended)


class AsyncInstallationsResourceWithStreamingResponse:
    def __init__(self, installations: AsyncInstallationsResource) -> None:
        self._installations = installations

        self.retrieve = async_to_streamed_response_wrapper(
            installations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            installations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            installations.delete,
        )
        self.create_access_token = async_to_streamed_response_wrapper(
            installations.create_access_token,
        )

    @cached_property
    def suspended(self) -> AsyncSuspendedResourceWithStreamingResponse:
        return AsyncSuspendedResourceWithStreamingResponse(self._installations.suspended)
