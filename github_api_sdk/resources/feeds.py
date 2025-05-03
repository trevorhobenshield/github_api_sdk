from __future__ import annotations

import httpx

from .._base_client import make_request_options
from .._compat import cached_property
from .._resource import AsyncAPIResource, SyncAPIResource
from .._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..types.feed_list_response import FeedListResponse

__all__ = ["FeedsResource", "AsyncFeedsResource"]


class FeedsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return FeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return FeedsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedListResponse:
        """Lists the feeds available to the authenticated user.

        The response provides a URL
        for each feed. You can then get a specific feed by sending a request to one of
        the feed URLs.

        - **Timeline**: The GitHub global public timeline
        - **User**: The public timeline for any user, using `uri_template`. For more
          information, see
          "[Hypermedia](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia)."
        - **Current user public**: The public timeline for the authenticated user
        - **Current user**: The private timeline for the authenticated user
        - **Current user actor**: The private timeline for activity created by the
          authenticated user
        - **Current user organizations**: The private timeline for the organizations the
          authenticated user is a member of.
        - **Security advisories**: A collection of public announcements that provide
          information about security-related vulnerabilities in software on GitHub.

        By default, timeline resources are returned in JSON. You can specify the
        `application/atom+xml` type in the `Accept` header to return timeline resources
        in Atom format. For more information, see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        > [!NOTE] Private feeds are only returned when
        > [authenticating via Basic Auth](https://docs.github.com/rest/authentication/authenticating-to-the-rest-api#using-basic-authentication)
        > since current feed URIs use the older, non revocable auth tokens.
        """
        return self._get(
            "/feeds",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedListResponse,
        )


class AsyncFeedsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncFeedsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedListResponse:
        """Lists the feeds available to the authenticated user.

        The response provides a URL
        for each feed. You can then get a specific feed by sending a request to one of
        the feed URLs.

        - **Timeline**: The GitHub global public timeline
        - **User**: The public timeline for any user, using `uri_template`. For more
          information, see
          "[Hypermedia](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia)."
        - **Current user public**: The public timeline for the authenticated user
        - **Current user**: The private timeline for the authenticated user
        - **Current user actor**: The private timeline for activity created by the
          authenticated user
        - **Current user organizations**: The private timeline for the organizations the
          authenticated user is a member of.
        - **Security advisories**: A collection of public announcements that provide
          information about security-related vulnerabilities in software on GitHub.

        By default, timeline resources are returned in JSON. You can specify the
        `application/atom+xml` type in the `Accept` header to return timeline resources
        in Atom format. For more information, see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        > [!NOTE] Private feeds are only returned when
        > [authenticating via Basic Auth](https://docs.github.com/rest/authentication/authenticating-to-the-rest-api#using-basic-authentication)
        > since current feed URIs use the older, non revocable auth tokens.
        """
        return await self._get(
            "/feeds",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FeedListResponse,
        )


class FeedsResourceWithRawResponse:
    def __init__(self, feeds: FeedsResource) -> None:
        self._feeds = feeds

        self.list = to_raw_response_wrapper(
            feeds.list,
        )


class AsyncFeedsResourceWithRawResponse:
    def __init__(self, feeds: AsyncFeedsResource) -> None:
        self._feeds = feeds

        self.list = async_to_raw_response_wrapper(
            feeds.list,
        )


class FeedsResourceWithStreamingResponse:
    def __init__(self, feeds: FeedsResource) -> None:
        self._feeds = feeds

        self.list = to_streamed_response_wrapper(
            feeds.list,
        )


class AsyncFeedsResourceWithStreamingResponse:
    def __init__(self, feeds: AsyncFeedsResource) -> None:
        self._feeds = feeds

        self.list = async_to_streamed_response_wrapper(
            feeds.list,
        )
