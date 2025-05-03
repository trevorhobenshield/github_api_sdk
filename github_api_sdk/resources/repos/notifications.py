from __future__ import annotations

from datetime import datetime
from typing import Union

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
from ...types.repos import notification_list_params, notification_mark_as_read_params
from ...types.repos.notification_list_response import NotificationListResponse
from ...types.repos.notification_mark_as_read_response import NotificationMarkAsReadResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def list(
        self,
        repo: str,
        *,
        owner: str,
        all: bool | NotGiven = NOT_GIVEN,
        before: str | datetime | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        participating: bool | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationListResponse:
        """
        Lists all notifications for the current user in the specified repository.

        Args:
          all: If `true`, show notifications marked as read.

          before: Only show notifications updated before the given time. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          participating: If `true`, only shows notifications in which the user is directly participating
              or mentioned.

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

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
            f"/repos/{owner}/{repo}/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "all": all,
                        "before": before,
                        "page": page,
                        "participating": participating,
                        "per_page": per_page,
                        "since": since,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    def mark_as_read(
        self,
        repo: str,
        *,
        owner: str,
        last_read_at: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationMarkAsReadResponse:
        """Marks all notifications in a repository as "read" for the current user.

        If the
        number of notifications is too large to complete in one request, you will
        receive a `202 Accepted` status and GitHub will run an asynchronous process to
        mark notifications as "read." To check whether any "unread" notifications
        remain, you can use the
        [List repository notifications for the authenticated user](https://docs.github.com/rest/activity/notifications#list-repository-notifications-for-the-authenticated-user)
        endpoint and pass the query parameter `all=false`.

        Args:
          last_read_at: Describes the last point that notifications were checked. Anything updated since
              this time will not be marked as read. If you omit this parameter, all
              notifications are marked as read. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`. Default: The current timestamp.

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
            f"/repos/{owner}/{repo}/notifications",
            body=maybe_transform({"last_read_at": last_read_at}, notification_mark_as_read_params.NotificationMarkAsReadParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NotificationMarkAsReadResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        all: bool | NotGiven = NOT_GIVEN,
        before: str | datetime | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        participating: bool | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationListResponse:
        """
        Lists all notifications for the current user in the specified repository.

        Args:
          all: If `true`, show notifications marked as read.

          before: Only show notifications updated before the given time. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          participating: If `true`, only shows notifications in which the user is directly participating
              or mentioned.

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

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
            f"/repos/{owner}/{repo}/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "all": all,
                        "before": before,
                        "page": page,
                        "participating": participating,
                        "per_page": per_page,
                        "since": since,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    async def mark_as_read(
        self,
        repo: str,
        *,
        owner: str,
        last_read_at: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NotificationMarkAsReadResponse:
        """Marks all notifications in a repository as "read" for the current user.

        If the
        number of notifications is too large to complete in one request, you will
        receive a `202 Accepted` status and GitHub will run an asynchronous process to
        mark notifications as "read." To check whether any "unread" notifications
        remain, you can use the
        [List repository notifications for the authenticated user](https://docs.github.com/rest/activity/notifications#list-repository-notifications-for-the-authenticated-user)
        endpoint and pass the query parameter `all=false`.

        Args:
          last_read_at: Describes the last point that notifications were checked. Anything updated since
              this time will not be marked as read. If you omit this parameter, all
              notifications are marked as read. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`. Default: The current timestamp.

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
            f"/repos/{owner}/{repo}/notifications",
            body=await async_maybe_transform({"last_read_at": last_read_at}, notification_mark_as_read_params.NotificationMarkAsReadParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NotificationMarkAsReadResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_raw_response_wrapper(
            notifications.list,
        )
        self.mark_as_read = to_raw_response_wrapper(
            notifications.mark_as_read,
        )


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )
        self.mark_as_read = async_to_raw_response_wrapper(
            notifications.mark_as_read,
        )


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_streamed_response_wrapper(
            notifications.list,
        )
        self.mark_as_read = to_streamed_response_wrapper(
            notifications.mark_as_read,
        )


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )
        self.mark_as_read = async_to_streamed_response_wrapper(
            notifications.mark_as_read,
        )
