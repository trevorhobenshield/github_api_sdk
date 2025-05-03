from __future__ import annotations

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
from ...types.orgs.docker_list_conflicts_response import DockerListConflictsResponse

__all__ = ["DockerResource", "AsyncDockerResource"]


class DockerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DockerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DockerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DockerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DockerResourceWithStreamingResponse(self)

    def list_conflicts(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DockerListConflictsResponse:
        """
        Lists all packages that are in a specific organization, are readable by the
        requesting user, and that encountered a conflict during a Docker migration.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/docker/conflicts",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DockerListConflictsResponse,
        )


class AsyncDockerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDockerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDockerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDockerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDockerResourceWithStreamingResponse(self)

    async def list_conflicts(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DockerListConflictsResponse:
        """
        Lists all packages that are in a specific organization, are readable by the
        requesting user, and that encountered a conflict during a Docker migration.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/docker/conflicts",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DockerListConflictsResponse,
        )


class DockerResourceWithRawResponse:
    def __init__(self, docker: DockerResource) -> None:
        self._docker = docker

        self.list_conflicts = to_raw_response_wrapper(
            docker.list_conflicts,
        )


class AsyncDockerResourceWithRawResponse:
    def __init__(self, docker: AsyncDockerResource) -> None:
        self._docker = docker

        self.list_conflicts = async_to_raw_response_wrapper(
            docker.list_conflicts,
        )


class DockerResourceWithStreamingResponse:
    def __init__(self, docker: DockerResource) -> None:
        self._docker = docker

        self.list_conflicts = to_streamed_response_wrapper(
            docker.list_conflicts,
        )


class AsyncDockerResourceWithStreamingResponse:
    def __init__(self, docker: AsyncDockerResource) -> None:
        self._docker = docker

        self.list_conflicts = async_to_streamed_response_wrapper(
            docker.list_conflicts,
        )
