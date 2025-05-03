from __future__ import annotations

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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.users import installation_list_params
from ....types.users.installation_list_response import InstallationListResponse
from .repositories import (
    AsyncRepositoriesResource,
    AsyncRepositoriesResourceWithRawResponse,
    AsyncRepositoriesResourceWithStreamingResponse,
    RepositoriesResource,
    RepositoriesResourceWithRawResponse,
    RepositoriesResourceWithStreamingResponse,
)

__all__ = ["InstallationsResource", "AsyncInstallationsResource"]


class InstallationsResource(SyncAPIResource):
    @cached_property
    def repositories(self) -> RepositoriesResource:
        return RepositoriesResource(self._client)

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

    def list(
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
    ) -> InstallationListResponse:
        """
        Lists installations of your GitHub App that the authenticated user has explicit
        permission (`:read`, `:write`, or `:admin`) to access.

        The authenticated user has explicit permission to access repositories they own,
        repositories where they are a collaborator, and repositories that they can
        access through an organization membership.

        You can find the permissions for the installation under the `permissions` key.

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
            "/user/installations",
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
                    installation_list_params.InstallationListParams,
                ),
            ),
            cast_to=InstallationListResponse,
        )


class AsyncInstallationsResource(AsyncAPIResource):
    @cached_property
    def repositories(self) -> AsyncRepositoriesResource:
        return AsyncRepositoriesResource(self._client)

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

    async def list(
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
    ) -> InstallationListResponse:
        """
        Lists installations of your GitHub App that the authenticated user has explicit
        permission (`:read`, `:write`, or `:admin`) to access.

        The authenticated user has explicit permission to access repositories they own,
        repositories where they are a collaborator, and repositories that they can
        access through an organization membership.

        You can find the permissions for the installation under the `permissions` key.

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
            "/user/installations",
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
                    installation_list_params.InstallationListParams,
                ),
            ),
            cast_to=InstallationListResponse,
        )


class InstallationsResourceWithRawResponse:
    def __init__(self, installations: InstallationsResource) -> None:
        self._installations = installations

        self.list = to_raw_response_wrapper(
            installations.list,
        )

    @cached_property
    def repositories(self) -> RepositoriesResourceWithRawResponse:
        return RepositoriesResourceWithRawResponse(self._installations.repositories)


class AsyncInstallationsResourceWithRawResponse:
    def __init__(self, installations: AsyncInstallationsResource) -> None:
        self._installations = installations

        self.list = async_to_raw_response_wrapper(
            installations.list,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithRawResponse:
        return AsyncRepositoriesResourceWithRawResponse(self._installations.repositories)


class InstallationsResourceWithStreamingResponse:
    def __init__(self, installations: InstallationsResource) -> None:
        self._installations = installations

        self.list = to_streamed_response_wrapper(
            installations.list,
        )

    @cached_property
    def repositories(self) -> RepositoriesResourceWithStreamingResponse:
        return RepositoriesResourceWithStreamingResponse(self._installations.repositories)


class AsyncInstallationsResourceWithStreamingResponse:
    def __init__(self, installations: AsyncInstallationsResource) -> None:
        self._installations = installations

        self.list = async_to_streamed_response_wrapper(
            installations.list,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self._installations.repositories)
