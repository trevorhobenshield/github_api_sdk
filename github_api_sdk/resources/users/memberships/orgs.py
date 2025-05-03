from __future__ import annotations

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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.orgs.org_membership import OrgMembership
from ....types.users.memberships import org_list_params, org_update_params
from ....types.users.memberships.org_list_response import OrgListResponse

__all__ = ["OrgsResource", "AsyncOrgsResource"]


class OrgsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return OrgsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgMembership:
        """
        If the authenticated user is an active or pending member of the organization,
        this endpoint will return the user's membership. If the authenticated user is
        not affiliated with the organization, a `404` is returned. This endpoint will
        return a `403` if the request is made by a GitHub App that is blocked by the
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/user/memberships/orgs/{org}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgMembership,
        )

    def update(
        self,
        org: str,
        *,
        state: Literal["active"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgMembership:
        """
        Converts the authenticated user to an active member of the organization, if that
        user has a pending invitation from the organization.

        Args:
          state: The state that the membership should be in. Only `"active"` will be accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._patch(
            f"/user/memberships/orgs/{org}",
            body=maybe_transform({"state": state}, org_update_params.OrgUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgMembership,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        state: Literal["active", "pending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListResponse:
        """
        Lists all of the authenticated user's organization memberships.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          state: Indicates the state of the memberships to return. If not specified, the API
              returns both active and pending memberships.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/memberships/orgs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    org_list_params.OrgListParams,
                ),
            ),
            cast_to=OrgListResponse,
        )


class AsyncOrgsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrgsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrgsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrgsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncOrgsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgMembership:
        """
        If the authenticated user is an active or pending member of the organization,
        this endpoint will return the user's membership. If the authenticated user is
        not affiliated with the organization, a `404` is returned. This endpoint will
        return a `403` if the request is made by a GitHub App that is blocked by the
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/user/memberships/orgs/{org}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgMembership,
        )

    async def update(
        self,
        org: str,
        *,
        state: Literal["active"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgMembership:
        """
        Converts the authenticated user to an active member of the organization, if that
        user has a pending invitation from the organization.

        Args:
          state: The state that the membership should be in. Only `"active"` will be accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._patch(
            f"/user/memberships/orgs/{org}",
            body=await async_maybe_transform({"state": state}, org_update_params.OrgUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrgMembership,
        )

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        state: Literal["active", "pending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrgListResponse:
        """
        Lists all of the authenticated user's organization memberships.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          state: Indicates the state of the memberships to return. If not specified, the API
              returns both active and pending memberships.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/memberships/orgs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    org_list_params.OrgListParams,
                ),
            ),
            cast_to=OrgListResponse,
        )


class OrgsResourceWithRawResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.retrieve = to_raw_response_wrapper(
            orgs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            orgs.update,
        )
        self.list = to_raw_response_wrapper(
            orgs.list,
        )


class AsyncOrgsResourceWithRawResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.retrieve = async_to_raw_response_wrapper(
            orgs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            orgs.update,
        )
        self.list = async_to_raw_response_wrapper(
            orgs.list,
        )


class OrgsResourceWithStreamingResponse:
    def __init__(self, orgs: OrgsResource) -> None:
        self._orgs = orgs

        self.retrieve = to_streamed_response_wrapper(
            orgs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            orgs.update,
        )
        self.list = to_streamed_response_wrapper(
            orgs.list,
        )


class AsyncOrgsResourceWithStreamingResponse:
    def __init__(self, orgs: AsyncOrgsResource) -> None:
        self._orgs = orgs

        self.retrieve = async_to_streamed_response_wrapper(
            orgs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            orgs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            orgs.list,
        )
