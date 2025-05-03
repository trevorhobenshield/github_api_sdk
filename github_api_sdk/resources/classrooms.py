from __future__ import annotations

import httpx

from .._base_client import make_request_options
from .._compat import cached_property
from .._resource import AsyncAPIResource, SyncAPIResource
from .._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from .._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ..types import classroom_list_assignments_params, classroom_list_params
from ..types.classroom import Classroom
from ..types.classroom_list_assignments_response import ClassroomListAssignmentsResponse
from ..types.classroom_list_response import ClassroomListResponse

__all__ = ["ClassroomsResource", "AsyncClassroomsResource"]


class ClassroomsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassroomsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ClassroomsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassroomsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ClassroomsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        classroom_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Classroom:
        """Gets a GitHub Classroom classroom for the current user.

        Classroom will only be
        returned if the current user is an administrator of the GitHub Classroom.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/classrooms/{classroom_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Classroom,
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
    ) -> ClassroomListResponse:
        """Lists GitHub Classroom classrooms for the current user.

        Classrooms will only be
        returned if the current user is an administrator of one or more GitHub
        Classrooms.

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
            "/classrooms",
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
                    classroom_list_params.ClassroomListParams,
                ),
            ),
            cast_to=ClassroomListResponse,
        )

    def list_assignments(
        self,
        classroom_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassroomListAssignmentsResponse:
        """Lists GitHub Classroom assignments for a classroom.

        Assignments will only be
        returned if the current user is an administrator of the GitHub Classroom.

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
            f"/classrooms/{classroom_id}/assignments",
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
                    classroom_list_assignments_params.ClassroomListAssignmentsParams,
                ),
            ),
            cast_to=ClassroomListAssignmentsResponse,
        )


class AsyncClassroomsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassroomsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassroomsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassroomsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncClassroomsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        classroom_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Classroom:
        """Gets a GitHub Classroom classroom for the current user.

        Classroom will only be
        returned if the current user is an administrator of the GitHub Classroom.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/classrooms/{classroom_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Classroom,
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
    ) -> ClassroomListResponse:
        """Lists GitHub Classroom classrooms for the current user.

        Classrooms will only be
        returned if the current user is an administrator of one or more GitHub
        Classrooms.

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
            "/classrooms",
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
                    classroom_list_params.ClassroomListParams,
                ),
            ),
            cast_to=ClassroomListResponse,
        )

    async def list_assignments(
        self,
        classroom_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassroomListAssignmentsResponse:
        """Lists GitHub Classroom assignments for a classroom.

        Assignments will only be
        returned if the current user is an administrator of the GitHub Classroom.

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
            f"/classrooms/{classroom_id}/assignments",
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
                    classroom_list_assignments_params.ClassroomListAssignmentsParams,
                ),
            ),
            cast_to=ClassroomListAssignmentsResponse,
        )


class ClassroomsResourceWithRawResponse:
    def __init__(self, classrooms: ClassroomsResource) -> None:
        self._classrooms = classrooms

        self.retrieve = to_raw_response_wrapper(
            classrooms.retrieve,
        )
        self.list = to_raw_response_wrapper(
            classrooms.list,
        )
        self.list_assignments = to_raw_response_wrapper(
            classrooms.list_assignments,
        )


class AsyncClassroomsResourceWithRawResponse:
    def __init__(self, classrooms: AsyncClassroomsResource) -> None:
        self._classrooms = classrooms

        self.retrieve = async_to_raw_response_wrapper(
            classrooms.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            classrooms.list,
        )
        self.list_assignments = async_to_raw_response_wrapper(
            classrooms.list_assignments,
        )


class ClassroomsResourceWithStreamingResponse:
    def __init__(self, classrooms: ClassroomsResource) -> None:
        self._classrooms = classrooms

        self.retrieve = to_streamed_response_wrapper(
            classrooms.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            classrooms.list,
        )
        self.list_assignments = to_streamed_response_wrapper(
            classrooms.list_assignments,
        )


class AsyncClassroomsResourceWithStreamingResponse:
    def __init__(self, classrooms: AsyncClassroomsResource) -> None:
        self._classrooms = classrooms

        self.retrieve = async_to_streamed_response_wrapper(
            classrooms.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            classrooms.list,
        )
        self.list_assignments = async_to_streamed_response_wrapper(
            classrooms.list_assignments,
        )
