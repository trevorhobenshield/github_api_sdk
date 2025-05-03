from __future__ import annotations

import builtins
from typing import Dict, List, Optional, Union

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
from ....types.repos import deployment_create_params, deployment_list_params
from ....types.repos.deployment import Deployment
from ....types.repos.deployment_list_response import DeploymentListResponse
from .statuses import (
    AsyncStatusesResource,
    AsyncStatusesResourceWithRawResponse,
    AsyncStatusesResourceWithStreamingResponse,
    StatusesResource,
    StatusesResourceWithRawResponse,
    StatusesResourceWithStreamingResponse,
)

__all__ = ["DeploymentsResource", "AsyncDeploymentsResource"]


class DeploymentsResource(SyncAPIResource):
    @cached_property
    def statuses(self) -> StatusesResource:
        return StatusesResource(self._client)

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
        ref: str,
        auto_merge: bool | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        payload: dict[str, object] | str | NotGiven = NOT_GIVEN,
        production_environment: bool | NotGiven = NOT_GIVEN,
        required_contexts: builtins.list[str] | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        transient_environment: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """
        Deployments offer a few configurable parameters with certain defaults.

        The `ref` parameter can be any named branch, tag, or SHA. At GitHub we often
        deploy branches and verify them before we merge a pull request.

        The `environment` parameter allows deployments to be issued to different runtime
        environments. Teams often have multiple environments for verifying their
        applications, such as `production`, `staging`, and `qa`. This parameter makes it
        easier to track which environments have requested deployments. The default
        environment is `production`.

        The `auto_merge` parameter is used to ensure that the requested ref is not
        behind the repository's default branch. If the ref _is_ behind the default
        branch for the repository, we will attempt to merge it for you. If the merge
        succeeds, the API will return a successful merge commit. If merge conflicts
        prevent the merge from succeeding, the API will return a failure response.

        By default, [commit statuses](https://docs.github.com/rest/commits/statuses) for
        every submitted context must be in a `success` state. The `required_contexts`
        parameter allows you to specify a subset of contexts that must be `success`, or
        to specify contexts that have not yet been submitted. You are not required to
        use commit statuses to deploy. If you do not require any contexts or create any
        commit statuses, the deployment will always succeed.

        The `payload` parameter is available for any extra information that a deployment
        system might need. It is a JSON text field that will be passed on when a
        deployment event is dispatched.

        The `task` parameter is used by the deployment system to allow different
        execution paths. In the web world this might be `deploy:migrations` to run
        schema changes on the system. In the compiled world this could be a flag to
        compile an application with debugging enabled.

        Merged branch response:

        You will see this response when GitHub automatically merges the base branch into
        the topic branch instead of creating a deployment. This auto-merge happens when:

        - Auto-merge option is enabled in the repository
        - Topic branch does not include the latest changes on the base branch, which is
          `master` in the response example
        - There are no merge conflicts

        If there are no new commits in the base branch, a new request to create a
        deployment should give a successful response.

        Merge conflict response:

        This error happens when the `auto_merge` option is enabled and when the default
        branch (in this case `master`), can't be merged into the branch that's being
        deployed (in this case `topic-branch`), due to merge conflicts.

        Failed commit status checks:

        This error happens when the `required_contexts` parameter indicates that one or
        more contexts need to have a `success` status for the commit to be deployed, but
        one or more of the required contexts do not have a state of `success`.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repo_deployment` scope to use this endpoint.

        Args:
          ref: The ref to deploy. This can be a branch, tag, or SHA.

          auto_merge: Attempts to automatically merge the default branch into the requested ref, if
              it's behind the default branch.

          description: Short description of the deployment.

          environment: Name for the target deployment environment (e.g., `production`, `staging`,
              `qa`).

          payload: JSON payload with extra information about the deployment.

          production_environment: Specifies if the given environment is one that end-users directly interact with.
              Default: `true` when `environment` is `production` and `false` otherwise.

          required_contexts: The [status](https://docs.github.com/rest/commits/statuses) contexts to verify
              against commit status checks. If you omit this parameter, GitHub verifies all
              unique contexts before creating a deployment. To bypass checking entirely, pass
              an empty array. Defaults to all unique contexts.

          task: Specifies a task to execute (e.g., `deploy` or `deploy:migrations`).

          transient_environment: Specifies if the given environment is specific to the deployment and will no
              longer exist at some point in the future. Default: `false`

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
            f"/repos/{owner}/{repo}/deployments",
            body=maybe_transform(
                {
                    "ref": ref,
                    "auto_merge": auto_merge,
                    "description": description,
                    "environment": environment,
                    "payload": payload,
                    "production_environment": production_environment,
                    "required_contexts": required_contexts,
                    "task": task,
                    "transient_environment": transient_environment,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Deployment,
        )

    def retrieve(
        self,
        deployment_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """
        Get a deployment

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
            f"/repos/{owner}/{repo}/deployments/{deployment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Deployment,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        environment: str | None | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        sha: str | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentListResponse:
        """
        Simple filtering of deployments is available via query parameters:

        Args:
          environment: The name of the environment that was deployed to (e.g., `staging` or
              `production`).

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          ref: The name of the ref. This can be a branch, tag, or SHA.

          sha: The SHA recorded at creation time.

          task: The name of the task for the deployment (e.g., `deploy` or `deploy:migrations`).

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
            f"/repos/{owner}/{repo}/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "page": page,
                        "per_page": per_page,
                        "ref": ref,
                        "sha": sha,
                        "task": task,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            cast_to=DeploymentListResponse,
        )

    def delete(
        self,
        deployment_id: int,
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
        If the repository only has one deployment, you can delete the deployment
        regardless of its status. If the repository has more than one deployment, you
        can only delete inactive deployments. This ensures that repositories with
        multiple deployments will always have an active deployment.

        To set a deployment as inactive, you must:

        - Create a new deployment that is active so that the system has a record of the
          current state, then delete the previously active deployment.
        - Mark the active deployment as inactive by adding any non-successful deployment
          status.

        For more information, see
        "[Create a deployment](https://docs.github.com/rest/deployments/deployments/#create-a-deployment)"
        and
        "[Create a deployment status](https://docs.github.com/rest/deployments/statuses#create-a-deployment-status)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repo_deployment` scope to use this endpoint.

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
        return self._delete(
            f"/repos/{owner}/{repo}/deployments/{deployment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncDeploymentsResource(AsyncAPIResource):
    @cached_property
    def statuses(self) -> AsyncStatusesResource:
        return AsyncStatusesResource(self._client)

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
        ref: str,
        auto_merge: bool | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        payload: dict[str, object] | str | NotGiven = NOT_GIVEN,
        production_environment: bool | NotGiven = NOT_GIVEN,
        required_contexts: builtins.list[str] | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        transient_environment: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """
        Deployments offer a few configurable parameters with certain defaults.

        The `ref` parameter can be any named branch, tag, or SHA. At GitHub we often
        deploy branches and verify them before we merge a pull request.

        The `environment` parameter allows deployments to be issued to different runtime
        environments. Teams often have multiple environments for verifying their
        applications, such as `production`, `staging`, and `qa`. This parameter makes it
        easier to track which environments have requested deployments. The default
        environment is `production`.

        The `auto_merge` parameter is used to ensure that the requested ref is not
        behind the repository's default branch. If the ref _is_ behind the default
        branch for the repository, we will attempt to merge it for you. If the merge
        succeeds, the API will return a successful merge commit. If merge conflicts
        prevent the merge from succeeding, the API will return a failure response.

        By default, [commit statuses](https://docs.github.com/rest/commits/statuses) for
        every submitted context must be in a `success` state. The `required_contexts`
        parameter allows you to specify a subset of contexts that must be `success`, or
        to specify contexts that have not yet been submitted. You are not required to
        use commit statuses to deploy. If you do not require any contexts or create any
        commit statuses, the deployment will always succeed.

        The `payload` parameter is available for any extra information that a deployment
        system might need. It is a JSON text field that will be passed on when a
        deployment event is dispatched.

        The `task` parameter is used by the deployment system to allow different
        execution paths. In the web world this might be `deploy:migrations` to run
        schema changes on the system. In the compiled world this could be a flag to
        compile an application with debugging enabled.

        Merged branch response:

        You will see this response when GitHub automatically merges the base branch into
        the topic branch instead of creating a deployment. This auto-merge happens when:

        - Auto-merge option is enabled in the repository
        - Topic branch does not include the latest changes on the base branch, which is
          `master` in the response example
        - There are no merge conflicts

        If there are no new commits in the base branch, a new request to create a
        deployment should give a successful response.

        Merge conflict response:

        This error happens when the `auto_merge` option is enabled and when the default
        branch (in this case `master`), can't be merged into the branch that's being
        deployed (in this case `topic-branch`), due to merge conflicts.

        Failed commit status checks:

        This error happens when the `required_contexts` parameter indicates that one or
        more contexts need to have a `success` status for the commit to be deployed, but
        one or more of the required contexts do not have a state of `success`.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repo_deployment` scope to use this endpoint.

        Args:
          ref: The ref to deploy. This can be a branch, tag, or SHA.

          auto_merge: Attempts to automatically merge the default branch into the requested ref, if
              it's behind the default branch.

          description: Short description of the deployment.

          environment: Name for the target deployment environment (e.g., `production`, `staging`,
              `qa`).

          payload: JSON payload with extra information about the deployment.

          production_environment: Specifies if the given environment is one that end-users directly interact with.
              Default: `true` when `environment` is `production` and `false` otherwise.

          required_contexts: The [status](https://docs.github.com/rest/commits/statuses) contexts to verify
              against commit status checks. If you omit this parameter, GitHub verifies all
              unique contexts before creating a deployment. To bypass checking entirely, pass
              an empty array. Defaults to all unique contexts.

          task: Specifies a task to execute (e.g., `deploy` or `deploy:migrations`).

          transient_environment: Specifies if the given environment is specific to the deployment and will no
              longer exist at some point in the future. Default: `false`

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
            f"/repos/{owner}/{repo}/deployments",
            body=await async_maybe_transform(
                {
                    "ref": ref,
                    "auto_merge": auto_merge,
                    "description": description,
                    "environment": environment,
                    "payload": payload,
                    "production_environment": production_environment,
                    "required_contexts": required_contexts,
                    "task": task,
                    "transient_environment": transient_environment,
                },
                deployment_create_params.DeploymentCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Deployment,
        )

    async def retrieve(
        self,
        deployment_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Deployment:
        """
        Get a deployment

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
            f"/repos/{owner}/{repo}/deployments/{deployment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Deployment,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        environment: str | None | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        sha: str | NotGiven = NOT_GIVEN,
        task: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentListResponse:
        """
        Simple filtering of deployments is available via query parameters:

        Args:
          environment: The name of the environment that was deployed to (e.g., `staging` or
              `production`).

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          ref: The name of the ref. This can be a branch, tag, or SHA.

          sha: The SHA recorded at creation time.

          task: The name of the task for the deployment (e.g., `deploy` or `deploy:migrations`).

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
            f"/repos/{owner}/{repo}/deployments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "environment": environment,
                        "page": page,
                        "per_page": per_page,
                        "ref": ref,
                        "sha": sha,
                        "task": task,
                    },
                    deployment_list_params.DeploymentListParams,
                ),
            ),
            cast_to=DeploymentListResponse,
        )

    async def delete(
        self,
        deployment_id: int,
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
        If the repository only has one deployment, you can delete the deployment
        regardless of its status. If the repository has more than one deployment, you
        can only delete inactive deployments. This ensures that repositories with
        multiple deployments will always have an active deployment.

        To set a deployment as inactive, you must:

        - Create a new deployment that is active so that the system has a record of the
          current state, then delete the previously active deployment.
        - Mark the active deployment as inactive by adding any non-successful deployment
          status.

        For more information, see
        "[Create a deployment](https://docs.github.com/rest/deployments/deployments/#create-a-deployment)"
        and
        "[Create a deployment status](https://docs.github.com/rest/deployments/statuses#create-a-deployment-status)."

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repo_deployment` scope to use this endpoint.

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
        return await self._delete(
            f"/repos/{owner}/{repo}/deployments/{deployment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class DeploymentsResourceWithRawResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_raw_response_wrapper(
            deployments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deployments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            deployments.list,
        )
        self.delete = to_raw_response_wrapper(
            deployments.delete,
        )

    @cached_property
    def statuses(self) -> StatusesResourceWithRawResponse:
        return StatusesResourceWithRawResponse(self._deployments.statuses)


class AsyncDeploymentsResourceWithRawResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_raw_response_wrapper(
            deployments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deployments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            deployments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            deployments.delete,
        )

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithRawResponse:
        return AsyncStatusesResourceWithRawResponse(self._deployments.statuses)


class DeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: DeploymentsResource) -> None:
        self._deployments = deployments

        self.create = to_streamed_response_wrapper(
            deployments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deployments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            deployments.list,
        )
        self.delete = to_streamed_response_wrapper(
            deployments.delete,
        )

    @cached_property
    def statuses(self) -> StatusesResourceWithStreamingResponse:
        return StatusesResourceWithStreamingResponse(self._deployments.statuses)


class AsyncDeploymentsResourceWithStreamingResponse:
    def __init__(self, deployments: AsyncDeploymentsResource) -> None:
        self._deployments = deployments

        self.create = async_to_streamed_response_wrapper(
            deployments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deployments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            deployments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            deployments.delete,
        )

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithStreamingResponse:
        return AsyncStatusesResourceWithStreamingResponse(self._deployments.statuses)
