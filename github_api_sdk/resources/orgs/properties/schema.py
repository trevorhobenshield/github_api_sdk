from __future__ import annotations

import builtins
from typing import Iterable, List, Optional, Union

import httpx
from typing_extensions import Literal

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
from ....types.orgs.properties import schema_create_or_update_params, schema_update_params
from ....types.orgs.properties.custom_property import CustomProperty
from ....types.orgs.properties.custom_property_param import CustomPropertyParam
from ....types.orgs.properties.schema_list_response import SchemaListResponse
from ....types.orgs.properties.schema_update_response import SchemaUpdateResponse

__all__ = ["SchemaResource", "AsyncSchemaResource"]


class SchemaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SchemaResourceWithStreamingResponse(self)

    def retrieve(
        self,
        custom_property_name: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomProperty:
        """Gets a custom property that is defined for an organization.

        Organization members
        can read these properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not custom_property_name:
            raise ValueError(f"Expected a non-empty value for `custom_property_name` but received {custom_property_name!r}")
        return self._get(
            f"/orgs/{org}/properties/schema/{custom_property_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CustomProperty,
        )

    def update(
        self,
        org: str,
        *,
        properties: Iterable[CustomPropertyParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaUpdateResponse:
        """
        Creates new or updates existing custom properties defined for an organization in
        a batch.

        If the property already exists, the existing property will be replaced with the
        new values. Missing optional values will fall back to default values, previous
        values will be overwritten. E.g. if a property exists with
        `values_editable_by: org_and_repo_actors` and it's updated without specifying
        `values_editable_by`, it will be updated to default value `org_actors`.

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permission of
          `custom_properties_org_definitions_manager` in the organization.

        Args:
          properties: The array of custom properties to create or update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._patch(
            f"/orgs/{org}/properties/schema",
            body=maybe_transform({"properties": properties}, schema_update_params.SchemaUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaUpdateResponse,
        )

    def list(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaListResponse:
        """Gets all custom properties defined for an organization.

        Organization members can
        read these properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/properties/schema",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaListResponse,
        )

    def delete(
        self,
        custom_property_name: str,
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
        Removes a custom property that is defined for an organization.

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permission of
          `custom_properties_org_definitions_manager` in the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not custom_property_name:
            raise ValueError(f"Expected a non-empty value for `custom_property_name` but received {custom_property_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/properties/schema/{custom_property_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_or_update(
        self,
        custom_property_name: str,
        *,
        org: str,
        value_type: Literal["string", "single_select", "multi_select", "true_false"],
        allowed_values: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        default_value: str | builtins.list[str] | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        required: bool | NotGiven = NOT_GIVEN,
        values_editable_by: Literal["org_actors", "org_and_repo_actors"] | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomProperty:
        """
        Creates a new or updates an existing custom property that is defined for an
        organization.

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permission of
          `custom_properties_org_definitions_manager` in the organization.

        Args:
          value_type: The type of the value for the property

          allowed_values: An ordered list of the allowed values of the property. The property can have up
              to 200 allowed values.

          default_value: Default value of the property

          description: Short description of the property

          required: Whether the property is required.

          values_editable_by: Who can edit the values of the property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not custom_property_name:
            raise ValueError(f"Expected a non-empty value for `custom_property_name` but received {custom_property_name!r}")
        return self._put(
            f"/orgs/{org}/properties/schema/{custom_property_name}",
            body=maybe_transform(
                {
                    "value_type": value_type,
                    "allowed_values": allowed_values,
                    "default_value": default_value,
                    "description": description,
                    "required": required,
                    "values_editable_by": values_editable_by,
                },
                schema_create_or_update_params.SchemaCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CustomProperty,
        )


class AsyncSchemaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSchemaResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        custom_property_name: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomProperty:
        """Gets a custom property that is defined for an organization.

        Organization members
        can read these properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not custom_property_name:
            raise ValueError(f"Expected a non-empty value for `custom_property_name` but received {custom_property_name!r}")
        return await self._get(
            f"/orgs/{org}/properties/schema/{custom_property_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CustomProperty,
        )

    async def update(
        self,
        org: str,
        *,
        properties: Iterable[CustomPropertyParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaUpdateResponse:
        """
        Creates new or updates existing custom properties defined for an organization in
        a batch.

        If the property already exists, the existing property will be replaced with the
        new values. Missing optional values will fall back to default values, previous
        values will be overwritten. E.g. if a property exists with
        `values_editable_by: org_and_repo_actors` and it's updated without specifying
        `values_editable_by`, it will be updated to default value `org_actors`.

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permission of
          `custom_properties_org_definitions_manager` in the organization.

        Args:
          properties: The array of custom properties to create or update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._patch(
            f"/orgs/{org}/properties/schema",
            body=await async_maybe_transform({"properties": properties}, schema_update_params.SchemaUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaUpdateResponse,
        )

    async def list(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SchemaListResponse:
        """Gets all custom properties defined for an organization.

        Organization members can
        read these properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/properties/schema",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SchemaListResponse,
        )

    async def delete(
        self,
        custom_property_name: str,
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
        Removes a custom property that is defined for an organization.

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permission of
          `custom_properties_org_definitions_manager` in the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not custom_property_name:
            raise ValueError(f"Expected a non-empty value for `custom_property_name` but received {custom_property_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/properties/schema/{custom_property_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_or_update(
        self,
        custom_property_name: str,
        *,
        org: str,
        value_type: Literal["string", "single_select", "multi_select", "true_false"],
        allowed_values: builtins.list[str] | None | NotGiven = NOT_GIVEN,
        default_value: str | builtins.list[str] | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        required: bool | NotGiven = NOT_GIVEN,
        values_editable_by: Literal["org_actors", "org_and_repo_actors"] | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomProperty:
        """
        Creates a new or updates an existing custom property that is defined for an
        organization.

        To use this endpoint, the authenticated user must be one of:

        - An administrator for the organization.
        - A user, or a user on a team, with the fine-grained permission of
          `custom_properties_org_definitions_manager` in the organization.

        Args:
          value_type: The type of the value for the property

          allowed_values: An ordered list of the allowed values of the property. The property can have up
              to 200 allowed values.

          default_value: Default value of the property

          description: Short description of the property

          required: Whether the property is required.

          values_editable_by: Who can edit the values of the property

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not custom_property_name:
            raise ValueError(f"Expected a non-empty value for `custom_property_name` but received {custom_property_name!r}")
        return await self._put(
            f"/orgs/{org}/properties/schema/{custom_property_name}",
            body=await async_maybe_transform(
                {
                    "value_type": value_type,
                    "allowed_values": allowed_values,
                    "default_value": default_value,
                    "description": description,
                    "required": required,
                    "values_editable_by": values_editable_by,
                },
                schema_create_or_update_params.SchemaCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CustomProperty,
        )


class SchemaResourceWithRawResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.retrieve = to_raw_response_wrapper(
            schema.retrieve,
        )
        self.update = to_raw_response_wrapper(
            schema.update,
        )
        self.list = to_raw_response_wrapper(
            schema.list,
        )
        self.delete = to_raw_response_wrapper(
            schema.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            schema.create_or_update,
        )


class AsyncSchemaResourceWithRawResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.retrieve = async_to_raw_response_wrapper(
            schema.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            schema.update,
        )
        self.list = async_to_raw_response_wrapper(
            schema.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schema.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            schema.create_or_update,
        )


class SchemaResourceWithStreamingResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.retrieve = to_streamed_response_wrapper(
            schema.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            schema.update,
        )
        self.list = to_streamed_response_wrapper(
            schema.list,
        )
        self.delete = to_streamed_response_wrapper(
            schema.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            schema.create_or_update,
        )


class AsyncSchemaResourceWithStreamingResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.retrieve = async_to_streamed_response_wrapper(
            schema.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            schema.update,
        )
        self.list = async_to_streamed_response_wrapper(
            schema.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schema.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            schema.create_or_update,
        )
