from __future__ import annotations

from typing import Iterable

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
from ....types.orgs import RepositoryRuleEnforcement
from ....types.orgs.repository_rule_enforcement import RepositoryRuleEnforcement
from ....types.orgs.repository_rule_param import RepositoryRuleParam
from ....types.orgs.repository_ruleset import RepositoryRuleset
from ....types.orgs.repository_ruleset_bypass_actor_param import RepositoryRulesetBypassActorParam
from ....types.repos import (
    ruleset_create_params,
    ruleset_list_params,
    ruleset_retrieve_params,
    ruleset_update_params,
)
from ....types.repos.repository_ruleset_conditions_param import RepositoryRulesetConditionsParam
from ....types.repos.ruleset_list_response import RulesetListResponse
from .history import (
    AsyncHistoryResource,
    AsyncHistoryResourceWithRawResponse,
    AsyncHistoryResourceWithStreamingResponse,
    HistoryResource,
    HistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
)
from .rule_suites import (
    AsyncRuleSuitesResource,
    AsyncRuleSuitesResourceWithRawResponse,
    AsyncRuleSuitesResourceWithStreamingResponse,
    RuleSuitesResource,
    RuleSuitesResourceWithRawResponse,
    RuleSuitesResourceWithStreamingResponse,
)

__all__ = ["RulesetsResource", "AsyncRulesetsResource"]


class RulesetsResource(SyncAPIResource):
    @cached_property
    def rule_suites(self) -> RuleSuitesResource:
        return RuleSuitesResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> RulesetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RulesetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RulesetsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        enforcement: RepositoryRuleEnforcement,
        name: str,
        bypass_actors: Iterable[RepositoryRulesetBypassActorParam] | NotGiven = NOT_GIVEN,
        conditions: RepositoryRulesetConditionsParam | NotGiven = NOT_GIVEN,
        rules: Iterable[RepositoryRuleParam] | NotGiven = NOT_GIVEN,
        target: Literal["branch", "tag", "push"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryRuleset:
        """
        Create a ruleset for a repository.

        Args:
          enforcement: The enforcement level of the ruleset. `evaluate` allows admins to test rules
              before enforcing them. Admins can view insights on the Rule Insights page
              (`evaluate` is only available with GitHub Enterprise).

          name: The name of the ruleset.

          bypass_actors: The actors that can bypass the rules in this ruleset

          conditions: Parameters for a repository ruleset ref name condition

          rules: An array of rules within the ruleset.

          target: The target of the ruleset

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
            f"/repos/{owner}/{repo}/rulesets",
            body=maybe_transform(
                {
                    "enforcement": enforcement,
                    "name": name,
                    "bypass_actors": bypass_actors,
                    "conditions": conditions,
                    "rules": rules,
                    "target": target,
                },
                ruleset_create_params.RulesetCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryRuleset,
        )

    def retrieve(
        self,
        ruleset_id: int,
        *,
        owner: str,
        repo: str,
        includes_parents: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryRuleset:
        """
        Get a ruleset for a repository.

        **Note:** To prevent leaking sensitive information, the `bypass_actors` property
        is only returned if the user making the API request has write access to the
        ruleset.

        Args:
          includes_parents: Include rulesets configured at higher levels that apply to this repository

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
            f"/repos/{owner}/{repo}/rulesets/{ruleset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"includes_parents": includes_parents}, ruleset_retrieve_params.RulesetRetrieveParams),
            ),
            cast_to=RepositoryRuleset,
        )

    def update(
        self,
        ruleset_id: int,
        *,
        owner: str,
        repo: str,
        bypass_actors: Iterable[RepositoryRulesetBypassActorParam] | NotGiven = NOT_GIVEN,
        conditions: RepositoryRulesetConditionsParam | NotGiven = NOT_GIVEN,
        enforcement: RepositoryRuleEnforcement | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        rules: Iterable[RepositoryRuleParam] | NotGiven = NOT_GIVEN,
        target: Literal["branch", "tag", "push"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryRuleset:
        """
        Update a ruleset for a repository.

        Args:
          bypass_actors: The actors that can bypass the rules in this ruleset

          conditions: Parameters for a repository ruleset ref name condition

          enforcement: The enforcement level of the ruleset. `evaluate` allows admins to test rules
              before enforcing them. Admins can view insights on the Rule Insights page
              (`evaluate` is only available with GitHub Enterprise).

          name: The name of the ruleset.

          rules: An array of rules within the ruleset.

          target: The target of the ruleset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._put(
            f"/repos/{owner}/{repo}/rulesets/{ruleset_id}",
            body=maybe_transform(
                {
                    "bypass_actors": bypass_actors,
                    "conditions": conditions,
                    "enforcement": enforcement,
                    "name": name,
                    "rules": rules,
                    "target": target,
                },
                ruleset_update_params.RulesetUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryRuleset,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        includes_parents: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        targets: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetListResponse:
        """
        Get all the rulesets for a repository.

        Args:
          includes_parents: Include rulesets configured at higher levels that apply to this repository

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          targets: A comma-separated list of rule targets to filter by. If provided, only rulesets
              that apply to the specified targets will be returned. For example,
              `branch,tag,push`.

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
            f"/repos/{owner}/{repo}/rulesets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "includes_parents": includes_parents,
                        "page": page,
                        "per_page": per_page,
                        "targets": targets,
                    },
                    ruleset_list_params.RulesetListParams,
                ),
            ),
            cast_to=RulesetListResponse,
        )

    def delete(
        self,
        ruleset_id: int,
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
        Delete a ruleset for a repository.

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
            f"/repos/{owner}/{repo}/rulesets/{ruleset_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncRulesetsResource(AsyncAPIResource):
    @cached_property
    def rule_suites(self) -> AsyncRuleSuitesResource:
        return AsyncRuleSuitesResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRulesetsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        enforcement: RepositoryRuleEnforcement,
        name: str,
        bypass_actors: Iterable[RepositoryRulesetBypassActorParam] | NotGiven = NOT_GIVEN,
        conditions: RepositoryRulesetConditionsParam | NotGiven = NOT_GIVEN,
        rules: Iterable[RepositoryRuleParam] | NotGiven = NOT_GIVEN,
        target: Literal["branch", "tag", "push"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryRuleset:
        """
        Create a ruleset for a repository.

        Args:
          enforcement: The enforcement level of the ruleset. `evaluate` allows admins to test rules
              before enforcing them. Admins can view insights on the Rule Insights page
              (`evaluate` is only available with GitHub Enterprise).

          name: The name of the ruleset.

          bypass_actors: The actors that can bypass the rules in this ruleset

          conditions: Parameters for a repository ruleset ref name condition

          rules: An array of rules within the ruleset.

          target: The target of the ruleset

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
            f"/repos/{owner}/{repo}/rulesets",
            body=await async_maybe_transform(
                {
                    "enforcement": enforcement,
                    "name": name,
                    "bypass_actors": bypass_actors,
                    "conditions": conditions,
                    "rules": rules,
                    "target": target,
                },
                ruleset_create_params.RulesetCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryRuleset,
        )

    async def retrieve(
        self,
        ruleset_id: int,
        *,
        owner: str,
        repo: str,
        includes_parents: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryRuleset:
        """
        Get a ruleset for a repository.

        **Note:** To prevent leaking sensitive information, the `bypass_actors` property
        is only returned if the user making the API request has write access to the
        ruleset.

        Args:
          includes_parents: Include rulesets configured at higher levels that apply to this repository

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
            f"/repos/{owner}/{repo}/rulesets/{ruleset_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"includes_parents": includes_parents}, ruleset_retrieve_params.RulesetRetrieveParams),
            ),
            cast_to=RepositoryRuleset,
        )

    async def update(
        self,
        ruleset_id: int,
        *,
        owner: str,
        repo: str,
        bypass_actors: Iterable[RepositoryRulesetBypassActorParam] | NotGiven = NOT_GIVEN,
        conditions: RepositoryRulesetConditionsParam | NotGiven = NOT_GIVEN,
        enforcement: RepositoryRuleEnforcement | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        rules: Iterable[RepositoryRuleParam] | NotGiven = NOT_GIVEN,
        target: Literal["branch", "tag", "push"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryRuleset:
        """
        Update a ruleset for a repository.

        Args:
          bypass_actors: The actors that can bypass the rules in this ruleset

          conditions: Parameters for a repository ruleset ref name condition

          enforcement: The enforcement level of the ruleset. `evaluate` allows admins to test rules
              before enforcing them. Admins can view insights on the Rule Insights page
              (`evaluate` is only available with GitHub Enterprise).

          name: The name of the ruleset.

          rules: An array of rules within the ruleset.

          target: The target of the ruleset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/rulesets/{ruleset_id}",
            body=await async_maybe_transform(
                {
                    "bypass_actors": bypass_actors,
                    "conditions": conditions,
                    "enforcement": enforcement,
                    "name": name,
                    "rules": rules,
                    "target": target,
                },
                ruleset_update_params.RulesetUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryRuleset,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        includes_parents: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        targets: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetListResponse:
        """
        Get all the rulesets for a repository.

        Args:
          includes_parents: Include rulesets configured at higher levels that apply to this repository

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          targets: A comma-separated list of rule targets to filter by. If provided, only rulesets
              that apply to the specified targets will be returned. For example,
              `branch,tag,push`.

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
            f"/repos/{owner}/{repo}/rulesets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "includes_parents": includes_parents,
                        "page": page,
                        "per_page": per_page,
                        "targets": targets,
                    },
                    ruleset_list_params.RulesetListParams,
                ),
            ),
            cast_to=RulesetListResponse,
        )

    async def delete(
        self,
        ruleset_id: int,
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
        Delete a ruleset for a repository.

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
            f"/repos/{owner}/{repo}/rulesets/{ruleset_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class RulesetsResourceWithRawResponse:
    def __init__(self, rulesets: RulesetsResource) -> None:
        self._rulesets = rulesets

        self.create = to_raw_response_wrapper(
            rulesets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            rulesets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            rulesets.update,
        )
        self.list = to_raw_response_wrapper(
            rulesets.list,
        )
        self.delete = to_raw_response_wrapper(
            rulesets.delete,
        )

    @cached_property
    def rule_suites(self) -> RuleSuitesResourceWithRawResponse:
        return RuleSuitesResourceWithRawResponse(self._rulesets.rule_suites)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._rulesets.history)


class AsyncRulesetsResourceWithRawResponse:
    def __init__(self, rulesets: AsyncRulesetsResource) -> None:
        self._rulesets = rulesets

        self.create = async_to_raw_response_wrapper(
            rulesets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            rulesets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            rulesets.update,
        )
        self.list = async_to_raw_response_wrapper(
            rulesets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rulesets.delete,
        )

    @cached_property
    def rule_suites(self) -> AsyncRuleSuitesResourceWithRawResponse:
        return AsyncRuleSuitesResourceWithRawResponse(self._rulesets.rule_suites)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._rulesets.history)


class RulesetsResourceWithStreamingResponse:
    def __init__(self, rulesets: RulesetsResource) -> None:
        self._rulesets = rulesets

        self.create = to_streamed_response_wrapper(
            rulesets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            rulesets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            rulesets.update,
        )
        self.list = to_streamed_response_wrapper(
            rulesets.list,
        )
        self.delete = to_streamed_response_wrapper(
            rulesets.delete,
        )

    @cached_property
    def rule_suites(self) -> RuleSuitesResourceWithStreamingResponse:
        return RuleSuitesResourceWithStreamingResponse(self._rulesets.rule_suites)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._rulesets.history)


class AsyncRulesetsResourceWithStreamingResponse:
    def __init__(self, rulesets: AsyncRulesetsResource) -> None:
        self._rulesets = rulesets

        self.create = async_to_streamed_response_wrapper(
            rulesets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            rulesets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            rulesets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rulesets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rulesets.delete,
        )

    @cached_property
    def rule_suites(self) -> AsyncRuleSuitesResourceWithStreamingResponse:
        return AsyncRuleSuitesResourceWithStreamingResponse(self._rulesets.rule_suites)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._rulesets.history)
