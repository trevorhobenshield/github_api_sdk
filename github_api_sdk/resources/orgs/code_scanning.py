from __future__ import annotations

from typing import Optional

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
from ...types.orgs import AlertSeverity, AlertStateQuery, code_scanning_list_alerts_params
from ...types.orgs.alert_severity import AlertSeverity
from ...types.orgs.alert_state_query import AlertStateQuery
from ...types.orgs.code_scanning_list_alerts_response import CodeScanningListAlertsResponse

__all__ = ["CodeScanningResource", "AsyncCodeScanningResource"]


class CodeScanningResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CodeScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodeScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodeScanningResourceWithStreamingResponse(self)

    def list_alerts(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        severity: AlertSeverity | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        state: AlertStateQuery | NotGiven = NOT_GIVEN,
        tool_guid: str | None | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningListAlertsResponse:
        """
        Lists code scanning alerts for the default branch for all eligible repositories
        in an organization. Eligible repositories are repositories that are owned by
        organizations that you own or for which you are a security manager. For more
        information, see
        "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        or `repo`s cope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

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

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          severity: If specified, only code scanning alerts with this severity will be returned.

          sort: The property by which to sort the results.

          state: If specified, only code scanning alerts with this state will be returned.

          tool_guid: The GUID of a code scanning tool. Only results by this tool will be listed. Note
              that some code scanning tools may not include a GUID in their analysis data. You
              can specify the tool by using either `tool_guid` or `tool_name`, but not both.

          tool_name: The name of a code scanning tool. Only results by this tool will be listed. You
              can specify the tool by using either `tool_name` or `tool_guid`, but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/code-scanning/alerts",
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
                        "page": page,
                        "per_page": per_page,
                        "severity": severity,
                        "sort": sort,
                        "state": state,
                        "tool_guid": tool_guid,
                        "tool_name": tool_name,
                    },
                    code_scanning_list_alerts_params.CodeScanningListAlertsParams,
                ),
            ),
            cast_to=CodeScanningListAlertsResponse,
        )


class AsyncCodeScanningResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCodeScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodeScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodeScanningResourceWithStreamingResponse(self)

    async def list_alerts(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        severity: AlertSeverity | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        state: AlertStateQuery | NotGiven = NOT_GIVEN,
        tool_guid: str | None | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeScanningListAlertsResponse:
        """
        Lists code scanning alerts for the default branch for all eligible repositories
        in an organization. Eligible repositories are repositories that are owned by
        organizations that you own or for which you are a security manager. For more
        information, see
        "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

        The authenticated user must be an owner or security manager for the organization
        to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `security_events`
        or `repo`s cope to use this endpoint with private or public repositories, or the
        `public_repo` scope to use this endpoint with only public repositories.

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

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          severity: If specified, only code scanning alerts with this severity will be returned.

          sort: The property by which to sort the results.

          state: If specified, only code scanning alerts with this state will be returned.

          tool_guid: The GUID of a code scanning tool. Only results by this tool will be listed. Note
              that some code scanning tools may not include a GUID in their analysis data. You
              can specify the tool by using either `tool_guid` or `tool_name`, but not both.

          tool_name: The name of a code scanning tool. Only results by this tool will be listed. You
              can specify the tool by using either `tool_name` or `tool_guid`, but not both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/code-scanning/alerts",
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
                        "page": page,
                        "per_page": per_page,
                        "severity": severity,
                        "sort": sort,
                        "state": state,
                        "tool_guid": tool_guid,
                        "tool_name": tool_name,
                    },
                    code_scanning_list_alerts_params.CodeScanningListAlertsParams,
                ),
            ),
            cast_to=CodeScanningListAlertsResponse,
        )


class CodeScanningResourceWithRawResponse:
    def __init__(self, code_scanning: CodeScanningResource) -> None:
        self._code_scanning = code_scanning

        self.list_alerts = to_raw_response_wrapper(
            code_scanning.list_alerts,
        )


class AsyncCodeScanningResourceWithRawResponse:
    def __init__(self, code_scanning: AsyncCodeScanningResource) -> None:
        self._code_scanning = code_scanning

        self.list_alerts = async_to_raw_response_wrapper(
            code_scanning.list_alerts,
        )


class CodeScanningResourceWithStreamingResponse:
    def __init__(self, code_scanning: CodeScanningResource) -> None:
        self._code_scanning = code_scanning

        self.list_alerts = to_streamed_response_wrapper(
            code_scanning.list_alerts,
        )


class AsyncCodeScanningResourceWithStreamingResponse:
    def __init__(self, code_scanning: AsyncCodeScanningResource) -> None:
        self._code_scanning = code_scanning

        self.list_alerts = async_to_streamed_response_wrapper(
            code_scanning.list_alerts,
        )
