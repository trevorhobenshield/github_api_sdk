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
from ....types.notifications.threads import subscription_set_params
from ....types.notifications.threads.thread_subscription import ThreadSubscription

__all__ = ["SubscriptionResource", "AsyncSubscriptionResource"]


class SubscriptionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SubscriptionResourceWithStreamingResponse(self)

    def retrieve(
        self,
        thread_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadSubscription:
        """This checks to see if the current user is subscribed to a thread.

        You can also
        [get a repository subscription](https://docs.github.com/rest/activity/watching#get-a-repository-subscription).

        Note that subscriptions are only generated if a user is participating in a
        conversation--for example, they've replied to the thread, were **@mentioned**,
        or manually subscribe to a thread.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/notifications/threads/{thread_id}/subscription",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ThreadSubscription,
        )

    def delete(
        self,
        thread_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Mutes all future notifications for a conversation until you comment on the
        thread or get an **@mention**. If you are watching the repository of the thread,
        you will still receive notifications. To ignore future notifications for a
        repository you are watching, use the
        [Set a thread subscription](https://docs.github.com/rest/activity/notifications#set-a-thread-subscription)
        endpoint and set `ignore` to `true`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/notifications/threads/{thread_id}/subscription",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def set(
        self,
        thread_id: int,
        *,
        ignored: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadSubscription:
        """
        If you are watching a repository, you receive notifications for all threads by
        default. Use this endpoint to ignore future notifications for threads until you
        comment on the thread or get an **@mention**.

        You can also use this endpoint to subscribe to threads that you are currently
        not receiving notifications for or to subscribed to threads that you have
        previously ignored.

        Unsubscribing from a conversation in a repository that you are not watching is
        functionally equivalent to the
        [Delete a thread subscription](https://docs.github.com/rest/activity/notifications#delete-a-thread-subscription)
        endpoint.

        Args:
          ignored: Whether to block all notifications from a thread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/notifications/threads/{thread_id}/subscription",
            body=maybe_transform({"ignored": ignored}, subscription_set_params.SubscriptionSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ThreadSubscription,
        )


class AsyncSubscriptionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSubscriptionResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        thread_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadSubscription:
        """This checks to see if the current user is subscribed to a thread.

        You can also
        [get a repository subscription](https://docs.github.com/rest/activity/watching#get-a-repository-subscription).

        Note that subscriptions are only generated if a user is participating in a
        conversation--for example, they've replied to the thread, were **@mentioned**,
        or manually subscribe to a thread.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/notifications/threads/{thread_id}/subscription",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ThreadSubscription,
        )

    async def delete(
        self,
        thread_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Mutes all future notifications for a conversation until you comment on the
        thread or get an **@mention**. If you are watching the repository of the thread,
        you will still receive notifications. To ignore future notifications for a
        repository you are watching, use the
        [Set a thread subscription](https://docs.github.com/rest/activity/notifications#set-a-thread-subscription)
        endpoint and set `ignore` to `true`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/notifications/threads/{thread_id}/subscription",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def set(
        self,
        thread_id: int,
        *,
        ignored: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreadSubscription:
        """
        If you are watching a repository, you receive notifications for all threads by
        default. Use this endpoint to ignore future notifications for threads until you
        comment on the thread or get an **@mention**.

        You can also use this endpoint to subscribe to threads that you are currently
        not receiving notifications for or to subscribed to threads that you have
        previously ignored.

        Unsubscribing from a conversation in a repository that you are not watching is
        functionally equivalent to the
        [Delete a thread subscription](https://docs.github.com/rest/activity/notifications#delete-a-thread-subscription)
        endpoint.

        Args:
          ignored: Whether to block all notifications from a thread.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/notifications/threads/{thread_id}/subscription",
            body=await async_maybe_transform({"ignored": ignored}, subscription_set_params.SubscriptionSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ThreadSubscription,
        )


class SubscriptionResourceWithRawResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.retrieve = to_raw_response_wrapper(
            subscription.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            subscription.delete,
        )
        self.set = to_raw_response_wrapper(
            subscription.set,
        )


class AsyncSubscriptionResourceWithRawResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.retrieve = async_to_raw_response_wrapper(
            subscription.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            subscription.delete,
        )
        self.set = async_to_raw_response_wrapper(
            subscription.set,
        )


class SubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.retrieve = to_streamed_response_wrapper(
            subscription.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            subscription.delete,
        )
        self.set = to_streamed_response_wrapper(
            subscription.set,
        )


class AsyncSubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.retrieve = async_to_streamed_response_wrapper(
            subscription.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscription.delete,
        )
        self.set = async_to_streamed_response_wrapper(
            subscription.set,
        )
