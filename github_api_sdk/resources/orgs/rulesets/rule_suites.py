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
from ....types.orgs.rulesets import rule_suite_list_params
from ....types.orgs.rulesets.rule_suite import RuleSuite
from ....types.orgs.rulesets.rule_suite_list_response import RuleSuiteListResponse

__all__ = ["RuleSuitesResource", "AsyncRuleSuitesResource"]


class RuleSuitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RuleSuitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RuleSuitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RuleSuitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RuleSuitesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        rule_suite_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleSuite:
        """
        Gets information about a suite of rule evaluations from within an organization.
        For more information, see
        "[Managing rulesets for repositories in your organization](https://docs.github.com/organizations/managing-organization-settings/managing-rulesets-for-repositories-in-your-organization#viewing-insights-for-rulesets)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/rulesets/rule-suites/{rule_suite_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleSuite,
        )

    def list(
        self,
        org: str,
        *,
        actor_name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        repository_name: str | NotGiven = NOT_GIVEN,
        rule_suite_result: Literal["pass", "fail", "bypass", "all"] | NotGiven = NOT_GIVEN,
        time_period: Literal["hour", "day", "week", "month"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleSuiteListResponse:
        """Lists suites of rule evaluations at the organization level.

        For more
        information, see
        "[Managing rulesets for repositories in your organization](https://docs.github.com/organizations/managing-organization-settings/managing-rulesets-for-repositories-in-your-organization#viewing-insights-for-rulesets)."

        Args:
          actor_name: The handle for the GitHub user account to filter on. When specified, only rule
              evaluations triggered by this actor will be returned.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          ref: The name of the ref. Cannot contain wildcard characters. Optionally prefix with
              `refs/heads/` to limit to branches or `refs/tags/` to limit to tags. Omit the
              prefix to search across all refs. When specified, only rule evaluations
              triggered for this ref will be returned.

          repository_name: The name of the repository to filter on.

          rule_suite_result: The rule results to filter on. When specified, only suites with this result will
              be returned.

          time_period: The time period to filter by.

              For example, `day` will filter for rule suites that occurred in the past 24
              hours, and `week` will filter for insights that occurred in the past 7 days (168
              hours).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/rulesets/rule-suites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "actor_name": actor_name,
                        "page": page,
                        "per_page": per_page,
                        "ref": ref,
                        "repository_name": repository_name,
                        "rule_suite_result": rule_suite_result,
                        "time_period": time_period,
                    },
                    rule_suite_list_params.RuleSuiteListParams,
                ),
            ),
            cast_to=RuleSuiteListResponse,
        )


class AsyncRuleSuitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRuleSuitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRuleSuitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRuleSuitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRuleSuitesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        rule_suite_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleSuite:
        """
        Gets information about a suite of rule evaluations from within an organization.
        For more information, see
        "[Managing rulesets for repositories in your organization](https://docs.github.com/organizations/managing-organization-settings/managing-rulesets-for-repositories-in-your-organization#viewing-insights-for-rulesets)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/rulesets/rule-suites/{rule_suite_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RuleSuite,
        )

    async def list(
        self,
        org: str,
        *,
        actor_name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        repository_name: str | NotGiven = NOT_GIVEN,
        rule_suite_result: Literal["pass", "fail", "bypass", "all"] | NotGiven = NOT_GIVEN,
        time_period: Literal["hour", "day", "week", "month"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleSuiteListResponse:
        """Lists suites of rule evaluations at the organization level.

        For more
        information, see
        "[Managing rulesets for repositories in your organization](https://docs.github.com/organizations/managing-organization-settings/managing-rulesets-for-repositories-in-your-organization#viewing-insights-for-rulesets)."

        Args:
          actor_name: The handle for the GitHub user account to filter on. When specified, only rule
              evaluations triggered by this actor will be returned.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          ref: The name of the ref. Cannot contain wildcard characters. Optionally prefix with
              `refs/heads/` to limit to branches or `refs/tags/` to limit to tags. Omit the
              prefix to search across all refs. When specified, only rule evaluations
              triggered for this ref will be returned.

          repository_name: The name of the repository to filter on.

          rule_suite_result: The rule results to filter on. When specified, only suites with this result will
              be returned.

          time_period: The time period to filter by.

              For example, `day` will filter for rule suites that occurred in the past 24
              hours, and `week` will filter for insights that occurred in the past 7 days (168
              hours).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/rulesets/rule-suites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "actor_name": actor_name,
                        "page": page,
                        "per_page": per_page,
                        "ref": ref,
                        "repository_name": repository_name,
                        "rule_suite_result": rule_suite_result,
                        "time_period": time_period,
                    },
                    rule_suite_list_params.RuleSuiteListParams,
                ),
            ),
            cast_to=RuleSuiteListResponse,
        )


class RuleSuitesResourceWithRawResponse:
    def __init__(self, rule_suites: RuleSuitesResource) -> None:
        self._rule_suites = rule_suites

        self.retrieve = to_raw_response_wrapper(
            rule_suites.retrieve,
        )
        self.list = to_raw_response_wrapper(
            rule_suites.list,
        )


class AsyncRuleSuitesResourceWithRawResponse:
    def __init__(self, rule_suites: AsyncRuleSuitesResource) -> None:
        self._rule_suites = rule_suites

        self.retrieve = async_to_raw_response_wrapper(
            rule_suites.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            rule_suites.list,
        )


class RuleSuitesResourceWithStreamingResponse:
    def __init__(self, rule_suites: RuleSuitesResource) -> None:
        self._rule_suites = rule_suites

        self.retrieve = to_streamed_response_wrapper(
            rule_suites.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            rule_suites.list,
        )


class AsyncRuleSuitesResourceWithStreamingResponse:
    def __init__(self, rule_suites: AsyncRuleSuitesResource) -> None:
        self._rule_suites = rule_suites

        self.retrieve = async_to_streamed_response_wrapper(
            rule_suites.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            rule_suites.list,
        )
