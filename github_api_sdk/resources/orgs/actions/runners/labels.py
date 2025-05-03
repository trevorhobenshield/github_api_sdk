from __future__ import annotations

import builtins
from typing import List

import httpx

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs.actions.runners import label_add_params, label_set_params
from .....types.orgs.actions.runners.label_add_response import LabelAddResponse
from .....types.orgs.actions.runners.label_list_response import LabelListResponse
from .....types.orgs.actions.runners.label_remove_all_response import LabelRemoveAllResponse
from .....types.orgs.actions.runners.label_remove_response import LabelRemoveResponse
from .....types.orgs.actions.runners.label_set_response import LabelSetResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def list(
        self,
        runner_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelListResponse:
        """
        Lists all labels for a self-hosted runner configured in an organization.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/runners/{runner_id}/labels",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelListResponse,
        )

    def add(
        self,
        runner_id: int,
        *,
        org: str,
        labels: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """
        Adds custom labels to a self-hosted runner configured in an organization.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint.

        Args:
          labels: The names of the custom labels to add to the runner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/actions/runners/{runner_id}/labels",
            body=maybe_transform({"labels": labels}, label_add_params.LabelAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelAddResponse,
        )

    def remove(
        self,
        name: str,
        *,
        org: str,
        runner_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelRemoveResponse:
        """
        Remove a custom label from a self-hosted runner configured in an organization.
        Returns the remaining labels from the runner.

        This endpoint returns a `404 Not Found` status if the custom label is not
        present on the runner.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            f"/orgs/{org}/actions/runners/{runner_id}/labels/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelRemoveResponse,
        )

    def remove_all(
        self,
        runner_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelRemoveAllResponse:
        """Remove all custom labels from a self-hosted runner configured in an
        organization.

        Returns the remaining read-only labels from the runner.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._delete(
            f"/orgs/{org}/actions/runners/{runner_id}/labels",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelRemoveAllResponse,
        )

    def set(
        self,
        runner_id: int,
        *,
        org: str,
        labels: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Remove all previous custom labels and set the new custom labels for a specific
        self-hosted runner configured in an organization.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          labels: The names of the custom labels to set for the runner. You can pass an empty
              array to remove all custom labels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._put(
            f"/orgs/{org}/actions/runners/{runner_id}/labels",
            body=maybe_transform({"labels": labels}, label_set_params.LabelSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelSetResponse,
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def list(
        self,
        runner_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelListResponse:
        """
        Lists all labels for a self-hosted runner configured in an organization.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/runners/{runner_id}/labels",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelListResponse,
        )

    async def add(
        self,
        runner_id: int,
        *,
        org: str,
        labels: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """
        Adds custom labels to a self-hosted runner configured in an organization.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint.

        Args:
          labels: The names of the custom labels to add to the runner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/actions/runners/{runner_id}/labels",
            body=await async_maybe_transform({"labels": labels}, label_add_params.LabelAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelAddResponse,
        )

    async def remove(
        self,
        name: str,
        *,
        org: str,
        runner_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelRemoveResponse:
        """
        Remove a custom label from a self-hosted runner configured in an organization.
        Returns the remaining labels from the runner.

        This endpoint returns a `404 Not Found` status if the custom label is not
        present on the runner.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            f"/orgs/{org}/actions/runners/{runner_id}/labels/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelRemoveResponse,
        )

    async def remove_all(
        self,
        runner_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelRemoveAllResponse:
        """Remove all custom labels from a self-hosted runner configured in an
        organization.

        Returns the remaining read-only labels from the runner.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._delete(
            f"/orgs/{org}/actions/runners/{runner_id}/labels",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelRemoveAllResponse,
        )

    async def set(
        self,
        runner_id: int,
        *,
        org: str,
        labels: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Remove all previous custom labels and set the new custom labels for a specific
        self-hosted runner configured in an organization.

        Authenticated users must have admin access to the organization to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          labels: The names of the custom labels to set for the runner. You can pass an empty
              array to remove all custom labels.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._put(
            f"/orgs/{org}/actions/runners/{runner_id}/labels",
            body=await async_maybe_transform({"labels": labels}, label_set_params.LabelSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelSetResponse,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.list = to_raw_response_wrapper(
            labels.list,
        )
        self.add = to_raw_response_wrapper(
            labels.add,
        )
        self.remove = to_raw_response_wrapper(
            labels.remove,
        )
        self.remove_all = to_raw_response_wrapper(
            labels.remove_all,
        )
        self.set = to_raw_response_wrapper(
            labels.set,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.list = async_to_raw_response_wrapper(
            labels.list,
        )
        self.add = async_to_raw_response_wrapper(
            labels.add,
        )
        self.remove = async_to_raw_response_wrapper(
            labels.remove,
        )
        self.remove_all = async_to_raw_response_wrapper(
            labels.remove_all,
        )
        self.set = async_to_raw_response_wrapper(
            labels.set,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.list = to_streamed_response_wrapper(
            labels.list,
        )
        self.add = to_streamed_response_wrapper(
            labels.add,
        )
        self.remove = to_streamed_response_wrapper(
            labels.remove,
        )
        self.remove_all = to_streamed_response_wrapper(
            labels.remove_all,
        )
        self.set = to_streamed_response_wrapper(
            labels.set,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.list = async_to_streamed_response_wrapper(
            labels.list,
        )
        self.add = async_to_streamed_response_wrapper(
            labels.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            labels.remove,
        )
        self.remove_all = async_to_streamed_response_wrapper(
            labels.remove_all,
        )
        self.set = async_to_streamed_response_wrapper(
            labels.set,
        )
