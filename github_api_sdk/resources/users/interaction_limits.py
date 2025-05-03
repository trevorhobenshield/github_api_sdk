from __future__ import annotations

from typing import Any, cast

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
from ...types.orgs import InteractionGroup
from ...types.orgs.interaction_group import InteractionGroup
from ...types.orgs.interaction_limit_response import InteractionLimitResponse
from ...types.users import interaction_limit_set_params
from ...types.users.interaction_limit_retrieve_response import InteractionLimitRetrieveResponse

__all__ = ["InteractionLimitsResource", "AsyncInteractionLimitsResource"]


class InteractionLimitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InteractionLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return InteractionLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InteractionLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return InteractionLimitsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InteractionLimitRetrieveResponse:
        """
        Shows which type of GitHub user can interact with your public repositories and
        when the restriction expires.
        """
        return cast(
            InteractionLimitRetrieveResponse,
            self._get(
                "/user/interaction-limits",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, InteractionLimitRetrieveResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def remove(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Removes any interaction restrictions from your public repositories."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/user/interaction-limits",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def set(
        self,
        *,
        limit: InteractionGroup,
        expiry: Literal["one_day", "three_days", "one_week", "one_month", "six_months"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InteractionLimitResponse:
        """
        Temporarily restricts which type of GitHub user can interact with your public
        repositories. Setting the interaction limit at the user level will overwrite any
        interaction limits that are set for individual repositories owned by the user.

        Args:
          limit: The type of GitHub user that can comment, open issues, or create pull requests
              while the interaction limit is in effect.

          expiry: The duration of the interaction restriction. Default: `one_day`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/user/interaction-limits",
            body=maybe_transform(
                {
                    "limit": limit,
                    "expiry": expiry,
                },
                interaction_limit_set_params.InteractionLimitSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=InteractionLimitResponse,
        )


class AsyncInteractionLimitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInteractionLimitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInteractionLimitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInteractionLimitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncInteractionLimitsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InteractionLimitRetrieveResponse:
        """
        Shows which type of GitHub user can interact with your public repositories and
        when the restriction expires.
        """
        return cast(
            InteractionLimitRetrieveResponse,
            await self._get(
                "/user/interaction-limits",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, InteractionLimitRetrieveResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def remove(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Removes any interaction restrictions from your public repositories."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/user/interaction-limits",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def set(
        self,
        *,
        limit: InteractionGroup,
        expiry: Literal["one_day", "three_days", "one_week", "one_month", "six_months"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InteractionLimitResponse:
        """
        Temporarily restricts which type of GitHub user can interact with your public
        repositories. Setting the interaction limit at the user level will overwrite any
        interaction limits that are set for individual repositories owned by the user.

        Args:
          limit: The type of GitHub user that can comment, open issues, or create pull requests
              while the interaction limit is in effect.

          expiry: The duration of the interaction restriction. Default: `one_day`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/user/interaction-limits",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "expiry": expiry,
                },
                interaction_limit_set_params.InteractionLimitSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=InteractionLimitResponse,
        )


class InteractionLimitsResourceWithRawResponse:
    def __init__(self, interaction_limits: InteractionLimitsResource) -> None:
        self._interaction_limits = interaction_limits

        self.retrieve = to_raw_response_wrapper(
            interaction_limits.retrieve,
        )
        self.remove = to_raw_response_wrapper(
            interaction_limits.remove,
        )
        self.set = to_raw_response_wrapper(
            interaction_limits.set,
        )


class AsyncInteractionLimitsResourceWithRawResponse:
    def __init__(self, interaction_limits: AsyncInteractionLimitsResource) -> None:
        self._interaction_limits = interaction_limits

        self.retrieve = async_to_raw_response_wrapper(
            interaction_limits.retrieve,
        )
        self.remove = async_to_raw_response_wrapper(
            interaction_limits.remove,
        )
        self.set = async_to_raw_response_wrapper(
            interaction_limits.set,
        )


class InteractionLimitsResourceWithStreamingResponse:
    def __init__(self, interaction_limits: InteractionLimitsResource) -> None:
        self._interaction_limits = interaction_limits

        self.retrieve = to_streamed_response_wrapper(
            interaction_limits.retrieve,
        )
        self.remove = to_streamed_response_wrapper(
            interaction_limits.remove,
        )
        self.set = to_streamed_response_wrapper(
            interaction_limits.set,
        )


class AsyncInteractionLimitsResourceWithStreamingResponse:
    def __init__(self, interaction_limits: AsyncInteractionLimitsResource) -> None:
        self._interaction_limits = interaction_limits

        self.retrieve = async_to_streamed_response_wrapper(
            interaction_limits.retrieve,
        )
        self.remove = async_to_streamed_response_wrapper(
            interaction_limits.remove,
        )
        self.set = async_to_streamed_response_wrapper(
            interaction_limits.set,
        )
