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
from ....types.applications.hook.webhook_param import WebhookParam
from ....types.repos import hook_create_params, hook_list_params, hook_update_params
from ....types.repos.hook import Hook
from ....types.repos.hook_list_response import HookListResponse
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
        repo: str,
        *,
        owner: str,
        active: bool | NotGiven = NOT_GIVEN,
        config: hook_create_params.Config | NotGiven = NOT_GIVEN,
        events: builtins.list[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Hook:
        """Repositories can have multiple webhooks installed.

        Each webhook should have a
        unique `config`. Multiple webhooks can share the same `config` as long as those
        webhooks do not have any `events` that overlap.

        Args:
          active: Determines if notifications are sent when the webhook is triggered. Set to
              `true` to send notifications.

          config: Key/value pairs to provide settings for this webhook.

          events: Determines what [events](https://docs.github.com/webhooks/event-payloads) the
              hook is triggered for.

          name: Use `web` to create a webhook. Default: `web`. This parameter only accepts the
              value `web`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/hooks",
            body=maybe_transform(
                {
                    "active": active,
                    "config": config,
                    "events": events,
                    "name": name,
                },
                hook_create_params.HookCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Hook,
        )

    def retrieve(
        self,
        hook_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Hook:
        """Returns a webhook configured in a repository.

        To get only the webhook `config`
        properties, see
        "[Get a webhook configuration for a repository](/rest/webhooks/repo-config#get-a-webhook-configuration-for-a-repository)."

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
            f"/repos/{owner}/{repo}/hooks/{hook_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Hook,
        )

    def update(
        self,
        hook_id: int,
        *,
        owner: str,
        repo: str,
        active: bool | NotGiven = NOT_GIVEN,
        add_events: builtins.list[str] | NotGiven = NOT_GIVEN,
        config: WebhookParam | NotGiven = NOT_GIVEN,
        events: builtins.list[str] | NotGiven = NOT_GIVEN,
        remove_events: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Hook:
        """Updates a webhook configured in a repository.

        If you previously had a `secret`
        set, you must provide the same `secret` or set a new `secret` or the secret will
        be removed. If you are only updating individual webhook `config` properties, use
        "[Update a webhook configuration for a repository](/rest/webhooks/repo-config#update-a-webhook-configuration-for-a-repository)."

        Args:
          active: Determines if notifications are sent when the webhook is triggered. Set to
              `true` to send notifications.

          add_events: Determines a list of events to be added to the list of events that the Hook
              triggers for.

          config: Configuration object of the webhook

          events: Determines what [events](https://docs.github.com/webhooks/event-payloads) the
              hook is triggered for. This replaces the entire array of events.

          remove_events: Determines a list of events to be removed from the list of events that the Hook
              triggers for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/hooks/{hook_id}",
            body=maybe_transform(
                {
                    "active": active,
                    "add_events": add_events,
                    "config": config,
                    "events": events,
                    "remove_events": remove_events,
                },
                hook_update_params.HookUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Hook,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HookListResponse:
        """Lists webhooks for a repository.

        `last response` may return null if there have
        not been any deliveries within 30 days.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/hooks",
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
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a webhook for an organization.

        The authenticated user must be a repository owner, or have admin access in the
        repository, to delete the webhook.

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
            f"/repos/{owner}/{repo}/hooks/{hook_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def ping(
        self,
        hook_id: int,
        *,
        owner: str,
        repo: str,
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
        return self._post(
            f"/repos/{owner}/{repo}/hooks/{hook_id}/pings",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def test(
        self,
        hook_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This will trigger the hook with the latest push to the current repository if the
        hook is subscribed to `push` events. If the hook is not subscribed to `push`
        events, the server will respond with 204 but no test POST will be generated.

        > [!NOTE] Previously `/repos/:owner/:repo/hooks/:hook_id/test`

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
        return self._post(
            f"/repos/{owner}/{repo}/hooks/{hook_id}/tests",
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
        repo: str,
        *,
        owner: str,
        active: bool | NotGiven = NOT_GIVEN,
        config: hook_create_params.Config | NotGiven = NOT_GIVEN,
        events: builtins.list[str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Hook:
        """Repositories can have multiple webhooks installed.

        Each webhook should have a
        unique `config`. Multiple webhooks can share the same `config` as long as those
        webhooks do not have any `events` that overlap.

        Args:
          active: Determines if notifications are sent when the webhook is triggered. Set to
              `true` to send notifications.

          config: Key/value pairs to provide settings for this webhook.

          events: Determines what [events](https://docs.github.com/webhooks/event-payloads) the
              hook is triggered for.

          name: Use `web` to create a webhook. Default: `web`. This parameter only accepts the
              value `web`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/hooks",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "config": config,
                    "events": events,
                    "name": name,
                },
                hook_create_params.HookCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Hook,
        )

    async def retrieve(
        self,
        hook_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Hook:
        """Returns a webhook configured in a repository.

        To get only the webhook `config`
        properties, see
        "[Get a webhook configuration for a repository](/rest/webhooks/repo-config#get-a-webhook-configuration-for-a-repository)."

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
            f"/repos/{owner}/{repo}/hooks/{hook_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Hook,
        )

    async def update(
        self,
        hook_id: int,
        *,
        owner: str,
        repo: str,
        active: bool | NotGiven = NOT_GIVEN,
        add_events: builtins.list[str] | NotGiven = NOT_GIVEN,
        config: WebhookParam | NotGiven = NOT_GIVEN,
        events: builtins.list[str] | NotGiven = NOT_GIVEN,
        remove_events: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Hook:
        """Updates a webhook configured in a repository.

        If you previously had a `secret`
        set, you must provide the same `secret` or set a new `secret` or the secret will
        be removed. If you are only updating individual webhook `config` properties, use
        "[Update a webhook configuration for a repository](/rest/webhooks/repo-config#update-a-webhook-configuration-for-a-repository)."

        Args:
          active: Determines if notifications are sent when the webhook is triggered. Set to
              `true` to send notifications.

          add_events: Determines a list of events to be added to the list of events that the Hook
              triggers for.

          config: Configuration object of the webhook

          events: Determines what [events](https://docs.github.com/webhooks/event-payloads) the
              hook is triggered for. This replaces the entire array of events.

          remove_events: Determines a list of events to be removed from the list of events that the Hook
              triggers for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/hooks/{hook_id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "add_events": add_events,
                    "config": config,
                    "events": events,
                    "remove_events": remove_events,
                },
                hook_update_params.HookUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Hook,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HookListResponse:
        """Lists webhooks for a repository.

        `last response` may return null if there have
        not been any deliveries within 30 days.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/hooks",
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
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a webhook for an organization.

        The authenticated user must be a repository owner, or have admin access in the
        repository, to delete the webhook.

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
            f"/repos/{owner}/{repo}/hooks/{hook_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def ping(
        self,
        hook_id: int,
        *,
        owner: str,
        repo: str,
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
        return await self._post(
            f"/repos/{owner}/{repo}/hooks/{hook_id}/pings",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def test(
        self,
        hook_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This will trigger the hook with the latest push to the current repository if the
        hook is subscribed to `push` events. If the hook is not subscribed to `push`
        events, the server will respond with 204 but no test POST will be generated.

        > [!NOTE] Previously `/repos/:owner/:repo/hooks/:hook_id/test`

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
        return await self._post(
            f"/repos/{owner}/{repo}/hooks/{hook_id}/tests",
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
        self.test = to_raw_response_wrapper(
            hooks.test,
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
        self.test = async_to_raw_response_wrapper(
            hooks.test,
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
        self.test = to_streamed_response_wrapper(
            hooks.test,
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
        self.test = async_to_streamed_response_wrapper(
            hooks.test,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._hooks.config)

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        return AsyncDeliveriesResourceWithStreamingResponse(self._hooks.deliveries)
