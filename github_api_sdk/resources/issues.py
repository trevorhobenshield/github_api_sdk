from __future__ import annotations

from datetime import datetime
from typing import Union

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
from ..types import issue_list_params
from ..types.issue_list_response import IssueListResponse

__all__ = ["IssuesResource", "AsyncIssuesResource"]


class IssuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IssuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return IssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IssuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return IssuesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        collab: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        filter: Literal["assigned", "created", "mentioned", "subscribed", "repos", "all"] | NotGiven = NOT_GIVEN,
        labels: str | NotGiven = NOT_GIVEN,
        orgs: bool | NotGiven = NOT_GIVEN,
        owned: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        pulls: bool | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "comments"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueListResponse:
        """
        List issues assigned to the authenticated user across all visible repositories
        including owned repositories, member repositories, and organization
        repositories. You can use the `filter` query parameter to fetch issues that are
        not necessarily assigned to you.

        > [!NOTE] GitHub's REST API considers every pull request an issue, but not every
        > issue is a pull request. For this reason, "Issues" endpoints may return both
        > issues and pull requests in the response. You can identify pull requests by
        > the `pull_request` key. Be aware that the `id` of a pull request returned from
        > "Issues" endpoints will be an _issue id_. To find out the pull request id, use
        > the
        > "[List pull requests](https://docs.github.com/rest/pulls/pulls#list-pull-requests)"
        > endpoint.

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
          direction: The direction to sort the results by.

          filter: Indicates which sorts of issues to return. `assigned` means issues assigned to
              you. `created` means issues created by you. `mentioned` means issues mentioning
              you. `subscribed` means issues you're subscribed to updates for. `all` or
              `repos` means all issues you can see, regardless of participation or creation.

          labels: A list of comma separated label names. Example: `bug,ui,@high`

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: What to sort results by.

          state: Indicates the state of the issues to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/issues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collab": collab,
                        "direction": direction,
                        "filter": filter,
                        "labels": labels,
                        "orgs": orgs,
                        "owned": owned,
                        "page": page,
                        "per_page": per_page,
                        "pulls": pulls,
                        "since": since,
                        "sort": sort,
                        "state": state,
                    },
                    issue_list_params.IssueListParams,
                ),
            ),
            cast_to=IssueListResponse,
        )


class AsyncIssuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIssuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIssuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIssuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncIssuesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        collab: bool | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        filter: Literal["assigned", "created", "mentioned", "subscribed", "repos", "all"] | NotGiven = NOT_GIVEN,
        labels: str | NotGiven = NOT_GIVEN,
        orgs: bool | NotGiven = NOT_GIVEN,
        owned: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        pulls: bool | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "comments"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueListResponse:
        """
        List issues assigned to the authenticated user across all visible repositories
        including owned repositories, member repositories, and organization
        repositories. You can use the `filter` query parameter to fetch issues that are
        not necessarily assigned to you.

        > [!NOTE] GitHub's REST API considers every pull request an issue, but not every
        > issue is a pull request. For this reason, "Issues" endpoints may return both
        > issues and pull requests in the response. You can identify pull requests by
        > the `pull_request` key. Be aware that the `id` of a pull request returned from
        > "Issues" endpoints will be an _issue id_. To find out the pull request id, use
        > the
        > "[List pull requests](https://docs.github.com/rest/pulls/pulls#list-pull-requests)"
        > endpoint.

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
          direction: The direction to sort the results by.

          filter: Indicates which sorts of issues to return. `assigned` means issues assigned to
              you. `created` means issues created by you. `mentioned` means issues mentioning
              you. `subscribed` means issues you're subscribed to updates for. `all` or
              `repos` means all issues you can see, regardless of participation or creation.

          labels: A list of comma separated label names. Example: `bug,ui,@high`

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: What to sort results by.

          state: Indicates the state of the issues to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/issues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "collab": collab,
                        "direction": direction,
                        "filter": filter,
                        "labels": labels,
                        "orgs": orgs,
                        "owned": owned,
                        "page": page,
                        "per_page": per_page,
                        "pulls": pulls,
                        "since": since,
                        "sort": sort,
                        "state": state,
                    },
                    issue_list_params.IssueListParams,
                ),
            ),
            cast_to=IssueListResponse,
        )


class IssuesResourceWithRawResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.list = to_raw_response_wrapper(
            issues.list,
        )


class AsyncIssuesResourceWithRawResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.list = async_to_raw_response_wrapper(
            issues.list,
        )


class IssuesResourceWithStreamingResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.list = to_streamed_response_wrapper(
            issues.list,
        )


class AsyncIssuesResourceWithStreamingResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.list = async_to_streamed_response_wrapper(
            issues.list,
        )
