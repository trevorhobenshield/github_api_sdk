from __future__ import annotations

from typing import Any, cast

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
from ...types.repos import content_create_or_update_params, content_delete_params, content_retrieve_params
from ...types.repos.content_retrieve_response import ContentRetrieveResponse
from ...types.repos.file_commit import FileCommit

__all__ = ["ContentsResource", "AsyncContentsResource"]


class ContentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ContentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ContentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        path: str,
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
    ) -> ContentRetrieveResponse:
        """Gets the contents of a file or directory in a repository.

        Specify the file path
        or directory with the `path` parameter. If you omit the `path` parameter, you
        will receive the contents of the repository's root directory.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw file contents for files
          and symlinks.
        - **`application/vnd.github.html+json`**: Returns the file contents in HTML.
          Markup languages are rendered to HTML using GitHub's open-source
          [Markup library](https://github.com/github/markup).
        - **`application/vnd.github.object+json`**: Returns the contents in a consistent
          object format regardless of the content type. For example, instead of an array
          of objects for a directory, the response will be an object with an `entries`
          attribute containing the array of objects.

        If the content is a directory, the response will be an array of objects, one
        object for each item in the directory. When listing the contents of a directory,
        submodules have their "type" specified as "file". Logically, the value _should_
        be "submodule". This behavior exists
        [for backwards compatibility purposes](https://git.io/v1YCW). In the next major
        version of the API, the type will be returned as "submodule".

        If the content is a symlink and the symlink's target is a normal file in the
        repository, then the API responds with the content of the file. Otherwise, the
        API responds with an object describing the symlink itself.

        If the content is a submodule, the `submodule_git_url` field identifies the
        location of the submodule repository, and the `sha` identifies a specific commit
        within the submodule repository. Git uses the given URL when cloning the
        submodule repository, and checks out the submodule at that specific commit. If
        the submodule repository is not hosted on github.com, the Git URLs (`git_url`
        and `_links["git"]`) and the github.com URLs (`html_url` and `_links["html"]`)
        will have null values.

        **Notes**:

        - To get a repository's contents recursively, you can
          [recursively get the tree](https://docs.github.com/rest/git/trees#get-a-tree).
        - This API has an upper limit of 1,000 files for a directory. If you need to
          retrieve more files, use the
          [Git Trees API](https://docs.github.com/rest/git/trees#get-a-tree).
        - Download URLs expire and are meant to be used just once. To ensure the
          download URL does not expire, please use the contents API to obtain a fresh
          download URL for each download.
        - If the requested file's size is:
          - 1 MB or smaller: All features of this endpoint are supported.
          - Between 1-100 MB: Only the `raw` or `object` custom media types are
            supported. Both will work as normal, except that when using the `object`
            media type, the `content` field will be an empty string and the `encoding`
            field will be `"none"`. To get the contents of these larger files, use the
            `raw` media type.
          - Greater than 100 MB: This endpoint is not supported.

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
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return cast(
            ContentRetrieveResponse,
            self._get(
                f"/repos/{owner}/{repo}/contents/{path}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"ref": ref}, content_retrieve_params.ContentRetrieveParams),
                ),
                cast_to=cast(Any, ContentRetrieveResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        path: str,
        *,
        owner: str,
        repo: str,
        message: str,
        sha: str,
        author: content_delete_params.Author | NotGiven = NOT_GIVEN,
        branch: str | NotGiven = NOT_GIVEN,
        committer: content_delete_params.Committer | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileCommit:
        """
        Deletes a file in a repository.

        You can provide an additional `committer` parameter, which is an object
        containing information about the committer. Or, you can provide an `author`
        parameter, which is an object containing information about the author.

        The `author` section is optional and is filled in with the `committer`
        information if omitted. If the `committer` information is omitted, the
        authenticated user's information is used.

        You must provide values for both `name` and `email`, whether you choose to use
        `author` or `committer`. Otherwise, you'll receive a `422` status code.

        > [!NOTE] If you use this endpoint and the
        > "[Create or update file contents](https://docs.github.com/rest/repos/contents/#create-or-update-file-contents)"
        > endpoint in parallel, the concurrent requests will conflict and you will
        > receive errors. You must use these endpoints serially instead.

        Args:
          message: The commit message.

          sha: The blob SHA of the file being deleted.

          author: object containing information about the author.

          branch: The branch name. Default: the repository’s default branch

          committer: object containing information about the committer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return self._delete(
            f"/repos/{owner}/{repo}/contents/{path}",
            body=maybe_transform(
                {
                    "message": message,
                    "sha": sha,
                    "author": author,
                    "branch": branch,
                    "committer": committer,
                },
                content_delete_params.ContentDeleteParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FileCommit,
        )

    def create_or_update(
        self,
        path: str,
        *,
        owner: str,
        repo: str,
        content: str,
        message: str,
        author: content_create_or_update_params.Author | NotGiven = NOT_GIVEN,
        branch: str | NotGiven = NOT_GIVEN,
        committer: content_create_or_update_params.Committer | NotGiven = NOT_GIVEN,
        sha: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileCommit:
        """
        Creates a new file or replaces an existing file in a repository.

        > [!NOTE] If you use this endpoint and the
        > "[Delete a file](https://docs.github.com/rest/repos/contents/#delete-a-file)"
        > endpoint in parallel, the concurrent requests will conflict and you will
        > receive errors. You must use these endpoints serially instead.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint. The `workflow` scope is also required in order to modify
        files in the `.github/workflows` directory.

        Args:
          content: The new file content, using Base64 encoding.

          message: The commit message.

          author: The author of the file. Default: The `committer` or the authenticated user if
              you omit `committer`.

          branch: The branch name. Default: the repository’s default branch.

          committer: The person that committed the file. Default: the authenticated user.

          sha: **Required if you are updating a file**. The blob SHA of the file being
              replaced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return self._put(
            f"/repos/{owner}/{repo}/contents/{path}",
            body=maybe_transform(
                {
                    "content": content,
                    "message": message,
                    "author": author,
                    "branch": branch,
                    "committer": committer,
                    "sha": sha,
                },
                content_create_or_update_params.ContentCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FileCommit,
        )


class AsyncContentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncContentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        path: str,
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
    ) -> ContentRetrieveResponse:
        """Gets the contents of a file or directory in a repository.

        Specify the file path
        or directory with the `path` parameter. If you omit the `path` parameter, you
        will receive the contents of the repository's root directory.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw file contents for files
          and symlinks.
        - **`application/vnd.github.html+json`**: Returns the file contents in HTML.
          Markup languages are rendered to HTML using GitHub's open-source
          [Markup library](https://github.com/github/markup).
        - **`application/vnd.github.object+json`**: Returns the contents in a consistent
          object format regardless of the content type. For example, instead of an array
          of objects for a directory, the response will be an object with an `entries`
          attribute containing the array of objects.

        If the content is a directory, the response will be an array of objects, one
        object for each item in the directory. When listing the contents of a directory,
        submodules have their "type" specified as "file". Logically, the value _should_
        be "submodule". This behavior exists
        [for backwards compatibility purposes](https://git.io/v1YCW). In the next major
        version of the API, the type will be returned as "submodule".

        If the content is a symlink and the symlink's target is a normal file in the
        repository, then the API responds with the content of the file. Otherwise, the
        API responds with an object describing the symlink itself.

        If the content is a submodule, the `submodule_git_url` field identifies the
        location of the submodule repository, and the `sha` identifies a specific commit
        within the submodule repository. Git uses the given URL when cloning the
        submodule repository, and checks out the submodule at that specific commit. If
        the submodule repository is not hosted on github.com, the Git URLs (`git_url`
        and `_links["git"]`) and the github.com URLs (`html_url` and `_links["html"]`)
        will have null values.

        **Notes**:

        - To get a repository's contents recursively, you can
          [recursively get the tree](https://docs.github.com/rest/git/trees#get-a-tree).
        - This API has an upper limit of 1,000 files for a directory. If you need to
          retrieve more files, use the
          [Git Trees API](https://docs.github.com/rest/git/trees#get-a-tree).
        - Download URLs expire and are meant to be used just once. To ensure the
          download URL does not expire, please use the contents API to obtain a fresh
          download URL for each download.
        - If the requested file's size is:
          - 1 MB or smaller: All features of this endpoint are supported.
          - Between 1-100 MB: Only the `raw` or `object` custom media types are
            supported. Both will work as normal, except that when using the `object`
            media type, the `content` field will be an empty string and the `encoding`
            field will be `"none"`. To get the contents of these larger files, use the
            `raw` media type.
          - Greater than 100 MB: This endpoint is not supported.

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
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return cast(
            ContentRetrieveResponse,
            await self._get(
                f"/repos/{owner}/{repo}/contents/{path}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"ref": ref}, content_retrieve_params.ContentRetrieveParams),
                ),
                cast_to=cast(Any, ContentRetrieveResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        path: str,
        *,
        owner: str,
        repo: str,
        message: str,
        sha: str,
        author: content_delete_params.Author | NotGiven = NOT_GIVEN,
        branch: str | NotGiven = NOT_GIVEN,
        committer: content_delete_params.Committer | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileCommit:
        """
        Deletes a file in a repository.

        You can provide an additional `committer` parameter, which is an object
        containing information about the committer. Or, you can provide an `author`
        parameter, which is an object containing information about the author.

        The `author` section is optional and is filled in with the `committer`
        information if omitted. If the `committer` information is omitted, the
        authenticated user's information is used.

        You must provide values for both `name` and `email`, whether you choose to use
        `author` or `committer`. Otherwise, you'll receive a `422` status code.

        > [!NOTE] If you use this endpoint and the
        > "[Create or update file contents](https://docs.github.com/rest/repos/contents/#create-or-update-file-contents)"
        > endpoint in parallel, the concurrent requests will conflict and you will
        > receive errors. You must use these endpoints serially instead.

        Args:
          message: The commit message.

          sha: The blob SHA of the file being deleted.

          author: object containing information about the author.

          branch: The branch name. Default: the repository’s default branch

          committer: object containing information about the committer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return await self._delete(
            f"/repos/{owner}/{repo}/contents/{path}",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "sha": sha,
                    "author": author,
                    "branch": branch,
                    "committer": committer,
                },
                content_delete_params.ContentDeleteParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FileCommit,
        )

    async def create_or_update(
        self,
        path: str,
        *,
        owner: str,
        repo: str,
        content: str,
        message: str,
        author: content_create_or_update_params.Author | NotGiven = NOT_GIVEN,
        branch: str | NotGiven = NOT_GIVEN,
        committer: content_create_or_update_params.Committer | NotGiven = NOT_GIVEN,
        sha: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileCommit:
        """
        Creates a new file or replaces an existing file in a repository.

        > [!NOTE] If you use this endpoint and the
        > "[Delete a file](https://docs.github.com/rest/repos/contents/#delete-a-file)"
        > endpoint in parallel, the concurrent requests will conflict and you will
        > receive errors. You must use these endpoints serially instead.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint. The `workflow` scope is also required in order to modify
        files in the `.github/workflows` directory.

        Args:
          content: The new file content, using Base64 encoding.

          message: The commit message.

          author: The author of the file. Default: The `committer` or the authenticated user if
              you omit `committer`.

          branch: The branch name. Default: the repository’s default branch.

          committer: The person that committed the file. Default: the authenticated user.

          sha: **Required if you are updating a file**. The blob SHA of the file being
              replaced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/contents/{path}",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "message": message,
                    "author": author,
                    "branch": branch,
                    "committer": committer,
                    "sha": sha,
                },
                content_create_or_update_params.ContentCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FileCommit,
        )


class ContentsResourceWithRawResponse:
    def __init__(self, contents: ContentsResource) -> None:
        self._contents = contents

        self.retrieve = to_raw_response_wrapper(
            contents.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            contents.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            contents.create_or_update,
        )


class AsyncContentsResourceWithRawResponse:
    def __init__(self, contents: AsyncContentsResource) -> None:
        self._contents = contents

        self.retrieve = async_to_raw_response_wrapper(
            contents.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            contents.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            contents.create_or_update,
        )


class ContentsResourceWithStreamingResponse:
    def __init__(self, contents: ContentsResource) -> None:
        self._contents = contents

        self.retrieve = to_streamed_response_wrapper(
            contents.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            contents.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            contents.create_or_update,
        )


class AsyncContentsResourceWithStreamingResponse:
    def __init__(self, contents: AsyncContentsResource) -> None:
        self._contents = contents

        self.retrieve = async_to_streamed_response_wrapper(
            contents.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            contents.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            contents.create_or_update,
        )
