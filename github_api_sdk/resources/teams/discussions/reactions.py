from __future__ import annotations

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
from ....types.orgs.teams.discussions.comments.reaction import Reaction
from ....types.teams.discussions import reaction_create_params, reaction_list_params
from ....types.teams.discussions.reaction_list_response import ReactionListResponse

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
        discussion_number: int,
        *,
        team_id: int,
        content: Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Reaction:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`Create reaction for a team discussion`](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-team-discussion)
        > endpoint.

        Create a reaction to a
        [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).

        A response with an HTTP `200` status means that you already added the reaction
        type to this team discussion.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          content: The
              [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions)
              to add to the team discussion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/teams/{team_id}/discussions/{discussion_number}/reactions",
            body=maybe_transform({"content": content}, reaction_create_params.ReactionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Reaction,
        )

    def list(
        self,
        discussion_number: int,
        *,
        team_id: int,
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
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`List reactions for a team discussion`](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-team-discussion)
        > endpoint.

        List the reactions to a
        [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          content: Returns a single
              [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions).
              Omit this parameter to list all reactions to a team discussion.

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
            f"/teams/{team_id}/discussions/{discussion_number}/reactions",
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
        discussion_number: int,
        *,
        team_id: int,
        content: Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Reaction:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`Create reaction for a team discussion`](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-team-discussion)
        > endpoint.

        Create a reaction to a
        [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).

        A response with an HTTP `200` status means that you already added the reaction
        type to this team discussion.

        OAuth app tokens and personal access tokens (classic) need the
        `write:discussion` scope to use this endpoint.

        Args:
          content: The
              [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions)
              to add to the team discussion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/teams/{team_id}/discussions/{discussion_number}/reactions",
            body=await async_maybe_transform({"content": content}, reaction_create_params.ReactionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Reaction,
        )

    async def list(
        self,
        discussion_number: int,
        *,
        team_id: int,
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
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [`List reactions for a team discussion`](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-team-discussion)
        > endpoint.

        List the reactions to a
        [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).

        OAuth app tokens and personal access tokens (classic) need the `read:discussion`
        scope to use this endpoint.

        Args:
          content: Returns a single
              [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions).
              Omit this parameter to list all reactions to a team discussion.

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
            f"/teams/{team_id}/discussions/{discussion_number}/reactions",
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


class ReactionsResourceWithRawResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.create = to_raw_response_wrapper(
            reactions.create,
        )
        self.list = to_raw_response_wrapper(
            reactions.list,
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


class ReactionsResourceWithStreamingResponse:
    def __init__(self, reactions: ReactionsResource) -> None:
        self._reactions = reactions

        self.create = to_streamed_response_wrapper(
            reactions.create,
        )
        self.list = to_streamed_response_wrapper(
            reactions.list,
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
