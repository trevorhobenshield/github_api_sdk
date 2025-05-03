from __future__ import annotations

from datetime import datetime
from typing import Union

import httpx
from typing_extensions import Literal

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.repos.pulls import (
    comment_create_params,
    comment_list_params,
    comment_reply_params,
    comment_update_params,
)
from .....types.repos.pulls.comment_list_response import CommentListResponse
from .....types.repos.pulls.pull_request_review_comment import PullRequestReviewComment
from .reactions import (
    AsyncReactionsResource,
    AsyncReactionsResourceWithRawResponse,
    AsyncReactionsResourceWithStreamingResponse,
    ReactionsResource,
    ReactionsResourceWithRawResponse,
    ReactionsResourceWithStreamingResponse,
)

__all__ = ["CommentsResource", "AsyncCommentsResource"]


class CommentsResource(SyncAPIResource):
    @cached_property
    def reactions(self) -> ReactionsResource:
        return ReactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CommentsResourceWithStreamingResponse(self)

    def create(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        body: str,
        commit_id: str,
        path: str,
        in_reply_to: int | NotGiven = NOT_GIVEN,
        line: int | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        side: Literal["LEFT", "RIGHT"] | NotGiven = NOT_GIVEN,
        start_line: int | NotGiven = NOT_GIVEN,
        start_side: Literal["LEFT", "RIGHT", "side"] | NotGiven = NOT_GIVEN,
        subject_type: Literal["line", "file"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReviewComment:
        """Creates a review comment on the diff of a specified pull request.

        To add a
        regular comment to a pull request timeline, see
        "[Create an issue comment](https://docs.github.com/rest/issues/comments#create-an-issue-comment)."

        If your comment applies to more than one line in the pull request diff, you
        should use the parameters `line`, `side`, and optionally `start_line` and
        `start_side` in your request.

        The `position` parameter is closing down. If you use `position`, the `line`,
        `side`, `start_line`, and `start_side` parameters are not required.

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

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

        Args:
          body: The text of the review comment.

          commit_id: The SHA of the commit needing a comment. Not using the latest commit SHA may
              render your comment outdated if a subsequent commit modifies the line you
              specify as the `position`.

          path: The relative path to the file that necessitates a comment.

          in_reply_to: The ID of the review comment to reply to. To find the ID of a review comment
              with
              ["List review comments on a pull request"](#list-review-comments-on-a-pull-request).
              When specified, all parameters other than `body` in the request body are
              ignored.

          line: **Required unless using `subject_type:file`**. The line of the blob in the pull
              request diff that the comment applies to. For a multi-line comment, the last
              line of the range that your comment applies to.

          position: **This parameter is closing down. Use `line` instead**. The position in the diff
              where you want to add a review comment. Note this value is not the same as the
              line number in the file. The position value equals the number of lines down from
              the first "@@" hunk header in the file you want to add a comment. The line just
              below the "@@" line is position 1, the next line is position 2, and so on. The
              position in the diff continues to increase through lines of whitespace and
              additional hunks until the beginning of a new file.

          side: In a split diff view, the side of the diff that the pull request's changes
              appear on. Can be `LEFT` or `RIGHT`. Use `LEFT` for deletions that appear in
              red. Use `RIGHT` for additions that appear in green or unchanged lines that
              appear in white and are shown for context. For a multi-line comment, side
              represents whether the last line of the comment range is a deletion or addition.
              For more information, see
              "[Diff view options](https://docs.github.com/articles/about-comparing-branches-in-pull-requests#diff-view-options)"
              in the GitHub Help documentation.

          start_line: **Required when using multi-line comments unless using `in_reply_to`**. The
              `start_line` is the first line in the pull request diff that your multi-line
              comment applies to. To learn more about multi-line comments, see
              "[Commenting on a pull request](https://docs.github.com/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)"
              in the GitHub Help documentation.

          start_side: **Required when using multi-line comments unless using `in_reply_to`**. The
              `start_side` is the starting side of the diff that the comment applies to. Can
              be `LEFT` or `RIGHT`. To learn more about multi-line comments, see
              "[Commenting on a pull request](https://docs.github.com/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)"
              in the GitHub Help documentation. See `side` in this table for additional
              context.

          subject_type: The level at which the comment is targeted.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
            body=maybe_transform(
                {
                    "body": body,
                    "commit_id": commit_id,
                    "path": path,
                    "in_reply_to": in_reply_to,
                    "line": line,
                    "position": position,
                    "side": side,
                    "start_line": start_line,
                    "start_side": start_side,
                    "subject_type": subject_type,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReviewComment,
        )

    def retrieve(
        self,
        comment_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReviewComment:
        """
        Provides details for a specified review comment.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

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
            f"/repos/{owner}/{repo}/pulls/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReviewComment,
        )

    def update(
        self,
        comment_id: int,
        *,
        owner: str,
        repo: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReviewComment:
        """
        Edits the content of a specified review comment.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

        Args:
          body: The text of the reply to the review comment.

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
            f"/repos/{owner}/{repo}/pulls/comments/{comment_id}",
            body=maybe_transform({"body": body}, comment_update_params.CommentUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReviewComment,
        )

    def list(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentListResponse:
        """Lists all review comments for a specified pull request.

        By default, review
        comments are in ascending order by ID.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

        Args:
          direction: The direction to sort results. Ignored without `sort` parameter.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: The property to sort the results by.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "sort": sort,
                    },
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
        )

    def delete(
        self,
        comment_id: int,
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
        Deletes a review comment.

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
            f"/repos/{owner}/{repo}/pulls/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def reply(
        self,
        comment_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReviewComment:
        """Creates a reply to a review comment for a pull request.

        For the `comment_id`,
        provide the ID of the review comment you are replying to. This must be the ID of
        a _top-level review comment_, not a reply to that comment. Replies to replies
        are not supported.

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

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

        Args:
          body: The text of the review comment.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies",
            body=maybe_transform({"body": body}, comment_reply_params.CommentReplyParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReviewComment,
        )


class AsyncCommentsResource(AsyncAPIResource):
    @cached_property
    def reactions(self) -> AsyncReactionsResource:
        return AsyncReactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCommentsResourceWithStreamingResponse(self)

    async def create(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        body: str,
        commit_id: str,
        path: str,
        in_reply_to: int | NotGiven = NOT_GIVEN,
        line: int | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        side: Literal["LEFT", "RIGHT"] | NotGiven = NOT_GIVEN,
        start_line: int | NotGiven = NOT_GIVEN,
        start_side: Literal["LEFT", "RIGHT", "side"] | NotGiven = NOT_GIVEN,
        subject_type: Literal["line", "file"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReviewComment:
        """Creates a review comment on the diff of a specified pull request.

        To add a
        regular comment to a pull request timeline, see
        "[Create an issue comment](https://docs.github.com/rest/issues/comments#create-an-issue-comment)."

        If your comment applies to more than one line in the pull request diff, you
        should use the parameters `line`, `side`, and optionally `start_line` and
        `start_side` in your request.

        The `position` parameter is closing down. If you use `position`, the `line`,
        `side`, `start_line`, and `start_side` parameters are not required.

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

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

        Args:
          body: The text of the review comment.

          commit_id: The SHA of the commit needing a comment. Not using the latest commit SHA may
              render your comment outdated if a subsequent commit modifies the line you
              specify as the `position`.

          path: The relative path to the file that necessitates a comment.

          in_reply_to: The ID of the review comment to reply to. To find the ID of a review comment
              with
              ["List review comments on a pull request"](#list-review-comments-on-a-pull-request).
              When specified, all parameters other than `body` in the request body are
              ignored.

          line: **Required unless using `subject_type:file`**. The line of the blob in the pull
              request diff that the comment applies to. For a multi-line comment, the last
              line of the range that your comment applies to.

          position: **This parameter is closing down. Use `line` instead**. The position in the diff
              where you want to add a review comment. Note this value is not the same as the
              line number in the file. The position value equals the number of lines down from
              the first "@@" hunk header in the file you want to add a comment. The line just
              below the "@@" line is position 1, the next line is position 2, and so on. The
              position in the diff continues to increase through lines of whitespace and
              additional hunks until the beginning of a new file.

          side: In a split diff view, the side of the diff that the pull request's changes
              appear on. Can be `LEFT` or `RIGHT`. Use `LEFT` for deletions that appear in
              red. Use `RIGHT` for additions that appear in green or unchanged lines that
              appear in white and are shown for context. For a multi-line comment, side
              represents whether the last line of the comment range is a deletion or addition.
              For more information, see
              "[Diff view options](https://docs.github.com/articles/about-comparing-branches-in-pull-requests#diff-view-options)"
              in the GitHub Help documentation.

          start_line: **Required when using multi-line comments unless using `in_reply_to`**. The
              `start_line` is the first line in the pull request diff that your multi-line
              comment applies to. To learn more about multi-line comments, see
              "[Commenting on a pull request](https://docs.github.com/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)"
              in the GitHub Help documentation.

          start_side: **Required when using multi-line comments unless using `in_reply_to`**. The
              `start_side` is the starting side of the diff that the comment applies to. Can
              be `LEFT` or `RIGHT`. To learn more about multi-line comments, see
              "[Commenting on a pull request](https://docs.github.com/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)"
              in the GitHub Help documentation. See `side` in this table for additional
              context.

          subject_type: The level at which the comment is targeted.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "commit_id": commit_id,
                    "path": path,
                    "in_reply_to": in_reply_to,
                    "line": line,
                    "position": position,
                    "side": side,
                    "start_line": start_line,
                    "start_side": start_side,
                    "subject_type": subject_type,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReviewComment,
        )

    async def retrieve(
        self,
        comment_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReviewComment:
        """
        Provides details for a specified review comment.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

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
            f"/repos/{owner}/{repo}/pulls/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReviewComment,
        )

    async def update(
        self,
        comment_id: int,
        *,
        owner: str,
        repo: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReviewComment:
        """
        Edits the content of a specified review comment.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

        Args:
          body: The text of the reply to the review comment.

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
            f"/repos/{owner}/{repo}/pulls/comments/{comment_id}",
            body=await async_maybe_transform({"body": body}, comment_update_params.CommentUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReviewComment,
        )

    async def list(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentListResponse:
        """Lists all review comments for a specified pull request.

        By default, review
        comments are in ascending order by ID.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

        Args:
          direction: The direction to sort results. Ignored without `sort` parameter.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: The property to sort the results by.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "sort": sort,
                    },
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
        )

    async def delete(
        self,
        comment_id: int,
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
        Deletes a review comment.

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
            f"/repos/{owner}/{repo}/pulls/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def reply(
        self,
        comment_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReviewComment:
        """Creates a reply to a review comment for a pull request.

        For the `comment_id`,
        provide the ID of the review comment you are replying to. This must be the ID of
        a _top-level review comment_, not a reply to that comment. Replies to replies
        are not supported.

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

        - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown
          body. Response will include `body`. This is the default if you do not pass any
          specific media type.
        - **`application/vnd.github-commitcomment.text+json`**: Returns a text only
          representation of the markdown body. Response will include `body_text`.
        - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered
          from the body's markdown. Response will include `body_html`.
        - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and
          HTML representations. Response will include `body`, `body_text`, and
          `body_html`.

        Args:
          body: The text of the review comment.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies",
            body=await async_maybe_transform({"body": body}, comment_reply_params.CommentReplyParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReviewComment,
        )


class CommentsResourceWithRawResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_raw_response_wrapper(
            comments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            comments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            comments.update,
        )
        self.list = to_raw_response_wrapper(
            comments.list,
        )
        self.delete = to_raw_response_wrapper(
            comments.delete,
        )
        self.reply = to_raw_response_wrapper(
            comments.reply,
        )

    @cached_property
    def reactions(self) -> ReactionsResourceWithRawResponse:
        return ReactionsResourceWithRawResponse(self._comments.reactions)


class AsyncCommentsResourceWithRawResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_raw_response_wrapper(
            comments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            comments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            comments.update,
        )
        self.list = async_to_raw_response_wrapper(
            comments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            comments.delete,
        )
        self.reply = async_to_raw_response_wrapper(
            comments.reply,
        )

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithRawResponse:
        return AsyncReactionsResourceWithRawResponse(self._comments.reactions)


class CommentsResourceWithStreamingResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_streamed_response_wrapper(
            comments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            comments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            comments.update,
        )
        self.list = to_streamed_response_wrapper(
            comments.list,
        )
        self.delete = to_streamed_response_wrapper(
            comments.delete,
        )
        self.reply = to_streamed_response_wrapper(
            comments.reply,
        )

    @cached_property
    def reactions(self) -> ReactionsResourceWithStreamingResponse:
        return ReactionsResourceWithStreamingResponse(self._comments.reactions)


class AsyncCommentsResourceWithStreamingResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_streamed_response_wrapper(
            comments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            comments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            comments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            comments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            comments.delete,
        )
        self.reply = async_to_streamed_response_wrapper(
            comments.reply,
        )

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithStreamingResponse:
        return AsyncReactionsResourceWithStreamingResponse(self._comments.reactions)
