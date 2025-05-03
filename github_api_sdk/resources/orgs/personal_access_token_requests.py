from __future__ import annotations

import builtins
from datetime import datetime
from typing import Iterable, List, Optional, Union

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
    personal_access_token_request_list_params,
    personal_access_token_request_list_repositories_params,
    personal_access_token_request_review_params,
    personal_access_token_request_review_single_params,
)
from ...types.orgs.personal_access_token_request_list_repositories_response import (
    PersonalAccessTokenRequestListRepositoriesResponse,
)
from ...types.orgs.personal_access_token_request_list_response import PersonalAccessTokenRequestListResponse

__all__ = ["PersonalAccessTokenRequestsResource", "AsyncPersonalAccessTokenRequestsResource"]


class PersonalAccessTokenRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersonalAccessTokenRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PersonalAccessTokenRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonalAccessTokenRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PersonalAccessTokenRequestsResourceWithStreamingResponse(self)

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
    ) -> PersonalAccessTokenRequestListResponse:
        """
        Lists requests from organization members to access organization resources with a
        fine-grained personal access token.

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
            f"/orgs/{org}/personal-access-token-requests",
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
                    personal_access_token_request_list_params.PersonalAccessTokenRequestListParams,
                ),
            ),
            cast_to=PersonalAccessTokenRequestListResponse,
        )

    def list_repositories(
        self,
        pat_request_id: int,
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
    ) -> PersonalAccessTokenRequestListRepositoriesResponse:
        """
        Lists the repositories a fine-grained personal access token request is
        requesting access to.

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
            f"/orgs/{org}/personal-access-token-requests/{pat_request_id}/repositories",
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
                    personal_access_token_request_list_repositories_params.PersonalAccessTokenRequestListRepositoriesParams,
                ),
            ),
            cast_to=PersonalAccessTokenRequestListRepositoriesResponse,
        )

    def review(
        self,
        org: str,
        *,
        action: Literal["approve", "deny"],
        pat_request_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        reason: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Approves or denies multiple pending requests to access organization resources
        via a fine-grained personal access token.

        Only GitHub Apps can use this endpoint.

        Args:
          action: Action to apply to the requests.

          pat_request_ids: Unique identifiers of the requests for access via fine-grained personal access
              token. Must be formed of between 1 and 100 `pat_request_id` values.

          reason: Reason for approving or denying the requests. Max 1024 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/personal-access-token-requests",
            body=maybe_transform(
                {
                    "action": action,
                    "pat_request_ids": pat_request_ids,
                    "reason": reason,
                },
                personal_access_token_request_review_params.PersonalAccessTokenRequestReviewParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def review_single(
        self,
        pat_request_id: int,
        *,
        org: str,
        action: Literal["approve", "deny"],
        reason: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Approves or denies a pending request to access organization resources via a
        fine-grained personal access token.

        Only GitHub Apps can use this endpoint.

        Args:
          action: Action to apply to the request.

          reason: Reason for approving or denying the request. Max 1024 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/orgs/{org}/personal-access-token-requests/{pat_request_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "reason": reason,
                },
                personal_access_token_request_review_single_params.PersonalAccessTokenRequestReviewSingleParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncPersonalAccessTokenRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersonalAccessTokenRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonalAccessTokenRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonalAccessTokenRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPersonalAccessTokenRequestsResourceWithStreamingResponse(self)

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
    ) -> PersonalAccessTokenRequestListResponse:
        """
        Lists requests from organization members to access organization resources with a
        fine-grained personal access token.

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
            f"/orgs/{org}/personal-access-token-requests",
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
                    personal_access_token_request_list_params.PersonalAccessTokenRequestListParams,
                ),
            ),
            cast_to=PersonalAccessTokenRequestListResponse,
        )

    async def list_repositories(
        self,
        pat_request_id: int,
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
    ) -> PersonalAccessTokenRequestListRepositoriesResponse:
        """
        Lists the repositories a fine-grained personal access token request is
        requesting access to.

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
            f"/orgs/{org}/personal-access-token-requests/{pat_request_id}/repositories",
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
                    personal_access_token_request_list_repositories_params.PersonalAccessTokenRequestListRepositoriesParams,
                ),
            ),
            cast_to=PersonalAccessTokenRequestListRepositoriesResponse,
        )

    async def review(
        self,
        org: str,
        *,
        action: Literal["approve", "deny"],
        pat_request_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        reason: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Approves or denies multiple pending requests to access organization resources
        via a fine-grained personal access token.

        Only GitHub Apps can use this endpoint.

        Args:
          action: Action to apply to the requests.

          pat_request_ids: Unique identifiers of the requests for access via fine-grained personal access
              token. Must be formed of between 1 and 100 `pat_request_id` values.

          reason: Reason for approving or denying the requests. Max 1024 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/personal-access-token-requests",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "pat_request_ids": pat_request_ids,
                    "reason": reason,
                },
                personal_access_token_request_review_params.PersonalAccessTokenRequestReviewParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def review_single(
        self,
        pat_request_id: int,
        *,
        org: str,
        action: Literal["approve", "deny"],
        reason: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Approves or denies a pending request to access organization resources via a
        fine-grained personal access token.

        Only GitHub Apps can use this endpoint.

        Args:
          action: Action to apply to the request.

          reason: Reason for approving or denying the request. Max 1024 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/orgs/{org}/personal-access-token-requests/{pat_request_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "reason": reason,
                },
                personal_access_token_request_review_single_params.PersonalAccessTokenRequestReviewSingleParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class PersonalAccessTokenRequestsResourceWithRawResponse:
    def __init__(self, personal_access_token_requests: PersonalAccessTokenRequestsResource) -> None:
        self._personal_access_token_requests = personal_access_token_requests

        self.list = to_raw_response_wrapper(
            personal_access_token_requests.list,
        )
        self.list_repositories = to_raw_response_wrapper(
            personal_access_token_requests.list_repositories,
        )
        self.review = to_raw_response_wrapper(
            personal_access_token_requests.review,
        )
        self.review_single = to_raw_response_wrapper(
            personal_access_token_requests.review_single,
        )


class AsyncPersonalAccessTokenRequestsResourceWithRawResponse:
    def __init__(self, personal_access_token_requests: AsyncPersonalAccessTokenRequestsResource) -> None:
        self._personal_access_token_requests = personal_access_token_requests

        self.list = async_to_raw_response_wrapper(
            personal_access_token_requests.list,
        )
        self.list_repositories = async_to_raw_response_wrapper(
            personal_access_token_requests.list_repositories,
        )
        self.review = async_to_raw_response_wrapper(
            personal_access_token_requests.review,
        )
        self.review_single = async_to_raw_response_wrapper(
            personal_access_token_requests.review_single,
        )


class PersonalAccessTokenRequestsResourceWithStreamingResponse:
    def __init__(self, personal_access_token_requests: PersonalAccessTokenRequestsResource) -> None:
        self._personal_access_token_requests = personal_access_token_requests

        self.list = to_streamed_response_wrapper(
            personal_access_token_requests.list,
        )
        self.list_repositories = to_streamed_response_wrapper(
            personal_access_token_requests.list_repositories,
        )
        self.review = to_streamed_response_wrapper(
            personal_access_token_requests.review,
        )
        self.review_single = to_streamed_response_wrapper(
            personal_access_token_requests.review_single,
        )


class AsyncPersonalAccessTokenRequestsResourceWithStreamingResponse:
    def __init__(self, personal_access_token_requests: AsyncPersonalAccessTokenRequestsResource) -> None:
        self._personal_access_token_requests = personal_access_token_requests

        self.list = async_to_streamed_response_wrapper(
            personal_access_token_requests.list,
        )
        self.list_repositories = async_to_streamed_response_wrapper(
            personal_access_token_requests.list_repositories,
        )
        self.review = async_to_streamed_response_wrapper(
            personal_access_token_requests.review,
        )
        self.review_single = async_to_streamed_response_wrapper(
            personal_access_token_requests.review_single,
        )
