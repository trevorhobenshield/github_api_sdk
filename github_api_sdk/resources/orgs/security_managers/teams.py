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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return TeamsResourceWithStreamingResponse(self)

    def add(
        self,
        team_slug: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/orgs/{org}/security-managers/teams/{team_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def remove(
        self,
        team_slug: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/security-managers/teams/{team_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncTeamsResourceWithStreamingResponse(self)

    async def add(
        self,
        team_slug: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/orgs/{org}/security-managers/teams/{team_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def remove(
        self,
        team_slug: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/security-managers/teams/{team_slug}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.add = to_raw_response_wrapper(
            teams.add,
        )
        self.remove = to_raw_response_wrapper(
            teams.remove,
        )


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.add = async_to_raw_response_wrapper(
            teams.add,
        )
        self.remove = async_to_raw_response_wrapper(
            teams.remove,
        )


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

        self.add = to_streamed_response_wrapper(
            teams.add,
        )
        self.remove = to_streamed_response_wrapper(
            teams.remove,
        )


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

        self.add = async_to_streamed_response_wrapper(
            teams.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            teams.remove,
        )
