from __future__ import annotations

import builtins
from datetime import datetime
from typing import List, Optional, Union

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
from ....types.repos import issue_create_params, issue_list_params, issue_remove_sub_issue_params, issue_update_params
from ....types.repos.issue import Issue
from ....types.repos.issue_list_response import IssueListResponse
from .assignees import (
    AssigneesResource,
    AssigneesResourceWithRawResponse,
    AssigneesResourceWithStreamingResponse,
    AsyncAssigneesResource,
    AsyncAssigneesResourceWithRawResponse,
    AsyncAssigneesResourceWithStreamingResponse,
)
from .comments.comments import (
    AsyncCommentsResource,
    AsyncCommentsResourceWithRawResponse,
    AsyncCommentsResourceWithStreamingResponse,
    CommentsResource,
    CommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
)
from .events import (
    AsyncEventsResource,
    AsyncEventsResourceWithRawResponse,
    AsyncEventsResourceWithStreamingResponse,
    EventsResource,
    EventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
)
from .labels import (
    AsyncLabelsResource,
    AsyncLabelsResourceWithRawResponse,
    AsyncLabelsResourceWithStreamingResponse,
    LabelsResource,
    LabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
)
from .lock import (
    AsyncLockResource,
    AsyncLockResourceWithRawResponse,
    AsyncLockResourceWithStreamingResponse,
    LockResource,
    LockResourceWithRawResponse,
    LockResourceWithStreamingResponse,
)
from .reactions import (
    AsyncReactionsResource,
    AsyncReactionsResourceWithRawResponse,
    AsyncReactionsResourceWithStreamingResponse,
    ReactionsResource,
    ReactionsResourceWithRawResponse,
    ReactionsResourceWithStreamingResponse,
)
from .sub_issues import (
    AsyncSubIssuesResource,
    AsyncSubIssuesResourceWithRawResponse,
    AsyncSubIssuesResourceWithStreamingResponse,
    SubIssuesResource,
    SubIssuesResourceWithRawResponse,
    SubIssuesResourceWithStreamingResponse,
)
from .timeline import (
    AsyncTimelineResource,
    AsyncTimelineResourceWithRawResponse,
    AsyncTimelineResourceWithStreamingResponse,
    TimelineResource,
    TimelineResourceWithRawResponse,
    TimelineResourceWithStreamingResponse,
)

__all__ = ["IssuesResource", "AsyncIssuesResource"]


class IssuesResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def assignees(self) -> AssigneesResource:
        return AssigneesResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        return LabelsResource(self._client)

    @cached_property
    def lock(self) -> LockResource:
        return LockResource(self._client)

    @cached_property
    def reactions(self) -> ReactionsResource:
        return ReactionsResource(self._client)

    @cached_property
    def sub_issues(self) -> SubIssuesResource:
        return SubIssuesResource(self._client)

    @cached_property
    def timeline(self) -> TimelineResource:
        return TimelineResource(self._client)

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

    def create(
        self,
        repo: str,
        *,
        owner: str,
        title: str | int,
        assignee: str | None | NotGiven = NOT_GIVEN,
        assignees: builtins.list[str] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        labels: builtins.list[issue_create_params.Label] | NotGiven = NOT_GIVEN,
        milestone: str | int | None | NotGiven = NOT_GIVEN,
        type: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """Any user with pull access to a repository can create an issue.

        If
        [issues are disabled in the repository](https://docs.github.com/articles/disabling-issues/),
        the API returns a `410 Gone` status.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
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
          title: The title of the issue.

          assignee: Login for the user that this issue should be assigned to. _NOTE: Only users with
              push access can set the assignee for new issues. The assignee is silently
              dropped otherwise. **This field is closing down.**_

          assignees: Logins for Users to assign to this issue. _NOTE: Only users with push access can
              set assignees for new issues. Assignees are silently dropped otherwise._

          body: The contents of the issue.

          labels: Labels to associate with this issue. _NOTE: Only users with push access can set
              labels for new issues. Labels are silently dropped otherwise._

          milestone: The `number` of the milestone to associate this issue with. _NOTE: Only users
              with push access can set the milestone for new issues. The milestone is silently
              dropped otherwise._

          type: The name of the issue type to associate with this issue. _NOTE: Only users with
              push access can set the type for new issues. The type is silently dropped
              otherwise._

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
            f"/repos/{owner}/{repo}/issues",
            body=maybe_transform(
                {
                    "title": title,
                    "assignee": assignee,
                    "assignees": assignees,
                    "body": body,
                    "labels": labels,
                    "milestone": milestone,
                    "type": type,
                },
                issue_create_params.IssueCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    def retrieve(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        The API returns a
        [`301 Moved Permanently` status](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api#follow-redirects)
        if the issue was
        [transferred](https://docs.github.com/articles/transferring-an-issue-to-another-repository/)
        to another repository. If the issue was transferred to or deleted from a
        repository where the authenticated user lacks read access, the API returns a
        `404 Not Found` status. If the issue was deleted from a repository where the
        authenticated user has read access, the API returns a `410 Gone` status. To
        receive webhook events for transferred and deleted issues, subscribe to the
        [`issues`](https://docs.github.com/webhooks/event-payloads/#issues) webhook.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    def update(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        assignee: str | None | NotGiven = NOT_GIVEN,
        assignees: builtins.list[str] | NotGiven = NOT_GIVEN,
        body: str | None | NotGiven = NOT_GIVEN,
        labels: builtins.list[issue_update_params.Label] | NotGiven = NOT_GIVEN,
        milestone: str | int | None | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        state_reason: Literal["completed", "not_planned", "reopened"] | None | NotGiven = NOT_GIVEN,
        title: str | int | None | NotGiven = NOT_GIVEN,
        type: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        Issue owners and users with push access or Triage role can edit an issue.

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
          assignee: Username to assign to this issue. **This field is closing down.**

          assignees: Usernames to assign to this issue. Pass one or more user logins to _replace_ the
              set of assignees on this issue. Send an empty array (`[]`) to clear all
              assignees from the issue. Only users with push access can set assignees for new
              issues. Without push access to the repository, assignee changes are silently
              dropped.

          body: The contents of the issue.

          labels: Labels to associate with this issue. Pass one or more labels to _replace_ the
              set of labels on this issue. Send an empty array (`[]`) to clear all labels from
              the issue. Only users with push access can set labels for issues. Without push
              access to the repository, label changes are silently dropped.

          milestone: The `number` of the milestone to associate this issue with or use `null` to
              remove the current milestone. Only users with push access can set the milestone
              for issues. Without push access to the repository, milestone changes are
              silently dropped.

          state: The open or closed state of the issue.

          state_reason: The reason for the state change. Ignored unless `state` is changed.

          title: The title of the issue.

          type: The name of the issue type to associate with this issue or use `null` to remove
              the current issue type. Only users with push access can set the type for issues.
              Without push access to the repository, type changes are silently dropped.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}",
            body=maybe_transform(
                {
                    "assignee": assignee,
                    "assignees": assignees,
                    "body": body,
                    "labels": labels,
                    "milestone": milestone,
                    "state": state,
                    "state_reason": state_reason,
                    "title": title,
                    "type": type,
                },
                issue_update_params.IssueUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        assignee: str | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        labels: str | NotGiven = NOT_GIVEN,
        mentioned: str | NotGiven = NOT_GIVEN,
        milestone: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "comments"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueListResponse:
        """List issues in a repository.

        Only open issues will be listed.

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
          assignee: Can be the name of a user. Pass in `none` for issues with no assigned user, and
              `*` for issues assigned to any user.

          creator: The user that created the issue.

          direction: The direction to sort the results by.

          labels: A list of comma separated label names. Example: `bug,ui,@high`

          mentioned: A user that's mentioned in the issue.

          milestone: If an `integer` is passed, it should refer to a milestone by its `number` field.
              If the string `*` is passed, issues with any milestone are accepted. If the
              string `none` is passed, issues without milestones are returned.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: What to sort results by.

          state: Indicates the state of the issues to return.

          type: Can be the name of an issue type. If the string `*` is passed, issues with any
              type are accepted. If the string `none` is passed, issues without type are
              returned.

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
            f"/repos/{owner}/{repo}/issues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "assignee": assignee,
                        "creator": creator,
                        "direction": direction,
                        "labels": labels,
                        "mentioned": mentioned,
                        "milestone": milestone,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "sort": sort,
                        "state": state,
                        "type": type,
                    },
                    issue_list_params.IssueListParams,
                ),
            ),
            cast_to=IssueListResponse,
        )

    def remove_sub_issue(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        sub_issue_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """You can use the REST API to remove a sub-issue from an issue.

        Removing content
        too quickly using this endpoint may result in secondary rate limiting. For more
        information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."
        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass a specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          sub_issue_id: The id of the sub-issue to remove

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._delete(
            f"/repos/{owner}/{repo}/issues/{issue_number}/sub_issue",
            body=maybe_transform({"sub_issue_id": sub_issue_id}, issue_remove_sub_issue_params.IssueRemoveSubIssueParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )


class AsyncIssuesResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def assignees(self) -> AsyncAssigneesResource:
        return AsyncAssigneesResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        return AsyncLabelsResource(self._client)

    @cached_property
    def lock(self) -> AsyncLockResource:
        return AsyncLockResource(self._client)

    @cached_property
    def reactions(self) -> AsyncReactionsResource:
        return AsyncReactionsResource(self._client)

    @cached_property
    def sub_issues(self) -> AsyncSubIssuesResource:
        return AsyncSubIssuesResource(self._client)

    @cached_property
    def timeline(self) -> AsyncTimelineResource:
        return AsyncTimelineResource(self._client)

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

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        title: str | int,
        assignee: str | None | NotGiven = NOT_GIVEN,
        assignees: builtins.list[str] | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        labels: builtins.list[issue_create_params.Label] | NotGiven = NOT_GIVEN,
        milestone: str | int | None | NotGiven = NOT_GIVEN,
        type: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """Any user with pull access to a repository can create an issue.

        If
        [issues are disabled in the repository](https://docs.github.com/articles/disabling-issues/),
        the API returns a `410 Gone` status.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
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
          title: The title of the issue.

          assignee: Login for the user that this issue should be assigned to. _NOTE: Only users with
              push access can set the assignee for new issues. The assignee is silently
              dropped otherwise. **This field is closing down.**_

          assignees: Logins for Users to assign to this issue. _NOTE: Only users with push access can
              set assignees for new issues. Assignees are silently dropped otherwise._

          body: The contents of the issue.

          labels: Labels to associate with this issue. _NOTE: Only users with push access can set
              labels for new issues. Labels are silently dropped otherwise._

          milestone: The `number` of the milestone to associate this issue with. _NOTE: Only users
              with push access can set the milestone for new issues. The milestone is silently
              dropped otherwise._

          type: The name of the issue type to associate with this issue. _NOTE: Only users with
              push access can set the type for new issues. The type is silently dropped
              otherwise._

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
            f"/repos/{owner}/{repo}/issues",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "assignee": assignee,
                    "assignees": assignees,
                    "body": body,
                    "labels": labels,
                    "milestone": milestone,
                    "type": type,
                },
                issue_create_params.IssueCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    async def retrieve(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        The API returns a
        [`301 Moved Permanently` status](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api#follow-redirects)
        if the issue was
        [transferred](https://docs.github.com/articles/transferring-an-issue-to-another-repository/)
        to another repository. If the issue was transferred to or deleted from a
        repository where the authenticated user lacks read access, the API returns a
        `404 Not Found` status. If the issue was deleted from a repository where the
        authenticated user has read access, the API returns a `410 Gone` status. To
        receive webhook events for transferred and deleted issues, subscribe to the
        [`issues`](https://docs.github.com/webhooks/event-payloads/#issues) webhook.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    async def update(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        assignee: str | None | NotGiven = NOT_GIVEN,
        assignees: builtins.list[str] | NotGiven = NOT_GIVEN,
        body: str | None | NotGiven = NOT_GIVEN,
        labels: builtins.list[issue_update_params.Label] | NotGiven = NOT_GIVEN,
        milestone: str | int | None | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        state_reason: Literal["completed", "not_planned", "reopened"] | None | NotGiven = NOT_GIVEN,
        title: str | int | None | NotGiven = NOT_GIVEN,
        type: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """
        Issue owners and users with push access or Triage role can edit an issue.

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
          assignee: Username to assign to this issue. **This field is closing down.**

          assignees: Usernames to assign to this issue. Pass one or more user logins to _replace_ the
              set of assignees on this issue. Send an empty array (`[]`) to clear all
              assignees from the issue. Only users with push access can set assignees for new
              issues. Without push access to the repository, assignee changes are silently
              dropped.

          body: The contents of the issue.

          labels: Labels to associate with this issue. Pass one or more labels to _replace_ the
              set of labels on this issue. Send an empty array (`[]`) to clear all labels from
              the issue. Only users with push access can set labels for issues. Without push
              access to the repository, label changes are silently dropped.

          milestone: The `number` of the milestone to associate this issue with or use `null` to
              remove the current milestone. Only users with push access can set the milestone
              for issues. Without push access to the repository, milestone changes are
              silently dropped.

          state: The open or closed state of the issue.

          state_reason: The reason for the state change. Ignored unless `state` is changed.

          title: The title of the issue.

          type: The name of the issue type to associate with this issue or use `null` to remove
              the current issue type. Only users with push access can set the type for issues.
              Without push access to the repository, type changes are silently dropped.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}",
            body=await async_maybe_transform(
                {
                    "assignee": assignee,
                    "assignees": assignees,
                    "body": body,
                    "labels": labels,
                    "milestone": milestone,
                    "state": state,
                    "state_reason": state_reason,
                    "title": title,
                    "type": type,
                },
                issue_update_params.IssueUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        assignee: str | NotGiven = NOT_GIVEN,
        creator: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        labels: str | NotGiven = NOT_GIVEN,
        mentioned: str | NotGiven = NOT_GIVEN,
        milestone: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "comments"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueListResponse:
        """List issues in a repository.

        Only open issues will be listed.

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
          assignee: Can be the name of a user. Pass in `none` for issues with no assigned user, and
              `*` for issues assigned to any user.

          creator: The user that created the issue.

          direction: The direction to sort the results by.

          labels: A list of comma separated label names. Example: `bug,ui,@high`

          mentioned: A user that's mentioned in the issue.

          milestone: If an `integer` is passed, it should refer to a milestone by its `number` field.
              If the string `*` is passed, issues with any milestone are accepted. If the
              string `none` is passed, issues without milestones are returned.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: What to sort results by.

          state: Indicates the state of the issues to return.

          type: Can be the name of an issue type. If the string `*` is passed, issues with any
              type are accepted. If the string `none` is passed, issues without type are
              returned.

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
            f"/repos/{owner}/{repo}/issues",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "assignee": assignee,
                        "creator": creator,
                        "direction": direction,
                        "labels": labels,
                        "mentioned": mentioned,
                        "milestone": milestone,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "sort": sort,
                        "state": state,
                        "type": type,
                    },
                    issue_list_params.IssueListParams,
                ),
            ),
            cast_to=IssueListResponse,
        )

    async def remove_sub_issue(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        sub_issue_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Issue:
        """You can use the REST API to remove a sub-issue from an issue.

        Removing content
        too quickly using this endpoint may result in secondary rate limiting. For more
        information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."
        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass a specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          sub_issue_id: The id of the sub-issue to remove

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._delete(
            f"/repos/{owner}/{repo}/issues/{issue_number}/sub_issue",
            body=await async_maybe_transform({"sub_issue_id": sub_issue_id}, issue_remove_sub_issue_params.IssueRemoveSubIssueParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Issue,
        )


class IssuesResourceWithRawResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.create = to_raw_response_wrapper(
            issues.create,
        )
        self.retrieve = to_raw_response_wrapper(
            issues.retrieve,
        )
        self.update = to_raw_response_wrapper(
            issues.update,
        )
        self.list = to_raw_response_wrapper(
            issues.list,
        )
        self.remove_sub_issue = to_raw_response_wrapper(
            issues.remove_sub_issue,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._issues.comments)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._issues.events)

    @cached_property
    def assignees(self) -> AssigneesResourceWithRawResponse:
        return AssigneesResourceWithRawResponse(self._issues.assignees)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        return LabelsResourceWithRawResponse(self._issues.labels)

    @cached_property
    def lock(self) -> LockResourceWithRawResponse:
        return LockResourceWithRawResponse(self._issues.lock)

    @cached_property
    def reactions(self) -> ReactionsResourceWithRawResponse:
        return ReactionsResourceWithRawResponse(self._issues.reactions)

    @cached_property
    def sub_issues(self) -> SubIssuesResourceWithRawResponse:
        return SubIssuesResourceWithRawResponse(self._issues.sub_issues)

    @cached_property
    def timeline(self) -> TimelineResourceWithRawResponse:
        return TimelineResourceWithRawResponse(self._issues.timeline)


class AsyncIssuesResourceWithRawResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.create = async_to_raw_response_wrapper(
            issues.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            issues.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            issues.update,
        )
        self.list = async_to_raw_response_wrapper(
            issues.list,
        )
        self.remove_sub_issue = async_to_raw_response_wrapper(
            issues.remove_sub_issue,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._issues.comments)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._issues.events)

    @cached_property
    def assignees(self) -> AsyncAssigneesResourceWithRawResponse:
        return AsyncAssigneesResourceWithRawResponse(self._issues.assignees)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        return AsyncLabelsResourceWithRawResponse(self._issues.labels)

    @cached_property
    def lock(self) -> AsyncLockResourceWithRawResponse:
        return AsyncLockResourceWithRawResponse(self._issues.lock)

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithRawResponse:
        return AsyncReactionsResourceWithRawResponse(self._issues.reactions)

    @cached_property
    def sub_issues(self) -> AsyncSubIssuesResourceWithRawResponse:
        return AsyncSubIssuesResourceWithRawResponse(self._issues.sub_issues)

    @cached_property
    def timeline(self) -> AsyncTimelineResourceWithRawResponse:
        return AsyncTimelineResourceWithRawResponse(self._issues.timeline)


class IssuesResourceWithStreamingResponse:
    def __init__(self, issues: IssuesResource) -> None:
        self._issues = issues

        self.create = to_streamed_response_wrapper(
            issues.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            issues.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            issues.update,
        )
        self.list = to_streamed_response_wrapper(
            issues.list,
        )
        self.remove_sub_issue = to_streamed_response_wrapper(
            issues.remove_sub_issue,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._issues.comments)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._issues.events)

    @cached_property
    def assignees(self) -> AssigneesResourceWithStreamingResponse:
        return AssigneesResourceWithStreamingResponse(self._issues.assignees)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        return LabelsResourceWithStreamingResponse(self._issues.labels)

    @cached_property
    def lock(self) -> LockResourceWithStreamingResponse:
        return LockResourceWithStreamingResponse(self._issues.lock)

    @cached_property
    def reactions(self) -> ReactionsResourceWithStreamingResponse:
        return ReactionsResourceWithStreamingResponse(self._issues.reactions)

    @cached_property
    def sub_issues(self) -> SubIssuesResourceWithStreamingResponse:
        return SubIssuesResourceWithStreamingResponse(self._issues.sub_issues)

    @cached_property
    def timeline(self) -> TimelineResourceWithStreamingResponse:
        return TimelineResourceWithStreamingResponse(self._issues.timeline)


class AsyncIssuesResourceWithStreamingResponse:
    def __init__(self, issues: AsyncIssuesResource) -> None:
        self._issues = issues

        self.create = async_to_streamed_response_wrapper(
            issues.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            issues.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            issues.update,
        )
        self.list = async_to_streamed_response_wrapper(
            issues.list,
        )
        self.remove_sub_issue = async_to_streamed_response_wrapper(
            issues.remove_sub_issue,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._issues.comments)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._issues.events)

    @cached_property
    def assignees(self) -> AsyncAssigneesResourceWithStreamingResponse:
        return AsyncAssigneesResourceWithStreamingResponse(self._issues.assignees)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        return AsyncLabelsResourceWithStreamingResponse(self._issues.labels)

    @cached_property
    def lock(self) -> AsyncLockResourceWithStreamingResponse:
        return AsyncLockResourceWithStreamingResponse(self._issues.lock)

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithStreamingResponse:
        return AsyncReactionsResourceWithStreamingResponse(self._issues.reactions)

    @cached_property
    def sub_issues(self) -> AsyncSubIssuesResourceWithStreamingResponse:
        return AsyncSubIssuesResourceWithStreamingResponse(self._issues.sub_issues)

    @cached_property
    def timeline(self) -> AsyncTimelineResourceWithStreamingResponse:
        return AsyncTimelineResourceWithStreamingResponse(self._issues.timeline)
