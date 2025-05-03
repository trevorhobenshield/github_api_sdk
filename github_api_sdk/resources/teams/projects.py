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
from ...types.orgs.teams.team_project import TeamProject
from ...types.teams import project_add_or_update_permissions_params, project_list_params
from ...types.teams.project_list_response import ProjectListResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
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

    def list(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectListResponse:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

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
            f"/teams/{team_id}/projects",
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
                    project_list_params.ProjectListParams,
                ),
            ),
            cast_to=ProjectListResponse,
        )

    def add_or_update_permissions(
        self,
        project_id: int,
        *,
        team_id: int,
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
          permission: The permission to grant to the team for this project. Default: the team's
              `permission` attribute will be used to determine what permission to grant the
              team on this project. Note that, if you choose not to pass any parameters,
              you'll need to set `Content-Length` to zero when calling this endpoint. For more
              information, see
              "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/teams/{team_id}/projects/{project_id}",
            body=maybe_transform({"permission": permission}, project_add_or_update_permissions_params.ProjectAddOrUpdatePermissionsParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def check_permissions(
        self,
        project_id: int,
        *,
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamProject:
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
            f"/teams/{team_id}/projects/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamProject,
        )

    def remove(
        self,
        project_id: int,
        *,
        team_id: int,
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
            f"/teams/{team_id}/projects/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncProjectsResource(AsyncAPIResource):
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

    async def list(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectListResponse:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

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
            f"/teams/{team_id}/projects",
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
                    project_list_params.ProjectListParams,
                ),
            ),
            cast_to=ProjectListResponse,
        )

    async def add_or_update_permissions(
        self,
        project_id: int,
        *,
        team_id: int,
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
          permission: The permission to grant to the team for this project. Default: the team's
              `permission` attribute will be used to determine what permission to grant the
              team on this project. Note that, if you choose not to pass any parameters,
              you'll need to set `Content-Length` to zero when calling this endpoint. For more
              information, see
              "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/teams/{team_id}/projects/{project_id}",
            body=await async_maybe_transform(
                {"permission": permission}, project_add_or_update_permissions_params.ProjectAddOrUpdatePermissionsParams
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def check_permissions(
        self,
        project_id: int,
        *,
        team_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamProject:
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
            f"/teams/{team_id}/projects/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamProject,
        )

    async def remove(
        self,
        project_id: int,
        *,
        team_id: int,
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
            f"/teams/{team_id}/projects/{project_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.list = to_raw_response_wrapper(
            projects.list,
        )
        self.add_or_update_permissions = to_raw_response_wrapper(
            projects.add_or_update_permissions,
        )
        self.check_permissions = to_raw_response_wrapper(
            projects.check_permissions,
        )
        self.remove = to_raw_response_wrapper(
            projects.remove,
        )


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.list = async_to_raw_response_wrapper(
            projects.list,
        )
        self.add_or_update_permissions = async_to_raw_response_wrapper(
            projects.add_or_update_permissions,
        )
        self.check_permissions = async_to_raw_response_wrapper(
            projects.check_permissions,
        )
        self.remove = async_to_raw_response_wrapper(
            projects.remove,
        )


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.list = to_streamed_response_wrapper(
            projects.list,
        )
        self.add_or_update_permissions = to_streamed_response_wrapper(
            projects.add_or_update_permissions,
        )
        self.check_permissions = to_streamed_response_wrapper(
            projects.check_permissions,
        )
        self.remove = to_streamed_response_wrapper(
            projects.remove,
        )


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.list = async_to_streamed_response_wrapper(
            projects.list,
        )
        self.add_or_update_permissions = async_to_streamed_response_wrapper(
            projects.add_or_update_permissions,
        )
        self.check_permissions = async_to_streamed_response_wrapper(
            projects.check_permissions,
        )
        self.remove = async_to_streamed_response_wrapper(
            projects.remove,
        )
