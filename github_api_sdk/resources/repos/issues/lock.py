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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.issues import lock_lock_params

__all__ = ["LockResource", "AsyncLockResource"]


class LockResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return LockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return LockResourceWithStreamingResponse(self)

    def lock(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        lock_reason: Literal["off-topic", "too heated", "resolved", "spam"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Users with push access can lock an issue or pull request's conversation.

        Note that, if you choose not to pass any parameters, you'll need to set
        `Content-Length` to zero when calling out to this endpoint. For more
        information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        Args:
          lock_reason: The reason for locking the issue or pull request conversation. Lock will fail if
              you don't use one of these reasons:

              - `off-topic`
              - `too heated`
              - `resolved`
              - `spam`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/repos/{owner}/{repo}/issues/{issue_number}/lock",
            body=maybe_transform({"lock_reason": lock_reason}, lock_lock_params.LockLockParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def unlock(
        self,
        issue_number: int,
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
        Users with push access can unlock an issue's conversation.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/issues/{issue_number}/lock",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncLockResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncLockResourceWithStreamingResponse(self)

    async def lock(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        lock_reason: Literal["off-topic", "too heated", "resolved", "spam"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Users with push access can lock an issue or pull request's conversation.

        Note that, if you choose not to pass any parameters, you'll need to set
        `Content-Length` to zero when calling out to this endpoint. For more
        information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        Args:
          lock_reason: The reason for locking the issue or pull request conversation. Lock will fail if
              you don't use one of these reasons:

              - `off-topic`
              - `too heated`
              - `resolved`
              - `spam`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/repos/{owner}/{repo}/issues/{issue_number}/lock",
            body=await async_maybe_transform({"lock_reason": lock_reason}, lock_lock_params.LockLockParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def unlock(
        self,
        issue_number: int,
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
        Users with push access can unlock an issue's conversation.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/issues/{issue_number}/lock",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class LockResourceWithRawResponse:
    def __init__(self, lock: LockResource) -> None:
        self._lock = lock

        self.lock = to_raw_response_wrapper(
            lock.lock,
        )
        self.unlock = to_raw_response_wrapper(
            lock.unlock,
        )


class AsyncLockResourceWithRawResponse:
    def __init__(self, lock: AsyncLockResource) -> None:
        self._lock = lock

        self.lock = async_to_raw_response_wrapper(
            lock.lock,
        )
        self.unlock = async_to_raw_response_wrapper(
            lock.unlock,
        )


class LockResourceWithStreamingResponse:
    def __init__(self, lock: LockResource) -> None:
        self._lock = lock

        self.lock = to_streamed_response_wrapper(
            lock.lock,
        )
        self.unlock = to_streamed_response_wrapper(
            lock.unlock,
        )


class AsyncLockResourceWithStreamingResponse:
    def __init__(self, lock: AsyncLockResource) -> None:
        self._lock = lock

        self.lock = async_to_streamed_response_wrapper(
            lock.lock,
        )
        self.unlock = async_to_streamed_response_wrapper(
            lock.unlock,
        )
