from __future__ import annotations

from typing import Iterable

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
from ....types.repos.pulls import (
    review_create_params,
    review_dismiss_params,
    review_list_comments_params,
    review_list_params,
    review_submit_params,
    review_update_params,
)
from ....types.repos.pulls.pull_request_review import PullRequestReview
from ....types.repos.pulls.review_list_comments_response import ReviewListCommentsResponse
from ....types.repos.pulls.review_list_response import ReviewListResponse

__all__ = ["ReviewsResource", "AsyncReviewsResource"]


class ReviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ReviewsResourceWithStreamingResponse(self)

    def create(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        body: str | NotGiven = NOT_GIVEN,
        comments: Iterable[review_create_params.Comment] | NotGiven = NOT_GIVEN,
        commit_id: str | NotGiven = NOT_GIVEN,
        event: Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """
        Creates a review on a specified pull request.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Pull request reviews created in the `PENDING` state are not submitted and
        therefore do not include the `submitted_at` property in the response. To create
        a pending review for a pull request, leave the `event` parameter blank. For more
        information about submitting a `PENDING` review, see
        "[Submit a review for a pull request](https://docs.github.com/rest/pulls/reviews#submit-a-review-for-a-pull-request)."

        > [!NOTE] To comment on a specific line in a file, you need to first determine
        > the position of that line in the diff. To see a pull request diff, add the
        > `application/vnd.github.v3.diff` media type to the `Accept` header of a call
        > to the
        > [Get a pull request](https://docs.github.com/rest/pulls/pulls#get-a-pull-request)
        > endpoint.

        The `position` value equals the number of lines down from the first "@@" hunk
        header in the file you want to add a comment. The line just below the "@@" line
        is position 1, the next line is position 2, and so on. The position in the diff
        continues to increase through lines of whitespace and additional hunks until the
        beginning of a new file.

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
          body: **Required** when using `REQUEST_CHANGES` or `COMMENT` for the `event`
              parameter. The body text of the pull request review.

          comments: Use the following table to specify the location, destination, and contents of
              the draft review comment.

          commit_id: The SHA of the commit that needs a review. Not using the latest commit SHA may
              render your review comment outdated if a subsequent commit modifies the line you
              specify as the `position`. Defaults to the most recent commit in the pull
              request when you do not specify a value.

          event: The review action you want to perform. The review actions include: `APPROVE`,
              `REQUEST_CHANGES`, or `COMMENT`. By leaving this blank, you set the review
              action state to `PENDING`, which means you will need to
              [submit the pull request review](https://docs.github.com/rest/pulls/reviews#submit-a-review-for-a-pull-request)
              when you are ready.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
            body=maybe_transform(
                {
                    "body": body,
                    "comments": comments,
                    "commit_id": commit_id,
                    "event": event,
                },
                review_create_params.ReviewCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    def retrieve(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """
        Retrieves a pull request review by its ID.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    def update(
        self,
        review_id: int,
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
    ) -> PullRequestReview:
        """
        Updates the contents of a specified review summary comment.

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
          body: The body text of the pull request review.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._put(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
            body=maybe_transform({"body": body}, review_update_params.ReviewUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    def list(
        self,
        pull_number: int,
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
    ) -> ReviewListResponse:
        """Lists all reviews for a specified pull request.

        The list of reviews returns in
        chronological order.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
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
                    review_list_params.ReviewListParams,
                ),
            ),
            cast_to=ReviewListResponse,
        )

    def delete(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """Deletes a pull request review that has not been submitted.

        Submitted reviews
        cannot be deleted.

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
        return self._delete(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    def dismiss(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        message: str,
        event: Literal["DISMISS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """
        Dismisses a specified review on a pull request.

        > [!NOTE] To dismiss a pull request review on a
        > [protected branch](https://docs.github.com/rest/branches/branch-protection),
        > you must be a repository administrator or be included in the list of people or
        > teams who can dismiss pull request reviews.

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
          message: The message for the pull request review dismissal

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._put(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals",
            body=maybe_transform(
                {
                    "message": message,
                    "event": event,
                },
                review_dismiss_params.ReviewDismissParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    def list_comments(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReviewListCommentsResponse:
        """
        Lists comments for a specific pull request review.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments",
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
                    review_list_comments_params.ReviewListCommentsParams,
                ),
            ),
            cast_to=ReviewListCommentsResponse,
        )

    def submit(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        event: Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"],
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """Submits a pending review for a pull request.

        For more information about creating
        a pending review for a pull request, see
        "[Create a review for a pull request](https://docs.github.com/rest/pulls/reviews#create-a-review-for-a-pull-request)."

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
          event: The review action you want to perform. The review actions include: `APPROVE`,
              `REQUEST_CHANGES`, or `COMMENT`. When you leave this blank, the API returns
              _HTTP 422 (Unrecognizable entity)_ and sets the review action state to
              `PENDING`, which means you will need to re-submit the pull request review using
              a review action.

          body: The body text of the pull request review

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events",
            body=maybe_transform(
                {
                    "event": event,
                    "body": body,
                },
                review_submit_params.ReviewSubmitParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )


class AsyncReviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncReviewsResourceWithStreamingResponse(self)

    async def create(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        body: str | NotGiven = NOT_GIVEN,
        comments: Iterable[review_create_params.Comment] | NotGiven = NOT_GIVEN,
        commit_id: str | NotGiven = NOT_GIVEN,
        event: Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """
        Creates a review on a specified pull request.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Pull request reviews created in the `PENDING` state are not submitted and
        therefore do not include the `submitted_at` property in the response. To create
        a pending review for a pull request, leave the `event` parameter blank. For more
        information about submitting a `PENDING` review, see
        "[Submit a review for a pull request](https://docs.github.com/rest/pulls/reviews#submit-a-review-for-a-pull-request)."

        > [!NOTE] To comment on a specific line in a file, you need to first determine
        > the position of that line in the diff. To see a pull request diff, add the
        > `application/vnd.github.v3.diff` media type to the `Accept` header of a call
        > to the
        > [Get a pull request](https://docs.github.com/rest/pulls/pulls#get-a-pull-request)
        > endpoint.

        The `position` value equals the number of lines down from the first "@@" hunk
        header in the file you want to add a comment. The line just below the "@@" line
        is position 1, the next line is position 2, and so on. The position in the diff
        continues to increase through lines of whitespace and additional hunks until the
        beginning of a new file.

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
          body: **Required** when using `REQUEST_CHANGES` or `COMMENT` for the `event`
              parameter. The body text of the pull request review.

          comments: Use the following table to specify the location, destination, and contents of
              the draft review comment.

          commit_id: The SHA of the commit that needs a review. Not using the latest commit SHA may
              render your review comment outdated if a subsequent commit modifies the line you
              specify as the `position`. Defaults to the most recent commit in the pull
              request when you do not specify a value.

          event: The review action you want to perform. The review actions include: `APPROVE`,
              `REQUEST_CHANGES`, or `COMMENT`. By leaving this blank, you set the review
              action state to `PENDING`, which means you will need to
              [submit the pull request review](https://docs.github.com/rest/pulls/reviews#submit-a-review-for-a-pull-request)
              when you are ready.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "comments": comments,
                    "commit_id": commit_id,
                    "event": event,
                },
                review_create_params.ReviewCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    async def retrieve(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """
        Retrieves a pull request review by its ID.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    async def update(
        self,
        review_id: int,
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
    ) -> PullRequestReview:
        """
        Updates the contents of a specified review summary comment.

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
          body: The body text of the pull request review.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
            body=await async_maybe_transform({"body": body}, review_update_params.ReviewUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    async def list(
        self,
        pull_number: int,
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
    ) -> ReviewListResponse:
        """Lists all reviews for a specified pull request.

        The list of reviews returns in
        chronological order.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
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
                    review_list_params.ReviewListParams,
                ),
            ),
            cast_to=ReviewListResponse,
        )

    async def delete(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """Deletes a pull request review that has not been submitted.

        Submitted reviews
        cannot be deleted.

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
        return await self._delete(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    async def dismiss(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        message: str,
        event: Literal["DISMISS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """
        Dismisses a specified review on a pull request.

        > [!NOTE] To dismiss a pull request review on a
        > [protected branch](https://docs.github.com/rest/branches/branch-protection),
        > you must be a repository administrator or be included in the list of people or
        > teams who can dismiss pull request reviews.

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
          message: The message for the pull request review dismissal

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "event": event,
                },
                review_dismiss_params.ReviewDismissParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )

    async def list_comments(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReviewListCommentsResponse:
        """
        Lists comments for a specific pull request review.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments",
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
                    review_list_comments_params.ReviewListCommentsParams,
                ),
            ),
            cast_to=ReviewListCommentsResponse,
        )

    async def submit(
        self,
        review_id: int,
        *,
        owner: str,
        repo: str,
        pull_number: int,
        event: Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"],
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequestReview:
        """Submits a pending review for a pull request.

        For more information about creating
        a pending review for a pull request, see
        "[Create a review for a pull request](https://docs.github.com/rest/pulls/reviews#create-a-review-for-a-pull-request)."

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
          event: The review action you want to perform. The review actions include: `APPROVE`,
              `REQUEST_CHANGES`, or `COMMENT`. When you leave this blank, the API returns
              _HTTP 422 (Unrecognizable entity)_ and sets the review action state to
              `PENDING`, which means you will need to re-submit the pull request review using
              a review action.

          body: The body text of the pull request review

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events",
            body=await async_maybe_transform(
                {
                    "event": event,
                    "body": body,
                },
                review_submit_params.ReviewSubmitParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequestReview,
        )


class ReviewsResourceWithRawResponse:
    def __init__(self, reviews: ReviewsResource) -> None:
        self._reviews = reviews

        self.create = to_raw_response_wrapper(
            reviews.create,
        )
        self.retrieve = to_raw_response_wrapper(
            reviews.retrieve,
        )
        self.update = to_raw_response_wrapper(
            reviews.update,
        )
        self.list = to_raw_response_wrapper(
            reviews.list,
        )
        self.delete = to_raw_response_wrapper(
            reviews.delete,
        )
        self.dismiss = to_raw_response_wrapper(
            reviews.dismiss,
        )
        self.list_comments = to_raw_response_wrapper(
            reviews.list_comments,
        )
        self.submit = to_raw_response_wrapper(
            reviews.submit,
        )


class AsyncReviewsResourceWithRawResponse:
    def __init__(self, reviews: AsyncReviewsResource) -> None:
        self._reviews = reviews

        self.create = async_to_raw_response_wrapper(
            reviews.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            reviews.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            reviews.update,
        )
        self.list = async_to_raw_response_wrapper(
            reviews.list,
        )
        self.delete = async_to_raw_response_wrapper(
            reviews.delete,
        )
        self.dismiss = async_to_raw_response_wrapper(
            reviews.dismiss,
        )
        self.list_comments = async_to_raw_response_wrapper(
            reviews.list_comments,
        )
        self.submit = async_to_raw_response_wrapper(
            reviews.submit,
        )


class ReviewsResourceWithStreamingResponse:
    def __init__(self, reviews: ReviewsResource) -> None:
        self._reviews = reviews

        self.create = to_streamed_response_wrapper(
            reviews.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            reviews.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            reviews.update,
        )
        self.list = to_streamed_response_wrapper(
            reviews.list,
        )
        self.delete = to_streamed_response_wrapper(
            reviews.delete,
        )
        self.dismiss = to_streamed_response_wrapper(
            reviews.dismiss,
        )
        self.list_comments = to_streamed_response_wrapper(
            reviews.list_comments,
        )
        self.submit = to_streamed_response_wrapper(
            reviews.submit,
        )


class AsyncReviewsResourceWithStreamingResponse:
    def __init__(self, reviews: AsyncReviewsResource) -> None:
        self._reviews = reviews

        self.create = async_to_streamed_response_wrapper(
            reviews.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            reviews.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            reviews.update,
        )
        self.list = async_to_streamed_response_wrapper(
            reviews.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            reviews.delete,
        )
        self.dismiss = async_to_streamed_response_wrapper(
            reviews.dismiss,
        )
        self.list_comments = async_to_streamed_response_wrapper(
            reviews.list_comments,
        )
        self.submit = async_to_streamed_response_wrapper(
            reviews.submit,
        )
