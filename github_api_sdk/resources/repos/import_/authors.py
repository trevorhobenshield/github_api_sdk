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
from ....types.repos.import_ import author_list_params, author_map_params
from ....types.repos.import_.author_list_response import AuthorListResponse
from ....types.repos.import_.porter_author import PorterAuthor

__all__ = ["AuthorsResource", "AsyncAuthorsResource"]


class AuthorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AuthorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AuthorsResourceWithStreamingResponse(self)

    def list(
        self,
        repo: str,
        *,
        owner: str,
        since: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorListResponse:
        """Each type of source control system represents authors in a different way.

        For
        example, a Git commit author has a display name and an email address, but a
        Subversion commit author just has a username. The GitHub Importer will make the
        author information valid, but the author might not be correct. For example, it
        will change the bare Subversion username `hubot` into something like
        `hubot <hubot@12341234-abab-fefe-8787-fedcba987654>`.

        This endpoint and the
        [Map a commit author](https://docs.github.com/rest/migrations/source-imports#map-a-commit-author)
        endpoint allow you to provide correct Git author information.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          since: A user ID. Only return users with an ID greater than this ID.

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
            f"/repos/{owner}/{repo}/import/authors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"since": since}, author_list_params.AuthorListParams),
            ),
            cast_to=AuthorListResponse,
        )

    def map(
        self,
        author_id: int,
        *,
        owner: str,
        repo: str,
        email: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PorterAuthor:
        """Update an author's identity for the import.

        Your application can continue
        updating authors any time before you push new commits to the repository.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          email: The new Git author email.

          name: The new Git author name.

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
            f"/repos/{owner}/{repo}/import/authors/{author_id}",
            body=maybe_transform(
                {
                    "email": email,
                    "name": name,
                },
                author_map_params.AuthorMapParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PorterAuthor,
        )


class AsyncAuthorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAuthorsResourceWithStreamingResponse(self)

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        since: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorListResponse:
        """Each type of source control system represents authors in a different way.

        For
        example, a Git commit author has a display name and an email address, but a
        Subversion commit author just has a username. The GitHub Importer will make the
        author information valid, but the author might not be correct. For example, it
        will change the bare Subversion username `hubot` into something like
        `hubot <hubot@12341234-abab-fefe-8787-fedcba987654>`.

        This endpoint and the
        [Map a commit author](https://docs.github.com/rest/migrations/source-imports#map-a-commit-author)
        endpoint allow you to provide correct Git author information.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          since: A user ID. Only return users with an ID greater than this ID.

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
            f"/repos/{owner}/{repo}/import/authors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"since": since}, author_list_params.AuthorListParams),
            ),
            cast_to=AuthorListResponse,
        )

    async def map(
        self,
        author_id: int,
        *,
        owner: str,
        repo: str,
        email: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PorterAuthor:
        """Update an author's identity for the import.

        Your application can continue
        updating authors any time before you push new commits to the repository.

        > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage
        > and available alternatives, this endpoint is closing down and will no longer
        > be available from 00:00 UTC on April 12, 2024. For more details and
        > alternatives, see the
        > [changelog](https://gh.io/source-imports-api-deprecation).

        Args:
          email: The new Git author email.

          name: The new Git author name.

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
            f"/repos/{owner}/{repo}/import/authors/{author_id}",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "name": name,
                },
                author_map_params.AuthorMapParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PorterAuthor,
        )


class AuthorsResourceWithRawResponse:
    def __init__(self, authors: AuthorsResource) -> None:
        self._authors = authors

        self.list = to_raw_response_wrapper(
            authors.list,
        )
        self.map = to_raw_response_wrapper(
            authors.map,
        )


class AsyncAuthorsResourceWithRawResponse:
    def __init__(self, authors: AsyncAuthorsResource) -> None:
        self._authors = authors

        self.list = async_to_raw_response_wrapper(
            authors.list,
        )
        self.map = async_to_raw_response_wrapper(
            authors.map,
        )


class AuthorsResourceWithStreamingResponse:
    def __init__(self, authors: AuthorsResource) -> None:
        self._authors = authors

        self.list = to_streamed_response_wrapper(
            authors.list,
        )
        self.map = to_streamed_response_wrapper(
            authors.map,
        )


class AsyncAuthorsResourceWithStreamingResponse:
    def __init__(self, authors: AsyncAuthorsResource) -> None:
        self._authors = authors

        self.list = async_to_streamed_response_wrapper(
            authors.list,
        )
        self.map = async_to_streamed_response_wrapper(
            authors.map,
        )
