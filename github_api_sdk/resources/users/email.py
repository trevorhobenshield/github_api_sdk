from __future__ import annotations

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
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.users import email_set_visibility_params
from ...types.users.email_set_visibility_response import EmailSetVisibilityResponse

__all__ = ["EmailResource", "AsyncEmailResource"]


class EmailResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return EmailResourceWithStreamingResponse(self)

    def set_visibility(
        self,
        *,
        visibility: Literal["public", "private"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailSetVisibilityResponse:
        """
        Sets the visibility for your primary email addresses.

        Args:
          visibility: Denotes whether an email is publicly visible.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/user/email/visibility",
            body=maybe_transform({"visibility": visibility}, email_set_visibility_params.EmailSetVisibilityParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EmailSetVisibilityResponse,
        )


class AsyncEmailResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncEmailResourceWithStreamingResponse(self)

    async def set_visibility(
        self,
        *,
        visibility: Literal["public", "private"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailSetVisibilityResponse:
        """
        Sets the visibility for your primary email addresses.

        Args:
          visibility: Denotes whether an email is publicly visible.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/user/email/visibility",
            body=await async_maybe_transform({"visibility": visibility}, email_set_visibility_params.EmailSetVisibilityParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=EmailSetVisibilityResponse,
        )


class EmailResourceWithRawResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

        self.set_visibility = to_raw_response_wrapper(
            email.set_visibility,
        )


class AsyncEmailResourceWithRawResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

        self.set_visibility = async_to_raw_response_wrapper(
            email.set_visibility,
        )


class EmailResourceWithStreamingResponse:
    def __init__(self, email: EmailResource) -> None:
        self._email = email

        self.set_visibility = to_streamed_response_wrapper(
            email.set_visibility,
        )


class AsyncEmailResourceWithStreamingResponse:
    def __init__(self, email: AsyncEmailResource) -> None:
        self._email = email

        self.set_visibility = async_to_streamed_response_wrapper(
            email.set_visibility,
        )
