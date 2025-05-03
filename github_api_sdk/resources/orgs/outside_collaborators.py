from __future__ import annotations

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
from ...types.orgs import outside_collaborator_convert_params, outside_collaborator_list_params
from ...types.orgs.outside_collaborator_list_response import OutsideCollaboratorListResponse

__all__ = ["OutsideCollaboratorsResource", "AsyncOutsideCollaboratorsResource"]


class OutsideCollaboratorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OutsideCollaboratorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return OutsideCollaboratorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutsideCollaboratorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return OutsideCollaboratorsResourceWithStreamingResponse(self)

    def list(
        self,
        org: str,
        *,
        filter: Literal["2fa_disabled", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutsideCollaboratorListResponse:
        """
        List all users who are outside collaborators of an organization.

        Args:
          filter: Filter the list of outside collaborators. `2fa_disabled` means that only outside
              collaborators without
              [two-factor authentication](https://github.com/blog/1614-two-factor-authentication)
              enabled will be returned.

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
            f"/orgs/{org}/outside_collaborators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                    },
                    outside_collaborator_list_params.OutsideCollaboratorListParams,
                ),
            ),
            cast_to=OutsideCollaboratorListResponse,
        )

    def convert(
        self,
        username: str,
        *,
        org: str,
        async_: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        When an organization member is converted to an outside collaborator, they'll
        only have access to the repositories that their current team membership allows.
        The user will no longer be a member of the organization. For more information,
        see
        "[Converting an organization member to an outside collaborator](https://docs.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)".
        Converting an organization member to an outside collaborator may be restricted
        by enterprise administrators. For more information, see
        "[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories)."

        Args:
          async_: When set to `true`, the request will be performed asynchronously. Returns a 202
              status code when the job is successfully queued.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._put(
            f"/orgs/{org}/outside_collaborators/{username}",
            body=maybe_transform({"async_": async_}, outside_collaborator_convert_params.OutsideCollaboratorConvertParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def remove(
        self,
        username: str,
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
        Removing a user from this list will remove them from all the organization's
        repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/outside_collaborators/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncOutsideCollaboratorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOutsideCollaboratorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutsideCollaboratorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutsideCollaboratorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncOutsideCollaboratorsResourceWithStreamingResponse(self)

    async def list(
        self,
        org: str,
        *,
        filter: Literal["2fa_disabled", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OutsideCollaboratorListResponse:
        """
        List all users who are outside collaborators of an organization.

        Args:
          filter: Filter the list of outside collaborators. `2fa_disabled` means that only outside
              collaborators without
              [two-factor authentication](https://github.com/blog/1614-two-factor-authentication)
              enabled will be returned.

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
            f"/orgs/{org}/outside_collaborators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                    },
                    outside_collaborator_list_params.OutsideCollaboratorListParams,
                ),
            ),
            cast_to=OutsideCollaboratorListResponse,
        )

    async def convert(
        self,
        username: str,
        *,
        org: str,
        async_: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        When an organization member is converted to an outside collaborator, they'll
        only have access to the repositories that their current team membership allows.
        The user will no longer be a member of the organization. For more information,
        see
        "[Converting an organization member to an outside collaborator](https://docs.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)".
        Converting an organization member to an outside collaborator may be restricted
        by enterprise administrators. For more information, see
        "[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories)."

        Args:
          async_: When set to `true`, the request will be performed asynchronously. Returns a 202
              status code when the job is successfully queued.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._put(
            f"/orgs/{org}/outside_collaborators/{username}",
            body=await async_maybe_transform({"async_": async_}, outside_collaborator_convert_params.OutsideCollaboratorConvertParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def remove(
        self,
        username: str,
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
        Removing a user from this list will remove them from all the organization's
        repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/outside_collaborators/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class OutsideCollaboratorsResourceWithRawResponse:
    def __init__(self, outside_collaborators: OutsideCollaboratorsResource) -> None:
        self._outside_collaborators = outside_collaborators

        self.list = to_raw_response_wrapper(
            outside_collaborators.list,
        )
        self.convert = to_raw_response_wrapper(
            outside_collaborators.convert,
        )
        self.remove = to_raw_response_wrapper(
            outside_collaborators.remove,
        )


class AsyncOutsideCollaboratorsResourceWithRawResponse:
    def __init__(self, outside_collaborators: AsyncOutsideCollaboratorsResource) -> None:
        self._outside_collaborators = outside_collaborators

        self.list = async_to_raw_response_wrapper(
            outside_collaborators.list,
        )
        self.convert = async_to_raw_response_wrapper(
            outside_collaborators.convert,
        )
        self.remove = async_to_raw_response_wrapper(
            outside_collaborators.remove,
        )


class OutsideCollaboratorsResourceWithStreamingResponse:
    def __init__(self, outside_collaborators: OutsideCollaboratorsResource) -> None:
        self._outside_collaborators = outside_collaborators

        self.list = to_streamed_response_wrapper(
            outside_collaborators.list,
        )
        self.convert = to_streamed_response_wrapper(
            outside_collaborators.convert,
        )
        self.remove = to_streamed_response_wrapper(
            outside_collaborators.remove,
        )


class AsyncOutsideCollaboratorsResourceWithStreamingResponse:
    def __init__(self, outside_collaborators: AsyncOutsideCollaboratorsResource) -> None:
        self._outside_collaborators = outside_collaborators

        self.list = async_to_streamed_response_wrapper(
            outside_collaborators.list,
        )
        self.convert = async_to_streamed_response_wrapper(
            outside_collaborators.convert,
        )
        self.remove = async_to_streamed_response_wrapper(
            outside_collaborators.remove,
        )
