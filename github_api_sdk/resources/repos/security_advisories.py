from __future__ import annotations

import builtins
from typing import Iterable, List, Optional

import httpx
from typing_extensions import Literal

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.orgs.full_repository import FullRepository
from ...types.repos import (
    security_advisory_create_params,
    security_advisory_list_params,
    security_advisory_report_params,
    security_advisory_update_params,
)
from ...types.repos.repository_advisory import RepositoryAdvisory
from ...types.repos.security_advisory_list_response import SecurityAdvisoryListResponse

__all__ = ["SecurityAdvisoriesResource", "AsyncSecurityAdvisoriesResource"]


class SecurityAdvisoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecurityAdvisoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SecurityAdvisoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityAdvisoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SecurityAdvisoriesResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        description: str,
        summary: str,
        vulnerabilities: Iterable[security_advisory_create_params.Vulnerability],
        credits: Iterable[security_advisory_create_params.Credit] | None | NotGiven = NOT_GIVEN,
        cve_id: str | None | NotGiven = NOT_GIVEN,
        cvss_vector_string: str | None | NotGiven = NOT_GIVEN,
        cwe_ids: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        severity: Literal["critical", "high", "medium", "low"] | None | NotGiven = NOT_GIVEN,
        start_private_fork: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryAdvisory:
        """
        Creates a new repository security advisory.

        In order to create a draft repository security advisory, the authenticated user
        must be a security manager or administrator of that repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:write` scope to use this endpoint.

        Args:
          description: A detailed description of what the advisory impacts.

          summary: A short summary of the advisory.

          vulnerabilities: A product affected by the vulnerability detailed in a repository security
              advisory.

          credits: A list of users receiving credit for their participation in the security
              advisory.

          cve_id: The Common Vulnerabilities and Exposures (CVE) ID.

          cvss_vector_string: The CVSS vector that calculates the severity of the advisory. You must choose
              between setting this field or `severity`.

          cwe_ids: A list of Common Weakness Enumeration (CWE) IDs.

          severity: The severity of the advisory. You must choose between setting this field or
              `cvss_vector_string`.

          start_private_fork: Whether to create a temporary private fork of the repository to collaborate on a
              fix.

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
            f"/repos/{owner}/{repo}/security-advisories",
            body=maybe_transform(
                {
                    "description": description,
                    "summary": summary,
                    "vulnerabilities": vulnerabilities,
                    "credits": credits,
                    "cve_id": cve_id,
                    "cvss_vector_string": cvss_vector_string,
                    "cwe_ids": cwe_ids,
                    "severity": severity,
                    "start_private_fork": start_private_fork,
                },
                security_advisory_create_params.SecurityAdvisoryCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryAdvisory,
        )

    def retrieve(
        self,
        ghsa_id: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryAdvisory:
        """
        Get a repository security advisory using its GitHub Security Advisory (GHSA)
        identifier.

        Anyone can access any published security advisory on a public repository.

        The authenticated user can access an unpublished security advisory from a
        repository if they are a security manager or administrator of that repository,
        or if they are a collaborator on the security advisory.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:read` scope to to get a published security advisory in a
        private repository, or any unpublished security advisory that the authenticated
        user has access to.

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
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return self._get(
            f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryAdvisory,
        )

    def update(
        self,
        ghsa_id: str,
        *,
        owner: str,
        repo: str,
        collaborating_teams: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        collaborating_users: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        credits: Iterable[security_advisory_update_params.Credit] | None | NotGiven = NOT_GIVEN,
        cve_id: str | None | NotGiven = NOT_GIVEN,
        cvss_vector_string: str | None | NotGiven = NOT_GIVEN,
        cwe_ids: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        severity: Literal["critical", "high", "medium", "low"] | None | NotGiven = NOT_GIVEN,
        state: Literal["published", "closed", "draft"] | NotGiven = NOT_GIVEN,
        summary: str | NotGiven = NOT_GIVEN,
        vulnerabilities: Iterable[security_advisory_update_params.Vulnerability] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryAdvisory:
        """
        Update a repository security advisory using its GitHub Security Advisory (GHSA)
        identifier.

        In order to update any security advisory, the authenticated user must be a
        security manager or administrator of that repository, or a collaborator on the
        repository security advisory.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:write` scope to use this endpoint.

        Args:
          collaborating_teams: A list of team slugs which have been granted write access to the advisory.

          collaborating_users: A list of usernames who have been granted write access to the advisory.

          credits: A list of users receiving credit for their participation in the security
              advisory.

          cve_id: The Common Vulnerabilities and Exposures (CVE) ID.

          cvss_vector_string: The CVSS vector that calculates the severity of the advisory. You must choose
              between setting this field or `severity`.

          cwe_ids: A list of Common Weakness Enumeration (CWE) IDs.

          description: A detailed description of what the advisory impacts.

          severity: The severity of the advisory. You must choose between setting this field or
              `cvss_vector_string`.

          state: The state of the advisory.

          summary: A short summary of the advisory.

          vulnerabilities: A product affected by the vulnerability detailed in a repository security
              advisory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}",
            body=maybe_transform(
                {
                    "collaborating_teams": collaborating_teams,
                    "collaborating_users": collaborating_users,
                    "credits": credits,
                    "cve_id": cve_id,
                    "cvss_vector_string": cvss_vector_string,
                    "cwe_ids": cwe_ids,
                    "description": description,
                    "severity": severity,
                    "state": state,
                    "summary": summary,
                    "vulnerabilities": vulnerabilities,
                },
                security_advisory_update_params.SecurityAdvisoryUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryAdvisory,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "published"] | NotGiven = NOT_GIVEN,
        state: Literal["triage", "draft", "published", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityAdvisoryListResponse:
        """
        Lists security advisories in a repository.

        The authenticated user can access unpublished security advisories from a
        repository if they are a security manager or administrator of that repository,
        or if they are a collaborator on any security advisory.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:read` scope to to get a published security advisory in a
        private repository, or any unpublished security advisory that the authenticated
        user has access to.

        Args:
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

          direction: The direction to sort the results by.

          per_page: The number of advisories to return per page. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          state: Filter by state of the repository advisories. Only advisories of this state will
              be returned.

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
            f"/repos/{owner}/{repo}/security-advisories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    security_advisory_list_params.SecurityAdvisoryListParams,
                ),
            ),
            cast_to=SecurityAdvisoryListResponse,
        )

    def create_fork(
        self,
        ghsa_id: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """
        Create a temporary private fork to collaborate on fixing a security
        vulnerability in your repository.

        > [!NOTE] Forking a repository happens asynchronously. You may have to wait up
        > to 5 minutes before you can access the fork.

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
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return self._post(
            f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    def report(
        self,
        repo: str,
        *,
        owner: str,
        description: str,
        summary: str,
        cvss_vector_string: str | None | NotGiven = NOT_GIVEN,
        cwe_ids: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        severity: Literal["critical", "high", "medium", "low"] | None | NotGiven = NOT_GIVEN,
        start_private_fork: bool | NotGiven = NOT_GIVEN,
        vulnerabilities: Iterable[security_advisory_report_params.Vulnerability] | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryAdvisory:
        """Report a security vulnerability to the maintainers of the repository.

        See
        "[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)"
        for more information about private vulnerability reporting.

        Args:
          description: A detailed description of what the advisory impacts.

          summary: A short summary of the advisory.

          cvss_vector_string: The CVSS vector that calculates the severity of the advisory. You must choose
              between setting this field or `severity`.

          cwe_ids: A list of Common Weakness Enumeration (CWE) IDs.

          severity: The severity of the advisory. You must choose between setting this field or
              `cvss_vector_string`.

          start_private_fork: Whether to create a temporary private fork of the repository to collaborate on a
              fix.

          vulnerabilities: An array of products affected by the vulnerability detailed in a repository
              security advisory.

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
            f"/repos/{owner}/{repo}/security-advisories/reports",
            body=maybe_transform(
                {
                    "description": description,
                    "summary": summary,
                    "cvss_vector_string": cvss_vector_string,
                    "cwe_ids": cwe_ids,
                    "severity": severity,
                    "start_private_fork": start_private_fork,
                    "vulnerabilities": vulnerabilities,
                },
                security_advisory_report_params.SecurityAdvisoryReportParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryAdvisory,
        )

    def request_cve(
        self,
        ghsa_id: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        If you want a CVE identification number for the security vulnerability in your
        project, and don't already have one, you can request a CVE identification number
        from GitHub. For more information see
        "[Requesting a CVE identification number](https://docs.github.com/code-security/security-advisories/repository-security-advisories/publishing-a-repository-security-advisory#requesting-a-cve-identification-number-optional)."

        You may request a CVE for public repositories, but cannot do so for private
        repositories.

        In order to request a CVE for a repository security advisory, the authenticated
        user must be a security manager or administrator of that repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:write` scope to use this endpoint.

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
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return self._post(
            f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class AsyncSecurityAdvisoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecurityAdvisoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityAdvisoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityAdvisoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSecurityAdvisoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        description: str,
        summary: str,
        vulnerabilities: Iterable[security_advisory_create_params.Vulnerability],
        credits: Iterable[security_advisory_create_params.Credit] | None | NotGiven = NOT_GIVEN,
        cve_id: str | None | NotGiven = NOT_GIVEN,
        cvss_vector_string: str | None | NotGiven = NOT_GIVEN,
        cwe_ids: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        severity: Literal["critical", "high", "medium", "low"] | None | NotGiven = NOT_GIVEN,
        start_private_fork: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryAdvisory:
        """
        Creates a new repository security advisory.

        In order to create a draft repository security advisory, the authenticated user
        must be a security manager or administrator of that repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:write` scope to use this endpoint.

        Args:
          description: A detailed description of what the advisory impacts.

          summary: A short summary of the advisory.

          vulnerabilities: A product affected by the vulnerability detailed in a repository security
              advisory.

          credits: A list of users receiving credit for their participation in the security
              advisory.

          cve_id: The Common Vulnerabilities and Exposures (CVE) ID.

          cvss_vector_string: The CVSS vector that calculates the severity of the advisory. You must choose
              between setting this field or `severity`.

          cwe_ids: A list of Common Weakness Enumeration (CWE) IDs.

          severity: The severity of the advisory. You must choose between setting this field or
              `cvss_vector_string`.

          start_private_fork: Whether to create a temporary private fork of the repository to collaborate on a
              fix.

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
            f"/repos/{owner}/{repo}/security-advisories",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "summary": summary,
                    "vulnerabilities": vulnerabilities,
                    "credits": credits,
                    "cve_id": cve_id,
                    "cvss_vector_string": cvss_vector_string,
                    "cwe_ids": cwe_ids,
                    "severity": severity,
                    "start_private_fork": start_private_fork,
                },
                security_advisory_create_params.SecurityAdvisoryCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryAdvisory,
        )

    async def retrieve(
        self,
        ghsa_id: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryAdvisory:
        """
        Get a repository security advisory using its GitHub Security Advisory (GHSA)
        identifier.

        Anyone can access any published security advisory on a public repository.

        The authenticated user can access an unpublished security advisory from a
        repository if they are a security manager or administrator of that repository,
        or if they are a collaborator on the security advisory.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:read` scope to to get a published security advisory in a
        private repository, or any unpublished security advisory that the authenticated
        user has access to.

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
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryAdvisory,
        )

    async def update(
        self,
        ghsa_id: str,
        *,
        owner: str,
        repo: str,
        collaborating_teams: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        collaborating_users: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        credits: Iterable[security_advisory_update_params.Credit] | None | NotGiven = NOT_GIVEN,
        cve_id: str | None | NotGiven = NOT_GIVEN,
        cvss_vector_string: str | None | NotGiven = NOT_GIVEN,
        cwe_ids: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        severity: Literal["critical", "high", "medium", "low"] | None | NotGiven = NOT_GIVEN,
        state: Literal["published", "closed", "draft"] | NotGiven = NOT_GIVEN,
        summary: str | NotGiven = NOT_GIVEN,
        vulnerabilities: Iterable[security_advisory_update_params.Vulnerability] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryAdvisory:
        """
        Update a repository security advisory using its GitHub Security Advisory (GHSA)
        identifier.

        In order to update any security advisory, the authenticated user must be a
        security manager or administrator of that repository, or a collaborator on the
        repository security advisory.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:write` scope to use this endpoint.

        Args:
          collaborating_teams: A list of team slugs which have been granted write access to the advisory.

          collaborating_users: A list of usernames who have been granted write access to the advisory.

          credits: A list of users receiving credit for their participation in the security
              advisory.

          cve_id: The Common Vulnerabilities and Exposures (CVE) ID.

          cvss_vector_string: The CVSS vector that calculates the severity of the advisory. You must choose
              between setting this field or `severity`.

          cwe_ids: A list of Common Weakness Enumeration (CWE) IDs.

          description: A detailed description of what the advisory impacts.

          severity: The severity of the advisory. You must choose between setting this field or
              `cvss_vector_string`.

          state: The state of the advisory.

          summary: A short summary of the advisory.

          vulnerabilities: A product affected by the vulnerability detailed in a repository security
              advisory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}",
            body=await async_maybe_transform(
                {
                    "collaborating_teams": collaborating_teams,
                    "collaborating_users": collaborating_users,
                    "credits": credits,
                    "cve_id": cve_id,
                    "cvss_vector_string": cvss_vector_string,
                    "cwe_ids": cwe_ids,
                    "description": description,
                    "severity": severity,
                    "state": state,
                    "summary": summary,
                    "vulnerabilities": vulnerabilities,
                },
                security_advisory_update_params.SecurityAdvisoryUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryAdvisory,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "published"] | NotGiven = NOT_GIVEN,
        state: Literal["triage", "draft", "published", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecurityAdvisoryListResponse:
        """
        Lists security advisories in a repository.

        The authenticated user can access unpublished security advisories from a
        repository if they are a security manager or administrator of that repository,
        or if they are a collaborator on any security advisory.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:read` scope to to get a published security advisory in a
        private repository, or any unpublished security advisory that the authenticated
        user has access to.

        Args:
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

          direction: The direction to sort the results by.

          per_page: The number of advisories to return per page. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          state: Filter by state of the repository advisories. Only advisories of this state will
              be returned.

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
            f"/repos/{owner}/{repo}/security-advisories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    security_advisory_list_params.SecurityAdvisoryListParams,
                ),
            ),
            cast_to=SecurityAdvisoryListResponse,
        )

    async def create_fork(
        self,
        ghsa_id: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """
        Create a temporary private fork to collaborate on fixing a security
        vulnerability in your repository.

        > [!NOTE] Forking a repository happens asynchronously. You may have to wait up
        > to 5 minutes before you can access the fork.

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
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    async def report(
        self,
        repo: str,
        *,
        owner: str,
        description: str,
        summary: str,
        cvss_vector_string: str | None | NotGiven = NOT_GIVEN,
        cwe_ids: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        severity: Literal["critical", "high", "medium", "low"] | None | NotGiven = NOT_GIVEN,
        start_private_fork: bool | NotGiven = NOT_GIVEN,
        vulnerabilities: Iterable[security_advisory_report_params.Vulnerability] | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryAdvisory:
        """Report a security vulnerability to the maintainers of the repository.

        See
        "[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)"
        for more information about private vulnerability reporting.

        Args:
          description: A detailed description of what the advisory impacts.

          summary: A short summary of the advisory.

          cvss_vector_string: The CVSS vector that calculates the severity of the advisory. You must choose
              between setting this field or `severity`.

          cwe_ids: A list of Common Weakness Enumeration (CWE) IDs.

          severity: The severity of the advisory. You must choose between setting this field or
              `cvss_vector_string`.

          start_private_fork: Whether to create a temporary private fork of the repository to collaborate on a
              fix.

          vulnerabilities: An array of products affected by the vulnerability detailed in a repository
              security advisory.

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
            f"/repos/{owner}/{repo}/security-advisories/reports",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "summary": summary,
                    "cvss_vector_string": cvss_vector_string,
                    "cwe_ids": cwe_ids,
                    "severity": severity,
                    "start_private_fork": start_private_fork,
                    "vulnerabilities": vulnerabilities,
                },
                security_advisory_report_params.SecurityAdvisoryReportParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryAdvisory,
        )

    async def request_cve(
        self,
        ghsa_id: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        If you want a CVE identification number for the security vulnerability in your
        project, and don't already have one, you can request a CVE identification number
        from GitHub. For more information see
        "[Requesting a CVE identification number](https://docs.github.com/code-security/security-advisories/repository-security-advisories/publishing-a-repository-security-advisory#requesting-a-cve-identification-number-optional)."

        You may request a CVE for public repositories, but cannot do so for private
        repositories.

        In order to request a CVE for a repository security advisory, the authenticated
        user must be a security manager or administrator of that repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `repository_advisories:write` scope to use this endpoint.

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
        if not ghsa_id:
            raise ValueError(f"Expected a non-empty value for `ghsa_id` but received {ghsa_id!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class SecurityAdvisoriesResourceWithRawResponse:
    def __init__(self, security_advisories: SecurityAdvisoriesResource) -> None:
        self._security_advisories = security_advisories

        self.create = to_raw_response_wrapper(
            security_advisories.create,
        )
        self.retrieve = to_raw_response_wrapper(
            security_advisories.retrieve,
        )
        self.update = to_raw_response_wrapper(
            security_advisories.update,
        )
        self.list = to_raw_response_wrapper(
            security_advisories.list,
        )
        self.create_fork = to_raw_response_wrapper(
            security_advisories.create_fork,
        )
        self.report = to_raw_response_wrapper(
            security_advisories.report,
        )
        self.request_cve = to_raw_response_wrapper(
            security_advisories.request_cve,
        )


class AsyncSecurityAdvisoriesResourceWithRawResponse:
    def __init__(self, security_advisories: AsyncSecurityAdvisoriesResource) -> None:
        self._security_advisories = security_advisories

        self.create = async_to_raw_response_wrapper(
            security_advisories.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            security_advisories.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            security_advisories.update,
        )
        self.list = async_to_raw_response_wrapper(
            security_advisories.list,
        )
        self.create_fork = async_to_raw_response_wrapper(
            security_advisories.create_fork,
        )
        self.report = async_to_raw_response_wrapper(
            security_advisories.report,
        )
        self.request_cve = async_to_raw_response_wrapper(
            security_advisories.request_cve,
        )


class SecurityAdvisoriesResourceWithStreamingResponse:
    def __init__(self, security_advisories: SecurityAdvisoriesResource) -> None:
        self._security_advisories = security_advisories

        self.create = to_streamed_response_wrapper(
            security_advisories.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            security_advisories.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            security_advisories.update,
        )
        self.list = to_streamed_response_wrapper(
            security_advisories.list,
        )
        self.create_fork = to_streamed_response_wrapper(
            security_advisories.create_fork,
        )
        self.report = to_streamed_response_wrapper(
            security_advisories.report,
        )
        self.request_cve = to_streamed_response_wrapper(
            security_advisories.request_cve,
        )


class AsyncSecurityAdvisoriesResourceWithStreamingResponse:
    def __init__(self, security_advisories: AsyncSecurityAdvisoriesResource) -> None:
        self._security_advisories = security_advisories

        self.create = async_to_streamed_response_wrapper(
            security_advisories.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            security_advisories.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            security_advisories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            security_advisories.list,
        )
        self.create_fork = async_to_streamed_response_wrapper(
            security_advisories.create_fork,
        )
        self.report = async_to_streamed_response_wrapper(
            security_advisories.report,
        )
        self.request_cve = async_to_streamed_response_wrapper(
            security_advisories.request_cve,
        )
