from __future__ import annotations

from typing import Iterable, Optional

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
from ....types.repos import environment_create_or_update_params, environment_list_params
from ....types.repos.deployment_branch_policy_settings_param import DeploymentBranchPolicySettingsParam
from ....types.repos.environment import Environment
from ....types.repos.environment_list_response import EnvironmentListResponse
from .deployment_branch_policies import (
    AsyncDeploymentBranchPoliciesResource,
    AsyncDeploymentBranchPoliciesResourceWithRawResponse,
    AsyncDeploymentBranchPoliciesResourceWithStreamingResponse,
    DeploymentBranchPoliciesResource,
    DeploymentBranchPoliciesResourceWithRawResponse,
    DeploymentBranchPoliciesResourceWithStreamingResponse,
)
from .deployment_protection_rules import (
    AsyncDeploymentProtectionRulesResource,
    AsyncDeploymentProtectionRulesResourceWithRawResponse,
    AsyncDeploymentProtectionRulesResourceWithStreamingResponse,
    DeploymentProtectionRulesResource,
    DeploymentProtectionRulesResourceWithRawResponse,
    DeploymentProtectionRulesResourceWithStreamingResponse,
)
from .secrets import (
    AsyncSecretsResource,
    AsyncSecretsResourceWithRawResponse,
    AsyncSecretsResourceWithStreamingResponse,
    SecretsResource,
    SecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
)
from .variables import (
    AsyncVariablesResource,
    AsyncVariablesResourceWithRawResponse,
    AsyncVariablesResourceWithStreamingResponse,
    VariablesResource,
    VariablesResourceWithRawResponse,
    VariablesResourceWithStreamingResponse,
)

__all__ = ["EnvironmentsResource", "AsyncEnvironmentsResource"]


class EnvironmentsResource(SyncAPIResource):
    @cached_property
    def deployment_branch_policies(self) -> DeploymentBranchPoliciesResource:
        return DeploymentBranchPoliciesResource(self._client)

    @cached_property
    def deployment_protection_rules(self) -> DeploymentProtectionRulesResource:
        return DeploymentProtectionRulesResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def variables(self) -> VariablesResource:
        return VariablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return EnvironmentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """
        > [!NOTE] To get information about name patterns that branches must match in
        > order to deploy to this environment, see
        > "[Get a deployment branch policy](/rest/deployments/branch-policies#get-a-deployment-branch-policy)."

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
            f"/repos/{owner}/{repo}/environments/{environment_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Environment,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentListResponse:
        """
        Lists the environments for a repository.

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
        return self._get(
            f"/repos/{owner}/{repo}/environments",
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
                    environment_list_params.EnvironmentListParams,
                ),
            ),
            cast_to=EnvironmentListResponse,
        )

    def delete(
        self,
        environment_name: str,
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
            f"/repos/{owner}/{repo}/environments/{environment_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_or_update(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        deployment_branch_policy: DeploymentBranchPolicySettingsParam | None | NotGiven = NOT_GIVEN,
        prevent_self_review: bool | NotGiven = NOT_GIVEN,
        reviewers: Iterable[environment_create_or_update_params.Reviewer] | None | NotGiven = NOT_GIVEN,
        wait_timer: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """
        Create or update an environment with protection rules, such as required
        reviewers. For more information about environment protection rules, see
        "[Environments](/actions/reference/environments#environment-protection-rules)."

        > [!NOTE] To create or update name patterns that branches must match in order to
        > deploy to this environment, see
        > "[Deployment branch policies](/rest/deployments/branch-policies)."

        > [!NOTE] To create or update secrets for an environment, see
        > "[GitHub Actions secrets](/rest/actions/secrets)."

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          deployment_branch_policy: The type of deployment branch policy for this environment. To allow all branches
              to deploy, set to `null`.

          prevent_self_review: Whether or not a user who created the job is prevented from approving their own
              job.

          reviewers: The people or teams that may review jobs that reference the environment. You can
              list up to six users or teams as reviewers. The reviewers must have at least
              read access to the repository. Only one of the required reviewers needs to
              approve the job for it to proceed.

          wait_timer: The amount of time to delay a job after the job is initially triggered. The time
              (in minutes) must be an integer between 0 and 43,200 (30 days).

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
            f"/repos/{owner}/{repo}/environments/{environment_name}",
            body=maybe_transform(
                {
                    "deployment_branch_policy": deployment_branch_policy,
                    "prevent_self_review": prevent_self_review,
                    "reviewers": reviewers,
                    "wait_timer": wait_timer,
                },
                environment_create_or_update_params.EnvironmentCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Environment,
        )


class AsyncEnvironmentsResource(AsyncAPIResource):
    @cached_property
    def deployment_branch_policies(self) -> AsyncDeploymentBranchPoliciesResource:
        return AsyncDeploymentBranchPoliciesResource(self._client)

    @cached_property
    def deployment_protection_rules(self) -> AsyncDeploymentProtectionRulesResource:
        return AsyncDeploymentProtectionRulesResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def variables(self) -> AsyncVariablesResource:
        return AsyncVariablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncEnvironmentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """
        > [!NOTE] To get information about name patterns that branches must match in
        > order to deploy to this environment, see
        > "[Get a deployment branch policy](/rest/deployments/branch-policies#get-a-deployment-branch-policy)."

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
            f"/repos/{owner}/{repo}/environments/{environment_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Environment,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentListResponse:
        """
        Lists the environments for a repository.

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
        return await self._get(
            f"/repos/{owner}/{repo}/environments",
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
                    environment_list_params.EnvironmentListParams,
                ),
            ),
            cast_to=EnvironmentListResponse,
        )

    async def delete(
        self,
        environment_name: str,
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
            f"/repos/{owner}/{repo}/environments/{environment_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_or_update(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        deployment_branch_policy: DeploymentBranchPolicySettingsParam | None | NotGiven = NOT_GIVEN,
        prevent_self_review: bool | NotGiven = NOT_GIVEN,
        reviewers: Iterable[environment_create_or_update_params.Reviewer] | None | NotGiven = NOT_GIVEN,
        wait_timer: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Environment:
        """
        Create or update an environment with protection rules, such as required
        reviewers. For more information about environment protection rules, see
        "[Environments](/actions/reference/environments#environment-protection-rules)."

        > [!NOTE] To create or update name patterns that branches must match in order to
        > deploy to this environment, see
        > "[Deployment branch policies](/rest/deployments/branch-policies)."

        > [!NOTE] To create or update secrets for an environment, see
        > "[GitHub Actions secrets](/rest/actions/secrets)."

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          deployment_branch_policy: The type of deployment branch policy for this environment. To allow all branches
              to deploy, set to `null`.

          prevent_self_review: Whether or not a user who created the job is prevented from approving their own
              job.

          reviewers: The people or teams that may review jobs that reference the environment. You can
              list up to six users or teams as reviewers. The reviewers must have at least
              read access to the repository. Only one of the required reviewers needs to
              approve the job for it to proceed.

          wait_timer: The amount of time to delay a job after the job is initially triggered. The time
              (in minutes) must be an integer between 0 and 43,200 (30 days).

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
            f"/repos/{owner}/{repo}/environments/{environment_name}",
            body=await async_maybe_transform(
                {
                    "deployment_branch_policy": deployment_branch_policy,
                    "prevent_self_review": prevent_self_review,
                    "reviewers": reviewers,
                    "wait_timer": wait_timer,
                },
                environment_create_or_update_params.EnvironmentCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Environment,
        )


class EnvironmentsResourceWithRawResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.retrieve = to_raw_response_wrapper(
            environments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            environments.list,
        )
        self.delete = to_raw_response_wrapper(
            environments.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            environments.create_or_update,
        )

    @cached_property
    def deployment_branch_policies(self) -> DeploymentBranchPoliciesResourceWithRawResponse:
        return DeploymentBranchPoliciesResourceWithRawResponse(self._environments.deployment_branch_policies)

    @cached_property
    def deployment_protection_rules(self) -> DeploymentProtectionRulesResourceWithRawResponse:
        return DeploymentProtectionRulesResourceWithRawResponse(self._environments.deployment_protection_rules)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._environments.secrets)

    @cached_property
    def variables(self) -> VariablesResourceWithRawResponse:
        return VariablesResourceWithRawResponse(self._environments.variables)


class AsyncEnvironmentsResourceWithRawResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.retrieve = async_to_raw_response_wrapper(
            environments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            environments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            environments.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            environments.create_or_update,
        )

    @cached_property
    def deployment_branch_policies(self) -> AsyncDeploymentBranchPoliciesResourceWithRawResponse:
        return AsyncDeploymentBranchPoliciesResourceWithRawResponse(self._environments.deployment_branch_policies)

    @cached_property
    def deployment_protection_rules(self) -> AsyncDeploymentProtectionRulesResourceWithRawResponse:
        return AsyncDeploymentProtectionRulesResourceWithRawResponse(self._environments.deployment_protection_rules)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._environments.secrets)

    @cached_property
    def variables(self) -> AsyncVariablesResourceWithRawResponse:
        return AsyncVariablesResourceWithRawResponse(self._environments.variables)


class EnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.retrieve = to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            environments.list,
        )
        self.delete = to_streamed_response_wrapper(
            environments.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            environments.create_or_update,
        )

    @cached_property
    def deployment_branch_policies(self) -> DeploymentBranchPoliciesResourceWithStreamingResponse:
        return DeploymentBranchPoliciesResourceWithStreamingResponse(self._environments.deployment_branch_policies)

    @cached_property
    def deployment_protection_rules(self) -> DeploymentProtectionRulesResourceWithStreamingResponse:
        return DeploymentProtectionRulesResourceWithStreamingResponse(self._environments.deployment_protection_rules)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._environments.secrets)

    @cached_property
    def variables(self) -> VariablesResourceWithStreamingResponse:
        return VariablesResourceWithStreamingResponse(self._environments.variables)


class AsyncEnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.retrieve = async_to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            environments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            environments.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            environments.create_or_update,
        )

    @cached_property
    def deployment_branch_policies(self) -> AsyncDeploymentBranchPoliciesResourceWithStreamingResponse:
        return AsyncDeploymentBranchPoliciesResourceWithStreamingResponse(self._environments.deployment_branch_policies)

    @cached_property
    def deployment_protection_rules(self) -> AsyncDeploymentProtectionRulesResourceWithStreamingResponse:
        return AsyncDeploymentProtectionRulesResourceWithStreamingResponse(self._environments.deployment_protection_rules)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._environments.secrets)

    @cached_property
    def variables(self) -> AsyncVariablesResourceWithStreamingResponse:
        return AsyncVariablesResourceWithStreamingResponse(self._environments.variables)
