from __future__ import annotations

from typing import List

import httpx

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
from .....types.repos.code_scanning.codeql import CodeScanningVariantAnalysisLanguage, variant_analysis_create_params
from .....types.repos.code_scanning.codeql.code_scanning_variant_analysis import CodeScanningVariantAnalysis
from .....types.repos.code_scanning.codeql.code_scanning_variant_analysis_language import (
    CodeScanningVariantAnalysisLanguage,
)
from .....types.repos.code_scanning.codeql.variant_analysis_get_repo_analysis_status_response import (
    VariantAnalysisGetRepoAnalysisStatusResponse,
)

__all__ = ["VariantAnalysesResource", "AsyncVariantAnalysesResource"]


class VariantAnalysesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VariantAnalysesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return VariantAnalysesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariantAnalysesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return VariantAnalysesResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        language: CodeScanningVariantAnalysisLanguage,
        query_pack: str,
        repositories: list[str] | NotGiven = NOT_GIVEN,
        repository_lists: list[str] | NotGiven = NOT_GIVEN,
        repository_owners: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningVariantAnalysis:
        """
        Creates a new CodeQL variant analysis, which will run a CodeQL query against one
        or more repositories.

        Get started by learning more about
        [running CodeQL queries at scale with Multi-Repository Variant Analysis](https://docs.github.com/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis).

        Use the `owner` and `repo` parameters in the URL to specify the controller
        repository that will be used for running GitHub Actions workflows and storing
        the results of the CodeQL variant analysis.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          language: The language targeted by the CodeQL query

          query_pack: A Base64-encoded tarball containing a CodeQL query and all its dependencies

          repositories: List of repository names (in the form `owner/repo-name`) to run the query
              against. Precisely one property from `repositories`, `repository_lists` and
              `repository_owners` is required.

          repository_lists: List of repository lists to run the query against. Precisely one property from
              `repositories`, `repository_lists` and `repository_owners` is required.

          repository_owners: List of organization or user names whose repositories the query should be run
              against. Precisely one property from `repositories`, `repository_lists` and
              `repository_owners` is required.

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
            f"/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses",
            body=maybe_transform(
                {
                    "language": language,
                    "query_pack": query_pack,
                    "repositories": repositories,
                    "repository_lists": repository_lists,
                    "repository_owners": repository_owners,
                },
                variant_analysis_create_params.VariantAnalysisCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningVariantAnalysis,
        )

    def retrieve(
        self,
        codeql_variant_analysis_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningVariantAnalysis:
        """
        Gets the summary of a CodeQL variant analysis.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

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
            f"/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningVariantAnalysis,
        )

    def get_repo_analysis_status(
        self,
        repo_name: str,
        *,
        owner: str,
        repo: str,
        codeql_variant_analysis_id: int,
        repo_owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantAnalysisGetRepoAnalysisStatusResponse:
        """
        Gets the analysis status of a repository in a CodeQL variant analysis.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

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
        if not repo_owner:
            raise ValueError(f"Expected a non-empty value for `repo_owner` but received {repo_owner!r}")
        if not repo_name:
            raise ValueError(f"Expected a non-empty value for `repo_name` but received {repo_name!r}")
        return self._get(
            f"/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id}/repos/{repo_owner}/{repo_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VariantAnalysisGetRepoAnalysisStatusResponse,
        )


class AsyncVariantAnalysesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVariantAnalysesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVariantAnalysesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariantAnalysesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncVariantAnalysesResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        language: CodeScanningVariantAnalysisLanguage,
        query_pack: str,
        repositories: list[str] | NotGiven = NOT_GIVEN,
        repository_lists: list[str] | NotGiven = NOT_GIVEN,
        repository_owners: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningVariantAnalysis:
        """
        Creates a new CodeQL variant analysis, which will run a CodeQL query against one
        or more repositories.

        Get started by learning more about
        [running CodeQL queries at scale with Multi-Repository Variant Analysis](https://docs.github.com/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis).

        Use the `owner` and `repo` parameters in the URL to specify the controller
        repository that will be used for running GitHub Actions workflows and storing
        the results of the CodeQL variant analysis.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          language: The language targeted by the CodeQL query

          query_pack: A Base64-encoded tarball containing a CodeQL query and all its dependencies

          repositories: List of repository names (in the form `owner/repo-name`) to run the query
              against. Precisely one property from `repositories`, `repository_lists` and
              `repository_owners` is required.

          repository_lists: List of repository lists to run the query against. Precisely one property from
              `repositories`, `repository_lists` and `repository_owners` is required.

          repository_owners: List of organization or user names whose repositories the query should be run
              against. Precisely one property from `repositories`, `repository_lists` and
              `repository_owners` is required.

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
            f"/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses",
            body=await async_maybe_transform(
                {
                    "language": language,
                    "query_pack": query_pack,
                    "repositories": repositories,
                    "repository_lists": repository_lists,
                    "repository_owners": repository_owners,
                },
                variant_analysis_create_params.VariantAnalysisCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningVariantAnalysis,
        )

    async def retrieve(
        self,
        codeql_variant_analysis_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningVariantAnalysis:
        """
        Gets the summary of a CodeQL variant analysis.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

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
            f"/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodeScanningVariantAnalysis,
        )

    async def get_repo_analysis_status(
        self,
        repo_name: str,
        *,
        owner: str,
        repo: str,
        codeql_variant_analysis_id: int,
        repo_owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VariantAnalysisGetRepoAnalysisStatusResponse:
        """
        Gets the analysis status of a repository in a CodeQL variant analysis.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

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
        if not repo_owner:
            raise ValueError(f"Expected a non-empty value for `repo_owner` but received {repo_owner!r}")
        if not repo_name:
            raise ValueError(f"Expected a non-empty value for `repo_name` but received {repo_name!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id}/repos/{repo_owner}/{repo_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VariantAnalysisGetRepoAnalysisStatusResponse,
        )


class VariantAnalysesResourceWithRawResponse:
    def __init__(self, variant_analyses: VariantAnalysesResource) -> None:
        self._variant_analyses = variant_analyses

        self.create = to_raw_response_wrapper(
            variant_analyses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            variant_analyses.retrieve,
        )
        self.get_repo_analysis_status = to_raw_response_wrapper(
            variant_analyses.get_repo_analysis_status,
        )


class AsyncVariantAnalysesResourceWithRawResponse:
    def __init__(self, variant_analyses: AsyncVariantAnalysesResource) -> None:
        self._variant_analyses = variant_analyses

        self.create = async_to_raw_response_wrapper(
            variant_analyses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            variant_analyses.retrieve,
        )
        self.get_repo_analysis_status = async_to_raw_response_wrapper(
            variant_analyses.get_repo_analysis_status,
        )


class VariantAnalysesResourceWithStreamingResponse:
    def __init__(self, variant_analyses: VariantAnalysesResource) -> None:
        self._variant_analyses = variant_analyses

        self.create = to_streamed_response_wrapper(
            variant_analyses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            variant_analyses.retrieve,
        )
        self.get_repo_analysis_status = to_streamed_response_wrapper(
            variant_analyses.get_repo_analysis_status,
        )


class AsyncVariantAnalysesResourceWithStreamingResponse:
    def __init__(self, variant_analyses: AsyncVariantAnalysesResource) -> None:
        self._variant_analyses = variant_analyses

        self.create = async_to_streamed_response_wrapper(
            variant_analyses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            variant_analyses.retrieve,
        )
        self.get_repo_analysis_status = async_to_streamed_response_wrapper(
            variant_analyses.get_repo_analysis_status,
        )
