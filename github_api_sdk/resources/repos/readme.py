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
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.repos import readme_retrieve_for_directory_params, readme_retrieve_params
from ...types.repos.content_file import ContentFile

__all__ = ["ReadmeResource", "AsyncReadmeResource"]


class ReadmeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReadmeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReadmeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReadmeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ReadmeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        repo: str,
        *,
        owner: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentFile:
        """
        Gets the preferred README for a repository.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw file contents. This is
          the default if you do not specify a media type.
        - **`application/vnd.github.html+json`**: Returns the README in HTML. Markup
          languages are rendered to HTML using GitHub's open-source
          [Markup library](https://github.com/github/markup).

        Args:
          ref: The name of the commit/branch/tag. Default: the repository’s default branch.

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
            f"/repos/{owner}/{repo}/readme",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ref": ref}, readme_retrieve_params.ReadmeRetrieveParams),
            ),
            cast_to=ContentFile,
        )

    def retrieve_for_directory(
        self,
        dir: str,
        *,
        owner: str,
        repo: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentFile:
        """
        Gets the README from a repository directory.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw file contents. This is
          the default if you do not specify a media type.
        - **`application/vnd.github.html+json`**: Returns the README in HTML. Markup
          languages are rendered to HTML using GitHub's open-source
          [Markup library](https://github.com/github/markup).

        Args:
          ref: The name of the commit/branch/tag. Default: the repository’s default branch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not dir:
            raise ValueError(f"Expected a non-empty value for `dir` but received {dir!r}")
        return self._get(
            f"/repos/{owner}/{repo}/readme/{dir}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ref": ref}, readme_retrieve_for_directory_params.ReadmeRetrieveForDirectoryParams),
            ),
            cast_to=ContentFile,
        )


class AsyncReadmeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReadmeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReadmeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReadmeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncReadmeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        repo: str,
        *,
        owner: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentFile:
        """
        Gets the preferred README for a repository.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw file contents. This is
          the default if you do not specify a media type.
        - **`application/vnd.github.html+json`**: Returns the README in HTML. Markup
          languages are rendered to HTML using GitHub's open-source
          [Markup library](https://github.com/github/markup).

        Args:
          ref: The name of the commit/branch/tag. Default: the repository’s default branch.

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
            f"/repos/{owner}/{repo}/readme",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ref": ref}, readme_retrieve_params.ReadmeRetrieveParams),
            ),
            cast_to=ContentFile,
        )

    async def retrieve_for_directory(
        self,
        dir: str,
        *,
        owner: str,
        repo: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContentFile:
        """
        Gets the README from a repository directory.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw file contents. This is
          the default if you do not specify a media type.
        - **`application/vnd.github.html+json`**: Returns the README in HTML. Markup
          languages are rendered to HTML using GitHub's open-source
          [Markup library](https://github.com/github/markup).

        Args:
          ref: The name of the commit/branch/tag. Default: the repository’s default branch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not dir:
            raise ValueError(f"Expected a non-empty value for `dir` but received {dir!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/readme/{dir}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ref": ref}, readme_retrieve_for_directory_params.ReadmeRetrieveForDirectoryParams),
            ),
            cast_to=ContentFile,
        )


class ReadmeResourceWithRawResponse:
    def __init__(self, readme: ReadmeResource) -> None:
        self._readme = readme

        self.retrieve = to_raw_response_wrapper(
            readme.retrieve,
        )
        self.retrieve_for_directory = to_raw_response_wrapper(
            readme.retrieve_for_directory,
        )


class AsyncReadmeResourceWithRawResponse:
    def __init__(self, readme: AsyncReadmeResource) -> None:
        self._readme = readme

        self.retrieve = async_to_raw_response_wrapper(
            readme.retrieve,
        )
        self.retrieve_for_directory = async_to_raw_response_wrapper(
            readme.retrieve_for_directory,
        )


class ReadmeResourceWithStreamingResponse:
    def __init__(self, readme: ReadmeResource) -> None:
        self._readme = readme

        self.retrieve = to_streamed_response_wrapper(
            readme.retrieve,
        )
        self.retrieve_for_directory = to_streamed_response_wrapper(
            readme.retrieve_for_directory,
        )


class AsyncReadmeResourceWithStreamingResponse:
    def __init__(self, readme: AsyncReadmeResource) -> None:
        self._readme = readme

        self.retrieve = async_to_streamed_response_wrapper(
            readme.retrieve,
        )
        self.retrieve_for_directory = async_to_streamed_response_wrapper(
            readme.retrieve_for_directory,
        )
