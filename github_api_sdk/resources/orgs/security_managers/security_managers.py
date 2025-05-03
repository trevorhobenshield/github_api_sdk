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
from ....types.orgs.security_manager_list_response import SecurityManagerListResponse
from .teams import (
    AsyncTeamsResource,
    AsyncTeamsResourceWithRawResponse,
    AsyncTeamsResourceWithStreamingResponse,
    TeamsResource,
    TeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
)

__all__ = ["SecurityManagersResource", "AsyncSecurityManagersResource"]


class SecurityManagersResource(SyncAPIResource):
    @cached_property
    def teams(self) -> TeamsResource:
        return TeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecurityManagersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SecurityManagersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityManagersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SecurityManagersResourceWithStreamingResponse(self)

    def list(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityManagerListResponse:
        """
        > [!WARNING] > **Closing down notice:** This operation is closing down and will
        > be removed starting January 1, 2026. Please use the
        > "[Organization Roles](https://docs.github.com/rest/orgs/organization-roles)"
        > endpoints instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/security-managers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SecurityManagerListResponse,
        )


class AsyncSecurityManagersResource(AsyncAPIResource):
    @cached_property
    def teams(self) -> AsyncTeamsResource:
        return AsyncTeamsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecurityManagersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityManagersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityManagersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSecurityManagersResourceWithStreamingResponse(self)

    async def list(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityManagerListResponse:
        """
        > [!WARNING] > **Closing down notice:** This operation is closing down and will
        > be removed starting January 1, 2026. Please use the
        > "[Organization Roles](https://docs.github.com/rest/orgs/organization-roles)"
        > endpoints instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/security-managers",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SecurityManagerListResponse,
        )


class SecurityManagersResourceWithRawResponse:
    def __init__(self, security_managers: SecurityManagersResource) -> None:
        self._security_managers = security_managers

        self.list = to_raw_response_wrapper(
            security_managers.list,
        )

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self._security_managers.teams)


class AsyncSecurityManagersResourceWithRawResponse:
    def __init__(self, security_managers: AsyncSecurityManagersResource) -> None:
        self._security_managers = security_managers

        self.list = async_to_raw_response_wrapper(
            security_managers.list,
        )

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self._security_managers.teams)


class SecurityManagersResourceWithStreamingResponse:
    def __init__(self, security_managers: SecurityManagersResource) -> None:
        self._security_managers = security_managers

        self.list = to_streamed_response_wrapper(
            security_managers.list,
        )

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self._security_managers.teams)


class AsyncSecurityManagersResourceWithStreamingResponse:
    def __init__(self, security_managers: AsyncSecurityManagersResource) -> None:
        self._security_managers = security_managers

        self.list = async_to_streamed_response_wrapper(
            security_managers.list,
        )

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self._security_managers.teams)
