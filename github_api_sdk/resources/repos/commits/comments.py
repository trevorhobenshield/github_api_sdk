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
from ....types.repos.commit_comment import CommitComment
from ....types.repos.commits import comment_create_params, comment_list_params
from ....types.repos.commits.comment_list_response import CommentListResponse

__all__ = ["CommentsResource", "AsyncCommentsResource"]


class CommentsResource(SyncAPIResource):
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
        commit_sha: str,
        *,
        owner: str,
        repo: str,
        body: str,
        line: int | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitComment:
        """
        Create a comment for a commit using its `:commit_sha`.

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
          body: The contents of the comment.

          line: **Closing down notice**. Use **position** parameter instead. Line number in the
              file to comment on.

          path: Relative path of the file to comment on.

          position: Line index in the diff to comment on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not commit_sha:
            raise ValueError(f"Expected a non-empty value for `commit_sha` but received {commit_sha!r}")
        return self._post(
            f"/repos/{owner}/{repo}/commits/{commit_sha}/comments",
            body=maybe_transform(
                {
                    "body": body,
                    "line": line,
                    "path": path,
                    "position": position,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CommitComment,
        )

    def list(
        self,
        commit_sha: str,
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
    ) -> CommentListResponse:
        """
        Lists the comments for a specified commit.

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
        if not commit_sha:
            raise ValueError(f"Expected a non-empty value for `commit_sha` but received {commit_sha!r}")
        return self._get(
            f"/repos/{owner}/{repo}/commits/{commit_sha}/comments",
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
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
        )


class AsyncCommentsResource(AsyncAPIResource):
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
        commit_sha: str,
        *,
        owner: str,
        repo: str,
        body: str,
        line: int | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        position: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitComment:
        """
        Create a comment for a commit using its `:commit_sha`.

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
          body: The contents of the comment.

          line: **Closing down notice**. Use **position** parameter instead. Line number in the
              file to comment on.

          path: Relative path of the file to comment on.

          position: Line index in the diff to comment on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not commit_sha:
            raise ValueError(f"Expected a non-empty value for `commit_sha` but received {commit_sha!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/commits/{commit_sha}/comments",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "line": line,
                    "path": path,
                    "position": position,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CommitComment,
        )

    async def list(
        self,
        commit_sha: str,
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
    ) -> CommentListResponse:
        """
        Lists the comments for a specified commit.

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
        if not commit_sha:
            raise ValueError(f"Expected a non-empty value for `commit_sha` but received {commit_sha!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/commits/{commit_sha}/comments",
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
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
        )


class CommentsResourceWithRawResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_raw_response_wrapper(
            comments.create,
        )
        self.list = to_raw_response_wrapper(
            comments.list,
        )


class AsyncCommentsResourceWithRawResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_raw_response_wrapper(
            comments.create,
        )
        self.list = async_to_raw_response_wrapper(
            comments.list,
        )


class CommentsResourceWithStreamingResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_streamed_response_wrapper(
            comments.create,
        )
        self.list = to_streamed_response_wrapper(
            comments.list,
        )


class AsyncCommentsResourceWithStreamingResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_streamed_response_wrapper(
            comments.create,
        )
        self.list = async_to_streamed_response_wrapper(
            comments.list,
        )
