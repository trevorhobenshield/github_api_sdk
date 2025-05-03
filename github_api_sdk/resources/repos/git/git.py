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
from ....types.repos.git_list_matching_refs_response import GitListMatchingRefsResponse
from ....types.repos.git_ref import GitRef
from .blobs import (
    AsyncBlobsResource,
    AsyncBlobsResourceWithRawResponse,
    AsyncBlobsResourceWithStreamingResponse,
    BlobsResource,
    BlobsResourceWithRawResponse,
    BlobsResourceWithStreamingResponse,
)
from .commits import (
    AsyncCommitsResource,
    AsyncCommitsResourceWithRawResponse,
    AsyncCommitsResourceWithStreamingResponse,
    CommitsResource,
    CommitsResourceWithRawResponse,
    CommitsResourceWithStreamingResponse,
)
from .refs import (
    AsyncRefsResource,
    AsyncRefsResourceWithRawResponse,
    AsyncRefsResourceWithStreamingResponse,
    RefsResource,
    RefsResourceWithRawResponse,
    RefsResourceWithStreamingResponse,
)
from .tags import (
    AsyncTagsResource,
    AsyncTagsResourceWithRawResponse,
    AsyncTagsResourceWithStreamingResponse,
    TagsResource,
    TagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
)
from .trees import (
    AsyncTreesResource,
    AsyncTreesResourceWithRawResponse,
    AsyncTreesResourceWithStreamingResponse,
    TreesResource,
    TreesResourceWithRawResponse,
    TreesResourceWithStreamingResponse,
)

__all__ = ["GitResource", "AsyncGitResource"]


class GitResource(SyncAPIResource):
    @cached_property
    def blobs(self) -> BlobsResource:
        return BlobsResource(self._client)

    @cached_property
    def commits(self) -> CommitsResource:
        return CommitsResource(self._client)

    @cached_property
    def refs(self) -> RefsResource:
        return RefsResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def trees(self) -> TreesResource:
        return TreesResource(self._client)

    @cached_property
    def with_raw_response(self) -> GitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return GitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return GitResourceWithStreamingResponse(self)

    def list_matching_refs(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitListMatchingRefsResponse:
        """
        Returns an array of references from your Git database that match the supplied
        name. The `:ref` in the URL must be formatted as `heads/<branch name>` for
        branches and `tags/<tag name>` for tags. If the `:ref` doesn't exist in the
        repository, but existing refs start with `:ref`, they will be returned as an
        array.

        When you use this endpoint without providing a `:ref`, it will return an array
        of all the references from your Git database, including notes and stashes if
        they exist on the server. Anything in the namespace is returned, not just
        `heads` and `tags`.

        > [!NOTE] You need to explicitly
        > [request a pull request](https://docs.github.com/rest/pulls/pulls#get-a-pull-request)
        > to trigger a test merge commit, which checks the mergeability of pull
        > requests. For more information, see
        > "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".

        If you request matching references for a branch named `feature` but the branch
        `feature` doesn't exist, the response can still include other matching head refs
        that start with the word `feature`, such as `featureA` and `featureB`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            f"/repos/{owner}/{repo}/git/matching-refs/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitListMatchingRefsResponse,
        )

    def retrieve_ref(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitRef:
        """Returns a single reference from your Git database.

        The `:ref` in the URL must be
        formatted as `heads/<branch name>` for branches and `tags/<tag name>` for tags.
        If the `:ref` doesn't match an existing ref, a `404` is returned.

        > [!NOTE] You need to explicitly
        > [request a pull request](https://docs.github.com/rest/pulls/pulls#get-a-pull-request)
        > to trigger a test merge commit, which checks the mergeability of pull
        > requests. For more information, see
        > "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            f"/repos/{owner}/{repo}/git/ref/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitRef,
        )


class AsyncGitResource(AsyncAPIResource):
    @cached_property
    def blobs(self) -> AsyncBlobsResource:
        return AsyncBlobsResource(self._client)

    @cached_property
    def commits(self) -> AsyncCommitsResource:
        return AsyncCommitsResource(self._client)

    @cached_property
    def refs(self) -> AsyncRefsResource:
        return AsyncRefsResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def trees(self) -> AsyncTreesResource:
        return AsyncTreesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncGitResourceWithStreamingResponse(self)

    async def list_matching_refs(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitListMatchingRefsResponse:
        """
        Returns an array of references from your Git database that match the supplied
        name. The `:ref` in the URL must be formatted as `heads/<branch name>` for
        branches and `tags/<tag name>` for tags. If the `:ref` doesn't exist in the
        repository, but existing refs start with `:ref`, they will be returned as an
        array.

        When you use this endpoint without providing a `:ref`, it will return an array
        of all the references from your Git database, including notes and stashes if
        they exist on the server. Anything in the namespace is returned, not just
        `heads` and `tags`.

        > [!NOTE] You need to explicitly
        > [request a pull request](https://docs.github.com/rest/pulls/pulls#get-a-pull-request)
        > to trigger a test merge commit, which checks the mergeability of pull
        > requests. For more information, see
        > "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".

        If you request matching references for a branch named `feature` but the branch
        `feature` doesn't exist, the response can still include other matching head refs
        that start with the word `feature`, such as `featureA` and `featureB`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/git/matching-refs/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitListMatchingRefsResponse,
        )

    async def retrieve_ref(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitRef:
        """Returns a single reference from your Git database.

        The `:ref` in the URL must be
        formatted as `heads/<branch name>` for branches and `tags/<tag name>` for tags.
        If the `:ref` doesn't match an existing ref, a `404` is returned.

        > [!NOTE] You need to explicitly
        > [request a pull request](https://docs.github.com/rest/pulls/pulls#get-a-pull-request)
        > to trigger a test merge commit, which checks the mergeability of pull
        > requests. For more information, see
        > "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/git/ref/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitRef,
        )


class GitResourceWithRawResponse:
    def __init__(self, git: GitResource) -> None:
        self._git = git

        self.list_matching_refs = to_raw_response_wrapper(
            git.list_matching_refs,
        )
        self.retrieve_ref = to_raw_response_wrapper(
            git.retrieve_ref,
        )

    @cached_property
    def blobs(self) -> BlobsResourceWithRawResponse:
        return BlobsResourceWithRawResponse(self._git.blobs)

    @cached_property
    def commits(self) -> CommitsResourceWithRawResponse:
        return CommitsResourceWithRawResponse(self._git.commits)

    @cached_property
    def refs(self) -> RefsResourceWithRawResponse:
        return RefsResourceWithRawResponse(self._git.refs)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._git.tags)

    @cached_property
    def trees(self) -> TreesResourceWithRawResponse:
        return TreesResourceWithRawResponse(self._git.trees)


class AsyncGitResourceWithRawResponse:
    def __init__(self, git: AsyncGitResource) -> None:
        self._git = git

        self.list_matching_refs = async_to_raw_response_wrapper(
            git.list_matching_refs,
        )
        self.retrieve_ref = async_to_raw_response_wrapper(
            git.retrieve_ref,
        )

    @cached_property
    def blobs(self) -> AsyncBlobsResourceWithRawResponse:
        return AsyncBlobsResourceWithRawResponse(self._git.blobs)

    @cached_property
    def commits(self) -> AsyncCommitsResourceWithRawResponse:
        return AsyncCommitsResourceWithRawResponse(self._git.commits)

    @cached_property
    def refs(self) -> AsyncRefsResourceWithRawResponse:
        return AsyncRefsResourceWithRawResponse(self._git.refs)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._git.tags)

    @cached_property
    def trees(self) -> AsyncTreesResourceWithRawResponse:
        return AsyncTreesResourceWithRawResponse(self._git.trees)


class GitResourceWithStreamingResponse:
    def __init__(self, git: GitResource) -> None:
        self._git = git

        self.list_matching_refs = to_streamed_response_wrapper(
            git.list_matching_refs,
        )
        self.retrieve_ref = to_streamed_response_wrapper(
            git.retrieve_ref,
        )

    @cached_property
    def blobs(self) -> BlobsResourceWithStreamingResponse:
        return BlobsResourceWithStreamingResponse(self._git.blobs)

    @cached_property
    def commits(self) -> CommitsResourceWithStreamingResponse:
        return CommitsResourceWithStreamingResponse(self._git.commits)

    @cached_property
    def refs(self) -> RefsResourceWithStreamingResponse:
        return RefsResourceWithStreamingResponse(self._git.refs)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._git.tags)

    @cached_property
    def trees(self) -> TreesResourceWithStreamingResponse:
        return TreesResourceWithStreamingResponse(self._git.trees)


class AsyncGitResourceWithStreamingResponse:
    def __init__(self, git: AsyncGitResource) -> None:
        self._git = git

        self.list_matching_refs = async_to_streamed_response_wrapper(
            git.list_matching_refs,
        )
        self.retrieve_ref = async_to_streamed_response_wrapper(
            git.retrieve_ref,
        )

    @cached_property
    def blobs(self) -> AsyncBlobsResourceWithStreamingResponse:
        return AsyncBlobsResourceWithStreamingResponse(self._git.blobs)

    @cached_property
    def commits(self) -> AsyncCommitsResourceWithStreamingResponse:
        return AsyncCommitsResourceWithStreamingResponse(self._git.commits)

    @cached_property
    def refs(self) -> AsyncRefsResourceWithStreamingResponse:
        return AsyncRefsResourceWithStreamingResponse(self._git.refs)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._git.tags)

    @cached_property
    def trees(self) -> AsyncTreesResourceWithStreamingResponse:
        return AsyncTreesResourceWithStreamingResponse(self._git.trees)
