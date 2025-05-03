from __future__ import annotations

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
from ...types.users import received_event_list_public_received_events_params, received_event_list_received_events_params
from ...types.users.received_event_list_public_received_events_response import (
    ReceivedEventListPublicReceivedEventsResponse,
)
from ...types.users.received_event_list_received_events_response import ReceivedEventListReceivedEventsResponse

__all__ = ["ReceivedEventsResource", "AsyncReceivedEventsResource"]


class ReceivedEventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReceivedEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReceivedEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReceivedEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ReceivedEventsResourceWithStreamingResponse(self)

    def list_public_received_events(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReceivedEventListPublicReceivedEventsResponse:
        """> [!NOTE] This API is not built to serve real-time use cases.

        Depending on the
        > time of day, event latency can be anywhere from 30s to 6h.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/received_events/public",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    received_event_list_public_received_events_params.ReceivedEventListPublicReceivedEventsParams,
                ),
            ),
            cast_to=ReceivedEventListPublicReceivedEventsResponse,
        )

    def list_received_events(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReceivedEventListReceivedEventsResponse:
        """
        These are events that you've received by watching repositories and following
        users. If you are authenticated as the given user, you will see private events.
        Otherwise, you'll only see public events.

        > [!NOTE] This API is not built to serve real-time use cases. Depending on the
        > time of day, event latency can be anywhere from 30s to 6h.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/received_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    received_event_list_received_events_params.ReceivedEventListReceivedEventsParams,
                ),
            ),
            cast_to=ReceivedEventListReceivedEventsResponse,
        )


class AsyncReceivedEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReceivedEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReceivedEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReceivedEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncReceivedEventsResourceWithStreamingResponse(self)

    async def list_public_received_events(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReceivedEventListPublicReceivedEventsResponse:
        """> [!NOTE] This API is not built to serve real-time use cases.

        Depending on the
        > time of day, event latency can be anywhere from 30s to 6h.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/received_events/public",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    received_event_list_public_received_events_params.ReceivedEventListPublicReceivedEventsParams,
                ),
            ),
            cast_to=ReceivedEventListPublicReceivedEventsResponse,
        )

    async def list_received_events(
        self,
        username: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReceivedEventListReceivedEventsResponse:
        """
        These are events that you've received by watching repositories and following
        users. If you are authenticated as the given user, you will see private events.
        Otherwise, you'll only see public events.

        > [!NOTE] This API is not built to serve real-time use cases. Depending on the
        > time of day, event latency can be anywhere from 30s to 6h.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/received_events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    received_event_list_received_events_params.ReceivedEventListReceivedEventsParams,
                ),
            ),
            cast_to=ReceivedEventListReceivedEventsResponse,
        )


class ReceivedEventsResourceWithRawResponse:
    def __init__(self, received_events: ReceivedEventsResource) -> None:
        self._received_events = received_events

        self.list_public_received_events = to_raw_response_wrapper(
            received_events.list_public_received_events,
        )
        self.list_received_events = to_raw_response_wrapper(
            received_events.list_received_events,
        )


class AsyncReceivedEventsResourceWithRawResponse:
    def __init__(self, received_events: AsyncReceivedEventsResource) -> None:
        self._received_events = received_events

        self.list_public_received_events = async_to_raw_response_wrapper(
            received_events.list_public_received_events,
        )
        self.list_received_events = async_to_raw_response_wrapper(
            received_events.list_received_events,
        )


class ReceivedEventsResourceWithStreamingResponse:
    def __init__(self, received_events: ReceivedEventsResource) -> None:
        self._received_events = received_events

        self.list_public_received_events = to_streamed_response_wrapper(
            received_events.list_public_received_events,
        )
        self.list_received_events = to_streamed_response_wrapper(
            received_events.list_received_events,
        )


class AsyncReceivedEventsResourceWithStreamingResponse:
    def __init__(self, received_events: AsyncReceivedEventsResource) -> None:
        self._received_events = received_events

        self.list_public_received_events = async_to_streamed_response_wrapper(
            received_events.list_public_received_events,
        )
        self.list_received_events = async_to_streamed_response_wrapper(
            received_events.list_received_events,
        )
