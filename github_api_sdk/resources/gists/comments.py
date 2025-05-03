from __future__ import annotations

import httpx

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.gists import comment_create_params, comment_list_params, comment_update_params
from ...types.gists.comment_list_response import CommentListResponse
from ...types.gists.gist_comment import GistComment

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
        gist_id: str,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistComment:
        """
        Creates a comment on a gist.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

        Args:
          body: The comment text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return self._post(
            f"/gists/{gist_id}/comments",
            body=maybe_transform({"body": body}, comment_create_params.CommentCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistComment,
        )

    def retrieve(
        self,
        comment_id: int,
        *,
        gist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistComment:
        """
        Gets a comment on a gist.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return self._get(
            f"/gists/{gist_id}/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistComment,
        )

    def update(
        self,
        comment_id: int,
        *,
        gist_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistComment:
        """
        Updates a comment on a gist.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

        Args:
          body: The comment text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return self._patch(
            f"/gists/{gist_id}/comments/{comment_id}",
            body=maybe_transform({"body": body}, comment_update_params.CommentUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistComment,
        )

    def list(
        self,
        gist_id: str,
        *,
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
        Lists the comments on a gist.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

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
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return self._get(
            f"/gists/{gist_id}/comments",
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

    def delete(
        self,
        comment_id: int,
        *,
        gist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a gist comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/gists/{gist_id}/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
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
        gist_id: str,
        *,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistComment:
        """
        Creates a comment on a gist.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

        Args:
          body: The comment text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return await self._post(
            f"/gists/{gist_id}/comments",
            body=await async_maybe_transform({"body": body}, comment_create_params.CommentCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistComment,
        )

    async def retrieve(
        self,
        comment_id: int,
        *,
        gist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistComment:
        """
        Gets a comment on a gist.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return await self._get(
            f"/gists/{gist_id}/comments/{comment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistComment,
        )

    async def update(
        self,
        comment_id: int,
        *,
        gist_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistComment:
        """
        Updates a comment on a gist.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

        Args:
          body: The comment text.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return await self._patch(
            f"/gists/{gist_id}/comments/{comment_id}",
            body=await async_maybe_transform({"body": body}, comment_update_params.CommentUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistComment,
        )

    async def list(
        self,
        gist_id: str,
        *,
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
        Lists the comments on a gist.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

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
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return await self._get(
            f"/gists/{gist_id}/comments",
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

    async def delete(
        self,
        comment_id: int,
        *,
        gist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a gist comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/gists/{gist_id}/comments/{comment_id}",
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
