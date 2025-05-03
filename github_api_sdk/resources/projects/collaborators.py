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
from ...types.projects import collaborator_add_params, collaborator_list_params
from ...types.projects.collaborator_get_permission_response import CollaboratorGetPermissionResponse
from ...types.projects.collaborator_list_response import CollaboratorListResponse

__all__ = ["CollaboratorsResource", "AsyncCollaboratorsResource"]


class CollaboratorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollaboratorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CollaboratorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollaboratorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CollaboratorsResourceWithStreamingResponse(self)

    def list(
        self,
        project_id: int,
        *,
        affiliation: Literal["outside", "direct", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollaboratorListResponse:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          affiliation: Filters the collaborators by their affiliation. `outside` means outside
              collaborators of a project that are not a member of the project's organization.
              `direct` means collaborators with permissions to a project, regardless of
              organization membership status. `all` means all collaborators the authenticated
              user can see.

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
            f"/projects/{project_id}/collaborators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "affiliation": affiliation,
                        "page": page,
                        "per_page": per_page,
                    },
                    collaborator_list_params.CollaboratorListParams,
                ),
            ),
            cast_to=CollaboratorListResponse,
        )

    def add(
        self,
        username: str,
        *,
        project_id: int,
        permission: Literal["read", "write", "admin"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          permission: The permission to grant the collaborator.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/projects/{project_id}/collaborators/{username}",
            body=maybe_transform({"permission": permission}, collaborator_add_params.CollaboratorAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_permission(
        self,
        username: str,
        *,
        project_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollaboratorGetPermissionResponse:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/projects/{project_id}/collaborators/{username}/permission",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CollaboratorGetPermissionResponse,
        )

    def remove(
        self,
        username: str,
        *,
        project_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/projects/{project_id}/collaborators/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncCollaboratorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollaboratorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollaboratorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollaboratorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCollaboratorsResourceWithStreamingResponse(self)

    async def list(
        self,
        project_id: int,
        *,
        affiliation: Literal["outside", "direct", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollaboratorListResponse:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          affiliation: Filters the collaborators by their affiliation. `outside` means outside
              collaborators of a project that are not a member of the project's organization.
              `direct` means collaborators with permissions to a project, regardless of
              organization membership status. `all` means all collaborators the authenticated
              user can see.

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
            f"/projects/{project_id}/collaborators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "affiliation": affiliation,
                        "page": page,
                        "per_page": per_page,
                    },
                    collaborator_list_params.CollaboratorListParams,
                ),
            ),
            cast_to=CollaboratorListResponse,
        )

    async def add(
        self,
        username: str,
        *,
        project_id: int,
        permission: Literal["read", "write", "admin"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          permission: The permission to grant the collaborator.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/projects/{project_id}/collaborators/{username}",
            body=await async_maybe_transform({"permission": permission}, collaborator_add_params.CollaboratorAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_permission(
        self,
        username: str,
        *,
        project_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollaboratorGetPermissionResponse:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/projects/{project_id}/collaborators/{username}/permission",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CollaboratorGetPermissionResponse,
        )

    async def remove(
        self,
        username: str,
        *,
        project_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/projects/{project_id}/collaborators/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class CollaboratorsResourceWithRawResponse:
    def __init__(self, collaborators: CollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = to_raw_response_wrapper(
            collaborators.list,
        )
        self.add = to_raw_response_wrapper(
            collaborators.add,
        )
        self.get_permission = to_raw_response_wrapper(
            collaborators.get_permission,
        )
        self.remove = to_raw_response_wrapper(
            collaborators.remove,
        )


class AsyncCollaboratorsResourceWithRawResponse:
    def __init__(self, collaborators: AsyncCollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = async_to_raw_response_wrapper(
            collaborators.list,
        )
        self.add = async_to_raw_response_wrapper(
            collaborators.add,
        )
        self.get_permission = async_to_raw_response_wrapper(
            collaborators.get_permission,
        )
        self.remove = async_to_raw_response_wrapper(
            collaborators.remove,
        )


class CollaboratorsResourceWithStreamingResponse:
    def __init__(self, collaborators: CollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = to_streamed_response_wrapper(
            collaborators.list,
        )
        self.add = to_streamed_response_wrapper(
            collaborators.add,
        )
        self.get_permission = to_streamed_response_wrapper(
            collaborators.get_permission,
        )
        self.remove = to_streamed_response_wrapper(
            collaborators.remove,
        )


class AsyncCollaboratorsResourceWithStreamingResponse:
    def __init__(self, collaborators: AsyncCollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = async_to_streamed_response_wrapper(
            collaborators.list,
        )
        self.add = async_to_streamed_response_wrapper(
            collaborators.add,
        )
        self.get_permission = async_to_streamed_response_wrapper(
            collaborators.get_permission,
        )
        self.remove = async_to_streamed_response_wrapper(
            collaborators.remove,
        )
