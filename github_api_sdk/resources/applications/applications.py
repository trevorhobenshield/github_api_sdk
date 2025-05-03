from __future__ import annotations

from typing import Optional

import httpx

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types import application_list_installation_requests_params
from ...types.application_list_installation_requests_response import ApplicationListInstallationRequestsResponse
from ...types.integration import Integration
from .hook.hook import (
    AsyncHookResource,
    AsyncHookResourceWithRawResponse,
    AsyncHookResourceWithStreamingResponse,
    HookResource,
    HookResourceWithRawResponse,
    HookResourceWithStreamingResponse,
)
from .installations.installations import (
    AsyncInstallationsResource,
    AsyncInstallationsResourceWithRawResponse,
    AsyncInstallationsResourceWithStreamingResponse,
    InstallationsResource,
    InstallationsResourceWithRawResponse,
    InstallationsResourceWithStreamingResponse,
)

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def hook(self) -> HookResource:
        return HookResource(self._client)

    @cached_property
    def installations(self) -> InstallationsResource:
        return InstallationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    def list_installation_requests(
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
    ) -> ApplicationListInstallationRequestsResponse:
        """
        Lists all the pending installation requests for the authenticated GitHub App.

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
            "/app/installation-requests",
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
                    application_list_installation_requests_params.ApplicationListInstallationRequestsParams,
                ),
            ),
            cast_to=ApplicationListInstallationRequestsResponse,
        )

    def retrieve_0(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Integration | None:
        """Returns the GitHub App associated with the authentication credentials used.

        To
        see how many app installations are associated with this GitHub App, see the
        `installations_count` in the response. For more details about your app's
        installations, see the
        "[List installations for the authenticated app](https://docs.github.com/rest/apps/apps#list-installations-for-the-authenticated-app)"
        endpoint.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.
        """
        return self._get(
            "/app",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Integration,
        )

    def retrieve_1(
        self,
        app_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Integration | None:
        """> [!NOTE] The `:app_slug` is just the URL-friendly name of your GitHub App.

        You
        > can find this on the settings page for your GitHub App (e.g.,
        > `https://github.com/settings/apps/:app_slug`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_slug:
            raise ValueError(f"Expected a non-empty value for `app_slug` but received {app_slug!r}")
        return self._get(
            f"/apps/{app_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Integration,
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def hook(self) -> AsyncHookResource:
        return AsyncHookResource(self._client)

    @cached_property
    def installations(self) -> AsyncInstallationsResource:
        return AsyncInstallationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    async def list_installation_requests(
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
    ) -> ApplicationListInstallationRequestsResponse:
        """
        Lists all the pending installation requests for the authenticated GitHub App.

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
            "/app/installation-requests",
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
                    application_list_installation_requests_params.ApplicationListInstallationRequestsParams,
                ),
            ),
            cast_to=ApplicationListInstallationRequestsResponse,
        )

    async def retrieve_0(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Integration | None:
        """Returns the GitHub App associated with the authentication credentials used.

        To
        see how many app installations are associated with this GitHub App, see the
        `installations_count` in the response. For more details about your app's
        installations, see the
        "[List installations for the authenticated app](https://docs.github.com/rest/apps/apps#list-installations-for-the-authenticated-app)"
        endpoint.

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.
        """
        return await self._get(
            "/app",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Integration,
        )

    async def retrieve_1(
        self,
        app_slug: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Integration | None:
        """> [!NOTE] The `:app_slug` is just the URL-friendly name of your GitHub App.

        You
        > can find this on the settings page for your GitHub App (e.g.,
        > `https://github.com/settings/apps/:app_slug`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_slug:
            raise ValueError(f"Expected a non-empty value for `app_slug` but received {app_slug!r}")
        return await self._get(
            f"/apps/{app_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Integration,
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.list_installation_requests = to_raw_response_wrapper(
            applications.list_installation_requests,
        )
        self.retrieve_0 = to_raw_response_wrapper(
            applications.retrieve_0,
        )
        self.retrieve_1 = to_raw_response_wrapper(
            applications.retrieve_1,
        )

    @cached_property
    def hook(self) -> HookResourceWithRawResponse:
        return HookResourceWithRawResponse(self._applications.hook)

    @cached_property
    def installations(self) -> InstallationsResourceWithRawResponse:
        return InstallationsResourceWithRawResponse(self._applications.installations)


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.list_installation_requests = async_to_raw_response_wrapper(
            applications.list_installation_requests,
        )
        self.retrieve_0 = async_to_raw_response_wrapper(
            applications.retrieve_0,
        )
        self.retrieve_1 = async_to_raw_response_wrapper(
            applications.retrieve_1,
        )

    @cached_property
    def hook(self) -> AsyncHookResourceWithRawResponse:
        return AsyncHookResourceWithRawResponse(self._applications.hook)

    @cached_property
    def installations(self) -> AsyncInstallationsResourceWithRawResponse:
        return AsyncInstallationsResourceWithRawResponse(self._applications.installations)


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.list_installation_requests = to_streamed_response_wrapper(
            applications.list_installation_requests,
        )
        self.retrieve_0 = to_streamed_response_wrapper(
            applications.retrieve_0,
        )
        self.retrieve_1 = to_streamed_response_wrapper(
            applications.retrieve_1,
        )

    @cached_property
    def hook(self) -> HookResourceWithStreamingResponse:
        return HookResourceWithStreamingResponse(self._applications.hook)

    @cached_property
    def installations(self) -> InstallationsResourceWithStreamingResponse:
        return InstallationsResourceWithStreamingResponse(self._applications.installations)


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.list_installation_requests = async_to_streamed_response_wrapper(
            applications.list_installation_requests,
        )
        self.retrieve_0 = async_to_streamed_response_wrapper(
            applications.retrieve_0,
        )
        self.retrieve_1 = async_to_streamed_response_wrapper(
            applications.retrieve_1,
        )

    @cached_property
    def hook(self) -> AsyncHookResourceWithStreamingResponse:
        return AsyncHookResourceWithStreamingResponse(self._applications.hook)

    @cached_property
    def installations(self) -> AsyncInstallationsResourceWithStreamingResponse:
        return AsyncInstallationsResourceWithStreamingResponse(self._applications.installations)
