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
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.environments import (
    deployment_protection_rule_create_params,
    deployment_protection_rule_list_integrations_params,
)
from ....types.repos.environments.deployment_protection_rule import DeploymentProtectionRule
from ....types.repos.environments.deployment_protection_rule_list_integrations_response import (
    DeploymentProtectionRuleListIntegrationsResponse,
)
from ....types.repos.environments.deployment_protection_rule_list_response import DeploymentProtectionRuleListResponse

__all__ = ["DeploymentProtectionRulesResource", "AsyncDeploymentProtectionRulesResource"]


class DeploymentProtectionRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DeploymentProtectionRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DeploymentProtectionRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentProtectionRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DeploymentProtectionRulesResourceWithStreamingResponse(self)

    def create(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        integration_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentProtectionRule:
        """
        Enable a custom deployment protection rule for an environment.

        The authenticated user must have admin or owner permissions to the repository to
        use this endpoint.

        For more information about the app that is providing this custom deployment
        rule, see the
        [documentation for the `GET /apps/{app_slug}` endpoint](https://docs.github.com/rest/apps/apps#get-an-app),
        as well as the
        [guide to creating custom deployment protection rules](https://docs.github.com/actions/managing-workflow-runs-and-deployments/managing-deployments/creating-custom-deployment-protection-rules).

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          integration_id: The ID of the custom app that will be enabled on the environment.

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules",
            body=maybe_transform(
                {"integration_id": integration_id},
                deployment_protection_rule_create_params.DeploymentProtectionRuleCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentProtectionRule,
        )

    def retrieve(
        self,
        protection_rule_id: int,
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
    ) -> DeploymentProtectionRule:
        """Gets an enabled custom deployment protection rule for an environment.

        Anyone
        with read access to the repository can use this endpoint. For more information
        about environments, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        For more information about the app that is providing this custom deployment
        rule, see
        [`GET /apps/{app_slug}`](https://docs.github.com/rest/apps/apps#get-an-app).

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentProtectionRule,
        )

    def list(
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
    ) -> DeploymentProtectionRuleListResponse:
        """
        Gets all custom deployment protection rules that are enabled for an environment.
        Anyone with read access to the repository can use this endpoint. For more
        information about environments, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        For more information about the app that is providing this custom deployment
        rule, see the
        [documentation for the `GET /apps/{app_slug}` endpoint](https://docs.github.com/rest/apps/apps#get-an-app).

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentProtectionRuleListResponse,
        )

    def disable(
        self,
        protection_rule_id: int,
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
        Disables a custom deployment protection rule for an environment.

        The authenticated user must have admin or owner permissions to the repository to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_integrations(
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
    ) -> DeploymentProtectionRuleListIntegrationsResponse:
        """
        Gets all custom deployment protection rule integrations that are available for
        an environment.

        The authenticated user must have admin or owner permissions to the repository to
        use this endpoint.

        For more information about environments, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        For more information about the app that is providing this custom deployment
        rule, see "[GET an app](https://docs.github.com/rest/apps/apps#get-an-app)".

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/apps",
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
                    deployment_protection_rule_list_integrations_params.DeploymentProtectionRuleListIntegrationsParams,
                ),
            ),
            cast_to=DeploymentProtectionRuleListIntegrationsResponse,
        )


class AsyncDeploymentProtectionRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDeploymentProtectionRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeploymentProtectionRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentProtectionRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDeploymentProtectionRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        integration_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DeploymentProtectionRule:
        """
        Enable a custom deployment protection rule for an environment.

        The authenticated user must have admin or owner permissions to the repository to
        use this endpoint.

        For more information about the app that is providing this custom deployment
        rule, see the
        [documentation for the `GET /apps/{app_slug}` endpoint](https://docs.github.com/rest/apps/apps#get-an-app),
        as well as the
        [guide to creating custom deployment protection rules](https://docs.github.com/actions/managing-workflow-runs-and-deployments/managing-deployments/creating-custom-deployment-protection-rules).

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          integration_id: The ID of the custom app that will be enabled on the environment.

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules",
            body=await async_maybe_transform(
                {"integration_id": integration_id},
                deployment_protection_rule_create_params.DeploymentProtectionRuleCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentProtectionRule,
        )

    async def retrieve(
        self,
        protection_rule_id: int,
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
    ) -> DeploymentProtectionRule:
        """Gets an enabled custom deployment protection rule for an environment.

        Anyone
        with read access to the repository can use this endpoint. For more information
        about environments, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        For more information about the app that is providing this custom deployment
        rule, see
        [`GET /apps/{app_slug}`](https://docs.github.com/rest/apps/apps#get-an-app).

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentProtectionRule,
        )

    async def list(
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
    ) -> DeploymentProtectionRuleListResponse:
        """
        Gets all custom deployment protection rules that are enabled for an environment.
        Anyone with read access to the repository can use this endpoint. For more
        information about environments, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        For more information about the app that is providing this custom deployment
        rule, see the
        [documentation for the `GET /apps/{app_slug}` endpoint](https://docs.github.com/rest/apps/apps#get-an-app).

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DeploymentProtectionRuleListResponse,
        )

    async def disable(
        self,
        protection_rule_id: int,
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
        Disables a custom deployment protection rule for an environment.

        The authenticated user must have admin or owner permissions to the repository to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_integrations(
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
    ) -> DeploymentProtectionRuleListIntegrationsResponse:
        """
        Gets all custom deployment protection rule integrations that are available for
        an environment.

        The authenticated user must have admin or owner permissions to the repository to
        use this endpoint.

        For more information about environments, see
        "[Using environments for deployment](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)."

        For more information about the app that is providing this custom deployment
        rule, see "[GET an app](https://docs.github.com/rest/apps/apps#get-an-app)".

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
            f"/repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/apps",
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
                    deployment_protection_rule_list_integrations_params.DeploymentProtectionRuleListIntegrationsParams,
                ),
            ),
            cast_to=DeploymentProtectionRuleListIntegrationsResponse,
        )


class DeploymentProtectionRulesResourceWithRawResponse:
    def __init__(self, deployment_protection_rules: DeploymentProtectionRulesResource) -> None:
        self._deployment_protection_rules = deployment_protection_rules

        self.create = to_raw_response_wrapper(
            deployment_protection_rules.create,
        )
        self.retrieve = to_raw_response_wrapper(
            deployment_protection_rules.retrieve,
        )
        self.list = to_raw_response_wrapper(
            deployment_protection_rules.list,
        )
        self.disable = to_raw_response_wrapper(
            deployment_protection_rules.disable,
        )
        self.list_integrations = to_raw_response_wrapper(
            deployment_protection_rules.list_integrations,
        )


class AsyncDeploymentProtectionRulesResourceWithRawResponse:
    def __init__(self, deployment_protection_rules: AsyncDeploymentProtectionRulesResource) -> None:
        self._deployment_protection_rules = deployment_protection_rules

        self.create = async_to_raw_response_wrapper(
            deployment_protection_rules.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            deployment_protection_rules.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            deployment_protection_rules.list,
        )
        self.disable = async_to_raw_response_wrapper(
            deployment_protection_rules.disable,
        )
        self.list_integrations = async_to_raw_response_wrapper(
            deployment_protection_rules.list_integrations,
        )


class DeploymentProtectionRulesResourceWithStreamingResponse:
    def __init__(self, deployment_protection_rules: DeploymentProtectionRulesResource) -> None:
        self._deployment_protection_rules = deployment_protection_rules

        self.create = to_streamed_response_wrapper(
            deployment_protection_rules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            deployment_protection_rules.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            deployment_protection_rules.list,
        )
        self.disable = to_streamed_response_wrapper(
            deployment_protection_rules.disable,
        )
        self.list_integrations = to_streamed_response_wrapper(
            deployment_protection_rules.list_integrations,
        )


class AsyncDeploymentProtectionRulesResourceWithStreamingResponse:
    def __init__(self, deployment_protection_rules: AsyncDeploymentProtectionRulesResource) -> None:
        self._deployment_protection_rules = deployment_protection_rules

        self.create = async_to_streamed_response_wrapper(
            deployment_protection_rules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            deployment_protection_rules.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            deployment_protection_rules.list,
        )
        self.disable = async_to_streamed_response_wrapper(
            deployment_protection_rules.disable,
        )
        self.list_integrations = async_to_streamed_response_wrapper(
            deployment_protection_rules.list_integrations,
        )
