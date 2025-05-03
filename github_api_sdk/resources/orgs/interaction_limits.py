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
from ...types.orgs import InteractionGroup, interaction_limit_update_params
from ...types.orgs.interaction_group import InteractionGroup
from ...types.orgs.interaction_limit_response import InteractionLimitResponse
from ...types.orgs.interaction_limit_retrieve_response import InteractionLimitRetrieveResponse

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
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InteractionLimitRetrieveResponse:
        """
        Shows which type of GitHub user can interact with this organization and when the
        restriction expires. If there is no restrictions, you will see an empty
        response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return cast(
            InteractionLimitRetrieveResponse,
            self._get(
                f"/orgs/{org}/interaction-limits",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, InteractionLimitRetrieveResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        org: str,
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
        Temporarily restricts interactions to a certain type of GitHub user in any
        public repository in the given organization. You must be an organization owner
        to set these restrictions. Setting the interaction limit at the organization
        level will overwrite any interaction limits that are set for individual
        repositories owned by the organization.

        Args:
          limit: The type of GitHub user that can comment, open issues, or create pull requests
              while the interaction limit is in effect.

          expiry: The duration of the interaction restriction. Default: `one_day`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._put(
            f"/orgs/{org}/interaction-limits",
            body=maybe_transform(
                {
                    "limit": limit,
                    "expiry": expiry,
                },
                interaction_limit_update_params.InteractionLimitUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=InteractionLimitResponse,
        )

    def delete(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes all interaction restrictions from public repositories in the given
        organization. You must be an organization owner to remove restrictions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/interaction-limits",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
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
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InteractionLimitRetrieveResponse:
        """
        Shows which type of GitHub user can interact with this organization and when the
        restriction expires. If there is no restrictions, you will see an empty
        response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return cast(
            InteractionLimitRetrieveResponse,
            await self._get(
                f"/orgs/{org}/interaction-limits",
                options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
                cast_to=cast(Any, InteractionLimitRetrieveResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        org: str,
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
        Temporarily restricts interactions to a certain type of GitHub user in any
        public repository in the given organization. You must be an organization owner
        to set these restrictions. Setting the interaction limit at the organization
        level will overwrite any interaction limits that are set for individual
        repositories owned by the organization.

        Args:
          limit: The type of GitHub user that can comment, open issues, or create pull requests
              while the interaction limit is in effect.

          expiry: The duration of the interaction restriction. Default: `one_day`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._put(
            f"/orgs/{org}/interaction-limits",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "expiry": expiry,
                },
                interaction_limit_update_params.InteractionLimitUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=InteractionLimitResponse,
        )

    async def delete(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes all interaction restrictions from public repositories in the given
        organization. You must be an organization owner to remove restrictions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/interaction-limits",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class InteractionLimitsResourceWithRawResponse:
    def __init__(self, interaction_limits: InteractionLimitsResource) -> None:
        self._interaction_limits = interaction_limits

        self.retrieve = to_raw_response_wrapper(
            interaction_limits.retrieve,
        )
        self.update = to_raw_response_wrapper(
            interaction_limits.update,
        )
        self.delete = to_raw_response_wrapper(
            interaction_limits.delete,
        )


class AsyncInteractionLimitsResourceWithRawResponse:
    def __init__(self, interaction_limits: AsyncInteractionLimitsResource) -> None:
        self._interaction_limits = interaction_limits

        self.retrieve = async_to_raw_response_wrapper(
            interaction_limits.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            interaction_limits.update,
        )
        self.delete = async_to_raw_response_wrapper(
            interaction_limits.delete,
        )


class InteractionLimitsResourceWithStreamingResponse:
    def __init__(self, interaction_limits: InteractionLimitsResource) -> None:
        self._interaction_limits = interaction_limits

        self.retrieve = to_streamed_response_wrapper(
            interaction_limits.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            interaction_limits.update,
        )
        self.delete = to_streamed_response_wrapper(
            interaction_limits.delete,
        )


class AsyncInteractionLimitsResourceWithStreamingResponse:
    def __init__(self, interaction_limits: AsyncInteractionLimitsResource) -> None:
        self._interaction_limits = interaction_limits

        self.retrieve = async_to_streamed_response_wrapper(
            interaction_limits.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            interaction_limits.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            interaction_limits.delete,
        )
