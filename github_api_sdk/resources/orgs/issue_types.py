from __future__ import annotations

from typing import Optional

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
from ...types.orgs import issue_type_create_params, issue_type_update_params
from ...types.orgs.issue_type import IssueType
from ...types.orgs.issue_type_list_response import IssueTypeListResponse

__all__ = ["IssueTypesResource", "AsyncIssueTypesResource"]


class IssueTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IssueTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return IssueTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IssueTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return IssueTypesResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        is_enabled: bool,
        name: str,
        color: Literal["gray", "blue", "green", "yellow", "orange", "red", "pink", "purple"] | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueType | None:
        """
        Create a new issue type for an organization.

        You can find out more about issue types in
        [Managing issue types in an organization](https://docs.github.com/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization).

        To use this endpoint, the authenticated user must be an administrator for the
        organization. OAuth app tokens and personal access tokens (classic) need the
        `admin:org` scope to use this endpoint.

        Args:
          is_enabled: Whether or not the issue type is enabled at the organization level.

          name: Name of the issue type.

          color: Color for the issue type.

          description: Description of the issue type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/issue-types",
            body=maybe_transform(
                {
                    "is_enabled": is_enabled,
                    "name": name,
                    "color": color,
                    "description": description,
                },
                issue_type_create_params.IssueTypeCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueType,
        )

    def update(
        self,
        issue_type_id: int,
        *,
        org: str,
        is_enabled: bool,
        name: str,
        color: Literal["gray", "blue", "green", "yellow", "orange", "red", "pink", "purple"] | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueType | None:
        """
        Updates an issue type for an organization.

        You can find out more about issue types in
        [Managing issue types in an organization](https://docs.github.com/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization).

        To use this endpoint, the authenticated user must be an administrator for the
        organization. OAuth app tokens and personal access tokens (classic) need the
        `admin:org` scope to use this endpoint.

        Args:
          is_enabled: Whether or not the issue type is enabled at the organization level.

          name: Name of the issue type.

          color: Color for the issue type.

          description: Description of the issue type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._put(
            f"/orgs/{org}/issue-types/{issue_type_id}",
            body=maybe_transform(
                {
                    "is_enabled": is_enabled,
                    "name": name,
                    "color": color,
                    "description": description,
                },
                issue_type_update_params.IssueTypeUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueType,
        )

    def list(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueTypeListResponse:
        """Lists all issue types for an organization.

        OAuth app tokens and personal access
        tokens (classic) need the read:org scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/issue-types",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueTypeListResponse,
        )

    def delete(
        self,
        issue_type_id: int,
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
        Deletes an issue type for an organization.

        You can find out more about issue types in
        [Managing issue types in an organization](https://docs.github.com/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization).

        To use this endpoint, the authenticated user must be an administrator for the
        organization. OAuth app tokens and personal access tokens (classic) need the
        `admin:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/issue-types/{issue_type_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncIssueTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIssueTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIssueTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIssueTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncIssueTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        is_enabled: bool,
        name: str,
        color: Literal["gray", "blue", "green", "yellow", "orange", "red", "pink", "purple"] | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueType | None:
        """
        Create a new issue type for an organization.

        You can find out more about issue types in
        [Managing issue types in an organization](https://docs.github.com/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization).

        To use this endpoint, the authenticated user must be an administrator for the
        organization. OAuth app tokens and personal access tokens (classic) need the
        `admin:org` scope to use this endpoint.

        Args:
          is_enabled: Whether or not the issue type is enabled at the organization level.

          name: Name of the issue type.

          color: Color for the issue type.

          description: Description of the issue type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/issue-types",
            body=await async_maybe_transform(
                {
                    "is_enabled": is_enabled,
                    "name": name,
                    "color": color,
                    "description": description,
                },
                issue_type_create_params.IssueTypeCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueType,
        )

    async def update(
        self,
        issue_type_id: int,
        *,
        org: str,
        is_enabled: bool,
        name: str,
        color: Literal["gray", "blue", "green", "yellow", "orange", "red", "pink", "purple"] | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueType | None:
        """
        Updates an issue type for an organization.

        You can find out more about issue types in
        [Managing issue types in an organization](https://docs.github.com/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization).

        To use this endpoint, the authenticated user must be an administrator for the
        organization. OAuth app tokens and personal access tokens (classic) need the
        `admin:org` scope to use this endpoint.

        Args:
          is_enabled: Whether or not the issue type is enabled at the organization level.

          name: Name of the issue type.

          color: Color for the issue type.

          description: Description of the issue type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._put(
            f"/orgs/{org}/issue-types/{issue_type_id}",
            body=await async_maybe_transform(
                {
                    "is_enabled": is_enabled,
                    "name": name,
                    "color": color,
                    "description": description,
                },
                issue_type_update_params.IssueTypeUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueType,
        )

    async def list(
        self,
        org: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IssueTypeListResponse:
        """Lists all issue types for an organization.

        OAuth app tokens and personal access
        tokens (classic) need the read:org scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/issue-types",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=IssueTypeListResponse,
        )

    async def delete(
        self,
        issue_type_id: int,
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
        Deletes an issue type for an organization.

        You can find out more about issue types in
        [Managing issue types in an organization](https://docs.github.com/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization).

        To use this endpoint, the authenticated user must be an administrator for the
        organization. OAuth app tokens and personal access tokens (classic) need the
        `admin:org` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/issue-types/{issue_type_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class IssueTypesResourceWithRawResponse:
    def __init__(self, issue_types: IssueTypesResource) -> None:
        self._issue_types = issue_types

        self.create = to_raw_response_wrapper(
            issue_types.create,
        )
        self.update = to_raw_response_wrapper(
            issue_types.update,
        )
        self.list = to_raw_response_wrapper(
            issue_types.list,
        )
        self.delete = to_raw_response_wrapper(
            issue_types.delete,
        )


class AsyncIssueTypesResourceWithRawResponse:
    def __init__(self, issue_types: AsyncIssueTypesResource) -> None:
        self._issue_types = issue_types

        self.create = async_to_raw_response_wrapper(
            issue_types.create,
        )
        self.update = async_to_raw_response_wrapper(
            issue_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            issue_types.list,
        )
        self.delete = async_to_raw_response_wrapper(
            issue_types.delete,
        )


class IssueTypesResourceWithStreamingResponse:
    def __init__(self, issue_types: IssueTypesResource) -> None:
        self._issue_types = issue_types

        self.create = to_streamed_response_wrapper(
            issue_types.create,
        )
        self.update = to_streamed_response_wrapper(
            issue_types.update,
        )
        self.list = to_streamed_response_wrapper(
            issue_types.list,
        )
        self.delete = to_streamed_response_wrapper(
            issue_types.delete,
        )


class AsyncIssueTypesResourceWithStreamingResponse:
    def __init__(self, issue_types: AsyncIssueTypesResource) -> None:
        self._issue_types = issue_types

        self.create = async_to_streamed_response_wrapper(
            issue_types.create,
        )
        self.update = async_to_streamed_response_wrapper(
            issue_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            issue_types.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            issue_types.delete,
        )
