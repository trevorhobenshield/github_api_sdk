from __future__ import annotations

import builtins
from datetime import datetime
from typing import Iterable, List, Union

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
from ...types.orgs import (
    personal_access_token_list_params,
    personal_access_token_list_repositories_params,
    personal_access_token_update_params,
    personal_access_token_update_single_params,
)
from ...types.orgs.personal_access_token_list_repositories_response import PersonalAccessTokenListRepositoriesResponse
from ...types.orgs.personal_access_token_list_response import PersonalAccessTokenListResponse

__all__ = ["PersonalAccessTokensResource", "AsyncPersonalAccessTokensResource"]


class PersonalAccessTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersonalAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PersonalAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonalAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PersonalAccessTokensResourceWithStreamingResponse(self)

    def update(
        self,
        org: str,
        *,
        action: Literal["revoke"],
        pat_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates the access organization members have to organization resources via
        fine-grained personal access tokens. Limited to revoking a token's existing
        access.

        Only GitHub Apps can use this endpoint.

        Args:
          action: Action to apply to the fine-grained personal access token.

          pat_ids: The IDs of the fine-grained personal access tokens.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/personal-access-tokens",
            body=maybe_transform(
                {
                    "action": action,
                    "pat_ids": pat_ids,
                },
                personal_access_token_update_params.PersonalAccessTokenUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def list(
        self,
        org: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        last_used_after: str | datetime | NotGiven = NOT_GIVEN,
        last_used_before: str | datetime | NotGiven = NOT_GIVEN,
        owner: builtins.list[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        permission: str | NotGiven = NOT_GIVEN,
        repository: str | NotGiven = NOT_GIVEN,
        sort: Literal["created_at"] | NotGiven = NOT_GIVEN,
        token_id: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalAccessTokenListResponse:
        """
        Lists approved fine-grained personal access tokens owned by organization members
        that can access organization resources.

        Only GitHub Apps can use this endpoint.

        Args:
          direction: The direction to sort the results by.

          last_used_after: Only show fine-grained personal access tokens used after the given time. This is
              a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          last_used_before: Only show fine-grained personal access tokens used before the given time. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          owner: A list of owner usernames to use to filter the results.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          permission: The permission to use to filter the results.

          repository: The name of the repository to use to filter the results.

          sort: The property by which to sort the results.

          token_id: The ID of the token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/personal-access-tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "last_used_after": last_used_after,
                        "last_used_before": last_used_before,
                        "owner": owner,
                        "page": page,
                        "per_page": per_page,
                        "permission": permission,
                        "repository": repository,
                        "sort": sort,
                        "token_id": token_id,
                    },
                    personal_access_token_list_params.PersonalAccessTokenListParams,
                ),
            ),
            cast_to=PersonalAccessTokenListResponse,
        )

    def list_repositories(
        self,
        pat_id: int,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalAccessTokenListRepositoriesResponse:
        """
        Lists the repositories a fine-grained personal access token has access to.

        Only GitHub Apps can use this endpoint.

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
            f"/orgs/{org}/personal-access-tokens/{pat_id}/repositories",
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
                    personal_access_token_list_repositories_params.PersonalAccessTokenListRepositoriesParams,
                ),
            ),
            cast_to=PersonalAccessTokenListRepositoriesResponse,
        )

    def update_single(
        self,
        pat_id: int,
        *,
        org: str,
        action: Literal["revoke"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates the access an organization member has to organization resources via a
        fine-grained personal access token. Limited to revoking the token's existing
        access. Limited to revoking a token's existing access.

        Only GitHub Apps can use this endpoint.

        Args:
          action: Action to apply to the fine-grained personal access token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/orgs/{org}/personal-access-tokens/{pat_id}",
            body=maybe_transform({"action": action}, personal_access_token_update_single_params.PersonalAccessTokenUpdateSingleParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncPersonalAccessTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersonalAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonalAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonalAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPersonalAccessTokensResourceWithStreamingResponse(self)

    async def update(
        self,
        org: str,
        *,
        action: Literal["revoke"],
        pat_ids: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates the access organization members have to organization resources via
        fine-grained personal access tokens. Limited to revoking a token's existing
        access.

        Only GitHub Apps can use this endpoint.

        Args:
          action: Action to apply to the fine-grained personal access token.

          pat_ids: The IDs of the fine-grained personal access tokens.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/personal-access-tokens",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "pat_ids": pat_ids,
                },
                personal_access_token_update_params.PersonalAccessTokenUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def list(
        self,
        org: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        last_used_after: str | datetime | NotGiven = NOT_GIVEN,
        last_used_before: str | datetime | NotGiven = NOT_GIVEN,
        owner: builtins.list[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        permission: str | NotGiven = NOT_GIVEN,
        repository: str | NotGiven = NOT_GIVEN,
        sort: Literal["created_at"] | NotGiven = NOT_GIVEN,
        token_id: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalAccessTokenListResponse:
        """
        Lists approved fine-grained personal access tokens owned by organization members
        that can access organization resources.

        Only GitHub Apps can use this endpoint.

        Args:
          direction: The direction to sort the results by.

          last_used_after: Only show fine-grained personal access tokens used after the given time. This is
              a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          last_used_before: Only show fine-grained personal access tokens used before the given time. This
              is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          owner: A list of owner usernames to use to filter the results.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          permission: The permission to use to filter the results.

          repository: The name of the repository to use to filter the results.

          sort: The property by which to sort the results.

          token_id: The ID of the token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/personal-access-tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "last_used_after": last_used_after,
                        "last_used_before": last_used_before,
                        "owner": owner,
                        "page": page,
                        "per_page": per_page,
                        "permission": permission,
                        "repository": repository,
                        "sort": sort,
                        "token_id": token_id,
                    },
                    personal_access_token_list_params.PersonalAccessTokenListParams,
                ),
            ),
            cast_to=PersonalAccessTokenListResponse,
        )

    async def list_repositories(
        self,
        pat_id: int,
        *,
        org: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalAccessTokenListRepositoriesResponse:
        """
        Lists the repositories a fine-grained personal access token has access to.

        Only GitHub Apps can use this endpoint.

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
            f"/orgs/{org}/personal-access-tokens/{pat_id}/repositories",
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
                    personal_access_token_list_repositories_params.PersonalAccessTokenListRepositoriesParams,
                ),
            ),
            cast_to=PersonalAccessTokenListRepositoriesResponse,
        )

    async def update_single(
        self,
        pat_id: int,
        *,
        org: str,
        action: Literal["revoke"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates the access an organization member has to organization resources via a
        fine-grained personal access token. Limited to revoking the token's existing
        access. Limited to revoking a token's existing access.

        Only GitHub Apps can use this endpoint.

        Args:
          action: Action to apply to the fine-grained personal access token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/orgs/{org}/personal-access-tokens/{pat_id}",
            body=await async_maybe_transform({"action": action}, personal_access_token_update_single_params.PersonalAccessTokenUpdateSingleParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class PersonalAccessTokensResourceWithRawResponse:
    def __init__(self, personal_access_tokens: PersonalAccessTokensResource) -> None:
        self._personal_access_tokens = personal_access_tokens

        self.update = to_raw_response_wrapper(
            personal_access_tokens.update,
        )
        self.list = to_raw_response_wrapper(
            personal_access_tokens.list,
        )
        self.list_repositories = to_raw_response_wrapper(
            personal_access_tokens.list_repositories,
        )
        self.update_single = to_raw_response_wrapper(
            personal_access_tokens.update_single,
        )


class AsyncPersonalAccessTokensResourceWithRawResponse:
    def __init__(self, personal_access_tokens: AsyncPersonalAccessTokensResource) -> None:
        self._personal_access_tokens = personal_access_tokens

        self.update = async_to_raw_response_wrapper(
            personal_access_tokens.update,
        )
        self.list = async_to_raw_response_wrapper(
            personal_access_tokens.list,
        )
        self.list_repositories = async_to_raw_response_wrapper(
            personal_access_tokens.list_repositories,
        )
        self.update_single = async_to_raw_response_wrapper(
            personal_access_tokens.update_single,
        )


class PersonalAccessTokensResourceWithStreamingResponse:
    def __init__(self, personal_access_tokens: PersonalAccessTokensResource) -> None:
        self._personal_access_tokens = personal_access_tokens

        self.update = to_streamed_response_wrapper(
            personal_access_tokens.update,
        )
        self.list = to_streamed_response_wrapper(
            personal_access_tokens.list,
        )
        self.list_repositories = to_streamed_response_wrapper(
            personal_access_tokens.list_repositories,
        )
        self.update_single = to_streamed_response_wrapper(
            personal_access_tokens.update_single,
        )


class AsyncPersonalAccessTokensResourceWithStreamingResponse:
    def __init__(self, personal_access_tokens: AsyncPersonalAccessTokensResource) -> None:
        self._personal_access_tokens = personal_access_tokens

        self.update = async_to_streamed_response_wrapper(
            personal_access_tokens.update,
        )
        self.list = async_to_streamed_response_wrapper(
            personal_access_tokens.list,
        )
        self.list_repositories = async_to_streamed_response_wrapper(
            personal_access_tokens.list_repositories,
        )
        self.update_single = async_to_streamed_response_wrapper(
            personal_access_tokens.update_single,
        )
