from __future__ import annotations

from typing import Union

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
from ....types.repos.pages import deployment_create_params
from ....types.repos.pages.deployment_create_response import DeploymentCreateResponse
from ....types.repos.pages.deployment_get_status_response import DeploymentGetStatusResponse

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DeploymentsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        oidc_token: str,
        pages_build_version: str,
        artifact_id: float | NotGiven = NOT_GIVEN,
        artifact_url: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentCreateResponse:
        """
        Create a GitHub Pages deployment for a repository.

        The authenticated user must have write permission to the repository.

        Args:
          oidc_token: The OIDC token issued by GitHub Actions certifying the origin of the deployment.

          pages_build_version: A unique string that represents the version of the build for this deployment.

          artifact_id: The ID of an artifact that contains the .zip or .tar of static assets to deploy.
              The artifact belongs to the repository. Either `artifact_id` or `artifact_url`
              are required.

          artifact_url: The URL of an artifact that contains the .zip or .tar of static assets to
              deploy. The artifact belongs to the repository. Either `artifact_id` or
              `artifact_url` are required.

          environment: The target environment for this GitHub Pages deployment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/pages/deployments",
            body=maybe_transform(
                {
                    "oidc_token": oidc_token,
                    "pages_build_version": pages_build_version,
                    "artifact_id": artifact_id,
                    "artifact_url": artifact_url,
                    "environment": environment,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentCreateResponse,
        )

    def cancel(
        self,
        pages_deployment_id: int | str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Cancels a GitHub Pages deployment.

        The authenticated user must have write permissions for the GitHub Pages site.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/repos/{owner}/{repo}/pages/deployments/{pages_deployment_id}/cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_status(
        self,
        pages_deployment_id: int | str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentGetStatusResponse:
        """
        Gets the current status of a GitHub Pages deployment.

        The authenticated user must have read permission for the GitHub Pages site.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/pages/deployments/{pages_deployment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentGetStatusResponse,
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDeploymentsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        oidc_token: str,
        pages_build_version: str,
        artifact_id: float | NotGiven = NOT_GIVEN,
        artifact_url: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentCreateResponse:
        """
        Create a GitHub Pages deployment for a repository.

        The authenticated user must have write permission to the repository.

        Args:
          oidc_token: The OIDC token issued by GitHub Actions certifying the origin of the deployment.

          pages_build_version: A unique string that represents the version of the build for this deployment.

          artifact_id: The ID of an artifact that contains the .zip or .tar of static assets to deploy.
              The artifact belongs to the repository. Either `artifact_id` or `artifact_url`
              are required.

          artifact_url: The URL of an artifact that contains the .zip or .tar of static assets to
              deploy. The artifact belongs to the repository. Either `artifact_id` or
              `artifact_url` are required.

          environment: The target environment for this GitHub Pages deployment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/pages/deployments",
            body=await async_maybe_transform(
                {
                    "oidc_token": oidc_token,
                    "pages_build_version": pages_build_version,
                    "artifact_id": artifact_id,
                    "artifact_url": artifact_url,
                    "environment": environment,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentCreateResponse,
        )

    async def cancel(
        self,
        pages_deployment_id: int | str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Cancels a GitHub Pages deployment.

        The authenticated user must have write permissions for the GitHub Pages site.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/repos/{owner}/{repo}/pages/deployments/{pages_deployment_id}/cancel",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_status(
        self,
        pages_deployment_id: int | str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentGetStatusResponse:
        """
        Gets the current status of a GitHub Pages deployment.

        The authenticated user must have read permission for the GitHub Pages site.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/pages/deployments/{pages_deployment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentGetStatusResponse,
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_raw_response_wrapper(
            deployments.create,
        )
        self.cancel = to_raw_response_wrapper(
            deployments.cancel,
        )
        self.get_status = to_raw_response_wrapper(
            deployments.get_status,
        )


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_raw_response_wrapper(
            deployments.create,
        )
        self.cancel = async_to_raw_response_wrapper(
            deployments.cancel,
        )
        self.get_status = async_to_raw_response_wrapper(
            deployments.get_status,
        )


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_streamed_response_wrapper(
            deployments.create,
        )
        self.cancel = to_streamed_response_wrapper(
            deployments.cancel,
        )
        self.get_status = to_streamed_response_wrapper(
            deployments.get_status,
        )


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_streamed_response_wrapper(
            deployments.create,
        )
        self.cancel = async_to_streamed_response_wrapper(
            deployments.cancel,
        )
        self.get_status = async_to_streamed_response_wrapper(
            deployments.get_status,
        )
