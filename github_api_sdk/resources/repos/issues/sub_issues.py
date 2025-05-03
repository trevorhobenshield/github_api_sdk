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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.issue import Issue
from ....types.repos.issues import sub_issue_add_params, sub_issue_list_params, sub_issue_reprioritize_params
from ....types.repos.issues.sub_issue_list_response import SubIssueListResponse

__all__ = ["SubIssuesResource", "AsyncSubIssuesResource"]


class SubIssuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubIssuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubIssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubIssuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SubIssuesResourceWithStreamingResponse(self)

    def list(
        self,
        issue_number: int,
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
    ) -> SubIssueListResponse:
        """
        You can use the REST API to list the sub-issues on an issue.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/sub_issues",
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
                    sub_issue_list_params.SubIssueListParams,
                ),
            ),
            cast_to=SubIssueListResponse,
        )

    def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        sub_issue_id: int,
        replace_parent: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        You can use the REST API to add sub-issues to issues.

        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          sub_issue_id: The id of the sub-issue to add. The sub-issue must belong to the same repository
              owner as the parent issue

          replace_parent: Option that, when true, instructs the operation to replace the sub-issues
              current parent issue

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/sub_issues",
            body=maybe_transform(
                {
                    "sub_issue_id": sub_issue_id,
                    "replace_parent": replace_parent,
                },
                sub_issue_add_params.SubIssueAddParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    def reprioritize(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        sub_issue_id: int,
        after_id: int | NotGiven = NOT_GIVEN,
        before_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        You can use the REST API to reprioritize a sub-issue to a different position in
        the parent list.

        Args:
          sub_issue_id: The id of the sub-issue to reprioritize

          after_id: The id of the sub-issue to be prioritized after (either positional argument
              after OR before should be specified).

          before_id: The id of the sub-issue to be prioritized before (either positional argument
              after OR before should be specified).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority",
            body=maybe_transform(
                {
                    "sub_issue_id": sub_issue_id,
                    "after_id": after_id,
                    "before_id": before_id,
                },
                sub_issue_reprioritize_params.SubIssueReprioritizeParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )


class AsyncSubIssuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubIssuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubIssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubIssuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSubIssuesResourceWithStreamingResponse(self)

    async def list(
        self,
        issue_number: int,
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
    ) -> SubIssueListResponse:
        """
        You can use the REST API to list the sub-issues on an issue.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/sub_issues",
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
                    sub_issue_list_params.SubIssueListParams,
                ),
            ),
            cast_to=SubIssueListResponse,
        )

    async def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        sub_issue_id: int,
        replace_parent: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        You can use the REST API to add sub-issues to issues.

        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          sub_issue_id: The id of the sub-issue to add. The sub-issue must belong to the same repository
              owner as the parent issue

          replace_parent: Option that, when true, instructs the operation to replace the sub-issues
              current parent issue

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/sub_issues",
            body=await async_maybe_transform(
                {
                    "sub_issue_id": sub_issue_id,
                    "replace_parent": replace_parent,
                },
                sub_issue_add_params.SubIssueAddParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    async def reprioritize(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        sub_issue_id: int,
        after_id: int | NotGiven = NOT_GIVEN,
        before_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        You can use the REST API to reprioritize a sub-issue to a different position in
        the parent list.

        Args:
          sub_issue_id: The id of the sub-issue to reprioritize

          after_id: The id of the sub-issue to be prioritized after (either positional argument
              after OR before should be specified).

          before_id: The id of the sub-issue to be prioritized before (either positional argument
              after OR before should be specified).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority",
            body=await async_maybe_transform(
                {
                    "sub_issue_id": sub_issue_id,
                    "after_id": after_id,
                    "before_id": before_id,
                },
                sub_issue_reprioritize_params.SubIssueReprioritizeParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )


class SubIssuesResourceWithRawResponse:
    def __init__(self, sub_issues: SubIssuesResource) -> None:
        self._sub_issues = sub_issues

        self.list = to_raw_response_wrapper(
            sub_issues.list,
        )
        self.add = to_raw_response_wrapper(
            sub_issues.add,
        )
        self.reprioritize = to_raw_response_wrapper(
            sub_issues.reprioritize,
        )


class AsyncSubIssuesResourceWithRawResponse:
    def __init__(self, sub_issues: AsyncSubIssuesResource) -> None:
        self._sub_issues = sub_issues

        self.list = async_to_raw_response_wrapper(
            sub_issues.list,
        )
        self.add = async_to_raw_response_wrapper(
            sub_issues.add,
        )
        self.reprioritize = async_to_raw_response_wrapper(
            sub_issues.reprioritize,
        )


class SubIssuesResourceWithStreamingResponse:
    def __init__(self, sub_issues: SubIssuesResource) -> None:
        self._sub_issues = sub_issues

        self.list = to_streamed_response_wrapper(
            sub_issues.list,
        )
        self.add = to_streamed_response_wrapper(
            sub_issues.add,
        )
        self.reprioritize = to_streamed_response_wrapper(
            sub_issues.reprioritize,
        )


class AsyncSubIssuesResourceWithStreamingResponse:
    def __init__(self, sub_issues: AsyncSubIssuesResource) -> None:
        self._sub_issues = sub_issues

        self.list = async_to_streamed_response_wrapper(
            sub_issues.list,
        )
        self.add = async_to_streamed_response_wrapper(
            sub_issues.add,
        )
        self.reprioritize = async_to_streamed_response_wrapper(
            sub_issues.reprioritize,
        )
