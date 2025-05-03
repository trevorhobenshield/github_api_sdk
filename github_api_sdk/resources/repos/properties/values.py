from __future__ import annotations

from typing import Iterable

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
from ....types.repos.properties import value_update_or_create_params
from ....types.repos.properties.custom_property_value_param import CustomPropertyValueParam
from ....types.repos.properties.value_get_all_response import ValueGetAllResponse

__all__ = ["ValuesResource", "AsyncValuesResource"]


class ValuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ValuesResourceWithStreamingResponse(self)

    def get_all(
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
    ) -> ValueGetAllResponse:
        """Gets all custom property values that are set for a repository.

        Users with read
        access to the repository can use this endpoint.

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
            f"/repos/{owner}/{repo}/properties/values",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ValueGetAllResponse,
        )

    def update_or_create(
        self,
        repo: str,
        *,
        owner: str,
        properties: Iterable[CustomPropertyValueParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create new or update existing custom property values for a repository.

        Using a
        value of `null` for a custom property will remove or 'unset' the property value
        from the repository.

        Repository admins and other users with the repository-level "edit custom
        property values" fine-grained permission can use this endpoint.

        Args:
          properties: A list of custom property names and associated values to apply to the
              repositories.

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
        return self._patch(
            f"/repos/{owner}/{repo}/properties/values",
            body=maybe_transform({"properties": properties}, value_update_or_create_params.ValueUpdateOrCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncValuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncValuesResourceWithStreamingResponse(self)

    async def get_all(
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
    ) -> ValueGetAllResponse:
        """Gets all custom property values that are set for a repository.

        Users with read
        access to the repository can use this endpoint.

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
            f"/repos/{owner}/{repo}/properties/values",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ValueGetAllResponse,
        )

    async def update_or_create(
        self,
        repo: str,
        *,
        owner: str,
        properties: Iterable[CustomPropertyValueParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create new or update existing custom property values for a repository.

        Using a
        value of `null` for a custom property will remove or 'unset' the property value
        from the repository.

        Repository admins and other users with the repository-level "edit custom
        property values" fine-grained permission can use this endpoint.

        Args:
          properties: A list of custom property names and associated values to apply to the
              repositories.

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
        return await self._patch(
            f"/repos/{owner}/{repo}/properties/values",
            body=await async_maybe_transform({"properties": properties}, value_update_or_create_params.ValueUpdateOrCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ValuesResourceWithRawResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.get_all = to_raw_response_wrapper(
            values.get_all,
        )
        self.update_or_create = to_raw_response_wrapper(
            values.update_or_create,
        )


class AsyncValuesResourceWithRawResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.get_all = async_to_raw_response_wrapper(
            values.get_all,
        )
        self.update_or_create = async_to_raw_response_wrapper(
            values.update_or_create,
        )


class ValuesResourceWithStreamingResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.get_all = to_streamed_response_wrapper(
            values.get_all,
        )
        self.update_or_create = to_streamed_response_wrapper(
            values.update_or_create,
        )


class AsyncValuesResourceWithStreamingResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.get_all = async_to_streamed_response_wrapper(
            values.get_all,
        )
        self.update_or_create = async_to_streamed_response_wrapper(
            values.update_or_create,
        )
