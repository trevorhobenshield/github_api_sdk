from __future__ import annotations

import builtins
from typing import List

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
from ...types.users import social_account_add_params, social_account_delete_params, social_account_list_params
from ...types.users.social_account_add_response import SocialAccountAddResponse
from ...types.users.social_account_list_response import SocialAccountListResponse

__all__ = ["SocialAccountsResource", "AsyncSocialAccountsResource"]


class SocialAccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SocialAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SocialAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SocialAccountsResourceWithStreamingResponse(self)

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
    ) -> SocialAccountListResponse:
        """
        Lists all of your social accounts.

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
            "/user/social_accounts",
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
                    social_account_list_params.SocialAccountListParams,
                ),
            ),
            cast_to=SocialAccountListResponse,
        )

    def delete(
        self,
        *,
        account_urls: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes one or more social accounts from the authenticated user's profile.

        OAuth app tokens and personal access tokens (classic) need the `user` scope to
        use this endpoint.

        Args:
          account_urls: Full URLs for the social media profiles to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/user/social_accounts",
            body=maybe_transform({"account_urls": account_urls}, social_account_delete_params.SocialAccountDeleteParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def add(
        self,
        *,
        account_urls: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SocialAccountAddResponse:
        """
        Add one or more social accounts to the authenticated user's profile.

        OAuth app tokens and personal access tokens (classic) need the `user` scope to
        use this endpoint.

        Args:
          account_urls: Full URLs for the social media profiles to add.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/social_accounts",
            body=maybe_transform({"account_urls": account_urls}, social_account_add_params.SocialAccountAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SocialAccountAddResponse,
        )


class AsyncSocialAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSocialAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSocialAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSocialAccountsResourceWithStreamingResponse(self)

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
    ) -> SocialAccountListResponse:
        """
        Lists all of your social accounts.

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
            "/user/social_accounts",
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
                    social_account_list_params.SocialAccountListParams,
                ),
            ),
            cast_to=SocialAccountListResponse,
        )

    async def delete(
        self,
        *,
        account_urls: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes one or more social accounts from the authenticated user's profile.

        OAuth app tokens and personal access tokens (classic) need the `user` scope to
        use this endpoint.

        Args:
          account_urls: Full URLs for the social media profiles to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/user/social_accounts",
            body=await async_maybe_transform({"account_urls": account_urls}, social_account_delete_params.SocialAccountDeleteParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def add(
        self,
        *,
        account_urls: builtins.list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SocialAccountAddResponse:
        """
        Add one or more social accounts to the authenticated user's profile.

        OAuth app tokens and personal access tokens (classic) need the `user` scope to
        use this endpoint.

        Args:
          account_urls: Full URLs for the social media profiles to add.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/social_accounts",
            body=await async_maybe_transform({"account_urls": account_urls}, social_account_add_params.SocialAccountAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SocialAccountAddResponse,
        )


class SocialAccountsResourceWithRawResponse:
    def __init__(self, social_accounts: SocialAccountsResource) -> None:
        self._social_accounts = social_accounts

        self.list = to_raw_response_wrapper(
            social_accounts.list,
        )
        self.delete = to_raw_response_wrapper(
            social_accounts.delete,
        )
        self.add = to_raw_response_wrapper(
            social_accounts.add,
        )


class AsyncSocialAccountsResourceWithRawResponse:
    def __init__(self, social_accounts: AsyncSocialAccountsResource) -> None:
        self._social_accounts = social_accounts

        self.list = async_to_raw_response_wrapper(
            social_accounts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            social_accounts.delete,
        )
        self.add = async_to_raw_response_wrapper(
            social_accounts.add,
        )


class SocialAccountsResourceWithStreamingResponse:
    def __init__(self, social_accounts: SocialAccountsResource) -> None:
        self._social_accounts = social_accounts

        self.list = to_streamed_response_wrapper(
            social_accounts.list,
        )
        self.delete = to_streamed_response_wrapper(
            social_accounts.delete,
        )
        self.add = to_streamed_response_wrapper(
            social_accounts.add,
        )


class AsyncSocialAccountsResourceWithStreamingResponse:
    def __init__(self, social_accounts: AsyncSocialAccountsResource) -> None:
        self._social_accounts = social_accounts

        self.list = async_to_streamed_response_wrapper(
            social_accounts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            social_accounts.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            social_accounts.add,
        )
