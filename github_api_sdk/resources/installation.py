from __future__ import annotations

import httpx

from .._base_client import make_request_options
from .._compat import cached_property
from .._resource import AsyncAPIResource, SyncAPIResource
from .._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from .._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ..types import installation_list_repositories_params
from ..types.installation_list_repositories_response import InstallationListRepositoriesResponse

__all__ = ["InstallationResource", "AsyncInstallationResource"]


class InstallationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstallationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return InstallationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return InstallationResourceWithStreamingResponse(self)

    def list_repositories(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstallationListRepositoriesResponse:
        """
        List repositories that an app installation can access.

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
        return self._get(
            "/installation/repositories",
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
                    installation_list_repositories_params.InstallationListRepositoriesParams,
                ),
            ),
            cast_to=InstallationListRepositoriesResponse,
        )

    def revoke_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Revokes the installation token you're using to authenticate as an installation
        and access this endpoint.

        Once an installation token is revoked, the token is invalidated and cannot be
        used. Other endpoints that require the revoked installation token must have a
        new installation token to work. You can create a new token using the
        "[Create an installation access token for an app](https://docs.github.com/rest/apps/apps#create-an-installation-access-token-for-an-app)"
        endpoint.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/installation/token",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncInstallationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstallationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstallationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncInstallationResourceWithStreamingResponse(self)

    async def list_repositories(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InstallationListRepositoriesResponse:
        """
        List repositories that an app installation can access.

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
        return await self._get(
            "/installation/repositories",
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
                    installation_list_repositories_params.InstallationListRepositoriesParams,
                ),
            ),
            cast_to=InstallationListRepositoriesResponse,
        )

    async def revoke_token(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Revokes the installation token you're using to authenticate as an installation
        and access this endpoint.

        Once an installation token is revoked, the token is invalidated and cannot be
        used. Other endpoints that require the revoked installation token must have a
        new installation token to work. You can create a new token using the
        "[Create an installation access token for an app](https://docs.github.com/rest/apps/apps#create-an-installation-access-token-for-an-app)"
        endpoint.
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/installation/token",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class InstallationResourceWithRawResponse:
    def __init__(self, installation: InstallationResource) -> None:
        self._installation = installation

        self.list_repositories = to_raw_response_wrapper(
            installation.list_repositories,
        )
        self.revoke_token = to_raw_response_wrapper(
            installation.revoke_token,
        )


class AsyncInstallationResourceWithRawResponse:
    def __init__(self, installation: AsyncInstallationResource) -> None:
        self._installation = installation

        self.list_repositories = async_to_raw_response_wrapper(
            installation.list_repositories,
        )
        self.revoke_token = async_to_raw_response_wrapper(
            installation.revoke_token,
        )


class InstallationResourceWithStreamingResponse:
    def __init__(self, installation: InstallationResource) -> None:
        self._installation = installation

        self.list_repositories = to_streamed_response_wrapper(
            installation.list_repositories,
        )
        self.revoke_token = to_streamed_response_wrapper(
            installation.revoke_token,
        )


class AsyncInstallationResourceWithStreamingResponse:
    def __init__(self, installation: AsyncInstallationResource) -> None:
        self._installation = installation

        self.list_repositories = async_to_streamed_response_wrapper(
            installation.list_repositories,
        )
        self.revoke_token = async_to_streamed_response_wrapper(
            installation.revoke_token,
        )
