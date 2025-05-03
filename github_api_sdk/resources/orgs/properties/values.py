from __future__ import annotations

import builtins
from typing import Iterable, List

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
from ....types.orgs.properties import value_list_params, value_update_params
from ....types.orgs.properties.value_list_response import ValueListResponse
from ....types.repos.properties.custom_property_value_param import CustomPropertyValueParam

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

    def update(
        self,
        org: str,
        *,
        properties: Iterable[CustomPropertyValueParam],
        repository_names: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create new or update existing custom property values for repositories in a batch
        that belong to an organization. Each target repository will have its custom
        property values updated to match the values provided in the request.

        A maximum of 30 repositories can be updated in a single request.

        Using a value of `null` for a custom property will remove or 'unset' the
        property value from the repository.

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permission of
          `custom_properties_org_values_editor` in the organization.

        Args:
          properties: List of custom property names and associated values to apply to the
              repositories.

          repository_names: The names of repositories that the custom property values will be applied to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/orgs/{org}/properties/values",
            body=maybe_transform(
                {
                    "properties": properties,
                    "repository_names": repository_names,
                },
                value_update_params.ValueUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        repository_query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueListResponse:
        """
        Lists organization repositories with all of their custom property values.
        Organization members can read these properties.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          repository_query: Finds repositories in the organization with a query containing one or more
              search keywords and qualifiers. Qualifiers allow you to limit your search to
              specific areas of GitHub. The REST API supports the same qualifiers as the web
              interface for GitHub. To learn more about the format of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching for repositories](https://docs.github.com/articles/searching-for-repositories/)"
              for a detailed list of qualifiers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/properties/values",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "repository_query": repository_query,
                    },
                    value_list_params.ValueListParams,
                ),
            ),
            cast_to=ValueListResponse,
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

    async def update(
        self,
        org: str,
        *,
        properties: Iterable[CustomPropertyValueParam],
        repository_names: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Create new or update existing custom property values for repositories in a batch
        that belong to an organization. Each target repository will have its custom
        property values updated to match the values provided in the request.

        A maximum of 30 repositories can be updated in a single request.

        Using a value of `null` for a custom property will remove or 'unset' the
        property value from the repository.

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permission of
          `custom_properties_org_values_editor` in the organization.

        Args:
          properties: List of custom property names and associated values to apply to the
              repositories.

          repository_names: The names of repositories that the custom property values will be applied to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/orgs/{org}/properties/values",
            body=await async_maybe_transform(
                {
                    "properties": properties,
                    "repository_names": repository_names,
                },
                value_update_params.ValueUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list(
        self,
        org: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        repository_query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ValueListResponse:
        """
        Lists organization repositories with all of their custom property values.
        Organization members can read these properties.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          repository_query: Finds repositories in the organization with a query containing one or more
              search keywords and qualifiers. Qualifiers allow you to limit your search to
              specific areas of GitHub. The REST API supports the same qualifiers as the web
              interface for GitHub. To learn more about the format of the query, see
              [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query).
              See
              "[Searching for repositories](https://docs.github.com/articles/searching-for-repositories/)"
              for a detailed list of qualifiers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/properties/values",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "repository_query": repository_query,
                    },
                    value_list_params.ValueListParams,
                ),
            ),
            cast_to=ValueListResponse,
        )


class ValuesResourceWithRawResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.update = to_raw_response_wrapper(
            values.update,
        )
        self.list = to_raw_response_wrapper(
            values.list,
        )


class AsyncValuesResourceWithRawResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.update = async_to_raw_response_wrapper(
            values.update,
        )
        self.list = async_to_raw_response_wrapper(
            values.list,
        )


class ValuesResourceWithStreamingResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.update = to_streamed_response_wrapper(
            values.update,
        )
        self.list = to_streamed_response_wrapper(
            values.list,
        )


class AsyncValuesResourceWithStreamingResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.update = async_to_streamed_response_wrapper(
            values.update,
        )
        self.list = async_to_streamed_response_wrapper(
            values.list,
        )
