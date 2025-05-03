from __future__ import annotations

import builtins
from typing import List, Union

import httpx
from typing_extensions import Literal

from .._base_client import make_request_options
from .._compat import cached_property
from .._resource import AsyncAPIResource, SyncAPIResource
from .._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from .._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ..types import SecurityAdvisoryEcosystem, advisory_list_params
from ..types.advisory_list_response import AdvisoryListResponse
from ..types.global_advisory import GlobalAdvisory
from ..types.security_advisory_ecosystem import SecurityAdvisoryEcosystem

__all__ = ["AdvisoriesResource", "AsyncAdvisoriesResource"]


class AdvisoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AdvisoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AdvisoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvisoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AdvisoriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        ghsa_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalAdvisory:
        """
        Gets a global security advisory using its GitHub Security Advisory (GHSA)
        identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return self._get(
            f"/advisories/{ghsa_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GlobalAdvisory,
        )

    def list(
        self,
        *,
        affects: str | builtins.list[str] | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        cve_id: str | NotGiven = NOT_GIVEN,
        cwes: str | builtins.list[str] | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        ecosystem: SecurityAdvisoryEcosystem | NotGiven = NOT_GIVEN,
        epss_percentage: str | NotGiven = NOT_GIVEN,
        epss_percentile: str | NotGiven = NOT_GIVEN,
        ghsa_id: str | NotGiven = NOT_GIVEN,
        is_withdrawn: bool | NotGiven = NOT_GIVEN,
        modified: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        published: str | NotGiven = NOT_GIVEN,
        severity: Literal["unknown", "low", "medium", "high", "critical"] | NotGiven = NOT_GIVEN,
        sort: Literal["updated", "published", "epss_percentage", "epss_percentile"] | NotGiven = NOT_GIVEN,
        type: Literal["reviewed", "malware", "unreviewed"] | NotGiven = NOT_GIVEN,
        updated: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdvisoryListResponse:
        """Lists all global security advisories that match the specified parameters.

        If no
        other parameters are defined, the request will return only GitHub-reviewed
        advisories that are not malware.

        By default, all responses will exclude advisories for malware, because malware
        are not standard vulnerabilities. To list advisories for malware, you must
        include the `type` parameter in your request, with the value `malware`. For more
        information about the different types of security advisories, see
        "[About the GitHub Advisory database](https://docs.github.com/code-security/security-advisories/global-security-advisories/about-the-github-advisory-database#about-types-of-security-advisories)."

        Args:
          affects: If specified, only return advisories that affect any of `package` or
              `package@version`. A maximum of 1000 packages can be specified. If the query
              parameter causes the URL to exceed the maximum URL length supported by your
              client, you must specify fewer packages.

              Example: `affects=package1,package2@1.0.0,package3@^2.0.0` or
              `affects[]=package1&affects[]=package2@1.0.0`

          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          cve_id: If specified, only advisories with this CVE (Common Vulnerabilities and
              Exposures) identifier will be returned.

          cwes: If specified, only advisories with these Common Weakness Enumerations (CWEs)
              will be returned.

              Example: `cwes=79,284,22` or `cwes[]=79&cwes[]=284&cwes[]=22`

          direction: The direction to sort the results by.

          ecosystem: If specified, only advisories for these ecosystems will be returned.

          epss_percentage: If specified, only return advisories that have an EPSS percentage score that
              matches the provided value. The EPSS percentage represents the likelihood of a
              CVE being exploited.

          epss_percentile: If specified, only return advisories that have an EPSS percentile score that
              matches the provided value. The EPSS percentile represents the relative rank of
              the CVE's likelihood of being exploited compared to other CVEs.

          ghsa_id: If specified, only advisories with this GHSA (GitHub Security Advisory)
              identifier will be returned.

          is_withdrawn: Whether to only return advisories that have been withdrawn.

          modified: If specified, only show advisories that were updated or published on a date or
              date range.

              For more information on the syntax of the date range, see
              "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          published: If specified, only return advisories that were published on a date or date
              range.

              For more information on the syntax of the date range, see
              "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."

          severity: If specified, only advisories with these severities will be returned.

          sort: The property to sort the results by.

          type: If specified, only advisories of this type will be returned. By default, a
              request with no other parameters defined will only return reviewed advisories
              that are not malware.

          updated: If specified, only return advisories that were updated on a date or date range.

              For more information on the syntax of the date range, see
              "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/advisories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "affects": affects,
                        "after": after,
                        "before": before,
                        "cve_id": cve_id,
                        "cwes": cwes,
                        "direction": direction,
                        "ecosystem": ecosystem,
                        "epss_percentage": epss_percentage,
                        "epss_percentile": epss_percentile,
                        "ghsa_id": ghsa_id,
                        "is_withdrawn": is_withdrawn,
                        "modified": modified,
                        "per_page": per_page,
                        "published": published,
                        "severity": severity,
                        "sort": sort,
                        "type": type,
                        "updated": updated,
                    },
                    advisory_list_params.AdvisoryListParams,
                ),
            ),
            cast_to=AdvisoryListResponse,
        )


class AsyncAdvisoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAdvisoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvisoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvisoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAdvisoriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        ghsa_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalAdvisory:
        """
        Gets a global security advisory using its GitHub Security Advisory (GHSA)
        identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return await self._get(
            f"/advisories/{ghsa_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GlobalAdvisory,
        )

    async def list(
        self,
        *,
        affects: str | builtins.list[str] | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        cve_id: str | NotGiven = NOT_GIVEN,
        cwes: str | builtins.list[str] | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        ecosystem: SecurityAdvisoryEcosystem | NotGiven = NOT_GIVEN,
        epss_percentage: str | NotGiven = NOT_GIVEN,
        epss_percentile: str | NotGiven = NOT_GIVEN,
        ghsa_id: str | NotGiven = NOT_GIVEN,
        is_withdrawn: bool | NotGiven = NOT_GIVEN,
        modified: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        published: str | NotGiven = NOT_GIVEN,
        severity: Literal["unknown", "low", "medium", "high", "critical"] | NotGiven = NOT_GIVEN,
        sort: Literal["updated", "published", "epss_percentage", "epss_percentile"] | NotGiven = NOT_GIVEN,
        type: Literal["reviewed", "malware", "unreviewed"] | NotGiven = NOT_GIVEN,
        updated: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AdvisoryListResponse:
        """Lists all global security advisories that match the specified parameters.

        If no
        other parameters are defined, the request will return only GitHub-reviewed
        advisories that are not malware.

        By default, all responses will exclude advisories for malware, because malware
        are not standard vulnerabilities. To list advisories for malware, you must
        include the `type` parameter in your request, with the value `malware`. For more
        information about the different types of security advisories, see
        "[About the GitHub Advisory database](https://docs.github.com/code-security/security-advisories/global-security-advisories/about-the-github-advisory-database#about-types-of-security-advisories)."

        Args:
          affects: If specified, only return advisories that affect any of `package` or
              `package@version`. A maximum of 1000 packages can be specified. If the query
              parameter causes the URL to exceed the maximum URL length supported by your
              client, you must specify fewer packages.

              Example: `affects=package1,package2@1.0.0,package3@^2.0.0` or
              `affects[]=package1&affects[]=package2@1.0.0`

          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          cve_id: If specified, only advisories with this CVE (Common Vulnerabilities and
              Exposures) identifier will be returned.

          cwes: If specified, only advisories with these Common Weakness Enumerations (CWEs)
              will be returned.

              Example: `cwes=79,284,22` or `cwes[]=79&cwes[]=284&cwes[]=22`

          direction: The direction to sort the results by.

          ecosystem: If specified, only advisories for these ecosystems will be returned.

          epss_percentage: If specified, only return advisories that have an EPSS percentage score that
              matches the provided value. The EPSS percentage represents the likelihood of a
              CVE being exploited.

          epss_percentile: If specified, only return advisories that have an EPSS percentile score that
              matches the provided value. The EPSS percentile represents the relative rank of
              the CVE's likelihood of being exploited compared to other CVEs.

          ghsa_id: If specified, only advisories with this GHSA (GitHub Security Advisory)
              identifier will be returned.

          is_withdrawn: Whether to only return advisories that have been withdrawn.

          modified: If specified, only show advisories that were updated or published on a date or
              date range.

              For more information on the syntax of the date range, see
              "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          published: If specified, only return advisories that were published on a date or date
              range.

              For more information on the syntax of the date range, see
              "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."

          severity: If specified, only advisories with these severities will be returned.

          sort: The property to sort the results by.

          type: If specified, only advisories of this type will be returned. By default, a
              request with no other parameters defined will only return reviewed advisories
              that are not malware.

          updated: If specified, only return advisories that were updated on a date or date range.

              For more information on the syntax of the date range, see
              "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/advisories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "affects": affects,
                        "after": after,
                        "before": before,
                        "cve_id": cve_id,
                        "cwes": cwes,
                        "direction": direction,
                        "ecosystem": ecosystem,
                        "epss_percentage": epss_percentage,
                        "epss_percentile": epss_percentile,
                        "ghsa_id": ghsa_id,
                        "is_withdrawn": is_withdrawn,
                        "modified": modified,
                        "per_page": per_page,
                        "published": published,
                        "severity": severity,
                        "sort": sort,
                        "type": type,
                        "updated": updated,
                    },
                    advisory_list_params.AdvisoryListParams,
                ),
            ),
            cast_to=AdvisoryListResponse,
        )


class AdvisoriesResourceWithRawResponse:
    def __init__(self, advisories: AdvisoriesResource) -> None:
        self._advisories = advisories

        self.retrieve = to_raw_response_wrapper(
            advisories.retrieve,
        )
        self.list = to_raw_response_wrapper(
            advisories.list,
        )


class AsyncAdvisoriesResourceWithRawResponse:
    def __init__(self, advisories: AsyncAdvisoriesResource) -> None:
        self._advisories = advisories

        self.retrieve = async_to_raw_response_wrapper(
            advisories.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            advisories.list,
        )


class AdvisoriesResourceWithStreamingResponse:
    def __init__(self, advisories: AdvisoriesResource) -> None:
        self._advisories = advisories

        self.retrieve = to_streamed_response_wrapper(
            advisories.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            advisories.list,
        )


class AsyncAdvisoriesResourceWithStreamingResponse:
    def __init__(self, advisories: AsyncAdvisoriesResource) -> None:
        self._advisories = advisories

        self.retrieve = async_to_streamed_response_wrapper(
            advisories.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            advisories.list,
        )
