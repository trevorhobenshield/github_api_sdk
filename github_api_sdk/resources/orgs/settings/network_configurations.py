from __future__ import annotations

import builtins
from typing import List

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
from ....types.orgs.settings import (
    network_configuration_create_params,
    network_configuration_list_params,
    network_configuration_update_params,
)
from ....types.orgs.settings.network_configuration import NetworkConfiguration
from ....types.orgs.settings.network_configuration_list_response import NetworkConfigurationListResponse

__all__ = ["NetworkConfigurationsResource", "AsyncNetworkConfigurationsResource"]


class NetworkConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return NetworkConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return NetworkConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        name: str,
        network_settings_ids: builtins.list[str],
        compute_service: Literal["none", "actions"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkConfiguration:
        """
        Creates a hosted compute network configuration for an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `write:network_configurations` scope to use this endpoint.

        Args:
          name: Name of the network configuration. Must be between 1 and 100 characters and may
              only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '\\__'.

          network_settings_ids: The identifier of the network settings to use for the network configuration.
              Exactly one network settings must be specified.

          compute_service: The hosted compute service to use for the network configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/settings/network-configurations",
            body=maybe_transform(
                {
                    "name": name,
                    "network_settings_ids": network_settings_ids,
                    "compute_service": compute_service,
                },
                network_configuration_create_params.NetworkConfigurationCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NetworkConfiguration,
        )

    def retrieve(
        self,
        network_configuration_id: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkConfiguration:
        """
        Gets a hosted compute network configuration configured in an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `read:network_configurations` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not network_configuration_id:
            raise ValueError(f"Expected a non-empty value for `network_configuration_id` but received {network_configuration_id!r}")
        return self._get(
            f"/orgs/{org}/settings/network-configurations/{network_configuration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NetworkConfiguration,
        )

    def update(
        self,
        network_configuration_id: str,
        *,
        org: str,
        compute_service: Literal["none", "actions"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        network_settings_ids: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkConfiguration:
        """
        Updates a hosted compute network configuration for an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `write:network_configurations` scope to use this endpoint.

        Args:
          compute_service: The hosted compute service to use for the network configuration.

          name: Name of the network configuration. Must be between 1 and 100 characters and may
              only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '\\__'.

          network_settings_ids: The identifier of the network settings to use for the network configuration.
              Exactly one network settings must be specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not network_configuration_id:
            raise ValueError(f"Expected a non-empty value for `network_configuration_id` but received {network_configuration_id!r}")
        return self._patch(
            f"/orgs/{org}/settings/network-configurations/{network_configuration_id}",
            body=maybe_transform(
                {
                    "compute_service": compute_service,
                    "name": name,
                    "network_settings_ids": network_settings_ids,
                },
                network_configuration_update_params.NetworkConfigurationUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NetworkConfiguration,
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
    ) -> NetworkConfigurationListResponse:
        """
        Lists all hosted compute network configurations configured in an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `read:network_configurations` scope to use this endpoint.

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
            f"/orgs/{org}/settings/network-configurations",
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
                    network_configuration_list_params.NetworkConfigurationListParams,
                ),
            ),
            cast_to=NetworkConfigurationListResponse,
        )

    def delete(
        self,
        network_configuration_id: str,
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
        Deletes a hosted compute network configuration from an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `write:network_configurations` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not network_configuration_id:
            raise ValueError(f"Expected a non-empty value for `network_configuration_id` but received {network_configuration_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/settings/network-configurations/{network_configuration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncNetworkConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncNetworkConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        name: str,
        network_settings_ids: builtins.list[str],
        compute_service: Literal["none", "actions"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkConfiguration:
        """
        Creates a hosted compute network configuration for an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `write:network_configurations` scope to use this endpoint.

        Args:
          name: Name of the network configuration. Must be between 1 and 100 characters and may
              only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '\\__'.

          network_settings_ids: The identifier of the network settings to use for the network configuration.
              Exactly one network settings must be specified.

          compute_service: The hosted compute service to use for the network configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/settings/network-configurations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "network_settings_ids": network_settings_ids,
                    "compute_service": compute_service,
                },
                network_configuration_create_params.NetworkConfigurationCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NetworkConfiguration,
        )

    async def retrieve(
        self,
        network_configuration_id: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkConfiguration:
        """
        Gets a hosted compute network configuration configured in an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `read:network_configurations` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not network_configuration_id:
            raise ValueError(f"Expected a non-empty value for `network_configuration_id` but received {network_configuration_id!r}")
        return await self._get(
            f"/orgs/{org}/settings/network-configurations/{network_configuration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NetworkConfiguration,
        )

    async def update(
        self,
        network_configuration_id: str,
        *,
        org: str,
        compute_service: Literal["none", "actions"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        network_settings_ids: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkConfiguration:
        """
        Updates a hosted compute network configuration for an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `write:network_configurations` scope to use this endpoint.

        Args:
          compute_service: The hosted compute service to use for the network configuration.

          name: Name of the network configuration. Must be between 1 and 100 characters and may
              only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '\\__'.

          network_settings_ids: The identifier of the network settings to use for the network configuration.
              Exactly one network settings must be specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not network_configuration_id:
            raise ValueError(f"Expected a non-empty value for `network_configuration_id` but received {network_configuration_id!r}")
        return await self._patch(
            f"/orgs/{org}/settings/network-configurations/{network_configuration_id}",
            body=await async_maybe_transform(
                {
                    "compute_service": compute_service,
                    "name": name,
                    "network_settings_ids": network_settings_ids,
                },
                network_configuration_update_params.NetworkConfigurationUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NetworkConfiguration,
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
    ) -> NetworkConfigurationListResponse:
        """
        Lists all hosted compute network configurations configured in an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `read:network_configurations` scope to use this endpoint.

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
            f"/orgs/{org}/settings/network-configurations",
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
                    network_configuration_list_params.NetworkConfigurationListParams,
                ),
            ),
            cast_to=NetworkConfigurationListResponse,
        )

    async def delete(
        self,
        network_configuration_id: str,
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
        Deletes a hosted compute network configuration from an organization.

        OAuth app tokens and personal access tokens (classic) need the
        `write:network_configurations` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not network_configuration_id:
            raise ValueError(f"Expected a non-empty value for `network_configuration_id` but received {network_configuration_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/settings/network-configurations/{network_configuration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class NetworkConfigurationsResourceWithRawResponse:
    def __init__(self, network_configurations: NetworkConfigurationsResource) -> None:
        self._network_configurations = network_configurations

        self.create = to_raw_response_wrapper(
            network_configurations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            network_configurations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            network_configurations.update,
        )
        self.list = to_raw_response_wrapper(
            network_configurations.list,
        )
        self.delete = to_raw_response_wrapper(
            network_configurations.delete,
        )


class AsyncNetworkConfigurationsResourceWithRawResponse:
    def __init__(self, network_configurations: AsyncNetworkConfigurationsResource) -> None:
        self._network_configurations = network_configurations

        self.create = async_to_raw_response_wrapper(
            network_configurations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            network_configurations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            network_configurations.update,
        )
        self.list = async_to_raw_response_wrapper(
            network_configurations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            network_configurations.delete,
        )


class NetworkConfigurationsResourceWithStreamingResponse:
    def __init__(self, network_configurations: NetworkConfigurationsResource) -> None:
        self._network_configurations = network_configurations

        self.create = to_streamed_response_wrapper(
            network_configurations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            network_configurations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            network_configurations.update,
        )
        self.list = to_streamed_response_wrapper(
            network_configurations.list,
        )
        self.delete = to_streamed_response_wrapper(
            network_configurations.delete,
        )


class AsyncNetworkConfigurationsResourceWithStreamingResponse:
    def __init__(self, network_configurations: AsyncNetworkConfigurationsResource) -> None:
        self._network_configurations = network_configurations

        self.create = async_to_streamed_response_wrapper(
            network_configurations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            network_configurations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            network_configurations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            network_configurations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            network_configurations.delete,
        )
