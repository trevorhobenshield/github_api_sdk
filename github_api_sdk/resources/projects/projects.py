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
from ...types import project_update_params
from ...types.orgs.project import Project
from .collaborators import (
    AsyncCollaboratorsResource,
    AsyncCollaboratorsResourceWithRawResponse,
    AsyncCollaboratorsResourceWithStreamingResponse,
    CollaboratorsResource,
    CollaboratorsResourceWithRawResponse,
    CollaboratorsResourceWithStreamingResponse,
)
from .columns.columns import (
    AsyncColumnsResource,
    AsyncColumnsResourceWithRawResponse,
    AsyncColumnsResourceWithStreamingResponse,
    ColumnsResource,
    ColumnsResourceWithRawResponse,
    ColumnsResourceWithStreamingResponse,
)

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def columns(self) -> ColumnsResource:
        return ColumnsResource(self._client)

    @cached_property
    def collaborators(self) -> CollaboratorsResource:
        return CollaboratorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        project_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
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
        return self._get(
            f"/projects/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    def update(
        self,
        project_id: int,
        *,
        body: str | None | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization_permission: Literal["read", "write", "admin", "none"] | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          body: Body of the project

          name: Name of the project

          organization_permission: The baseline permission that all organization members have on this project

          private: Whether or not this project can be seen by everyone.

          state: State of the project; either 'open' or 'closed'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/projects/{project_id}",
            body=maybe_transform(
                {
                    "body": body,
                    "name": name,
                    "organization_permission": organization_permission,
                    "private": private,
                    "state": state,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    def delete(
        self,
        project_id: int,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/projects/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def columns(self) -> AsyncColumnsResource:
        return AsyncColumnsResource(self._client)

    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResource:
        return AsyncCollaboratorsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        project_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
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
        return await self._get(
            f"/projects/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    async def update(
        self,
        project_id: int,
        *,
        body: str | None | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        organization_permission: Literal["read", "write", "admin", "none"] | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Project:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          body: Body of the project

          name: Name of the project

          organization_permission: The baseline permission that all organization members have on this project

          private: Whether or not this project can be seen by everyone.

          state: State of the project; either 'open' or 'closed'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/projects/{project_id}",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "name": name,
                    "organization_permission": organization_permission,
                    "private": private,
                    "state": state,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Project,
        )

    async def delete(
        self,
        project_id: int,
        *,
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/projects/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.retrieve = to_raw_response_wrapper(
            projects.retrieve,
        )
        self.update = to_raw_response_wrapper(
            projects.update,
        )
        self.delete = to_raw_response_wrapper(
            projects.delete,
        )

    @cached_property
    def columns(self) -> ColumnsResourceWithRawResponse:
        return ColumnsResourceWithRawResponse(self._projects.columns)

    @cached_property
    def collaborators(self) -> CollaboratorsResourceWithRawResponse:
        return CollaboratorsResourceWithRawResponse(self._projects.collaborators)


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.retrieve = async_to_raw_response_wrapper(
            projects.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            projects.update,
        )
        self.delete = async_to_raw_response_wrapper(
            projects.delete,
        )

    @cached_property
    def columns(self) -> AsyncColumnsResourceWithRawResponse:
        return AsyncColumnsResourceWithRawResponse(self._projects.columns)

    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResourceWithRawResponse:
        return AsyncCollaboratorsResourceWithRawResponse(self._projects.collaborators)


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.retrieve = to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            projects.update,
        )
        self.delete = to_streamed_response_wrapper(
            projects.delete,
        )

    @cached_property
    def columns(self) -> ColumnsResourceWithStreamingResponse:
        return ColumnsResourceWithStreamingResponse(self._projects.columns)

    @cached_property
    def collaborators(self) -> CollaboratorsResourceWithStreamingResponse:
        return CollaboratorsResourceWithStreamingResponse(self._projects.collaborators)


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.retrieve = async_to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            projects.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            projects.delete,
        )

    @cached_property
    def columns(self) -> AsyncColumnsResourceWithStreamingResponse:
        return AsyncColumnsResourceWithStreamingResponse(self._projects.columns)

    @cached_property
    def collaborators(self) -> AsyncCollaboratorsResourceWithStreamingResponse:
        return AsyncCollaboratorsResourceWithStreamingResponse(self._projects.collaborators)
