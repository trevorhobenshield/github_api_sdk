from __future__ import annotations

import httpx
from typing_extensions import Literal

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.search import user_search_params
from ...types.search.user_search_response import UserSearchResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        q: str,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["followers", "repositories", "joined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSearchResponse:
        """Find users via various criteria.

        This method returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).

        When searching for users, you can get text match metadata for the issue
        **login**, public **email**, and **name** fields when you pass the `text-match`
        media type. For more details about highlighting search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).
        For more details about how to receive highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you're looking for a list of popular users, you might try this
        query:

        `q=tom+repos:%3E42+followers:%3E1000`

        This query searches for users with the name `tom`. The results are restricted to
        users with more than 42 repositories and over 1,000 followers.

        This endpoint does not accept authentication and will only include publicly
        visible users. As an alternative, you can use the GraphQL API. The GraphQL API
        requires authentication and will return private users, including Enterprise
        Managed Users (EMUs), that you are authorized to view. For more information, see
        "[GraphQL Queries](https://docs.github.com/graphql/reference/queries#search)."

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching users](https://docs.github.com/search-github/searching-on-github/searching-users)"
              for a detailed list of qualifiers.

          order: Determines whether the first search result returned is the highest number of
              matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
              unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: Sorts the results of your query by number of `followers` or `repositories`, or
              when the person `joined` GitHub. Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/search/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    user_search_params.UserSearchParams,
                ),
            ),
            cast_to=UserSearchResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        q: str,
        order: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["followers", "repositories", "joined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSearchResponse:
        """Find users via various criteria.

        This method returns up to 100 results
        [per page](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api).

        When searching for users, you can get text match metadata for the issue
        **login**, public **email**, and **name** fields when you pass the `text-match`
        media type. For more details about highlighting search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).
        For more details about how to receive highlighted search results, see
        [Text match metadata](https://docs.github.com/rest/search/search#text-match-metadata).

        For example, if you're looking for a list of popular users, you might try this
        query:

        `q=tom+repos:%3E42+followers:%3E1000`

        This query searches for users with the name `tom`. The results are restricted to
        users with more than 42 repositories and over 1,000 followers.

        This endpoint does not accept authentication and will only include publicly
        visible users. As an alternative, you can use the GraphQL API. The GraphQL API
        requires authentication and will return private users, including Enterprise
        Managed Users (EMUs), that you are authorized to view. For more information, see
        "[GraphQL Queries](https://docs.github.com/graphql/reference/queries#search)."

        Args:
          q: The query contains one or more search keywords and qualifiers. Qualifiers allow
              you to limit your search to specific areas of GitHub. The REST API supports the
              same qualifiers as the web interface for GitHub. To learn more about the format
              of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching users](https://docs.github.com/search-github/searching-on-github/searching-users)"
              for a detailed list of qualifiers.

          order: Determines whether the first search result returned is the highest number of
              matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored
              unless you provide `sort`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: Sorts the results of your query by number of `followers` or `repositories`, or
              when the person `joined` GitHub. Default:
              [best match](https://docs.github.com/rest/search/search#ranking-search-results)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/search/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                    },
                    user_search_params.UserSearchParams,
                ),
            ),
            cast_to=UserSearchResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.search = to_raw_response_wrapper(
            users.search,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.search = async_to_raw_response_wrapper(
            users.search,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.search = to_streamed_response_wrapper(
            users.search,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.search = async_to_streamed_response_wrapper(
            users.search,
        )
