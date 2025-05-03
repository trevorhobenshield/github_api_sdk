from __future__ import annotations

import httpx
from typing_extensions import Literal

from ......_base_client import make_request_options
from ......_compat import cached_property
from ......_resource import AsyncAPIResource, SyncAPIResource
from ......_response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ......_types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ......_utils import (
    async_maybe_transform,
    maybe_transform,
)
from ......types.orgs.teams.discussions.comments import reaction_create_params, reaction_list_params
from ......types.orgs.teams.discussions.comments.reaction import Reaction
from ......types.orgs.teams.discussions.comments.reaction_list_response import ReactionListResponse

__all__ = ["ReactionsResource", "AsyncReactionsResource"]


class ReactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ReactionsResourceWithStreamingResponse(self)

    def create(
        self,
        comment_number: int,
        *,
        org: str,
        team_slug: str,
        discussion_number: int,
        content: Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Reaction:
        """
        Create a reaction to a
        [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).

        A response with an HTTP `200` status means that you already added the reaction
        type to this team discussion comment.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          content: The
              [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions)
              to add to the team discussion comment.

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
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions",
            body=maybe_transform({"content": content}, reaction_create_params.ReactionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Reaction,
        )

    def list(
        self,
        comment_number: int,
        *,
        org: str,
        team_slug: str,
        discussion_number: int,
        content: Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReactionListResponse:
        """
        List the reactions to a
        [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          content: Returns a single
              [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions).
              Omit this parameter to list all reactions to a team discussion comment.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

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
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "content": content,
                        "page": page,
                        "per_page": per_page,
                    },
                    reaction_list_params.ReactionListParams,
                ),
            ),
            cast_to=ReactionListResponse,
        )

    def delete(
        self,
        reaction_id: int,
        *,
        org: str,
        team_slug: str,
        discussion_number: int,
        comment_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!NOTE] You can also specify a team or organization with `team_id` and
        > `org_id` using the route
        > `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id`.

        Delete a reaction to a
        [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).

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
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncReactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncReactionsResourceWithStreamingResponse(self)

    async def create(
        self,
        comment_number: int,
        *,
        org: str,
        team_slug: str,
        discussion_number: int,
        content: Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Reaction:
        """
        Create a reaction to a
        [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).

        A response with an HTTP `200` status means that you already added the reaction
        type to this team discussion comment.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          content: The
              [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions)
              to add to the team discussion comment.

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
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions",
            body=await async_maybe_transform({"content": content}, reaction_create_params.ReactionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Reaction,
        )

    async def list(
        self,
        comment_number: int,
        *,
        org: str,
        team_slug: str,
        discussion_number: int,
        content: Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReactionListResponse:
        """
        List the reactions to a
        [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          content: Returns a single
              [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions).
              Omit this parameter to list all reactions to a team discussion comment.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

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
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "content": content,
                        "page": page,
                        "per_page": per_page,
                    },
                    reaction_list_params.ReactionListParams,
                ),
            ),
            cast_to=ReactionListResponse,
        )

    async def delete(
        self,
        reaction_id: int,
        *,
        org: str,
        team_slug: str,
        discussion_number: int,
        comment_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!NOTE] You can also specify a team or organization with `team_id` and
        > `org_id` using the route
        > `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id`.

        Delete a reaction to a
        [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).

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
            f"/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ReactionsResourceWithRawResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.create = to_raw_response_wrapper(
            reactions.create,
        )
        self.list = to_raw_response_wrapper(
            reactions.list,
        )
        self.delete = to_raw_response_wrapper(
            reactions.delete,
        )


class AsyncReactionsResourceWithRawResponse:
    def __init__(self, reactions: AsyncReactionsResource) -> None:
        self._reactions = reactions

        self.create = async_to_raw_response_wrapper(
            reactions.create,
        )
        self.list = async_to_raw_response_wrapper(
            reactions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            reactions.delete,
        )


class ReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.create = to_streamed_response_wrapper(
            reactions.create,
        )
        self.list = to_streamed_response_wrapper(
            reactions.list,
        )
        self.delete = to_streamed_response_wrapper(
            reactions.delete,
        )


class AsyncReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: AsyncReactionsResource) -> None:
        self._reactions = reactions

        self.create = async_to_streamed_response_wrapper(
            reactions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            reactions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            reactions.delete,
        )
