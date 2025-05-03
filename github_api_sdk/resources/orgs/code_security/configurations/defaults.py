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
from ....._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs.code_security.configurations import default_set_params
from .....types.orgs.code_security.configurations.default_list_response import DefaultListResponse
from .....types.orgs.code_security.configurations.default_set_response import DefaultSetResponse

__all__ = ["DefaultsResource", "AsyncDefaultsResource"]


class DefaultsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefaultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DefaultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefaultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DefaultsResourceWithStreamingResponse(self)

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
    ) -> DefaultListResponse:
        """
        Lists the default code security configurations for an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/code-security/configurations/defaults",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DefaultListResponse,
        )

    def set(
        self,
        configuration_id: int,
        *,
        org: str,
        default_for_new_repos: Literal["all", "none", "private_and_internal", "public"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultSetResponse:
        """
        Sets a code security configuration as a default to be applied to new
        repositories in your organization.

        This configuration will be applied to the matching repository type (all, none,
        public, private and internal) by default when they are created.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          default_for_new_repos: Specify which types of repository this security configuration should be applied
              to by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._put(
            f"/orgs/{org}/code-security/configurations/{configuration_id}/defaults",
            body=maybe_transform({"default_for_new_repos": default_for_new_repos}, default_set_params.DefaultSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DefaultSetResponse,
        )


class AsyncDefaultsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefaultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefaultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefaultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDefaultsResourceWithStreamingResponse(self)

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
    ) -> DefaultListResponse:
        """
        Lists the default code security configurations for an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/code-security/configurations/defaults",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DefaultListResponse,
        )

    async def set(
        self,
        configuration_id: int,
        *,
        org: str,
        default_for_new_repos: Literal["all", "none", "private_and_internal", "public"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefaultSetResponse:
        """
        Sets a code security configuration as a default to be applied to new
        repositories in your organization.

        This configuration will be applied to the matching repository type (all, none,
        public, private and internal) by default when they are created.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          default_for_new_repos: Specify which types of repository this security configuration should be applied
              to by default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._put(
            f"/orgs/{org}/code-security/configurations/{configuration_id}/defaults",
            body=await async_maybe_transform({"default_for_new_repos": default_for_new_repos}, default_set_params.DefaultSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DefaultSetResponse,
        )


class DefaultsResourceWithRawResponse:
    def __init__(self, defaults: DefaultsResource) -> None:
        self._defaults = defaults

        self.list = to_raw_response_wrapper(
            defaults.list,
        )
        self.set = to_raw_response_wrapper(
            defaults.set,
        )


class AsyncDefaultsResourceWithRawResponse:
    def __init__(self, defaults: AsyncDefaultsResource) -> None:
        self._defaults = defaults

        self.list = async_to_raw_response_wrapper(
            defaults.list,
        )
        self.set = async_to_raw_response_wrapper(
            defaults.set,
        )


class DefaultsResourceWithStreamingResponse:
    def __init__(self, defaults: DefaultsResource) -> None:
        self._defaults = defaults

        self.list = to_streamed_response_wrapper(
            defaults.list,
        )
        self.set = to_streamed_response_wrapper(
            defaults.set,
        )


class AsyncDefaultsResourceWithStreamingResponse:
    def __init__(self, defaults: AsyncDefaultsResource) -> None:
        self._defaults = defaults

        self.list = async_to_streamed_response_wrapper(
            defaults.list,
        )
        self.set = async_to_streamed_response_wrapper(
            defaults.set,
        )
