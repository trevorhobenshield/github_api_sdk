from __future__ import annotations

from typing import List

import httpx

from ......_base_client import make_request_options
from ......_compat import cached_property
from ......_resource import AsyncAPIResource, SyncAPIResource
from ......_response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ......_types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ......_utils import (
    async_maybe_transform,
    maybe_transform,
)
from ......types.repos.actions.oidc.customization import sub_update_params
from ......types.repos.actions.oidc.customization.sub_retrieve_response import SubRetrieveResponse

__all__ = ["SubResource", "AsyncSubResource"]


class SubResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SubResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> SubRetrieveResponse:
        """
        Gets the customization template for an OpenID Connect (OIDC) subject claim.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
            f"/repos/{owner}/{repo}/actions/oidc/customization/sub",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SubRetrieveResponse,
        )

    def update(
        self,
        repo: str,
        *,
        owner: str,
        use_default: bool,
        include_claim_keys: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Sets the customization template and `opt-in` or `opt-out` flag for an OpenID
        Connect (OIDC) subject claim for a repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          use_default: Whether to use the default template or not. If `true`, the `include_claim_keys`
              field is ignored.

          include_claim_keys: Array of unique strings. Each claim key can only contain alphanumeric characters
              and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._put(
            f"/repos/{owner}/{repo}/actions/oidc/customization/sub",
            body=maybe_transform(
                {
                    "use_default": use_default,
                    "include_claim_keys": include_claim_keys,
                },
                sub_update_params.SubUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class AsyncSubResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSubResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> SubRetrieveResponse:
        """
        Gets the customization template for an OpenID Connect (OIDC) subject claim.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
            f"/repos/{owner}/{repo}/actions/oidc/customization/sub",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SubRetrieveResponse,
        )

    async def update(
        self,
        repo: str,
        *,
        owner: str,
        use_default: bool,
        include_claim_keys: list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Sets the customization template and `opt-in` or `opt-out` flag for an OpenID
        Connect (OIDC) subject claim for a repository.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          use_default: Whether to use the default template or not. If `true`, the `include_claim_keys`
              field is ignored.

          include_claim_keys: Array of unique strings. Each claim key can only contain alphanumeric characters
              and underscores.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/actions/oidc/customization/sub",
            body=await async_maybe_transform(
                {
                    "use_default": use_default,
                    "include_claim_keys": include_claim_keys,
                },
                sub_update_params.SubUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class SubResourceWithRawResponse:
    def __init__(self, sub: SubResource) -> None:
        self._sub = sub

        self.retrieve = to_raw_response_wrapper(
            sub.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sub.update,
        )


class AsyncSubResourceWithRawResponse:
    def __init__(self, sub: AsyncSubResource) -> None:
        self._sub = sub

        self.retrieve = async_to_raw_response_wrapper(
            sub.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sub.update,
        )


class SubResourceWithStreamingResponse:
    def __init__(self, sub: SubResource) -> None:
        self._sub = sub

        self.retrieve = to_streamed_response_wrapper(
            sub.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sub.update,
        )


class AsyncSubResourceWithStreamingResponse:
    def __init__(self, sub: AsyncSubResource) -> None:
        self._sub = sub

        self.retrieve = async_to_streamed_response_wrapper(
            sub.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sub.update,
        )
