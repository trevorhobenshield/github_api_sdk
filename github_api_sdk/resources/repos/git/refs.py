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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.git import ref_create_params, ref_update_params
from ....types.repos.git_ref import GitRef

__all__ = ["RefsResource", "AsyncRefsResource"]


class RefsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RefsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RefsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        ref: str,
        sha: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitRef:
        """Creates a reference for your repository.

        You are unable to create new references
        for empty repositories, even if the commit SHA-1 hash used exists. Empty
        repositories are repositories without branches.

        Args:
          ref: The name of the fully qualified reference (ie: `refs/heads/master`). If it
              doesn't start with 'refs' and have at least two slashes, it will be rejected.

          sha: The SHA1 value for this reference.

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
            f"/repos/{owner}/{repo}/git/refs",
            body=maybe_transform(
                {
                    "ref": ref,
                    "sha": sha,
                },
                ref_create_params.RefCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitRef,
        )

    def update(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        sha: str,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitRef:
        """Updates the provided reference to point to a new SHA.

        For more information, see
        "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
        in the Git documentation.

        Args:
          sha: The SHA1 value to set this reference to

          force: Indicates whether to force the update or to make sure the update is a
              fast-forward update. Leaving this out or setting it to `false` will make sure
              you're not overwriting work.

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
        return self._patch(
            f"/repos/{owner}/{repo}/git/refs/{ref}",
            body=maybe_transform(
                {
                    "sha": sha,
                    "force": force,
                },
                ref_update_params.RefUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitRef,
        )

    def delete(
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
    ) -> None:
        """
        Deletes the provided reference.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/git/refs/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncRefsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRefsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRefsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        ref: str,
        sha: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitRef:
        """Creates a reference for your repository.

        You are unable to create new references
        for empty repositories, even if the commit SHA-1 hash used exists. Empty
        repositories are repositories without branches.

        Args:
          ref: The name of the fully qualified reference (ie: `refs/heads/master`). If it
              doesn't start with 'refs' and have at least two slashes, it will be rejected.

          sha: The SHA1 value for this reference.

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
            f"/repos/{owner}/{repo}/git/refs",
            body=await async_maybe_transform(
                {
                    "ref": ref,
                    "sha": sha,
                },
                ref_create_params.RefCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitRef,
        )

    async def update(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        sha: str,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitRef:
        """Updates the provided reference to point to a new SHA.

        For more information, see
        "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
        in the Git documentation.

        Args:
          sha: The SHA1 value to set this reference to

          force: Indicates whether to force the update or to make sure the update is a
              fast-forward update. Leaving this out or setting it to `false` will make sure
              you're not overwriting work.

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
        return await self._patch(
            f"/repos/{owner}/{repo}/git/refs/{ref}",
            body=await async_maybe_transform(
                {
                    "sha": sha,
                    "force": force,
                },
                ref_update_params.RefUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitRef,
        )

    async def delete(
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
    ) -> None:
        """
        Deletes the provided reference.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/git/refs/{ref}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class RefsResourceWithRawResponse:
    def __init__(self, refs: RefsResource) -> None:
        self._refs = refs

        self.create = to_raw_response_wrapper(
            refs.create,
        )
        self.update = to_raw_response_wrapper(
            refs.update,
        )
        self.delete = to_raw_response_wrapper(
            refs.delete,
        )


class AsyncRefsResourceWithRawResponse:
    def __init__(self, refs: AsyncRefsResource) -> None:
        self._refs = refs

        self.create = async_to_raw_response_wrapper(
            refs.create,
        )
        self.update = async_to_raw_response_wrapper(
            refs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            refs.delete,
        )


class RefsResourceWithStreamingResponse:
    def __init__(self, refs: RefsResource) -> None:
        self._refs = refs

        self.create = to_streamed_response_wrapper(
            refs.create,
        )
        self.update = to_streamed_response_wrapper(
            refs.update,
        )
        self.delete = to_streamed_response_wrapper(
            refs.delete,
        )


class AsyncRefsResourceWithStreamingResponse:
    def __init__(self, refs: AsyncRefsResource) -> None:
        self._refs = refs

        self.create = async_to_streamed_response_wrapper(
            refs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            refs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            refs.delete,
        )
