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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.applications.hook import config_update_params
from ....types.applications.hook.insecure_ssl_param import InsecureSslParam
from ....types.applications.hook.webhook import Webhook

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Webhook:
        """Returns the webhook configuration for a GitHub App.

        For more information about
        configuring a webhook for your app, see
        "[Creating a GitHub App](/developers/apps/creating-a-github-app)."

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.
        """
        return self._get(
            "/app/hook/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Webhook,
        )

    def update(
        self,
        *,
        content_type: str | NotGiven = NOT_GIVEN,
        insecure_ssl: InsecureSslParam | NotGiven = NOT_GIVEN,
        secret: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Webhook:
        """Updates the webhook configuration for a GitHub App.

        For more information about
        configuring a webhook for your app, see
        "[Creating a GitHub App](/developers/apps/creating-a-github-app)."

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          content_type: The media type used to serialize the payloads. Supported values include `json`
              and `form`. The default is `form`.

          insecure_ssl: Determines whether the SSL certificate of the host for `url` will be verified
              when delivering payloads. Supported values include `0` (verification is
              performed) and `1` (verification is not performed). The default is `0`. **We
              strongly recommend not setting this to `1` as you are subject to
              man-in-the-middle and other attacks.**

          secret: If provided, the `secret` will be used as the `key` to generate the HMAC hex
              digest value for
              [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).

          url: The URL to which the payloads will be delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/app/hook/config",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "insecure_ssl": insecure_ssl,
                    "secret": secret,
                    "url": url,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Webhook,
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Webhook:
        """Returns the webhook configuration for a GitHub App.

        For more information about
        configuring a webhook for your app, see
        "[Creating a GitHub App](/developers/apps/creating-a-github-app)."

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.
        """
        return await self._get(
            "/app/hook/config",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Webhook,
        )

    async def update(
        self,
        *,
        content_type: str | NotGiven = NOT_GIVEN,
        insecure_ssl: InsecureSslParam | NotGiven = NOT_GIVEN,
        secret: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Webhook:
        """Updates the webhook configuration for a GitHub App.

        For more information about
        configuring a webhook for your app, see
        "[Creating a GitHub App](/developers/apps/creating-a-github-app)."

        You must use a
        [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app)
        to access this endpoint.

        Args:
          content_type: The media type used to serialize the payloads. Supported values include `json`
              and `form`. The default is `form`.

          insecure_ssl: Determines whether the SSL certificate of the host for `url` will be verified
              when delivering payloads. Supported values include `0` (verification is
              performed) and `1` (verification is not performed). The default is `0`. **We
              strongly recommend not setting this to `1` as you are subject to
              man-in-the-middle and other attacks.**

          secret: If provided, the `secret` will be used as the `key` to generate the HMAC hex
              digest value for
              [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).

          url: The URL to which the payloads will be delivered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/app/hook/config",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "insecure_ssl": insecure_ssl,
                    "secret": secret,
                    "url": url,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Webhook,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.retrieve = to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = to_raw_response_wrapper(
            config.update,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.retrieve = async_to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            config.update,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.retrieve = to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            config.update,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.retrieve = async_to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
