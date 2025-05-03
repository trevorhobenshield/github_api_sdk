from __future__ import annotations

import builtins
from typing import List, Union

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
from ....._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.users.codespaces import secret_create_or_update_params, secret_list_params
from .....types.users.codespaces.codespace_secret import CodespaceSecret
from .....types.users.codespaces.secret_get_public_key_response import SecretGetPublicKeyResponse
from .....types.users.codespaces.secret_list_response import SecretListResponse
from .repositories import (
    AsyncRepositoriesResource,
    AsyncRepositoriesResourceWithRawResponse,
    AsyncRepositoriesResourceWithStreamingResponse,
    RepositoriesResource,
    RepositoriesResourceWithRawResponse,
    RepositoriesResourceWithStreamingResponse,
)

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
    @cached_property
    def repositories(self) -> RepositoriesResource:
        return RepositoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SecretsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        secret_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceSecret:
        """
        Gets a development environment secret available to a user's codespaces without
        revealing its encrypted value.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._get(
            f"/user/codespaces/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespaceSecret,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretListResponse:
        """
        Lists all development environment secrets available for a user's codespaces
        without revealing their encrypted values.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

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
        return self._get(
            "/user/codespaces/secrets",
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
                    secret_list_params.SecretListParams,
                ),
            ),
            cast_to=SecretListResponse,
        )

    def delete(
        self,
        secret_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a development environment secret from a user's codespaces using the
        secret name. Deleting the secret will remove access from all codespaces that
        were allowed to access the secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/user/codespaces/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_or_update(
        self,
        secret_name: str,
        *,
        key_id: str,
        encrypted_value: str | NotGiven = NOT_GIVEN,
        selected_repository_ids: builtins.list[int | str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Creates or updates a development environment secret for a user's codespace with
        an encrypted value. Encrypt your secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          key_id: ID of the key you used to encrypt the secret.

          encrypted_value: Value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get the public key for the authenticated user](https://docs.github.com/rest/codespaces/secrets#get-public-key-for-the-authenticated-user)
              endpoint.

          selected_repository_ids: An array of repository ids that can access the user secret. You can manage the
              list of selected repositories using the
              [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret),
              [Set selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#set-selected-repositories-for-a-user-secret),
              and
              [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret)
              endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._put(
            f"/user/codespaces/secrets/{secret_name}",
            body=maybe_transform(
                {
                    "key_id": key_id,
                    "encrypted_value": encrypted_value,
                    "selected_repository_ids": selected_repository_ids,
                },
                secret_create_or_update_params.SecretCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def get_public_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretGetPublicKeyResponse:
        """Gets your public key, which you need to encrypt secrets.

        You need to encrypt a
        secret before you can create or update secrets.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.
        """
        return self._get(
            "/user/codespaces/secrets/public-key",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SecretGetPublicKeyResponse,
        )


class AsyncSecretsResource(AsyncAPIResource):
    @cached_property
    def repositories(self) -> AsyncRepositoriesResource:
        return AsyncRepositoriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSecretsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        secret_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodespaceSecret:
        """
        Gets a development environment secret available to a user's codespaces without
        revealing its encrypted value.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._get(
            f"/user/codespaces/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CodespaceSecret,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretListResponse:
        """
        Lists all development environment secrets available for a user's codespaces
        without revealing their encrypted values.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

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
        return await self._get(
            "/user/codespaces/secrets",
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
                    secret_list_params.SecretListParams,
                ),
            ),
            cast_to=SecretListResponse,
        )

    async def delete(
        self,
        secret_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a development environment secret from a user's codespaces using the
        secret name. Deleting the secret will remove access from all codespaces that
        were allowed to access the secret.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/user/codespaces/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_or_update(
        self,
        secret_name: str,
        *,
        key_id: str,
        encrypted_value: str | NotGiven = NOT_GIVEN,
        selected_repository_ids: builtins.list[int | str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Creates or updates a development environment secret for a user's codespace with
        an encrypted value. Encrypt your secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.

        Args:
          key_id: ID of the key you used to encrypt the secret.

          encrypted_value: Value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get the public key for the authenticated user](https://docs.github.com/rest/codespaces/secrets#get-public-key-for-the-authenticated-user)
              endpoint.

          selected_repository_ids: An array of repository ids that can access the user secret. You can manage the
              list of selected repositories using the
              [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret),
              [Set selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#set-selected-repositories-for-a-user-secret),
              and
              [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret)
              endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._put(
            f"/user/codespaces/secrets/{secret_name}",
            body=await async_maybe_transform(
                {
                    "key_id": key_id,
                    "encrypted_value": encrypted_value,
                    "selected_repository_ids": selected_repository_ids,
                },
                secret_create_or_update_params.SecretCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def get_public_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretGetPublicKeyResponse:
        """Gets your public key, which you need to encrypt secrets.

        You need to encrypt a
        secret before you can create or update secrets.

        The authenticated user must have Codespaces access to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `codespace` or
        `codespace:secrets` scope to use this endpoint.
        """
        return await self._get(
            "/user/codespaces/secrets/public-key",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SecretGetPublicKeyResponse,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.retrieve = to_raw_response_wrapper(
            secrets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            secrets.create_or_update,
        )
        self.get_public_key = to_raw_response_wrapper(
            secrets.get_public_key,
        )

    @cached_property
    def repositories(self) -> RepositoriesResourceWithRawResponse:
        return RepositoriesResourceWithRawResponse(self._secrets.repositories)


class AsyncSecretsResourceWithRawResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.retrieve = async_to_raw_response_wrapper(
            secrets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            secrets.create_or_update,
        )
        self.get_public_key = async_to_raw_response_wrapper(
            secrets.get_public_key,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithRawResponse:
        return AsyncRepositoriesResourceWithRawResponse(self._secrets.repositories)


class SecretsResourceWithStreamingResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.retrieve = to_streamed_response_wrapper(
            secrets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            secrets.create_or_update,
        )
        self.get_public_key = to_streamed_response_wrapper(
            secrets.get_public_key,
        )

    @cached_property
    def repositories(self) -> RepositoriesResourceWithStreamingResponse:
        return RepositoriesResourceWithStreamingResponse(self._secrets.repositories)


class AsyncSecretsResourceWithStreamingResponse:
    def __init__(self, secrets: AsyncSecretsResource) -> None:
        self._secrets = secrets

        self.retrieve = async_to_streamed_response_wrapper(
            secrets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            secrets.create_or_update,
        )
        self.get_public_key = async_to_streamed_response_wrapper(
            secrets.get_public_key,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self._secrets.repositories)
