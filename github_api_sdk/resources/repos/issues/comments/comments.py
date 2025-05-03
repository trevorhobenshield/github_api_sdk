from __future__ import annotations

from datetime import datetime
from typing import Union

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
from ....._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.repos.issues import comment_create_params, comment_list_params, comment_update_params
from .....types.repos.issues.comment_list_response import CommentListResponse
from .....types.repos.issues.issue_comment import IssueComment
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
        issue_number: int,
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
    ) -> IssueComment:
        """You can use the REST API to create comments on issues and pull requests.

        Every
        pull request is an issue, but not every issue is a pull request.

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
          body: The contents of the comment.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
            body=maybe_transform({"body": body}, comment_create_params.CommentCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueComment,
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
    ) -> IssueComment:
        """You can use the REST API to get comments on issues and pull requests.

        Every pull
        request is an issue, but not every issue is a pull request.

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
            f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueComment,
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
    ) -> IssueComment:
        """You can use the REST API to update comments on issues and pull requests.

        Every
        pull request is an issue, but not every issue is a pull request.

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
          body: The contents of the comment.

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
            f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
            body=maybe_transform({"body": body}, comment_update_params.CommentUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueComment,
        )

    def list(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentListResponse:
        """You can use the REST API to list comments on issues and pull requests.

        Every
        pull request is an issue, but not every issue is a pull request.

        Issue comments are ordered by ascending ID.

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

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "since": since,
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
        """You can use the REST API to delete comments on issues and pull requests.

        Every
        pull request is an issue, but not every issue is a pull request.

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
            f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
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
        issue_number: int,
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
    ) -> IssueComment:
        """You can use the REST API to create comments on issues and pull requests.

        Every
        pull request is an issue, but not every issue is a pull request.

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
          body: The contents of the comment.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
            body=await async_maybe_transform({"body": body}, comment_create_params.CommentCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueComment,
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
    ) -> IssueComment:
        """You can use the REST API to get comments on issues and pull requests.

        Every pull
        request is an issue, but not every issue is a pull request.

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
            f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueComment,
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
    ) -> IssueComment:
        """You can use the REST API to update comments on issues and pull requests.

        Every
        pull request is an issue, but not every issue is a pull request.

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
          body: The contents of the comment.

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
            f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
            body=await async_maybe_transform({"body": body}, comment_update_params.CommentUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueComment,
        )

    async def list(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommentListResponse:
        """You can use the REST API to list comments on issues and pull requests.

        Every
        pull request is an issue, but not every issue is a pull request.

        Issue comments are ordered by ascending ID.

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

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "since": since,
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
        """You can use the REST API to delete comments on issues and pull requests.

        Every
        pull request is an issue, but not every issue is a pull request.

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
            f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
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

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithStreamingResponse:
        return AsyncReactionsResourceWithStreamingResponse(self._comments.reactions)
