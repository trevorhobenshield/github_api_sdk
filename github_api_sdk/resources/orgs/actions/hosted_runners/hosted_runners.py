from __future__ import annotations

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
from ....._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs.actions import hosted_runner_create_params, hosted_runner_list_params, hosted_runner_update_params
from .....types.orgs.actions.hosted_runner_get_limits_response import HostedRunnerGetLimitsResponse
from .....types.orgs.actions.hosted_runner_get_machine_sizes_response import HostedRunnerGetMachineSizesResponse
from .....types.orgs.actions.hosted_runner_get_platforms_response import HostedRunnerGetPlatformsResponse
from .....types.orgs.actions.hosted_runner_list_response import HostedRunnerListResponse
from .....types.orgs.actions.runner import Runner
from .images import (
    AsyncImagesResource,
    AsyncImagesResourceWithRawResponse,
    AsyncImagesResourceWithStreamingResponse,
    ImagesResource,
    ImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
)

__all__ = ["HostedRunnersResource", "AsyncHostedRunnersResource"]


class HostedRunnersResource(SyncAPIResource):
    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> HostedRunnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return HostedRunnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostedRunnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return HostedRunnersResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        image: hosted_runner_create_params.Image,
        name: str,
        runner_group_id: int,
        size: str,
        enable_static_ip: bool | NotGiven = NOT_GIVEN,
        maximum_runners: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runner:
        """Creates a GitHub-hosted runner for an organization.

        OAuth tokens and personal
        access tokens (classic) need the `manage_runners:org` scope to use this
        endpoint.

        Args:
          image: The image of runner. To list all available images, use
              `GET /actions/hosted-runners/images/github-owned` or
              `GET /actions/hosted-runners/images/partner`.

          name: Name of the runner. Must be between 1 and 64 characters and may only contain
              upper and lowercase letters a-z, numbers 0-9, '.', '-', and '\\__'.

          runner_group_id: The existing runner group to add this runner to.

          size: The machine size of the runner. To list available sizes, use
              `GET actions/hosted-runners/machine-sizes`

          enable_static_ip: Whether this runner should be created with a static public IP. Note limit on
              account. To list limits on account, use `GET actions/hosted-runners/limits`

          maximum_runners: The maximum amount of runners to scale up to. Runners will not auto-scale above
              this number. Use this setting to limit your cost.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/actions/hosted-runners",
            body=maybe_transform(
                {
                    "image": image,
                    "name": name,
                    "runner_group_id": runner_group_id,
                    "size": size,
                    "enable_static_ip": enable_static_ip,
                    "maximum_runners": maximum_runners,
                },
                hosted_runner_create_params.HostedRunnerCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Runner,
        )

    def retrieve(
        self,
        hosted_runner_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runner:
        """
        Gets a GitHub-hosted runner configured in an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `manage_runners:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/hosted-runners/{hosted_runner_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Runner,
        )

    def update(
        self,
        hosted_runner_id: int,
        *,
        org: str,
        enable_static_ip: bool | NotGiven = NOT_GIVEN,
        maximum_runners: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        runner_group_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runner:
        """Updates a GitHub-hosted runner for an organization.

        OAuth app tokens and
        personal access tokens (classic) need the `manage_runners:org` scope to use this
        endpoint.

        Args:
          enable_static_ip: Whether this runner should be updated with a static public IP. Note limit on
              account. To list limits on account, use `GET actions/hosted-runners/limits`

          maximum_runners: The maximum amount of runners to scale up to. Runners will not auto-scale above
              this number. Use this setting to limit your cost.

          name: Name of the runner. Must be between 1 and 64 characters and may only contain
              upper and lowercase letters a-z, numbers 0-9, '.', '-', and '\\__'.

          runner_group_id: The existing runner group to add this runner to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._patch(
            f"/orgs/{org}/actions/hosted-runners/{hosted_runner_id}",
            body=maybe_transform(
                {
                    "enable_static_ip": enable_static_ip,
                    "maximum_runners": maximum_runners,
                    "name": name,
                    "runner_group_id": runner_group_id,
                },
                hosted_runner_update_params.HostedRunnerUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Runner,
        )

    def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostedRunnerListResponse:
        """
        Lists all GitHub-hosted runners configured in an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `manage_runner:org` scope to use this endpoint.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/hosted-runners",
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
                    hosted_runner_list_params.HostedRunnerListParams,
                ),
            ),
            cast_to=HostedRunnerListResponse,
        )

    def delete(
        self,
        hosted_runner_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runner:
        """
        Deletes a GitHub-hosted runner for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._delete(
            f"/orgs/{org}/actions/hosted-runners/{hosted_runner_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Runner,
        )

    def get_limits(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostedRunnerGetLimitsResponse:
        """
        Get the GitHub-hosted runners limits for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/hosted-runners/limits",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=HostedRunnerGetLimitsResponse,
        )

    def get_machine_sizes(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostedRunnerGetMachineSizesResponse:
        """
        Get the list of machine specs available for GitHub-hosted runners for an
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/hosted-runners/machine-sizes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=HostedRunnerGetMachineSizesResponse,
        )

    def get_platforms(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostedRunnerGetPlatformsResponse:
        """
        Get the list of platforms available for GitHub-hosted runners for an
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/hosted-runners/platforms",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=HostedRunnerGetPlatformsResponse,
        )


class AsyncHostedRunnersResource(AsyncAPIResource):
    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostedRunnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostedRunnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostedRunnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncHostedRunnersResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        image: hosted_runner_create_params.Image,
        name: str,
        runner_group_id: int,
        size: str,
        enable_static_ip: bool | NotGiven = NOT_GIVEN,
        maximum_runners: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runner:
        """Creates a GitHub-hosted runner for an organization.

        OAuth tokens and personal
        access tokens (classic) need the `manage_runners:org` scope to use this
        endpoint.

        Args:
          image: The image of runner. To list all available images, use
              `GET /actions/hosted-runners/images/github-owned` or
              `GET /actions/hosted-runners/images/partner`.

          name: Name of the runner. Must be between 1 and 64 characters and may only contain
              upper and lowercase letters a-z, numbers 0-9, '.', '-', and '\\__'.

          runner_group_id: The existing runner group to add this runner to.

          size: The machine size of the runner. To list available sizes, use
              `GET actions/hosted-runners/machine-sizes`

          enable_static_ip: Whether this runner should be created with a static public IP. Note limit on
              account. To list limits on account, use `GET actions/hosted-runners/limits`

          maximum_runners: The maximum amount of runners to scale up to. Runners will not auto-scale above
              this number. Use this setting to limit your cost.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/actions/hosted-runners",
            body=await async_maybe_transform(
                {
                    "image": image,
                    "name": name,
                    "runner_group_id": runner_group_id,
                    "size": size,
                    "enable_static_ip": enable_static_ip,
                    "maximum_runners": maximum_runners,
                },
                hosted_runner_create_params.HostedRunnerCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Runner,
        )

    async def retrieve(
        self,
        hosted_runner_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runner:
        """
        Gets a GitHub-hosted runner configured in an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `manage_runners:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/hosted-runners/{hosted_runner_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Runner,
        )

    async def update(
        self,
        hosted_runner_id: int,
        *,
        org: str,
        enable_static_ip: bool | NotGiven = NOT_GIVEN,
        maximum_runners: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        runner_group_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runner:
        """Updates a GitHub-hosted runner for an organization.

        OAuth app tokens and
        personal access tokens (classic) need the `manage_runners:org` scope to use this
        endpoint.

        Args:
          enable_static_ip: Whether this runner should be updated with a static public IP. Note limit on
              account. To list limits on account, use `GET actions/hosted-runners/limits`

          maximum_runners: The maximum amount of runners to scale up to. Runners will not auto-scale above
              this number. Use this setting to limit your cost.

          name: Name of the runner. Must be between 1 and 64 characters and may only contain
              upper and lowercase letters a-z, numbers 0-9, '.', '-', and '\\__'.

          runner_group_id: The existing runner group to add this runner to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._patch(
            f"/orgs/{org}/actions/hosted-runners/{hosted_runner_id}",
            body=await async_maybe_transform(
                {
                    "enable_static_ip": enable_static_ip,
                    "maximum_runners": maximum_runners,
                    "name": name,
                    "runner_group_id": runner_group_id,
                },
                hosted_runner_update_params.HostedRunnerUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Runner,
        )

    async def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostedRunnerListResponse:
        """
        Lists all GitHub-hosted runners configured in an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `manage_runner:org` scope to use this endpoint.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/hosted-runners",
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
                    hosted_runner_list_params.HostedRunnerListParams,
                ),
            ),
            cast_to=HostedRunnerListResponse,
        )

    async def delete(
        self,
        hosted_runner_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runner:
        """
        Deletes a GitHub-hosted runner for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._delete(
            f"/orgs/{org}/actions/hosted-runners/{hosted_runner_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Runner,
        )

    async def get_limits(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostedRunnerGetLimitsResponse:
        """
        Get the GitHub-hosted runners limits for an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/hosted-runners/limits",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=HostedRunnerGetLimitsResponse,
        )

    async def get_machine_sizes(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostedRunnerGetMachineSizesResponse:
        """
        Get the list of machine specs available for GitHub-hosted runners for an
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/hosted-runners/machine-sizes",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=HostedRunnerGetMachineSizesResponse,
        )

    async def get_platforms(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostedRunnerGetPlatformsResponse:
        """
        Get the list of platforms available for GitHub-hosted runners for an
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/hosted-runners/platforms",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=HostedRunnerGetPlatformsResponse,
        )


class HostedRunnersResourceWithRawResponse:
    def __init__(self, hosted_runners: HostedRunnersResource) -> None:
        self._hosted_runners = hosted_runners

        self.create = to_raw_response_wrapper(
            hosted_runners.create,
        )
        self.retrieve = to_raw_response_wrapper(
            hosted_runners.retrieve,
        )
        self.update = to_raw_response_wrapper(
            hosted_runners.update,
        )
        self.list = to_raw_response_wrapper(
            hosted_runners.list,
        )
        self.delete = to_raw_response_wrapper(
            hosted_runners.delete,
        )
        self.get_limits = to_raw_response_wrapper(
            hosted_runners.get_limits,
        )
        self.get_machine_sizes = to_raw_response_wrapper(
            hosted_runners.get_machine_sizes,
        )
        self.get_platforms = to_raw_response_wrapper(
            hosted_runners.get_platforms,
        )

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._hosted_runners.images)


class AsyncHostedRunnersResourceWithRawResponse:
    def __init__(self, hosted_runners: AsyncHostedRunnersResource) -> None:
        self._hosted_runners = hosted_runners

        self.create = async_to_raw_response_wrapper(
            hosted_runners.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            hosted_runners.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            hosted_runners.update,
        )
        self.list = async_to_raw_response_wrapper(
            hosted_runners.list,
        )
        self.delete = async_to_raw_response_wrapper(
            hosted_runners.delete,
        )
        self.get_limits = async_to_raw_response_wrapper(
            hosted_runners.get_limits,
        )
        self.get_machine_sizes = async_to_raw_response_wrapper(
            hosted_runners.get_machine_sizes,
        )
        self.get_platforms = async_to_raw_response_wrapper(
            hosted_runners.get_platforms,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._hosted_runners.images)


class HostedRunnersResourceWithStreamingResponse:
    def __init__(self, hosted_runners: HostedRunnersResource) -> None:
        self._hosted_runners = hosted_runners

        self.create = to_streamed_response_wrapper(
            hosted_runners.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            hosted_runners.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            hosted_runners.update,
        )
        self.list = to_streamed_response_wrapper(
            hosted_runners.list,
        )
        self.delete = to_streamed_response_wrapper(
            hosted_runners.delete,
        )
        self.get_limits = to_streamed_response_wrapper(
            hosted_runners.get_limits,
        )
        self.get_machine_sizes = to_streamed_response_wrapper(
            hosted_runners.get_machine_sizes,
        )
        self.get_platforms = to_streamed_response_wrapper(
            hosted_runners.get_platforms,
        )

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._hosted_runners.images)


class AsyncHostedRunnersResourceWithStreamingResponse:
    def __init__(self, hosted_runners: AsyncHostedRunnersResource) -> None:
        self._hosted_runners = hosted_runners

        self.create = async_to_streamed_response_wrapper(
            hosted_runners.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            hosted_runners.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            hosted_runners.update,
        )
        self.list = async_to_streamed_response_wrapper(
            hosted_runners.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            hosted_runners.delete,
        )
        self.get_limits = async_to_streamed_response_wrapper(
            hosted_runners.get_limits,
        )
        self.get_machine_sizes = async_to_streamed_response_wrapper(
            hosted_runners.get_machine_sizes,
        )
        self.get_platforms = async_to_streamed_response_wrapper(
            hosted_runners.get_platforms,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._hosted_runners.images)
