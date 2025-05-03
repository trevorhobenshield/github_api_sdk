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
from .....types.orgs.teams import discussion_create_params, discussion_list_params, discussion_update_params
from .....types.orgs.teams.discussion_list_response import DiscussionListResponse
from .....types.orgs.teams.team_discussion import TeamDiscussion
from .comments.comments import (
    AsyncCommentsResource,
    AsyncCommentsResourceWithRawResponse,
    AsyncCommentsResourceWithStreamingResponse,
    CommentsResource,
    CommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
)
from .reactions import (
    AsyncReactionsResource,
    AsyncReactionsResourceWithRawResponse,
    AsyncReactionsResourceWithStreamingResponse,
    ReactionsResource,
    ReactionsResourceWithRawResponse,
    ReactionsResourceWithStreamingResponse,
)

__all__ = ["DiscussionsResource", "AsyncDiscussionsResource"]


class DiscussionsResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def reactions(self) -> ReactionsResource:
        return ReactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DiscussionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return DiscussionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscussionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return DiscussionsResourceWithStreamingResponse(self)

    def create(
        self,
        team_slug: str,
        *,
        org: str,
        body: str,
        title: str,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussion:
        """
        Creates a new discussion post on a team's page.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `POST /organizations/{org_id}/team/{team_id}/discussions`.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          body: The discussion post's body text.

          title: The discussion post's title.

          private: Private posts are only visible to team members, organization owners, and team
              maintainers. Public posts are visible to all members of the organization. Set to
              `true` to create a private post.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._post(
            f"/orgs/{org}/teams/{team_slug}/discussions",
            body=maybe_transform(
                {
                    "body": body,
                    "title": title,
                    "private": private,
                },
                discussion_create_params.DiscussionCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussion,
        )

    def retrieve(
        self,
        discussion_number: int,
        *,
        org: str,
        team_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussion:
        """
        Get a specific discussion on a team's page.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._get(
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussion,
        )

    def update(
        self,
        discussion_number: int,
        *,
        org: str,
        team_slug: str,
        body: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussion:
        """Edits the title and body text of a discussion post.

        Only the parameters you
        provide are updated.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          body: The discussion post's body text.

          title: The discussion post's title.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._patch(
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
            body=maybe_transform(
                {
                    "body": body,
                    "title": title,
                },
                discussion_update_params.DiscussionUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussion,
        )

    def list(
        self,
        team_slug: str,
        *,
        org: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        pinned: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionListResponse:
        """
        List all discussions on a team's page.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/discussions`.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          pinned: Pinned discussions only filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._get(
            f"/orgs/{org}/teams/{team_slug}/discussions",
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
                        "pinned": pinned,
                    },
                    discussion_list_params.DiscussionListParams,
                ),
            ),
            cast_to=DiscussionListResponse,
        )

    def delete(
        self,
        discussion_number: int,
        *,
        org: str,
        team_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a discussion from a team's page.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncDiscussionsResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def reactions(self) -> AsyncReactionsResource:
        return AsyncReactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDiscussionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiscussionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscussionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncDiscussionsResourceWithStreamingResponse(self)

    async def create(
        self,
        team_slug: str,
        *,
        org: str,
        body: str,
        title: str,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussion:
        """
        Creates a new discussion post on a team's page.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `POST /organizations/{org_id}/team/{team_id}/discussions`.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          body: The discussion post's body text.

          title: The discussion post's title.

          private: Private posts are only visible to team members, organization owners, and team
              maintainers. Public posts are visible to all members of the organization. Set to
              `true` to create a private post.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._post(
            f"/orgs/{org}/teams/{team_slug}/discussions",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "title": title,
                    "private": private,
                },
                discussion_create_params.DiscussionCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussion,
        )

    async def retrieve(
        self,
        discussion_number: int,
        *,
        org: str,
        team_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussion:
        """
        Get a specific discussion on a team's page.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussion,
        )

    async def update(
        self,
        discussion_number: int,
        *,
        org: str,
        team_slug: str,
        body: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamDiscussion:
        """Edits the title and body text of a discussion post.

        Only the parameters you
        provide are updated.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          body: The discussion post's body text.

          title: The discussion post's title.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._patch(
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "title": title,
                },
                discussion_update_params.DiscussionUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamDiscussion,
        )

    async def list(
        self,
        team_slug: str,
        *,
        org: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        pinned: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscussionListResponse:
        """
        List all discussions on a team's page.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/discussions`.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          direction: The direction to sort the results by.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          pinned: Pinned discussions only filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}/discussions",
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
                        "pinned": pinned,
                    },
                    discussion_list_params.DiscussionListParams,
                ),
            ),
            cast_to=DiscussionListResponse,
        )

    async def delete(
        self,
        discussion_number: int,
        *,
        org: str,
        team_slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a discussion from a team's page.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class DiscussionsResourceWithRawResponse:
    def __init__(self, discussions: DiscussionsResource) -> None:
        self._discussions = discussions

        self.create = to_raw_response_wrapper(
            discussions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            discussions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            discussions.update,
        )
        self.list = to_raw_response_wrapper(
            discussions.list,
        )
        self.delete = to_raw_response_wrapper(
            discussions.delete,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._discussions.comments)

    @cached_property
    def reactions(self) -> ReactionsResourceWithRawResponse:
        return ReactionsResourceWithRawResponse(self._discussions.reactions)


class AsyncDiscussionsResourceWithRawResponse:
    def __init__(self, discussions: AsyncDiscussionsResource) -> None:
        self._discussions = discussions

        self.create = async_to_raw_response_wrapper(
            discussions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            discussions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            discussions.update,
        )
        self.list = async_to_raw_response_wrapper(
            discussions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            discussions.delete,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._discussions.comments)

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithRawResponse:
        return AsyncReactionsResourceWithRawResponse(self._discussions.reactions)


class DiscussionsResourceWithStreamingResponse:
    def __init__(self, discussions: DiscussionsResource) -> None:
        self._discussions = discussions

        self.create = to_streamed_response_wrapper(
            discussions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            discussions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            discussions.update,
        )
        self.list = to_streamed_response_wrapper(
            discussions.list,
        )
        self.delete = to_streamed_response_wrapper(
            discussions.delete,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._discussions.comments)

    @cached_property
    def reactions(self) -> ReactionsResourceWithStreamingResponse:
        return ReactionsResourceWithStreamingResponse(self._discussions.reactions)


class AsyncDiscussionsResourceWithStreamingResponse:
    def __init__(self, discussions: AsyncDiscussionsResource) -> None:
        self._discussions = discussions

        self.create = async_to_streamed_response_wrapper(
            discussions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            discussions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            discussions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            discussions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            discussions.delete,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._discussions.comments)

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithStreamingResponse:
        return AsyncReactionsResourceWithStreamingResponse(self._discussions.reactions)
