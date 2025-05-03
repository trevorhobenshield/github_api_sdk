from __future__ import annotations

import httpx

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
from ...types.users import ssh_signing_key_create_params, ssh_signing_key_list_params
from ...types.users.ssh_signing_key import SSHSigningKey
from ...types.users.ssh_signing_key_list_response import SSHSigningKeyListResponse

__all__ = ["SSHSigningKeysResource", "AsyncSSHSigningKeysResource"]


class SSHSigningKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSHSigningKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SSHSigningKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSHSigningKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SSHSigningKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        key: str,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHSigningKey:
        """
        Creates an SSH signing key for the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the
        `write:ssh_signing_key` scope to use this endpoint.

        Args:
          key: The public SSH key to add to your GitHub account. For more information, see
              "[Checking for existing SSH keys](https://docs.github.com/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)."

          title: A descriptive name for the new key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/ssh_signing_keys",
            body=maybe_transform(
                {
                    "key": key,
                    "title": title,
                },
                ssh_signing_key_create_params.SSHSigningKeyCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SSHSigningKey,
        )

    def retrieve(
        self,
        ssh_signing_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHSigningKey:
        """
        Gets extended details for an SSH signing key.

        OAuth app tokens and personal access tokens (classic) need the
        `read:ssh_signing_key` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/user/ssh_signing_keys/{ssh_signing_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SSHSigningKey,
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
    ) -> SSHSigningKeyListResponse:
        """
        Lists the SSH signing keys for the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the
        `read:ssh_signing_key` scope to use this endpoint.

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
            "/user/ssh_signing_keys",
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
                    ssh_signing_key_list_params.SSHSigningKeyListParams,
                ),
            ),
            cast_to=SSHSigningKeyListResponse,
        )

    def delete(
        self,
        ssh_signing_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an SSH signing key from the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the
        `admin:ssh_signing_key` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/user/ssh_signing_keys/{ssh_signing_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncSSHSigningKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSHSigningKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSHSigningKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSHSigningKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSSHSigningKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        key: str,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHSigningKey:
        """
        Creates an SSH signing key for the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the
        `write:ssh_signing_key` scope to use this endpoint.

        Args:
          key: The public SSH key to add to your GitHub account. For more information, see
              "[Checking for existing SSH keys](https://docs.github.com/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)."

          title: A descriptive name for the new key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/ssh_signing_keys",
            body=await async_maybe_transform(
                {
                    "key": key,
                    "title": title,
                },
                ssh_signing_key_create_params.SSHSigningKeyCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SSHSigningKey,
        )

    async def retrieve(
        self,
        ssh_signing_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSHSigningKey:
        """
        Gets extended details for an SSH signing key.

        OAuth app tokens and personal access tokens (classic) need the
        `read:ssh_signing_key` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/user/ssh_signing_keys/{ssh_signing_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SSHSigningKey,
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
    ) -> SSHSigningKeyListResponse:
        """
        Lists the SSH signing keys for the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the
        `read:ssh_signing_key` scope to use this endpoint.

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
            "/user/ssh_signing_keys",
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
                    ssh_signing_key_list_params.SSHSigningKeyListParams,
                ),
            ),
            cast_to=SSHSigningKeyListResponse,
        )

    async def delete(
        self,
        ssh_signing_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an SSH signing key from the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the
        `admin:ssh_signing_key` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/user/ssh_signing_keys/{ssh_signing_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class SSHSigningKeysResourceWithRawResponse:
    def __init__(self, ssh_signing_keys: SSHSigningKeysResource) -> None:
        self._ssh_signing_keys = ssh_signing_keys

        self.create = to_raw_response_wrapper(
            ssh_signing_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ssh_signing_keys.retrieve,
        )
        self.list = to_raw_response_wrapper(
            ssh_signing_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            ssh_signing_keys.delete,
        )


class AsyncSSHSigningKeysResourceWithRawResponse:
    def __init__(self, ssh_signing_keys: AsyncSSHSigningKeysResource) -> None:
        self._ssh_signing_keys = ssh_signing_keys

        self.create = async_to_raw_response_wrapper(
            ssh_signing_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ssh_signing_keys.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            ssh_signing_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ssh_signing_keys.delete,
        )


class SSHSigningKeysResourceWithStreamingResponse:
    def __init__(self, ssh_signing_keys: SSHSigningKeysResource) -> None:
        self._ssh_signing_keys = ssh_signing_keys

        self.create = to_streamed_response_wrapper(
            ssh_signing_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ssh_signing_keys.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ssh_signing_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            ssh_signing_keys.delete,
        )


class AsyncSSHSigningKeysResourceWithStreamingResponse:
    def __init__(self, ssh_signing_keys: AsyncSSHSigningKeysResource) -> None:
        self._ssh_signing_keys = ssh_signing_keys

        self.create = async_to_streamed_response_wrapper(
            ssh_signing_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ssh_signing_keys.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ssh_signing_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ssh_signing_keys.delete,
        )
