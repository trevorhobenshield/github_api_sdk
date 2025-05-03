from __future__ import annotations

from typing import Iterable

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
from .....types.repos.actions.runs import pending_deployment_review_params
from .....types.repos.actions.runs.pending_deployment_list_response import PendingDeploymentListResponse
from .....types.repos.actions.runs.pending_deployment_review_response import PendingDeploymentReviewResponse

__all__ = ["PendingDeploymentsResource", "AsyncPendingDeploymentsResource"]


class PendingDeploymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PendingDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PendingDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PendingDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PendingDeploymentsResourceWithStreamingResponse(self)

    def list(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PendingDeploymentListResponse:
        """
        Get all deployment environments for a workflow run that are waiting for
        protection rules to pass.

        Anyone with read access to the repository can use this endpoint.

        If the repository is private, OAuth tokens and personal access tokens (classic)
        need the `repo` scope to use this endpoint.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PendingDeploymentListResponse,
        )

    def review(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        comment: str,
        environment_ids: Iterable[int],
        state: Literal["approved", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PendingDeploymentReviewResponse:
        """
        Approve or reject pending deployments that are waiting on approval by a required
        reviewer.

        Required reviewers with read access to the repository contents and deployments
        can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          comment: A comment to accompany the deployment review

          environment_ids: The list of environment ids to approve or reject

          state: Whether to approve or reject deployment to the specified environments.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments",
            body=maybe_transform(
                {
                    "comment": comment,
                    "environment_ids": environment_ids,
                    "state": state,
                },
                pending_deployment_review_params.PendingDeploymentReviewParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PendingDeploymentReviewResponse,
        )


class AsyncPendingDeploymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPendingDeploymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPendingDeploymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPendingDeploymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPendingDeploymentsResourceWithStreamingResponse(self)

    async def list(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PendingDeploymentListResponse:
        """
        Get all deployment environments for a workflow run that are waiting for
        protection rules to pass.

        Anyone with read access to the repository can use this endpoint.

        If the repository is private, OAuth tokens and personal access tokens (classic)
        need the `repo` scope to use this endpoint.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PendingDeploymentListResponse,
        )

    async def review(
        self,
        run_id: int,
        *,
        owner: str,
        repo: str,
        comment: str,
        environment_ids: Iterable[int],
        state: Literal["approved", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PendingDeploymentReviewResponse:
        """
        Approve or reject pending deployments that are waiting on approval by a required
        reviewer.

        Required reviewers with read access to the repository contents and deployments
        can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          comment: A comment to accompany the deployment review

          environment_ids: The list of environment ids to approve or reject

          state: Whether to approve or reject deployment to the specified environments.

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
            f"/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments",
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "environment_ids": environment_ids,
                    "state": state,
                },
                pending_deployment_review_params.PendingDeploymentReviewParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PendingDeploymentReviewResponse,
        )


class PendingDeploymentsResourceWithRawResponse:
    def __init__(self, pending_deployments: PendingDeploymentsResource) -> None:
        self._pending_deployments = pending_deployments

        self.list = to_raw_response_wrapper(
            pending_deployments.list,
        )
        self.review = to_raw_response_wrapper(
            pending_deployments.review,
        )


class AsyncPendingDeploymentsResourceWithRawResponse:
    def __init__(self, pending_deployments: AsyncPendingDeploymentsResource) -> None:
        self._pending_deployments = pending_deployments

        self.list = async_to_raw_response_wrapper(
            pending_deployments.list,
        )
        self.review = async_to_raw_response_wrapper(
            pending_deployments.review,
        )


class PendingDeploymentsResourceWithStreamingResponse:
    def __init__(self, pending_deployments: PendingDeploymentsResource) -> None:
        self._pending_deployments = pending_deployments

        self.list = to_streamed_response_wrapper(
            pending_deployments.list,
        )
        self.review = to_streamed_response_wrapper(
            pending_deployments.review,
        )


class AsyncPendingDeploymentsResourceWithStreamingResponse:
    def __init__(self, pending_deployments: AsyncPendingDeploymentsResource) -> None:
        self._pending_deployments = pending_deployments

        self.list = async_to_streamed_response_wrapper(
            pending_deployments.list,
        )
        self.review = async_to_streamed_response_wrapper(
            pending_deployments.review,
        )
