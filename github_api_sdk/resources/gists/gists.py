from __future__ import annotations

from datetime import datetime
from typing import Dict, Optional, Union

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
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types import (
    gist_create_params,
    gist_list_commits_params,
    gist_list_params,
    gist_list_public_params,
    gist_list_starred_params,
    gist_update_params,
)
from ...types.gist_list_commits_response import GistListCommitsResponse
from ...types.gist_list_public_response import GistListPublicResponse
from ...types.gist_list_response import GistListResponse
from ...types.gist_list_starred_response import GistListStarredResponse
from ...types.gist_simple import GistSimple
from .comments import (
    AsyncCommentsResource,
    AsyncCommentsResourceWithRawResponse,
    AsyncCommentsResourceWithStreamingResponse,
    CommentsResource,
    CommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
)
from .forks import (
    AsyncForksResource,
    AsyncForksResourceWithRawResponse,
    AsyncForksResourceWithStreamingResponse,
    ForksResource,
    ForksResourceWithRawResponse,
    ForksResourceWithStreamingResponse,
)
from .star import (
    AsyncStarResource,
    AsyncStarResourceWithRawResponse,
    AsyncStarResourceWithStreamingResponse,
    StarResource,
    StarResourceWithRawResponse,
    StarResourceWithStreamingResponse,
)

__all__ = ["GistsResource", "AsyncGistsResource"]


class GistsResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def forks(self) -> ForksResource:
        return ForksResource(self._client)

    @cached_property
    def star(self) -> StarResource:
        return StarResource(self._client)

    @cached_property
    def with_raw_response(self) -> GistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return GistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return GistsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        files: dict[str, gist_create_params.Files],
        description: str | NotGiven = NOT_GIVEN,
        public: bool | Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistSimple:
        """
        Allows you to add a new gist with one or more files.

        > [!NOTE] Don't name your files "gistfile" with a numerical suffix. This is the
        > format of the automatic naming scheme that Gist uses internally.

        Args:
          files: Names and content for the files that make up the gist

          description: Description of the gist

          public: Flag indicating whether the gist is public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gists",
            body=maybe_transform(
                {
                    "files": files,
                    "description": description,
                    "public": public,
                },
                gist_create_params.GistCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistSimple,
        )

    def retrieve(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistSimple:
        """Gets a specified gist.

        This endpoint supports the following custom media types.

        For more information,
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
            f"/gists/{gist_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistSimple,
        )

    def update(
        self,
        gist_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        files: dict[str, gist_update_params.Files | None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistSimple:
        """
        Allows you to update a gist's description and to update, delete, or rename gist
        files. Files from the previous version of the gist that aren't explicitly
        changed during an edit are unchanged.

        At least one of `description` or `files` is required.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

        Args:
          description: The description of the gist.

          files: The gist files to be updated, renamed, or deleted. Each `key` must match the
              current filename (including extension) of the targeted gist file. For example:
              `hello.py`.

              To delete a file, set the whole file to null. For example: `hello.py : null`.
              The file will also be deleted if the specified object does not contain at least
              one of `content` or `filename`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return self._patch(
            f"/gists/{gist_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "files": files,
                },
                gist_update_params.GistUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistSimple,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistListResponse:
        """
        Lists the authenticated user's gists or if called anonymously, this endpoint
        returns all public gists:

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
        return self._get(
            "/gists",
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
                    gist_list_params.GistListParams,
                ),
            ),
            cast_to=GistListResponse,
        )

    def delete(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a gist

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
            f"/gists/{gist_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_commits(
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
    ) -> GistListCommitsResponse:
        """List gist commits

        Args:
          page: The page number of the results to fetch.

        For more information, see
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
            f"/gists/{gist_id}/commits",
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
                    gist_list_commits_params.GistListCommitsParams,
                ),
            ),
            cast_to=GistListCommitsResponse,
        )

    def list_public(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistListPublicResponse:
        """
        List public gists sorted by most recently updated to least recently updated.

        Note: With
        [pagination](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api),
        you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30
        gists per page or 30 pages with 100 gists per page.

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
        return self._get(
            "/gists/public",
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
                    gist_list_public_params.GistListPublicParams,
                ),
            ),
            cast_to=GistListPublicResponse,
        )

    def list_starred(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistListStarredResponse:
        """
        List the authenticated user's starred gists:

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
        return self._get(
            "/gists/starred",
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
                    gist_list_starred_params.GistListStarredParams,
                ),
            ),
            cast_to=GistListStarredResponse,
        )

    def retrieve_revision(
        self,
        sha: str,
        *,
        gist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistSimple:
        """
        Gets a specified gist revision.

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
        if not sha:
            raise ValueError(f"Expected a non-empty value for `sha` but received {sha!r}")
        return self._get(
            f"/gists/{gist_id}/{sha}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistSimple,
        )


class AsyncGistsResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def forks(self) -> AsyncForksResource:
        return AsyncForksResource(self._client)

    @cached_property
    def star(self) -> AsyncStarResource:
        return AsyncStarResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGistsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGistsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGistsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncGistsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        files: dict[str, gist_create_params.Files],
        description: str | NotGiven = NOT_GIVEN,
        public: bool | Literal["true", "false"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistSimple:
        """
        Allows you to add a new gist with one or more files.

        > [!NOTE] Don't name your files "gistfile" with a numerical suffix. This is the
        > format of the automatic naming scheme that Gist uses internally.

        Args:
          files: Names and content for the files that make up the gist

          description: Description of the gist

          public: Flag indicating whether the gist is public

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gists",
            body=await async_maybe_transform(
                {
                    "files": files,
                    "description": description,
                    "public": public,
                },
                gist_create_params.GistCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistSimple,
        )

    async def retrieve(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistSimple:
        """Gets a specified gist.

        This endpoint supports the following custom media types.

        For more information,
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
            f"/gists/{gist_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistSimple,
        )

    async def update(
        self,
        gist_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        files: dict[str, gist_update_params.Files | None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistSimple:
        """
        Allows you to update a gist's description and to update, delete, or rename gist
        files. Files from the previous version of the gist that aren't explicitly
        changed during an edit are unchanged.

        At least one of `description` or `files` is required.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the
          default if you do not pass any specific media type.
        - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents.
          This can be useful if your gist contains any invalid UTF-8 sequences.

        Args:
          description: The description of the gist.

          files: The gist files to be updated, renamed, or deleted. Each `key` must match the
              current filename (including extension) of the targeted gist file. For example:
              `hello.py`.

              To delete a file, set the whole file to null. For example: `hello.py : null`.
              The file will also be deleted if the specified object does not contain at least
              one of `content` or `filename`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not gist_id:
            raise ValueError(f"Expected a non-empty value for `gist_id` but received {gist_id!r}")
        return await self._patch(
            f"/gists/{gist_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "files": files,
                },
                gist_update_params.GistUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistSimple,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistListResponse:
        """
        Lists the authenticated user's gists or if called anonymously, this endpoint
        returns all public gists:

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
        return await self._get(
            "/gists",
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
                    gist_list_params.GistListParams,
                ),
            ),
            cast_to=GistListResponse,
        )

    async def delete(
        self,
        gist_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a gist

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
            f"/gists/{gist_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_commits(
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
    ) -> GistListCommitsResponse:
        """List gist commits

        Args:
          page: The page number of the results to fetch.

        For more information, see
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
            f"/gists/{gist_id}/commits",
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
                    gist_list_commits_params.GistListCommitsParams,
                ),
            ),
            cast_to=GistListCommitsResponse,
        )

    async def list_public(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistListPublicResponse:
        """
        List public gists sorted by most recently updated to least recently updated.

        Note: With
        [pagination](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api),
        you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30
        gists per page or 30 pages with 100 gists per page.

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
        return await self._get(
            "/gists/public",
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
                    gist_list_public_params.GistListPublicParams,
                ),
            ),
            cast_to=GistListPublicResponse,
        )

    async def list_starred(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistListStarredResponse:
        """
        List the authenticated user's starred gists:

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
        return await self._get(
            "/gists/starred",
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
                    gist_list_starred_params.GistListStarredParams,
                ),
            ),
            cast_to=GistListStarredResponse,
        )

    async def retrieve_revision(
        self,
        sha: str,
        *,
        gist_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GistSimple:
        """
        Gets a specified gist revision.

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
        if not sha:
            raise ValueError(f"Expected a non-empty value for `sha` but received {sha!r}")
        return await self._get(
            f"/gists/{gist_id}/{sha}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GistSimple,
        )


class GistsResourceWithRawResponse:
    def __init__(self, gists: GistsResource) -> None:
        self._gists = gists

        self.create = to_raw_response_wrapper(
            gists.create,
        )
        self.retrieve = to_raw_response_wrapper(
            gists.retrieve,
        )
        self.update = to_raw_response_wrapper(
            gists.update,
        )
        self.list = to_raw_response_wrapper(
            gists.list,
        )
        self.delete = to_raw_response_wrapper(
            gists.delete,
        )
        self.list_commits = to_raw_response_wrapper(
            gists.list_commits,
        )
        self.list_public = to_raw_response_wrapper(
            gists.list_public,
        )
        self.list_starred = to_raw_response_wrapper(
            gists.list_starred,
        )
        self.retrieve_revision = to_raw_response_wrapper(
            gists.retrieve_revision,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._gists.comments)

    @cached_property
    def forks(self) -> ForksResourceWithRawResponse:
        return ForksResourceWithRawResponse(self._gists.forks)

    @cached_property
    def star(self) -> StarResourceWithRawResponse:
        return StarResourceWithRawResponse(self._gists.star)


class AsyncGistsResourceWithRawResponse:
    def __init__(self, gists: AsyncGistsResource) -> None:
        self._gists = gists

        self.create = async_to_raw_response_wrapper(
            gists.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            gists.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            gists.update,
        )
        self.list = async_to_raw_response_wrapper(
            gists.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gists.delete,
        )
        self.list_commits = async_to_raw_response_wrapper(
            gists.list_commits,
        )
        self.list_public = async_to_raw_response_wrapper(
            gists.list_public,
        )
        self.list_starred = async_to_raw_response_wrapper(
            gists.list_starred,
        )
        self.retrieve_revision = async_to_raw_response_wrapper(
            gists.retrieve_revision,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._gists.comments)

    @cached_property
    def forks(self) -> AsyncForksResourceWithRawResponse:
        return AsyncForksResourceWithRawResponse(self._gists.forks)

    @cached_property
    def star(self) -> AsyncStarResourceWithRawResponse:
        return AsyncStarResourceWithRawResponse(self._gists.star)


class GistsResourceWithStreamingResponse:
    def __init__(self, gists: GistsResource) -> None:
        self._gists = gists

        self.create = to_streamed_response_wrapper(
            gists.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            gists.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            gists.update,
        )
        self.list = to_streamed_response_wrapper(
            gists.list,
        )
        self.delete = to_streamed_response_wrapper(
            gists.delete,
        )
        self.list_commits = to_streamed_response_wrapper(
            gists.list_commits,
        )
        self.list_public = to_streamed_response_wrapper(
            gists.list_public,
        )
        self.list_starred = to_streamed_response_wrapper(
            gists.list_starred,
        )
        self.retrieve_revision = to_streamed_response_wrapper(
            gists.retrieve_revision,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._gists.comments)

    @cached_property
    def forks(self) -> ForksResourceWithStreamingResponse:
        return ForksResourceWithStreamingResponse(self._gists.forks)

    @cached_property
    def star(self) -> StarResourceWithStreamingResponse:
        return StarResourceWithStreamingResponse(self._gists.star)


class AsyncGistsResourceWithStreamingResponse:
    def __init__(self, gists: AsyncGistsResource) -> None:
        self._gists = gists

        self.create = async_to_streamed_response_wrapper(
            gists.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            gists.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            gists.update,
        )
        self.list = async_to_streamed_response_wrapper(
            gists.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gists.delete,
        )
        self.list_commits = async_to_streamed_response_wrapper(
            gists.list_commits,
        )
        self.list_public = async_to_streamed_response_wrapper(
            gists.list_public,
        )
        self.list_starred = async_to_streamed_response_wrapper(
            gists.list_starred,
        )
        self.retrieve_revision = async_to_streamed_response_wrapper(
            gists.retrieve_revision,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._gists.comments)

    @cached_property
    def forks(self) -> AsyncForksResourceWithStreamingResponse:
        return AsyncForksResourceWithStreamingResponse(self._gists.forks)

    @cached_property
    def star(self) -> AsyncStarResourceWithStreamingResponse:
        return AsyncStarResourceWithStreamingResponse(self._gists.star)
