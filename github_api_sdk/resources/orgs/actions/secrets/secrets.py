from __future__ import annotations

from typing import Iterable

import httpx
from typing_extensions import Literal

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
from .....types.orgs.actions import secret_create_or_update_params, secret_list_params
from .....types.orgs.actions.organization_secret import OrganizationSecret
from .....types.orgs.actions.public_key import PublicKey
from .....types.orgs.actions.secret_list_response import SecretListResponse
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
    ) -> SecretListResponse:
        """
        Lists all secrets available in an organization without revealing their encrypted
        values.

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

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
            f"/orgs/{org}/actions/secrets",
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
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a secret in an organization using the secret name.

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

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
            f"/orgs/{org}/actions/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_or_update(
        self,
        secret_name: str,
        *,
        org: str,
        encrypted_value: str,
        key_id: str,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Creates or updates an organization secret with an encrypted value.

        Encrypt your
        secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          encrypted_value: Value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get an organization public key](https://docs.github.com/rest/actions/secrets#get-an-organization-public-key)
              endpoint.

          key_id: ID of the key you used to encrypt the secret.

          visibility: Which type of organization repositories have access to the organization secret.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the secret.

          selected_repository_ids: An array of repository ids that can access the organization secret. You can only
              provide a list of repository ids when the `visibility` is set to `selected`. You
              can manage the list of selected repositories using the
              [List selected repositories for an organization secret](https://docs.github.com/rest/actions/secrets#list-selected-repositories-for-an-organization-secret),
              [Set selected repositories for an organization secret](https://docs.github.com/rest/actions/secrets#set-selected-repositories-for-an-organization-secret),
              and
              [Remove selected repository from an organization secret](https://docs.github.com/rest/actions/secrets#remove-selected-repository-from-an-organization-secret)
              endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._put(
            f"/orgs/{org}/actions/secrets/{secret_name}",
            body=maybe_transform(
                {
                    "encrypted_value": encrypted_value,
                    "key_id": key_id,
                    "visibility": visibility,
                    "selected_repository_ids": selected_repository_ids,
                },
                secret_create_or_update_params.SecretCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def get(
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
    ) -> OrganizationSecret:
        """
        Gets a single organization secret without revealing its encrypted value.

        The authenticated user must have collaborator access to a repository to create,
        update, or read secrets

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

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
            f"/orgs/{org}/actions/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationSecret,
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
    ) -> PublicKey:
        """Gets your public key, which you need to encrypt secrets.

        You need to encrypt a
        secret before you can create or update secrets.

        The authenticated user must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/secrets/public-key",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PublicKey,
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
    ) -> SecretListResponse:
        """
        Lists all secrets available in an organization without revealing their encrypted
        values.

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

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
            f"/orgs/{org}/actions/secrets",
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
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a secret in an organization using the secret name.

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

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
            f"/orgs/{org}/actions/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_or_update(
        self,
        secret_name: str,
        *,
        org: str,
        encrypted_value: str,
        key_id: str,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Creates or updates an organization secret with an encrypted value.

        Encrypt your
        secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        Authenticated users must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          encrypted_value: Value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get an organization public key](https://docs.github.com/rest/actions/secrets#get-an-organization-public-key)
              endpoint.

          key_id: ID of the key you used to encrypt the secret.

          visibility: Which type of organization repositories have access to the organization secret.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the secret.

          selected_repository_ids: An array of repository ids that can access the organization secret. You can only
              provide a list of repository ids when the `visibility` is set to `selected`. You
              can manage the list of selected repositories using the
              [List selected repositories for an organization secret](https://docs.github.com/rest/actions/secrets#list-selected-repositories-for-an-organization-secret),
              [Set selected repositories for an organization secret](https://docs.github.com/rest/actions/secrets#set-selected-repositories-for-an-organization-secret),
              and
              [Remove selected repository from an organization secret](https://docs.github.com/rest/actions/secrets#remove-selected-repository-from-an-organization-secret)
              endpoints.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._put(
            f"/orgs/{org}/actions/secrets/{secret_name}",
            body=await async_maybe_transform(
                {
                    "encrypted_value": encrypted_value,
                    "key_id": key_id,
                    "visibility": visibility,
                    "selected_repository_ids": selected_repository_ids,
                },
                secret_create_or_update_params.SecretCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def get(
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
    ) -> OrganizationSecret:
        """
        Gets a single organization secret without revealing its encrypted value.

        The authenticated user must have collaborator access to a repository to create,
        update, or read secrets

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

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
            f"/orgs/{org}/actions/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationSecret,
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
    ) -> PublicKey:
        """Gets your public key, which you need to encrypt secrets.

        You need to encrypt a
        secret before you can create or update secrets.

        The authenticated user must have collaborator access to a repository to create,
        update, or read secrets.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/secrets/public-key",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PublicKey,
        )


class SecretsResourceWithRawResponse:
    def __init__(self, secrets: SecretsResource) -> None:
        self._secrets = secrets

        self.list = to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            secrets.delete,
        )
        self.create_or_update = to_raw_response_wrapper(
            secrets.create_or_update,
        )
        self.get = to_raw_response_wrapper(
            secrets.get,
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

        self.list = async_to_raw_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            secrets.delete,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            secrets.create_or_update,
        )
        self.get = async_to_raw_response_wrapper(
            secrets.get,
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

        self.list = to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            secrets.delete,
        )
        self.create_or_update = to_streamed_response_wrapper(
            secrets.create_or_update,
        )
        self.get = to_streamed_response_wrapper(
            secrets.get,
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

        self.list = async_to_streamed_response_wrapper(
            secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            secrets.delete,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            secrets.create_or_update,
        )
        self.get = async_to_streamed_response_wrapper(
            secrets.get,
        )
        self.get_public_key = async_to_streamed_response_wrapper(
            secrets.get_public_key,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self._secrets.repositories)
