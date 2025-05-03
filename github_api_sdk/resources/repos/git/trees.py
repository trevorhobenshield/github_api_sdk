from __future__ import annotations

from typing import Iterable

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
from ....types.repos.git import tree_create_params, tree_retrieve_params
from ....types.repos.git.git_tree import GitTree

__all__ = ["TreesResource", "AsyncTreesResource"]


class TreesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TreesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return TreesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TreesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return TreesResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        tree: Iterable[tree_create_params.Tree],
        base_tree: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitTree:
        """The tree creation API accepts nested entries.

        If you specify both a tree and a
        nested path modifying that tree, this endpoint will overwrite the contents of
        the tree with the new path contents, and create a new tree structure.

        If you use this endpoint to add, delete, or modify the file contents in a tree,
        you will need to commit the tree and then update a branch to point to the
        commit. For more information see
        "[Create a commit](https://docs.github.com/rest/git/commits#create-a-commit)"
        and
        "[Update a reference](https://docs.github.com/rest/git/refs#update-a-reference)."

        Returns an error if you try to delete a file that does not exist.

        Args:
          tree: Objects (of `path`, `mode`, `type`, and `sha`) specifying a tree structure.

          base_tree: The SHA1 of an existing Git tree object which will be used as the base for the
              new tree. If provided, a new Git tree object will be created from entries in the
              Git tree object pointed to by `base_tree` and entries defined in the `tree`
              parameter. Entries defined in the `tree` parameter will overwrite items from
              `base_tree` with the same `path`. If you're creating new changes on a branch,
              then normally you'd set `base_tree` to the SHA1 of the Git tree object of the
              current latest commit on the branch you're working on. If not provided, GitHub
              will create a new Git tree object from only the entries defined in the `tree`
              parameter. If you create a new commit pointing to such a tree, then all files
              which were a part of the parent commit's tree and were not defined in the `tree`
              parameter will be listed as deleted by the new commit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/git/trees",
            body=maybe_transform(
                {
                    "tree": tree,
                    "base_tree": base_tree,
                },
                tree_create_params.TreeCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitTree,
        )

    def retrieve(
        self,
        tree_sha: str,
        *,
        owner: str,
        repo: str,
        recursive: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitTree:
        """
        Returns a single tree using the SHA1 value or ref name for that tree.

        If `truncated` is `true` in the response then the number of items in the `tree`
        array exceeded our maximum limit. If you need to fetch more items, use the
        non-recursive method of fetching trees, and fetch one sub-tree at a time.

        > [!NOTE] The limit for the `tree` array is 100,000 entries with a maximum size
        > of 7 MB when using the `recursive` parameter.

        Args:
          recursive: Setting this parameter to any value returns the objects or subtrees referenced
              by the tree specified in `:tree_sha`. For example, setting `recursive` to any of
              the following will enable returning objects or subtrees: `0`, `1`, `"true"`, and
              `"false"`. Omit this parameter to prevent recursively returning objects or
              subtrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not tree_sha:
            raise ValueError(f"Expected a non-empty value for `tree_sha` but received {tree_sha!r}")
        return self._get(
            f"/repos/{owner}/{repo}/git/trees/{tree_sha}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"recursive": recursive}, tree_retrieve_params.TreeRetrieveParams),
            ),
            cast_to=GitTree,
        )


class AsyncTreesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTreesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTreesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTreesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncTreesResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        tree: Iterable[tree_create_params.Tree],
        base_tree: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitTree:
        """The tree creation API accepts nested entries.

        If you specify both a tree and a
        nested path modifying that tree, this endpoint will overwrite the contents of
        the tree with the new path contents, and create a new tree structure.

        If you use this endpoint to add, delete, or modify the file contents in a tree,
        you will need to commit the tree and then update a branch to point to the
        commit. For more information see
        "[Create a commit](https://docs.github.com/rest/git/commits#create-a-commit)"
        and
        "[Update a reference](https://docs.github.com/rest/git/refs#update-a-reference)."

        Returns an error if you try to delete a file that does not exist.

        Args:
          tree: Objects (of `path`, `mode`, `type`, and `sha`) specifying a tree structure.

          base_tree: The SHA1 of an existing Git tree object which will be used as the base for the
              new tree. If provided, a new Git tree object will be created from entries in the
              Git tree object pointed to by `base_tree` and entries defined in the `tree`
              parameter. Entries defined in the `tree` parameter will overwrite items from
              `base_tree` with the same `path`. If you're creating new changes on a branch,
              then normally you'd set `base_tree` to the SHA1 of the Git tree object of the
              current latest commit on the branch you're working on. If not provided, GitHub
              will create a new Git tree object from only the entries defined in the `tree`
              parameter. If you create a new commit pointing to such a tree, then all files
              which were a part of the parent commit's tree and were not defined in the `tree`
              parameter will be listed as deleted by the new commit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/git/trees",
            body=await async_maybe_transform(
                {
                    "tree": tree,
                    "base_tree": base_tree,
                },
                tree_create_params.TreeCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitTree,
        )

    async def retrieve(
        self,
        tree_sha: str,
        *,
        owner: str,
        repo: str,
        recursive: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitTree:
        """
        Returns a single tree using the SHA1 value or ref name for that tree.

        If `truncated` is `true` in the response then the number of items in the `tree`
        array exceeded our maximum limit. If you need to fetch more items, use the
        non-recursive method of fetching trees, and fetch one sub-tree at a time.

        > [!NOTE] The limit for the `tree` array is 100,000 entries with a maximum size
        > of 7 MB when using the `recursive` parameter.

        Args:
          recursive: Setting this parameter to any value returns the objects or subtrees referenced
              by the tree specified in `:tree_sha`. For example, setting `recursive` to any of
              the following will enable returning objects or subtrees: `0`, `1`, `"true"`, and
              `"false"`. Omit this parameter to prevent recursively returning objects or
              subtrees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not tree_sha:
            raise ValueError(f"Expected a non-empty value for `tree_sha` but received {tree_sha!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/git/trees/{tree_sha}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"recursive": recursive}, tree_retrieve_params.TreeRetrieveParams),
            ),
            cast_to=GitTree,
        )


class TreesResourceWithRawResponse:
    def __init__(self, trees: TreesResource) -> None:
        self._trees = trees

        self.create = to_raw_response_wrapper(
            trees.create,
        )
        self.retrieve = to_raw_response_wrapper(
            trees.retrieve,
        )


class AsyncTreesResourceWithRawResponse:
    def __init__(self, trees: AsyncTreesResource) -> None:
        self._trees = trees

        self.create = async_to_raw_response_wrapper(
            trees.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            trees.retrieve,
        )


class TreesResourceWithStreamingResponse:
    def __init__(self, trees: TreesResource) -> None:
        self._trees = trees

        self.create = to_streamed_response_wrapper(
            trees.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            trees.retrieve,
        )


class AsyncTreesResourceWithStreamingResponse:
    def __init__(self, trees: AsyncTreesResource) -> None:
        self._trees = trees

        self.create = async_to_streamed_response_wrapper(
            trees.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            trees.retrieve,
        )
