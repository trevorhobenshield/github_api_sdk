from __future__ import annotations

from typing import Iterable, Optional

import httpx
from typing_extensions import Literal

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.orgs import private_registry_create_params, private_registry_list_params, private_registry_update_params
from ...types.orgs.org_private_registry_configuration import OrgPrivateRegistryConfiguration
from ...types.orgs.private_registry_create_response import PrivateRegistryCreateResponse
from ...types.orgs.private_registry_get_public_key_response import PrivateRegistryGetPublicKeyResponse
from ...types.orgs.private_registry_list_response import PrivateRegistryListResponse

__all__ = ["PrivateRegistriesResource", "AsyncPrivateRegistriesResource"]


class PrivateRegistriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrivateRegistriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PrivateRegistriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrivateRegistriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PrivateRegistriesResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        encrypted_value: str,
        key_id: str,
        registry_type: Literal["maven_repository"],
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        username: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateRegistryCreateResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Creates a private registry configuration with an encrypted value for an
        organization. Encrypt your secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          encrypted_value: The value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get private registries public key for an organization](https://docs.github.com/rest/private-registries/organization-configurations#get-private-registries-public-key-for-an-organization)
              endpoint.

          key_id: The ID of the key you used to encrypt the secret.

          registry_type: The registry type.

          visibility: Which type of organization repositories have access to the private registry.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the private registry.

          selected_repository_ids: An array of repository IDs that can access the organization private registry.
              You can only provide a list of repository IDs when `visibility` is set to
              `selected`. You can manage the list of selected repositories using the
              [Update a private registry for an organization](https://docs.github.com/rest/private-registries/organization-configurations#update-a-private-registry-for-an-organization)
              endpoint. This field should be omitted if `visibility` is set to `all` or
              `private`.

          username: The username to use when authenticating with the private registry. This field
              should be omitted if the private registry does not require a username for
              authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/private-registries",
            body=maybe_transform(
                {
                    "encrypted_value": encrypted_value,
                    "key_id": key_id,
                    "registry_type": registry_type,
                    "visibility": visibility,
                    "selected_repository_ids": selected_repository_ids,
                    "username": username,
                },
                private_registry_create_params.PrivateRegistryCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PrivateRegistryCreateResponse,
        )

    def retrieve(
        self,
        secret_name: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgPrivateRegistryConfiguration:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Get the configuration of a single private registry defined for an organization,
        omitting its encrypted value.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._get(
            f"/orgs/{org}/private-registries/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgPrivateRegistryConfiguration,
        )

    def update(
        self,
        secret_name: str,
        *,
        org: str,
        encrypted_value: str | NotGiven = NOT_GIVEN,
        key_id: str | NotGiven = NOT_GIVEN,
        registry_type: Literal["maven_repository"] | NotGiven = NOT_GIVEN,
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        username: str | None | NotGiven = NOT_GIVEN,
        visibility: Literal["all", "private", "selected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Updates a private registry configuration with an encrypted value for an
        organization. Encrypt your secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          encrypted_value: The value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get private registries public key for an organization](https://docs.github.com/rest/private-registries/organization-configurations#get-private-registries-public-key-for-an-organization)
              endpoint.

          key_id: The ID of the key you used to encrypt the secret.

          registry_type: The registry type.

          selected_repository_ids: An array of repository IDs that can access the organization private registry.
              You can only provide a list of repository IDs when `visibility` is set to
              `selected`. This field should be omitted if `visibility` is set to `all` or
              `private`.

          username: The username to use when authenticating with the private registry. This field
              should be omitted if the private registry does not require a username for
              authentication.

          visibility: Which type of organization repositories have access to the private registry.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the private registry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/orgs/{org}/private-registries/{secret_name}",
            body=maybe_transform(
                {
                    "encrypted_value": encrypted_value,
                    "key_id": key_id,
                    "registry_type": registry_type,
                    "selected_repository_ids": selected_repository_ids,
                    "username": username,
                    "visibility": visibility,
                },
                private_registry_update_params.PrivateRegistryUpdateParams,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateRegistryListResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Lists all private registry configurations available at the organization-level
        without revealing their encrypted values.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

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
            f"/orgs/{org}/private-registries",
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
                    private_registry_list_params.PrivateRegistryListParams,
                ),
            ),
            cast_to=PrivateRegistryListResponse,
        )

    def delete(
        self,
        secret_name: str,
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
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Delete a private registry configuration at the organization-level.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/private-registries/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_public_key(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateRegistryGetPublicKeyResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Gets the org public key, which is needed to encrypt private registry secrets.
        You need to encrypt a secret before you can create or update secrets.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/private-registries/public-key",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PrivateRegistryGetPublicKeyResponse,
        )


class AsyncPrivateRegistriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrivateRegistriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrivateRegistriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrivateRegistriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPrivateRegistriesResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        encrypted_value: str,
        key_id: str,
        registry_type: Literal["maven_repository"],
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        username: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateRegistryCreateResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Creates a private registry configuration with an encrypted value for an
        organization. Encrypt your secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          encrypted_value: The value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get private registries public key for an organization](https://docs.github.com/rest/private-registries/organization-configurations#get-private-registries-public-key-for-an-organization)
              endpoint.

          key_id: The ID of the key you used to encrypt the secret.

          registry_type: The registry type.

          visibility: Which type of organization repositories have access to the private registry.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the private registry.

          selected_repository_ids: An array of repository IDs that can access the organization private registry.
              You can only provide a list of repository IDs when `visibility` is set to
              `selected`. You can manage the list of selected repositories using the
              [Update a private registry for an organization](https://docs.github.com/rest/private-registries/organization-configurations#update-a-private-registry-for-an-organization)
              endpoint. This field should be omitted if `visibility` is set to `all` or
              `private`.

          username: The username to use when authenticating with the private registry. This field
              should be omitted if the private registry does not require a username for
              authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/private-registries",
            body=await async_maybe_transform(
                {
                    "encrypted_value": encrypted_value,
                    "key_id": key_id,
                    "registry_type": registry_type,
                    "visibility": visibility,
                    "selected_repository_ids": selected_repository_ids,
                    "username": username,
                },
                private_registry_create_params.PrivateRegistryCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PrivateRegistryCreateResponse,
        )

    async def retrieve(
        self,
        secret_name: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgPrivateRegistryConfiguration:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Get the configuration of a single private registry defined for an organization,
        omitting its encrypted value.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._get(
            f"/orgs/{org}/private-registries/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgPrivateRegistryConfiguration,
        )

    async def update(
        self,
        secret_name: str,
        *,
        org: str,
        encrypted_value: str | NotGiven = NOT_GIVEN,
        key_id: str | NotGiven = NOT_GIVEN,
        registry_type: Literal["maven_repository"] | NotGiven = NOT_GIVEN,
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        username: str | None | NotGiven = NOT_GIVEN,
        visibility: Literal["all", "private", "selected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Updates a private registry configuration with an encrypted value for an
        organization. Encrypt your secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          encrypted_value: The value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get private registries public key for an organization](https://docs.github.com/rest/private-registries/organization-configurations#get-private-registries-public-key-for-an-organization)
              endpoint.

          key_id: The ID of the key you used to encrypt the secret.

          registry_type: The registry type.

          selected_repository_ids: An array of repository IDs that can access the organization private registry.
              You can only provide a list of repository IDs when `visibility` is set to
              `selected`. This field should be omitted if `visibility` is set to `all` or
              `private`.

          username: The username to use when authenticating with the private registry. This field
              should be omitted if the private registry does not require a username for
              authentication.

          visibility: Which type of organization repositories have access to the private registry.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the private registry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/orgs/{org}/private-registries/{secret_name}",
            body=await async_maybe_transform(
                {
                    "encrypted_value": encrypted_value,
                    "key_id": key_id,
                    "registry_type": registry_type,
                    "selected_repository_ids": selected_repository_ids,
                    "username": username,
                    "visibility": visibility,
                },
                private_registry_update_params.PrivateRegistryUpdateParams,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateRegistryListResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Lists all private registry configurations available at the organization-level
        without revealing their encrypted values.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

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
            f"/orgs/{org}/private-registries",
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
                    private_registry_list_params.PrivateRegistryListParams,
                ),
            ),
            cast_to=PrivateRegistryListResponse,
        )

    async def delete(
        self,
        secret_name: str,
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
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Delete a private registry configuration at the organization-level.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/private-registries/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_public_key(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrivateRegistryGetPublicKeyResponse:
        """
        > [!NOTE] This endpoint is in public preview and is subject to change.

        Gets the org public key, which is needed to encrypt private registry secrets.
        You need to encrypt a secret before you can create or update secrets.

        OAuth tokens and personal access tokens (classic) need the `admin:org` scope to
        use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/private-registries/public-key",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PrivateRegistryGetPublicKeyResponse,
        )


class PrivateRegistriesResourceWithRawResponse:
    def __init__(self, private_registries: PrivateRegistriesResource) -> None:
        self._private_registries = private_registries

        self.create = to_raw_response_wrapper(
            private_registries.create,
        )
        self.retrieve = to_raw_response_wrapper(
            private_registries.retrieve,
        )
        self.update = to_raw_response_wrapper(
            private_registries.update,
        )
        self.list = to_raw_response_wrapper(
            private_registries.list,
        )
        self.delete = to_raw_response_wrapper(
            private_registries.delete,
        )
        self.get_public_key = to_raw_response_wrapper(
            private_registries.get_public_key,
        )


class AsyncPrivateRegistriesResourceWithRawResponse:
    def __init__(self, private_registries: AsyncPrivateRegistriesResource) -> None:
        self._private_registries = private_registries

        self.create = async_to_raw_response_wrapper(
            private_registries.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            private_registries.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            private_registries.update,
        )
        self.list = async_to_raw_response_wrapper(
            private_registries.list,
        )
        self.delete = async_to_raw_response_wrapper(
            private_registries.delete,
        )
        self.get_public_key = async_to_raw_response_wrapper(
            private_registries.get_public_key,
        )


class PrivateRegistriesResourceWithStreamingResponse:
    def __init__(self, private_registries: PrivateRegistriesResource) -> None:
        self._private_registries = private_registries

        self.create = to_streamed_response_wrapper(
            private_registries.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            private_registries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            private_registries.update,
        )
        self.list = to_streamed_response_wrapper(
            private_registries.list,
        )
        self.delete = to_streamed_response_wrapper(
            private_registries.delete,
        )
        self.get_public_key = to_streamed_response_wrapper(
            private_registries.get_public_key,
        )


class AsyncPrivateRegistriesResourceWithStreamingResponse:
    def __init__(self, private_registries: AsyncPrivateRegistriesResource) -> None:
        self._private_registries = private_registries

        self.create = async_to_streamed_response_wrapper(
            private_registries.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            private_registries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            private_registries.update,
        )
        self.list = async_to_streamed_response_wrapper(
            private_registries.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            private_registries.delete,
        )
        self.get_public_key = async_to_streamed_response_wrapper(
            private_registries.get_public_key,
        )
