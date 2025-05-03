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
from ...types.users import gpg_key_create_params, gpg_key_list_params
from ...types.users.gpg_key import GpgKey
from ...types.users.gpg_key_list_response import GpgKeyListResponse

__all__ = ["GpgKeysResource", "AsyncGpgKeysResource"]


class GpgKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GpgKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return GpgKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GpgKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return GpgKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        armored_public_key: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GpgKey:
        """
        Adds a GPG key to the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the `write:gpg_key`
        scope to use this endpoint.

        Args:
          armored_public_key: A GPG key in ASCII-armored format.

          name: A descriptive name for the new key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/gpg_keys",
            body=maybe_transform(
                {
                    "armored_public_key": armored_public_key,
                    "name": name,
                },
                gpg_key_create_params.GpgKeyCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GpgKey,
        )

    def retrieve(
        self,
        gpg_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GpgKey:
        """
        View extended details for a single GPG key.

        OAuth app tokens and personal access tokens (classic) need the `read:gpg_key`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/user/gpg_keys/{gpg_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GpgKey,
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
    ) -> GpgKeyListResponse:
        """
        Lists the current user's GPG keys.

        OAuth app tokens and personal access tokens (classic) need the `read:gpg_key`
        scope to use this endpoint.

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
            "/user/gpg_keys",
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
                    gpg_key_list_params.GpgKeyListParams,
                ),
            ),
            cast_to=GpgKeyListResponse,
        )

    def delete(
        self,
        gpg_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes a GPG key from the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the `admin:gpg_key`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/user/gpg_keys/{gpg_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncGpgKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGpgKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGpgKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGpgKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncGpgKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        armored_public_key: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GpgKey:
        """
        Adds a GPG key to the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the `write:gpg_key`
        scope to use this endpoint.

        Args:
          armored_public_key: A GPG key in ASCII-armored format.

          name: A descriptive name for the new key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/gpg_keys",
            body=await async_maybe_transform(
                {
                    "armored_public_key": armored_public_key,
                    "name": name,
                },
                gpg_key_create_params.GpgKeyCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GpgKey,
        )

    async def retrieve(
        self,
        gpg_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GpgKey:
        """
        View extended details for a single GPG key.

        OAuth app tokens and personal access tokens (classic) need the `read:gpg_key`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/user/gpg_keys/{gpg_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GpgKey,
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
    ) -> GpgKeyListResponse:
        """
        Lists the current user's GPG keys.

        OAuth app tokens and personal access tokens (classic) need the `read:gpg_key`
        scope to use this endpoint.

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
            "/user/gpg_keys",
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
                    gpg_key_list_params.GpgKeyListParams,
                ),
            ),
            cast_to=GpgKeyListResponse,
        )

    async def delete(
        self,
        gpg_key_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes a GPG key from the authenticated user's GitHub account.

        OAuth app tokens and personal access tokens (classic) need the `admin:gpg_key`
        scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/user/gpg_keys/{gpg_key_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class GpgKeysResourceWithRawResponse:
    def __init__(self, gpg_keys: GpgKeysResource) -> None:
        self._gpg_keys = gpg_keys

        self.create = to_raw_response_wrapper(
            gpg_keys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            gpg_keys.retrieve,
        )
        self.list = to_raw_response_wrapper(
            gpg_keys.list,
        )
        self.delete = to_raw_response_wrapper(
            gpg_keys.delete,
        )


class AsyncGpgKeysResourceWithRawResponse:
    def __init__(self, gpg_keys: AsyncGpgKeysResource) -> None:
        self._gpg_keys = gpg_keys

        self.create = async_to_raw_response_wrapper(
            gpg_keys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            gpg_keys.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            gpg_keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            gpg_keys.delete,
        )


class GpgKeysResourceWithStreamingResponse:
    def __init__(self, gpg_keys: GpgKeysResource) -> None:
        self._gpg_keys = gpg_keys

        self.create = to_streamed_response_wrapper(
            gpg_keys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            gpg_keys.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            gpg_keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            gpg_keys.delete,
        )


class AsyncGpgKeysResourceWithStreamingResponse:
    def __init__(self, gpg_keys: AsyncGpgKeysResource) -> None:
        self._gpg_keys = gpg_keys

        self.create = async_to_streamed_response_wrapper(
            gpg_keys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            gpg_keys.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            gpg_keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            gpg_keys.delete,
        )
