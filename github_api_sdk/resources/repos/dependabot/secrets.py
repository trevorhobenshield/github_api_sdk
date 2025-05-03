from __future__ import annotations

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
from ....types.orgs.dependabot.dependabot_public_key import DependabotPublicKey
from ....types.repos.dependabot import secret_create_or_update_params, secret_list_params
from ....types.repos.dependabot.dependabot_secret import DependabotSecret
from ....types.repos.dependabot.secret_list_response import SecretListResponse

__all__ = ["SecretsResource", "AsyncSecretsResource"]


class SecretsResource(SyncAPIResource):
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
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependabotSecret:
        """
        Gets a single repository secret without revealing its encrypted value.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._get(
            f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependabotSecret,
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
    ) -> SecretListResponse:
        """
        Lists all secrets available in a repository without revealing their encrypted
        values.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/dependabot/secrets",
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
        Deletes a secret in a repository using the secret name.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def create_or_update(
        self,
        secret_name: str,
        *,
        owner: str,
        repo: str,
        encrypted_value: str | NotGiven = NOT_GIVEN,
        key_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Creates or updates a repository secret with an encrypted value.

        Encrypt your
        secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          encrypted_value: Value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get a repository public key](https://docs.github.com/rest/dependabot/secrets#get-a-repository-public-key)
              endpoint.

          key_id: ID of the key you used to encrypt the secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return self._put(
            f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}",
            body=maybe_transform(
                {
                    "encrypted_value": encrypted_value,
                    "key_id": key_id,
                },
                secret_create_or_update_params.SecretCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def retrieve_public_key(
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
    ) -> DependabotPublicKey:
        """Gets your public key, which you need to encrypt secrets.

        You need to encrypt a
        secret before you can create or update secrets. Anyone with read access to the
        repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint if the repository is private.

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
            f"/repos/{owner}/{repo}/dependabot/secrets/public-key",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependabotPublicKey,
        )


class AsyncSecretsResource(AsyncAPIResource):
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
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DependabotSecret:
        """
        Gets a single repository secret without revealing its encrypted value.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependabotSecret,
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
    ) -> SecretListResponse:
        """
        Lists all secrets available in a repository without revealing their encrypted
        values.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/dependabot/secrets",
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
        Deletes a secret in a repository using the secret name.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def create_or_update(
        self,
        secret_name: str,
        *,
        owner: str,
        repo: str,
        encrypted_value: str | NotGiven = NOT_GIVEN,
        key_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Creates or updates a repository secret with an encrypted value.

        Encrypt your
        secret using
        [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For
        more information, see
        "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          encrypted_value: Value for your secret, encrypted with
              [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
              the public key retrieved from the
              [Get a repository public key](https://docs.github.com/rest/dependabot/secrets#get-a-repository-public-key)
              endpoint.

          key_id: ID of the key you used to encrypt the secret.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not secret_name:
            raise ValueError(f"Expected a non-empty value for `secret_name` but received {secret_name!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}",
            body=await async_maybe_transform(
                {
                    "encrypted_value": encrypted_value,
                    "key_id": key_id,
                },
                secret_create_or_update_params.SecretCreateOrUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def retrieve_public_key(
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
    ) -> DependabotPublicKey:
        """Gets your public key, which you need to encrypt secrets.

        You need to encrypt a
        secret before you can create or update secrets. Anyone with read access to the
        repository can use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint if the repository is private.

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
            f"/repos/{owner}/{repo}/dependabot/secrets/public-key",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=DependabotPublicKey,
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
        self.retrieve_public_key = to_raw_response_wrapper(
            secrets.retrieve_public_key,
        )


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
        self.retrieve_public_key = async_to_raw_response_wrapper(
            secrets.retrieve_public_key,
        )


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
        self.retrieve_public_key = to_streamed_response_wrapper(
            secrets.retrieve_public_key,
        )


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
        self.retrieve_public_key = async_to_streamed_response_wrapper(
            secrets.retrieve_public_key,
        )
