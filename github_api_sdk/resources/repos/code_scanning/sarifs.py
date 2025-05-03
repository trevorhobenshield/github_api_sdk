from __future__ import annotations

from datetime import datetime
from typing import Union

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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.code_scanning import sarif_upload_params
from ....types.repos.code_scanning.sarif_retrieve_response import SarifRetrieveResponse
from ....types.repos.code_scanning.sarif_upload_response import SarifUploadResponse

__all__ = ["SarifsResource", "AsyncSarifsResource"]


class SarifsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SarifsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SarifsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SarifsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SarifsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        sarif_id: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SarifRetrieveResponse:
        """
        Gets information about a SARIF upload, including the status and the URL of the
        analysis that was uploaded so that you can retrieve details of the analysis. For
        more information, see
        "[Get a code scanning analysis for a repository](/rest/code-scanning/code-scanning#get-a-code-scanning-analysis-for-a-repository)."
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
        if not sarif_id:
            raise ValueError(f"Expected a non-empty value for `sarif_id` but received {sarif_id!r}")
        return self._get(
            f"/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SarifRetrieveResponse,
        )

    def upload(
        self,
        repo: str,
        *,
        owner: str,
        commit_sha: str,
        ref: str,
        sarif: str,
        checkout_uri: str | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        validate: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SarifUploadResponse:
        """
        Uploads SARIF data containing the results of a code scanning analysis to make
        the results available in a repository. For troubleshooting information, see
        "[Troubleshooting SARIF uploads](https://docs.github.com/code-security/code-scanning/troubleshooting-sarif)."

        There are two places where you can upload code scanning results.

        - If you upload to a pull request, for example `--ref refs/pull/42/merge` or
          `--ref refs/pull/42/head`, then the results appear as alerts in a pull request
          check. For more information, see
          "[Triaging code scanning alerts in pull requests](/code-security/secure-coding/triaging-code-scanning-alerts-in-pull-requests)."
        - If you upload to a branch, for example `--ref refs/heads/my-branch`, then the
          results appear in the **Security** tab for your repository. For more
          information, see
          "[Managing code scanning alerts for your repository](/code-security/secure-coding/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository)."

        You must compress the SARIF-formatted analysis data that you want to upload,
        using `gzip`, and then encode it as a Base64 format string. For example:

        ```
        gzip -c analysis-data.sarif | base64 -w0
        ```

        SARIF upload supports a maximum number of entries per the following data
        objects, and an analysis will be rejected if any of these objects is above its
        maximum value. For some objects, there are additional values over which the
        entries will be ignored while keeping the most important entries whenever
        applicable. To get the most out of your analysis when it includes data above the
        supported limits, try to optimize the analysis configuration. For example, for
        the CodeQL tool, identify and remove the most noisy queries. For more
        information, see
        "[SARIF results exceed one or more limits](https://docs.github.com/code-security/code-scanning/troubleshooting-sarif/results-exceed-limit)."

        | **SARIF data**                   | **Maximum values** | **Additional limits**                                                            |
        | -------------------------------- | :----------------: | -------------------------------------------------------------------------------- |
        | Runs per file                    |         20         |                                                                                  |
        | Results per run                  |       25,000       | Only the top 5,000 results will be included, prioritized by severity.            |
        | Rules per run                    |       25,000       |                                                                                  |
        | Tool extensions per run          |        100         |                                                                                  |
        | Thread Flow Locations per result |       10,000       | Only the top 1,000 Thread Flow Locations will be included, using prioritization. |
        | Location per result              |       1,000        | Only 100 locations will be included.                                             |
        | Tags per rule                    |         20         | Only 10 tags will be included.                                                   |

        The `202 Accepted` response includes an `id` value. You can use this ID to check
        the status of the upload by using it in the `/sarifs/{sarif_id}` endpoint. For
        more information, see
        "[Get information about a SARIF upload](/rest/code-scanning/code-scanning#get-information-about-a-sarif-upload)."

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        This endpoint is limited to 1,000 requests per hour for each user or app
        installation calling it.

        Args:
          commit_sha: The SHA of the commit to which the analysis you are uploading relates.

          ref: The full Git reference, formatted as `refs/heads/<branch name>`,
              `refs/tags/<tag>`, `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.

          sarif: A Base64 string representing the SARIF file to upload. You must first compress
              your SARIF file using
              [`gzip`](http://www.gnu.org/software/gzip/manual/gzip.html) and then translate
              the contents of the file into a Base64 encoding string. For more information,
              see
              "[SARIF support for code scanning](https://docs.github.com/code-security/secure-coding/sarif-support-for-code-scanning)."

          checkout_uri: The base directory used in the analysis, as it appears in the SARIF file. This
              property is used to convert file paths from absolute to relative, so that alerts
              can be mapped to their correct location in the repository.

          started_at: The time that the analysis run began. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          tool_name: The name of the tool used to generate the code scanning analysis. If this
              parameter is not used, the tool name defaults to "API". If the uploaded SARIF
              contains a tool GUID, this will be available for filtering using the `tool_guid`
              parameter of operations such as
              `GET /repos/{owner}/{repo}/code-scanning/alerts`.

          validate: Whether the SARIF file will be validated according to the code scanning
              specifications. This parameter is intended to help integrators ensure that the
              uploaded SARIF files are correctly rendered by code scanning.

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
            f"/repos/{owner}/{repo}/code-scanning/sarifs",
            body=maybe_transform(
                {
                    "commit_sha": commit_sha,
                    "ref": ref,
                    "sarif": sarif,
                    "checkout_uri": checkout_uri,
                    "started_at": started_at,
                    "tool_name": tool_name,
                    "validate": validate,
                },
                sarif_upload_params.SarifUploadParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SarifUploadResponse,
        )


class AsyncSarifsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSarifsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSarifsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSarifsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSarifsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        sarif_id: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SarifRetrieveResponse:
        """
        Gets information about a SARIF upload, including the status and the URL of the
        analysis that was uploaded so that you can retrieve details of the analysis. For
        more information, see
        "[Get a code scanning analysis for a repository](/rest/code-scanning/code-scanning#get-a-code-scanning-analysis-for-a-repository)."
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
        if not sarif_id:
            raise ValueError(f"Expected a non-empty value for `sarif_id` but received {sarif_id!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SarifRetrieveResponse,
        )

    async def upload(
        self,
        repo: str,
        *,
        owner: str,
        commit_sha: str,
        ref: str,
        sarif: str,
        checkout_uri: str | NotGiven = NOT_GIVEN,
        started_at: str | datetime | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        validate: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SarifUploadResponse:
        """
        Uploads SARIF data containing the results of a code scanning analysis to make
        the results available in a repository. For troubleshooting information, see
        "[Troubleshooting SARIF uploads](https://docs.github.com/code-security/code-scanning/troubleshooting-sarif)."

        There are two places where you can upload code scanning results.

        - If you upload to a pull request, for example `--ref refs/pull/42/merge` or
          `--ref refs/pull/42/head`, then the results appear as alerts in a pull request
          check. For more information, see
          "[Triaging code scanning alerts in pull requests](/code-security/secure-coding/triaging-code-scanning-alerts-in-pull-requests)."
        - If you upload to a branch, for example `--ref refs/heads/my-branch`, then the
          results appear in the **Security** tab for your repository. For more
          information, see
          "[Managing code scanning alerts for your repository](/code-security/secure-coding/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository)."

        You must compress the SARIF-formatted analysis data that you want to upload,
        using `gzip`, and then encode it as a Base64 format string. For example:

        ```
        gzip -c analysis-data.sarif | base64 -w0
        ```

        SARIF upload supports a maximum number of entries per the following data
        objects, and an analysis will be rejected if any of these objects is above its
        maximum value. For some objects, there are additional values over which the
        entries will be ignored while keeping the most important entries whenever
        applicable. To get the most out of your analysis when it includes data above the
        supported limits, try to optimize the analysis configuration. For example, for
        the CodeQL tool, identify and remove the most noisy queries. For more
        information, see
        "[SARIF results exceed one or more limits](https://docs.github.com/code-security/code-scanning/troubleshooting-sarif/results-exceed-limit)."

        | **SARIF data**                   | **Maximum values** | **Additional limits**                                                            |
        | -------------------------------- | :----------------: | -------------------------------------------------------------------------------- |
        | Runs per file                    |         20         |                                                                                  |
        | Results per run                  |       25,000       | Only the top 5,000 results will be included, prioritized by severity.            |
        | Rules per run                    |       25,000       |                                                                                  |
        | Tool extensions per run          |        100         |                                                                                  |
        | Thread Flow Locations per result |       10,000       | Only the top 1,000 Thread Flow Locations will be included, using prioritization. |
        | Location per result              |       1,000        | Only 100 locations will be included.                                             |
        | Tags per rule                    |         20         | Only 10 tags will be included.                                                   |

        The `202 Accepted` response includes an `id` value. You can use this ID to check
        the status of the upload by using it in the `/sarifs/{sarif_id}` endpoint. For
        more information, see
        "[Get information about a SARIF upload](/rest/code-scanning/code-scanning#get-information-about-a-sarif-upload)."

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        scope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

        This endpoint is limited to 1,000 requests per hour for each user or app
        installation calling it.

        Args:
          commit_sha: The SHA of the commit to which the analysis you are uploading relates.

          ref: The full Git reference, formatted as `refs/heads/<branch name>`,
              `refs/tags/<tag>`, `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.

          sarif: A Base64 string representing the SARIF file to upload. You must first compress
              your SARIF file using
              [`gzip`](http://www.gnu.org/software/gzip/manual/gzip.html) and then translate
              the contents of the file into a Base64 encoding string. For more information,
              see
              "[SARIF support for code scanning](https://docs.github.com/code-security/secure-coding/sarif-support-for-code-scanning)."

          checkout_uri: The base directory used in the analysis, as it appears in the SARIF file. This
              property is used to convert file paths from absolute to relative, so that alerts
              can be mapped to their correct location in the repository.

          started_at: The time that the analysis run began. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          tool_name: The name of the tool used to generate the code scanning analysis. If this
              parameter is not used, the tool name defaults to "API". If the uploaded SARIF
              contains a tool GUID, this will be available for filtering using the `tool_guid`
              parameter of operations such as
              `GET /repos/{owner}/{repo}/code-scanning/alerts`.

          validate: Whether the SARIF file will be validated according to the code scanning
              specifications. This parameter is intended to help integrators ensure that the
              uploaded SARIF files are correctly rendered by code scanning.

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
            f"/repos/{owner}/{repo}/code-scanning/sarifs",
            body=await async_maybe_transform(
                {
                    "commit_sha": commit_sha,
                    "ref": ref,
                    "sarif": sarif,
                    "checkout_uri": checkout_uri,
                    "started_at": started_at,
                    "tool_name": tool_name,
                    "validate": validate,
                },
                sarif_upload_params.SarifUploadParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SarifUploadResponse,
        )


class SarifsResourceWithRawResponse:
    def __init__(self, sarifs: SarifsResource) -> None:
        self._sarifs = sarifs

        self.retrieve = to_raw_response_wrapper(
            sarifs.retrieve,
        )
        self.upload = to_raw_response_wrapper(
            sarifs.upload,
        )


class AsyncSarifsResourceWithRawResponse:
    def __init__(self, sarifs: AsyncSarifsResource) -> None:
        self._sarifs = sarifs

        self.retrieve = async_to_raw_response_wrapper(
            sarifs.retrieve,
        )
        self.upload = async_to_raw_response_wrapper(
            sarifs.upload,
        )


class SarifsResourceWithStreamingResponse:
    def __init__(self, sarifs: SarifsResource) -> None:
        self._sarifs = sarifs

        self.retrieve = to_streamed_response_wrapper(
            sarifs.retrieve,
        )
        self.upload = to_streamed_response_wrapper(
            sarifs.upload,
        )


class AsyncSarifsResourceWithStreamingResponse:
    def __init__(self, sarifs: AsyncSarifsResource) -> None:
        self._sarifs = sarifs

        self.retrieve = async_to_streamed_response_wrapper(
            sarifs.retrieve,
        )
        self.upload = async_to_streamed_response_wrapper(
            sarifs.upload,
        )
