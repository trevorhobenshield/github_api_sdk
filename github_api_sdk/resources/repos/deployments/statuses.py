from __future__ import annotations

import httpx
from typing_extensions import Literal

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
from ....types.repos.deployments import status_create_params, status_list_params
from ....types.repos.deployments.deployment_status import DeploymentStatus
from ....types.repos.deployments.status_list_response import StatusListResponse

__all__ = ["StatusesResource", "AsyncStatusesResource"]


class StatusesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return StatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return StatusesResourceWithStreamingResponse(self)

    def create(
        self,
        deployment_id: int,
        *,
        owner: str,
        repo: str,
        state: Literal["error", "failure", "inactive", "in_progress", "queued", "pending", "success"],
        auto_inactive: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        environment_url: str | NotGiven = NOT_GIVEN,
        log_url: str | NotGiven = NOT_GIVEN,
        target_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentStatus:
        """
        Users with `push` access can create deployment statuses for a given deployment.

        OAuth app tokens and personal access tokens (classic) need the `repo_deployment`
        scope to use this endpoint.

        Args:
          state: The state of the status. When you set a transient deployment to `inactive`, the
              deployment will be shown as `destroyed` in GitHub.

          auto_inactive: Adds a new `inactive` status to all prior non-transient, non-production
              environment deployments with the same repository and `environment` name as the
              created status's deployment. An `inactive` status is only added to deployments
              that had a `success` state. Default: `true`

          description: A short description of the status. The maximum description length is 140
              characters.

          environment: Name for the target deployment environment, which can be changed when setting a
              deploy status. For example, `production`, `staging`, or `qa`. If not defined,
              the environment of the previous status on the deployment will be used, if it
              exists. Otherwise, the environment of the deployment will be used.

          environment_url: Sets the URL for accessing your environment. Default: `""`

          log_url: The full URL of the deployment's output. This parameter replaces `target_url`.
              We will continue to accept `target_url` to support legacy uses, but we recommend
              replacing `target_url` with `log_url`. Setting `log_url` will automatically set
              `target_url` to the same value. Default: `""`

          target_url: The target URL to associate with this status. This URL should contain output to
              keep the user updated while the task is running or serve as historical
              information for what happened in the deployment.

              > [!NOTE] It's recommended to use the `log_url` parameter, which replaces
              > `target_url`.

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
            f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
            body=maybe_transform(
                {
                    "state": state,
                    "auto_inactive": auto_inactive,
                    "description": description,
                    "environment": environment,
                    "environment_url": environment_url,
                    "log_url": log_url,
                    "target_url": target_url,
                },
                status_create_params.StatusCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentStatus,
        )

    def retrieve(
        self,
        status_id: int,
        *,
        owner: str,
        repo: str,
        deployment_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentStatus:
        """
        Users with pull access can view a deployment status for a deployment:

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
            f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentStatus,
        )

    def list(
        self,
        deployment_id: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusListResponse:
        """
        Users with pull access can view deployment statuses for a deployment:

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
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
                    status_list_params.StatusListParams,
                ),
            ),
            cast_to=StatusListResponse,
        )


class AsyncStatusesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncStatusesResourceWithStreamingResponse(self)

    async def create(
        self,
        deployment_id: int,
        *,
        owner: str,
        repo: str,
        state: Literal["error", "failure", "inactive", "in_progress", "queued", "pending", "success"],
        auto_inactive: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        environment_url: str | NotGiven = NOT_GIVEN,
        log_url: str | NotGiven = NOT_GIVEN,
        target_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentStatus:
        """
        Users with `push` access can create deployment statuses for a given deployment.

        OAuth app tokens and personal access tokens (classic) need the `repo_deployment`
        scope to use this endpoint.

        Args:
          state: The state of the status. When you set a transient deployment to `inactive`, the
              deployment will be shown as `destroyed` in GitHub.

          auto_inactive: Adds a new `inactive` status to all prior non-transient, non-production
              environment deployments with the same repository and `environment` name as the
              created status's deployment. An `inactive` status is only added to deployments
              that had a `success` state. Default: `true`

          description: A short description of the status. The maximum description length is 140
              characters.

          environment: Name for the target deployment environment, which can be changed when setting a
              deploy status. For example, `production`, `staging`, or `qa`. If not defined,
              the environment of the previous status on the deployment will be used, if it
              exists. Otherwise, the environment of the deployment will be used.

          environment_url: Sets the URL for accessing your environment. Default: `""`

          log_url: The full URL of the deployment's output. This parameter replaces `target_url`.
              We will continue to accept `target_url` to support legacy uses, but we recommend
              replacing `target_url` with `log_url`. Setting `log_url` will automatically set
              `target_url` to the same value. Default: `""`

          target_url: The target URL to associate with this status. This URL should contain output to
              keep the user updated while the task is running or serve as historical
              information for what happened in the deployment.

              > [!NOTE] It's recommended to use the `log_url` parameter, which replaces
              > `target_url`.

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
            f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
            body=await async_maybe_transform(
                {
                    "state": state,
                    "auto_inactive": auto_inactive,
                    "description": description,
                    "environment": environment,
                    "environment_url": environment_url,
                    "log_url": log_url,
                    "target_url": target_url,
                },
                status_create_params.StatusCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentStatus,
        )

    async def retrieve(
        self,
        status_id: int,
        *,
        owner: str,
        repo: str,
        deployment_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentStatus:
        """
        Users with pull access can view a deployment status for a deployment:

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
            f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentStatus,
        )

    async def list(
        self,
        deployment_id: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StatusListResponse:
        """
        Users with pull access can view deployment statuses for a deployment:

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
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
                    status_list_params.StatusListParams,
                ),
            ),
            cast_to=StatusListResponse,
        )


class StatusesResourceWithRawResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

        self.create = to_raw_response_wrapper(
            statuses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            statuses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            statuses.list,
        )


class AsyncStatusesResourceWithRawResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

        self.create = async_to_raw_response_wrapper(
            statuses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            statuses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            statuses.list,
        )


class StatusesResourceWithStreamingResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

        self.create = to_streamed_response_wrapper(
            statuses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            statuses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            statuses.list,
        )


class AsyncStatusesResourceWithStreamingResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

        self.create = async_to_streamed_response_wrapper(
            statuses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            statuses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            statuses.list,
        )
