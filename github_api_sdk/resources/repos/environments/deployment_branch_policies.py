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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.environments import (
    deployment_branch_policy_create_params,
    deployment_branch_policy_list_params,
    deployment_branch_policy_update_params,
)
from ....types.repos.environments.deployment_branch_policy import DeploymentBranchPolicy
from ....types.repos.environments.deployment_branch_policy_list_response import DeploymentBranchPolicyListResponse

__all__ = ["DeploymentBranchPoliciesResource", "AsyncDeploymentBranchPoliciesResource"]


class DeploymentBranchPoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentBranchPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentBranchPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentBranchPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DeploymentBranchPoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        name: str,
        type: Literal["branch", "tag"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentBranchPolicy:
        """
        Creates a deployment branch or tag policy for an environment.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          name: The name pattern that branches or tags must match in order to deploy to the
              environment.

              Wildcard characters will not match `/`. For example, to match branches that
              begin with `release/` and contain an additional single slash, use `release/*/*`.
              For more information about pattern matching syntax, see the
              [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).

          type: Whether this rule targets a branch or tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._post(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                },
                deployment_branch_policy_create_params.DeploymentBranchPolicyCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentBranchPolicy,
        )

    def retrieve(
        self,
        branch_policy_id: int,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentBranchPolicy:
        """
        Gets a deployment branch or tag policy for an environment.

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._get(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentBranchPolicy,
        )

    def update(
        self,
        branch_policy_id: int,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentBranchPolicy:
        """
        Updates a deployment branch or tag policy for an environment.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          name: The name pattern that branches must match in order to deploy to the environment.

              Wildcard characters will not match `/`. For example, to match branches that
              begin with `release/` and contain an additional single slash, use `release/*/*`.
              For more information about pattern matching syntax, see the
              [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._put(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}",
            body=maybe_transform({"name": name}, deployment_branch_policy_update_params.DeploymentBranchPolicyUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentBranchPolicy,
        )

    def list(
        self,
        environment_name: str,
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
    ) -> DeploymentBranchPolicyListResponse:
        """
        Lists the deployment branch policies for an environment.

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._get(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies",
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
                    deployment_branch_policy_list_params.DeploymentBranchPolicyListParams,
                ),
            ),
            cast_to=DeploymentBranchPolicyListResponse,
        )

    def delete(
        self,
        branch_policy_id: int,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a deployment branch or tag policy for an environment.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncDeploymentBranchPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentBranchPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentBranchPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentBranchPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDeploymentBranchPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        name: str,
        type: Literal["branch", "tag"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentBranchPolicy:
        """
        Creates a deployment branch or tag policy for an environment.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          name: The name pattern that branches or tags must match in order to deploy to the
              environment.

              Wildcard characters will not match `/`. For example, to match branches that
              begin with `release/` and contain an additional single slash, use `release/*/*`.
              For more information about pattern matching syntax, see the
              [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).

          type: Whether this rule targets a branch or tag

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                },
                deployment_branch_policy_create_params.DeploymentBranchPolicyCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentBranchPolicy,
        )

    async def retrieve(
        self,
        branch_policy_id: int,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentBranchPolicy:
        """
        Gets a deployment branch or tag policy for an environment.

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentBranchPolicy,
        )

    async def update(
        self,
        branch_policy_id: int,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentBranchPolicy:
        """
        Updates a deployment branch or tag policy for an environment.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          name: The name pattern that branches must match in order to deploy to the environment.

              Wildcard characters will not match `/`. For example, to match branches that
              begin with `release/` and contain an additional single slash, use `release/*/*`.
              For more information about pattern matching syntax, see the
              [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}",
            body=await async_maybe_transform({"name": name}, deployment_branch_policy_update_params.DeploymentBranchPolicyUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentBranchPolicy,
        )

    async def list(
        self,
        environment_name: str,
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
    ) -> DeploymentBranchPolicyListResponse:
        """
        Lists the deployment branch policies for an environment.

        Anyone with read access to the repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint with a private repository.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies",
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
                    deployment_branch_policy_list_params.DeploymentBranchPolicyListParams,
                ),
            ),
            cast_to=DeploymentBranchPolicyListResponse,
        )

    async def delete(
        self,
        branch_policy_id: int,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a deployment branch or tag policy for an environment.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class DeploymentBranchPoliciesResourceWithRawResponse:
    def __init__(self, deployment_branch_policies: DeploymentBranchPoliciesResource) -> None:
        self._deployment_branch_policies = deployment_branch_policies

        self.create = to_raw_response_wrapper(
            deployment_branch_policies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deployment_branch_policies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            deployment_branch_policies.update,
        )
        self.list = to_raw_response_wrapper(
            deployment_branch_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            deployment_branch_policies.delete,
        )


class AsyncDeploymentBranchPoliciesResourceWithRawResponse:
    def __init__(self, deployment_branch_policies: AsyncDeploymentBranchPoliciesResource) -> None:
        self._deployment_branch_policies = deployment_branch_policies

        self.create = async_to_raw_response_wrapper(
            deployment_branch_policies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deployment_branch_policies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            deployment_branch_policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            deployment_branch_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            deployment_branch_policies.delete,
        )


class DeploymentBranchPoliciesResourceWithStreamingResponse:
    def __init__(self, deployment_branch_policies: DeploymentBranchPoliciesResource) -> None:
        self._deployment_branch_policies = deployment_branch_policies

        self.create = to_streamed_response_wrapper(
            deployment_branch_policies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deployment_branch_policies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            deployment_branch_policies.update,
        )
        self.list = to_streamed_response_wrapper(
            deployment_branch_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            deployment_branch_policies.delete,
        )


class AsyncDeploymentBranchPoliciesResourceWithStreamingResponse:
    def __init__(self, deployment_branch_policies: AsyncDeploymentBranchPoliciesResource) -> None:
        self._deployment_branch_policies = deployment_branch_policies

        self.create = async_to_streamed_response_wrapper(
            deployment_branch_policies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deployment_branch_policies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            deployment_branch_policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            deployment_branch_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            deployment_branch_policies.delete,
        )
