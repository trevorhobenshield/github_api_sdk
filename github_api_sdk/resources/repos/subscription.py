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
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.repos import subscription_set_params
from ...types.repos.repository_subscription import RepositorySubscription

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

    def delete(
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
    ) -> None:
        """This endpoint should only be used to stop watching a repository.

        To control
        whether or not you wish to receive notifications from a repository,
        [set the repository's subscription manually](https://docs.github.com/rest/activity/watching#set-a-repository-subscription).

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
            f"/repos/{owner}/{repo}/subscription",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get(
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
    ) -> RepositorySubscription:
        """
        Gets information about whether the authenticated user is subscribed to the
        repository.

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
            f"/repos/{owner}/{repo}/subscription",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositorySubscription,
        )

    def set(
        self,
        repo: str,
        *,
        owner: str,
        ignored: bool | NotGiven = NOT_GIVEN,
        subscribed: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositorySubscription:
        """If you would like to watch a repository, set `subscribed` to `true`.

        If you
        would like to ignore notifications made within a repository, set `ignored` to
        `true`. If you would like to stop watching a repository,
        [delete the repository's subscription](https://docs.github.com/rest/activity/watching#delete-a-repository-subscription)
        completely.

        Args:
          ignored: Determines if all notifications should be blocked from this repository.

          subscribed: Determines if notifications should be received from this repository.

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
            f"/repos/{owner}/{repo}/subscription",
            body=maybe_transform(
                {
                    "ignored": ignored,
                    "subscribed": subscribed,
                },
                subscription_set_params.SubscriptionSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositorySubscription,
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

    async def delete(
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
    ) -> None:
        """This endpoint should only be used to stop watching a repository.

        To control
        whether or not you wish to receive notifications from a repository,
        [set the repository's subscription manually](https://docs.github.com/rest/activity/watching#set-a-repository-subscription).

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
            f"/repos/{owner}/{repo}/subscription",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get(
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
    ) -> RepositorySubscription:
        """
        Gets information about whether the authenticated user is subscribed to the
        repository.

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
            f"/repos/{owner}/{repo}/subscription",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositorySubscription,
        )

    async def set(
        self,
        repo: str,
        *,
        owner: str,
        ignored: bool | NotGiven = NOT_GIVEN,
        subscribed: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositorySubscription:
        """If you would like to watch a repository, set `subscribed` to `true`.

        If you
        would like to ignore notifications made within a repository, set `ignored` to
        `true`. If you would like to stop watching a repository,
        [delete the repository's subscription](https://docs.github.com/rest/activity/watching#delete-a-repository-subscription)
        completely.

        Args:
          ignored: Determines if all notifications should be blocked from this repository.

          subscribed: Determines if notifications should be received from this repository.

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
            f"/repos/{owner}/{repo}/subscription",
            body=await async_maybe_transform(
                {
                    "ignored": ignored,
                    "subscribed": subscribed,
                },
                subscription_set_params.SubscriptionSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositorySubscription,
        )


class SubscriptionResourceWithRawResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.delete = to_raw_response_wrapper(
            subscription.delete,
        )
        self.get = to_raw_response_wrapper(
            subscription.get,
        )
        self.set = to_raw_response_wrapper(
            subscription.set,
        )


class AsyncSubscriptionResourceWithRawResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.delete = async_to_raw_response_wrapper(
            subscription.delete,
        )
        self.get = async_to_raw_response_wrapper(
            subscription.get,
        )
        self.set = async_to_raw_response_wrapper(
            subscription.set,
        )


class SubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: SubscriptionResource) -> None:
        self._subscription = subscription

        self.delete = to_streamed_response_wrapper(
            subscription.delete,
        )
        self.get = to_streamed_response_wrapper(
            subscription.get,
        )
        self.set = to_streamed_response_wrapper(
            subscription.set,
        )


class AsyncSubscriptionResourceWithStreamingResponse:
    def __init__(self, subscription: AsyncSubscriptionResource) -> None:
        self._subscription = subscription

        self.delete = async_to_streamed_response_wrapper(
            subscription.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            subscription.get,
        )
        self.set = async_to_streamed_response_wrapper(
            subscription.set,
        )
