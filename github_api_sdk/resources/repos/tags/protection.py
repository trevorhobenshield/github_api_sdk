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
from ....types.repos.tags import protection_create_params
from ....types.repos.tags.protection_list_response import ProtectionListResponse
from ....types.repos.tags.tag_protection import TagProtection

__all__ = ["ProtectionResource", "AsyncProtectionResource"]


class ProtectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ProtectionResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        pattern: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TagProtection:
        """
        > [!WARNING] > **Closing down notice:** This operation is closing down and will
        > be removed after August 30, 2024. Use the
        > "[Repository Rulesets](https://docs.github.com/rest/repos/rules#create-a-repository-ruleset)"
        > endpoint instead.

        This creates a tag protection state for a repository. This endpoint is only
        available to repository administrators.

        Args:
          pattern: An optional glob pattern to match against when enforcing tag protection.

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
            f"/repos/{owner}/{repo}/tags/protection",
            body=maybe_transform({"pattern": pattern}, protection_create_params.ProtectionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TagProtection,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectionListResponse:
        """
        > [!WARNING] > **Closing down notice:** This operation is closing down and will
        > be removed after August 30, 2024. Use the
        > "[Repository Rulesets](https://docs.github.com/rest/repos/rules#get-all-repository-rulesets)"
        > endpoint instead.

        This returns the tag protection states of a repository.

        This information is only available to repository administrators.

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
        return self._get(
            f"/repos/{owner}/{repo}/tags/protection",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectionListResponse,
        )

    def delete(
        self,
        tag_protection_id: int,
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
        > [!WARNING] > **Closing down notice:** This operation is closing down and will
        > be removed after August 30, 2024. Use the
        > "[Repository Rulesets](https://docs.github.com/rest/repos/rules#delete-a-repository-ruleset)"
        > endpoint instead.

        This deletes a tag protection state for a repository. This endpoint is only
        available to repository administrators.

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
            f"/repos/{owner}/{repo}/tags/protection/{tag_protection_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncProtectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncProtectionResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        pattern: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TagProtection:
        """
        > [!WARNING] > **Closing down notice:** This operation is closing down and will
        > be removed after August 30, 2024. Use the
        > "[Repository Rulesets](https://docs.github.com/rest/repos/rules#create-a-repository-ruleset)"
        > endpoint instead.

        This creates a tag protection state for a repository. This endpoint is only
        available to repository administrators.

        Args:
          pattern: An optional glob pattern to match against when enforcing tag protection.

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
            f"/repos/{owner}/{repo}/tags/protection",
            body=await async_maybe_transform({"pattern": pattern}, protection_create_params.ProtectionCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TagProtection,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectionListResponse:
        """
        > [!WARNING] > **Closing down notice:** This operation is closing down and will
        > be removed after August 30, 2024. Use the
        > "[Repository Rulesets](https://docs.github.com/rest/repos/rules#get-all-repository-rulesets)"
        > endpoint instead.

        This returns the tag protection states of a repository.

        This information is only available to repository administrators.

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
        return await self._get(
            f"/repos/{owner}/{repo}/tags/protection",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectionListResponse,
        )

    async def delete(
        self,
        tag_protection_id: int,
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
        > [!WARNING] > **Closing down notice:** This operation is closing down and will
        > be removed after August 30, 2024. Use the
        > "[Repository Rulesets](https://docs.github.com/rest/repos/rules#delete-a-repository-ruleset)"
        > endpoint instead.

        This deletes a tag protection state for a repository. This endpoint is only
        available to repository administrators.

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
            f"/repos/{owner}/{repo}/tags/protection/{tag_protection_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ProtectionResourceWithRawResponse:
    def __init__(self, protection: ProtectionResource) -> None:
        self._protection = protection

        self.create = to_raw_response_wrapper(
            protection.create,
        )
        self.list = to_raw_response_wrapper(
            protection.list,
        )
        self.delete = to_raw_response_wrapper(
            protection.delete,
        )


class AsyncProtectionResourceWithRawResponse:
    def __init__(self, protection: AsyncProtectionResource) -> None:
        self._protection = protection

        self.create = async_to_raw_response_wrapper(
            protection.create,
        )
        self.list = async_to_raw_response_wrapper(
            protection.list,
        )
        self.delete = async_to_raw_response_wrapper(
            protection.delete,
        )


class ProtectionResourceWithStreamingResponse:
    def __init__(self, protection: ProtectionResource) -> None:
        self._protection = protection

        self.create = to_streamed_response_wrapper(
            protection.create,
        )
        self.list = to_streamed_response_wrapper(
            protection.list,
        )
        self.delete = to_streamed_response_wrapper(
            protection.delete,
        )


class AsyncProtectionResourceWithStreamingResponse:
    def __init__(self, protection: AsyncProtectionResource) -> None:
        self._protection = protection

        self.create = async_to_streamed_response_wrapper(
            protection.create,
        )
        self.list = async_to_streamed_response_wrapper(
            protection.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            protection.delete,
        )
