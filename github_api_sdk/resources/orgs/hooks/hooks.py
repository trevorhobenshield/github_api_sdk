from __future__ import annotations

import builtins
from typing import List

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
from ....types.orgs import hook_create_params, hook_list_params, hook_update_params
from ....types.orgs.hook_list_response import HookListResponse
from ....types.orgs.org_hook import OrgHook
from .config import (
    AsyncConfigResource,
    AsyncConfigResourceWithRawResponse,
    AsyncConfigResourceWithStreamingResponse,
    ConfigResource,
    ConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
)
from .deliveries import (
    AsyncDeliveriesResource,
    AsyncDeliveriesResourceWithRawResponse,
    AsyncDeliveriesResourceWithStreamingResponse,
    DeliveriesResource,
    DeliveriesResourceWithRawResponse,
    DeliveriesResourceWithStreamingResponse,
)

__all__ = ["HooksResource", "AsyncHooksResource"]


class HooksResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def deliveries(self) -> DeliveriesResource:
        return DeliveriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> HooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return HooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return HooksResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        config: hook_create_params.Config,
        name: str,
        active: bool | NotGiven = NOT_GIVEN,
        events: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgHook:
        """
        Create a hook that posts payloads in JSON format.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          config: Key/value pairs to provide settings for this webhook.

          name: Must be passed as "web".

          active: Determines if notifications are sent when the webhook is triggered. Set to
              `true` to send notifications.

          events: Determines what [events](https://docs.github.com/webhooks/event-payloads) the
              hook is triggered for. Set to `["*"]` to receive all possible events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/hooks",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "active": active,
                    "events": events,
                },
                hook_create_params.HookCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgHook,
        )

    def retrieve(
        self,
        hook_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgHook:
        """Returns a webhook configured in an organization.

        To get only the webhook
        `config` properties, see
        "[Get a webhook configuration for an organization](/rest/orgs/webhooks#get-a-webhook-configuration-for-an-organization).

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/hooks/{hook_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgHook,
        )

    def update(
        self,
        hook_id: int,
        *,
        org: str,
        active: bool | NotGiven = NOT_GIVEN,
        config: hook_update_params.Config | NotGiven = NOT_GIVEN,
        events: builtins.list[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgHook:
        """Updates a webhook configured in an organization.

        When you update a webhook, the
        `secret` will be overwritten. If you previously had a `secret` set, you must
        provide the same `secret` or set a new `secret` or the secret will be removed.
        If you are only updating individual webhook `config` properties, use
        "[Update a webhook configuration for an organization](/rest/orgs/webhooks#update-a-webhook-configuration-for-an-organization)".

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          active: Determines if notifications are sent when the webhook is triggered. Set to
              `true` to send notifications.

          config: Key/value pairs to provide settings for this webhook.

          events: Determines what [events](https://docs.github.com/webhooks/event-payloads) the
              hook is triggered for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._patch(
            f"/orgs/{org}/hooks/{hook_id}",
            body=maybe_transform(
                {
                    "active": active,
                    "config": config,
                    "events": events,
                    "name": name,
                },
                hook_update_params.HookUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgHook,
        )

    def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HookListResponse:
        """
        List webhooks for an organization.

        The authenticated user must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/hooks",
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
                    hook_list_params.HookListParams,
                ),
            ),
            cast_to=HookListResponse,
        )

    def delete(
        self,
        hook_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a webhook for an organization.

        The authenticated user must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

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
            f"/orgs/{org}/hooks/{hook_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def ping(
        self,
        hook_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event)
        to be sent to the hook.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/orgs/{org}/hooks/{hook_id}/pings",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncHooksResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResource:
        return AsyncDeliveriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncHooksResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        config: hook_create_params.Config,
        name: str,
        active: bool | NotGiven = NOT_GIVEN,
        events: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgHook:
        """
        Create a hook that posts payloads in JSON format.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          config: Key/value pairs to provide settings for this webhook.

          name: Must be passed as "web".

          active: Determines if notifications are sent when the webhook is triggered. Set to
              `true` to send notifications.

          events: Determines what [events](https://docs.github.com/webhooks/event-payloads) the
              hook is triggered for. Set to `["*"]` to receive all possible events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/hooks",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "active": active,
                    "events": events,
                },
                hook_create_params.HookCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgHook,
        )

    async def retrieve(
        self,
        hook_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgHook:
        """Returns a webhook configured in an organization.

        To get only the webhook
        `config` properties, see
        "[Get a webhook configuration for an organization](/rest/orgs/webhooks#get-a-webhook-configuration-for-an-organization).

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/hooks/{hook_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgHook,
        )

    async def update(
        self,
        hook_id: int,
        *,
        org: str,
        active: bool | NotGiven = NOT_GIVEN,
        config: hook_update_params.Config | NotGiven = NOT_GIVEN,
        events: builtins.list[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgHook:
        """Updates a webhook configured in an organization.

        When you update a webhook, the
        `secret` will be overwritten. If you previously had a `secret` set, you must
        provide the same `secret` or set a new `secret` or the secret will be removed.
        If you are only updating individual webhook `config` properties, use
        "[Update a webhook configuration for an organization](/rest/orgs/webhooks#update-a-webhook-configuration-for-an-organization)".

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          active: Determines if notifications are sent when the webhook is triggered. Set to
              `true` to send notifications.

          config: Key/value pairs to provide settings for this webhook.

          events: Determines what [events](https://docs.github.com/webhooks/event-payloads) the
              hook is triggered for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._patch(
            f"/orgs/{org}/hooks/{hook_id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "config": config,
                    "events": events,
                    "name": name,
                },
                hook_update_params.HookUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgHook,
        )

    async def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HookListResponse:
        """
        List webhooks for an organization.

        The authenticated user must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/hooks",
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
                    hook_list_params.HookListParams,
                ),
            ),
            cast_to=HookListResponse,
        )

    async def delete(
        self,
        hook_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a webhook for an organization.

        The authenticated user must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

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
            f"/orgs/{org}/hooks/{hook_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def ping(
        self,
        hook_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event)
        to be sent to the hook.

        You must be an organization owner to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need `admin:org_hook`
        scope. OAuth apps cannot list, view, or edit webhooks that they did not create
        and users cannot list, view, or edit webhooks that were created by OAuth apps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/orgs/{org}/hooks/{hook_id}/pings",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class HooksResourceWithRawResponse:
    def __init__(self, hooks: HooksResource) -> None:
        self._hooks = hooks

        self.create = to_raw_response_wrapper(
            hooks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            hooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            hooks.update,
        )
        self.list = to_raw_response_wrapper(
            hooks.list,
        )
        self.delete = to_raw_response_wrapper(
            hooks.delete,
        )
        self.ping = to_raw_response_wrapper(
            hooks.ping,
        )

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._hooks.config)

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithRawResponse:
        return DeliveriesResourceWithRawResponse(self._hooks.deliveries)


class AsyncHooksResourceWithRawResponse:
    def __init__(self, hooks: AsyncHooksResource) -> None:
        self._hooks = hooks

        self.create = async_to_raw_response_wrapper(
            hooks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            hooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            hooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            hooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            hooks.delete,
        )
        self.ping = async_to_raw_response_wrapper(
            hooks.ping,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._hooks.config)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithRawResponse:
        return AsyncDeliveriesResourceWithRawResponse(self._hooks.deliveries)


class HooksResourceWithStreamingResponse:
    def __init__(self, hooks: HooksResource) -> None:
        self._hooks = hooks

        self.create = to_streamed_response_wrapper(
            hooks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            hooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            hooks.update,
        )
        self.list = to_streamed_response_wrapper(
            hooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            hooks.delete,
        )
        self.ping = to_streamed_response_wrapper(
            hooks.ping,
        )

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._hooks.config)

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithStreamingResponse:
        return DeliveriesResourceWithStreamingResponse(self._hooks.deliveries)


class AsyncHooksResourceWithStreamingResponse:
    def __init__(self, hooks: AsyncHooksResource) -> None:
        self._hooks = hooks

        self.create = async_to_streamed_response_wrapper(
            hooks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            hooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            hooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            hooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            hooks.delete,
        )
        self.ping = async_to_streamed_response_wrapper(
            hooks.ping,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._hooks.config)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        return AsyncDeliveriesResourceWithStreamingResponse(self._hooks.deliveries)
