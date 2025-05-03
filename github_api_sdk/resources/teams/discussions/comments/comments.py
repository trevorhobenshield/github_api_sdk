from __future__ import annotations

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
from .....types.orgs.teams.discussions.team_discussion_comment import TeamDiscussionComment
from .....types.teams.discussions import comment_create_params, comment_list_params, comment_update_params
from .....types.teams.discussions.comment_list_response import CommentListResponse
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
        discussion_number: int,
        *,
        team_id: int,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussionComment:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Create a discussion comment](https://docs.github.com/rest/teams/discussion-comments#create-a-discussion-comment)
        > endpoint.

        Creates a new comment on a team discussion.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          body: The discussion comment's body text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/teams/{team_id}/discussions/{discussion_number}/comments",
            body=maybe_transform({"body": body}, comment_create_params.CommentCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussionComment,
        )

    def retrieve(
        self,
        comment_number: int,
        *,
        team_id: int,
        discussion_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussionComment:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Get a discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment)
        > endpoint.

        Get a specific comment on a team discussion.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussionComment,
        )

    def update(
        self,
        comment_number: int,
        *,
        team_id: int,
        discussion_number: int,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussionComment:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Update a discussion comment](https://docs.github.com/rest/teams/discussion-comments#update-a-discussion-comment)
        > endpoint.

        Edits the body text of a discussion comment.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          body: The discussion comment's body text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
            body=maybe_transform({"body": body}, comment_update_params.CommentUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussionComment,
        )

    def list(
        self,
        discussion_number: int,
        *,
        team_id: int,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
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
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [List discussion comments](https://docs.github.com/rest/teams/discussion-comments#list-discussion-comments)
        > endpoint.

        List all comments on a team discussion.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/teams/{team_id}/discussions/{discussion_number}/comments",
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
                    },
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
        )

    def delete(
        self,
        comment_number: int,
        *,
        team_id: int,
        discussion_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Delete a discussion comment](https://docs.github.com/rest/teams/discussion-comments#delete-a-discussion-comment)
        > endpoint.

        Deletes a comment on a team discussion.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
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
        discussion_number: int,
        *,
        team_id: int,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussionComment:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Create a discussion comment](https://docs.github.com/rest/teams/discussion-comments#create-a-discussion-comment)
        > endpoint.

        Creates a new comment on a team discussion.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          body: The discussion comment's body text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/teams/{team_id}/discussions/{discussion_number}/comments",
            body=await async_maybe_transform({"body": body}, comment_create_params.CommentCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussionComment,
        )

    async def retrieve(
        self,
        comment_number: int,
        *,
        team_id: int,
        discussion_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussionComment:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Get a discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment)
        > endpoint.

        Get a specific comment on a team discussion.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussionComment,
        )

    async def update(
        self,
        comment_number: int,
        *,
        team_id: int,
        discussion_number: int,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussionComment:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Update a discussion comment](https://docs.github.com/rest/teams/discussion-comments#update-a-discussion-comment)
        > endpoint.

        Edits the body text of a discussion comment.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          body: The discussion comment's body text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
            body=await async_maybe_transform({"body": body}, comment_update_params.CommentUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussionComment,
        )

    async def list(
        self,
        discussion_number: int,
        *,
        team_id: int,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
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
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [List discussion comments](https://docs.github.com/rest/teams/discussion-comments#list-discussion-comments)
        > endpoint.

        List all comments on a team discussion.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/teams/{team_id}/discussions/{discussion_number}/comments",
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
                    },
                    comment_list_params.CommentListParams,
                ),
            ),
            cast_to=CommentListResponse,
        )

    async def delete(
        self,
        comment_number: int,
        *,
        team_id: int,
        discussion_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Delete a discussion comment](https://docs.github.com/rest/teams/discussion-comments#delete-a-discussion-comment)
        > endpoint.

        Deletes a comment on a team discussion.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
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
