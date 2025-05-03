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
from ..types import assignment_list_accepted_params
from ..types.assignment_list_accepted_response import AssignmentListAcceptedResponse
from ..types.assignment_retrieve_grades_response import AssignmentRetrieveGradesResponse
from ..types.assignment_retrieve_response import AssignmentRetrieveResponse

__all__ = ["AssignmentsResource", "AsyncAssignmentsResource"]


class AssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AssignmentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        assignment_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentRetrieveResponse:
        """Gets a GitHub Classroom assignment.

        Assignment will only be returned if the
        current user is an administrator of the GitHub Classroom for the assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/assignments/{assignment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AssignmentRetrieveResponse,
        )

    def list_accepted(
        self,
        assignment_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentListAcceptedResponse:
        """
        Lists any assignment repositories that have been created by students accepting a
        GitHub Classroom assignment. Accepted assignments will only be returned if the
        current user is an administrator of the GitHub Classroom for the assignment.

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
            f"/assignments/{assignment_id}/accepted_assignments",
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
                    assignment_list_accepted_params.AssignmentListAcceptedParams,
                ),
            ),
            cast_to=AssignmentListAcceptedResponse,
        )

    def retrieve_grades(
        self,
        assignment_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentRetrieveGradesResponse:
        """Gets grades for a GitHub Classroom assignment.

        Grades will only be returned if
        the current user is an administrator of the GitHub Classroom for the assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/assignments/{assignment_id}/grades",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AssignmentRetrieveGradesResponse,
        )


class AsyncAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAssignmentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        assignment_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentRetrieveResponse:
        """Gets a GitHub Classroom assignment.

        Assignment will only be returned if the
        current user is an administrator of the GitHub Classroom for the assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/assignments/{assignment_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AssignmentRetrieveResponse,
        )

    async def list_accepted(
        self,
        assignment_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentListAcceptedResponse:
        """
        Lists any assignment repositories that have been created by students accepting a
        GitHub Classroom assignment. Accepted assignments will only be returned if the
        current user is an administrator of the GitHub Classroom for the assignment.

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
            f"/assignments/{assignment_id}/accepted_assignments",
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
                    assignment_list_accepted_params.AssignmentListAcceptedParams,
                ),
            ),
            cast_to=AssignmentListAcceptedResponse,
        )

    async def retrieve_grades(
        self,
        assignment_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssignmentRetrieveGradesResponse:
        """Gets grades for a GitHub Classroom assignment.

        Grades will only be returned if
        the current user is an administrator of the GitHub Classroom for the assignment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/assignments/{assignment_id}/grades",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AssignmentRetrieveGradesResponse,
        )


class AssignmentsResourceWithRawResponse:
    def __init__(self, assignments: AssignmentsResource) -> None:
        self._assignments = assignments

        self.retrieve = to_raw_response_wrapper(
            assignments.retrieve,
        )
        self.list_accepted = to_raw_response_wrapper(
            assignments.list_accepted,
        )
        self.retrieve_grades = to_raw_response_wrapper(
            assignments.retrieve_grades,
        )


class AsyncAssignmentsResourceWithRawResponse:
    def __init__(self, assignments: AsyncAssignmentsResource) -> None:
        self._assignments = assignments

        self.retrieve = async_to_raw_response_wrapper(
            assignments.retrieve,
        )
        self.list_accepted = async_to_raw_response_wrapper(
            assignments.list_accepted,
        )
        self.retrieve_grades = async_to_raw_response_wrapper(
            assignments.retrieve_grades,
        )


class AssignmentsResourceWithStreamingResponse:
    def __init__(self, assignments: AssignmentsResource) -> None:
        self._assignments = assignments

        self.retrieve = to_streamed_response_wrapper(
            assignments.retrieve,
        )
        self.list_accepted = to_streamed_response_wrapper(
            assignments.list_accepted,
        )
        self.retrieve_grades = to_streamed_response_wrapper(
            assignments.retrieve_grades,
        )


class AsyncAssignmentsResourceWithStreamingResponse:
    def __init__(self, assignments: AsyncAssignmentsResource) -> None:
        self._assignments = assignments

        self.retrieve = async_to_streamed_response_wrapper(
            assignments.retrieve,
        )
        self.list_accepted = async_to_streamed_response_wrapper(
            assignments.list_accepted,
        )
        self.retrieve_grades = async_to_streamed_response_wrapper(
            assignments.retrieve_grades,
        )
