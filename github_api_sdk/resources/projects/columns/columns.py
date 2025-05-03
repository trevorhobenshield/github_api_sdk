from __future__ import annotations

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.projects import column_create_params, column_list_params, column_move_params, column_update_params
from ....types.projects.column_list_response import ColumnListResponse
from ....types.projects.project_column import ProjectColumn
from .cards import (
    AsyncCardsResource,
    AsyncCardsResourceWithRawResponse,
    AsyncCardsResourceWithStreamingResponse,
    CardsResource,
    CardsResourceWithRawResponse,
    CardsResourceWithStreamingResponse,
)

__all__ = ["ColumnsResource", "AsyncColumnsResource"]


class ColumnsResource(SyncAPIResource):
    @cached_property
    def cards(self) -> CardsResource:
        return CardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ColumnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ColumnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColumnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ColumnsResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectColumn:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          name: Name of the project column

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/projects/{project_id}/columns",
            body=maybe_transform({"name": name}, column_create_params.ColumnCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProjectColumn,
        )

    def retrieve(
        self,
        column_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectColumn:
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
            f"/projects/columns/{column_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProjectColumn,
        )

    def update(
        self,
        column_id: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectColumn:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          name: Name of the project column

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/projects/columns/{column_id}",
            body=maybe_transform({"name": name}, column_update_params.ColumnUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProjectColumn,
        )

    def list(
        self,
        project_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ColumnListResponse:
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
            f"/projects/{project_id}/columns",
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
                    column_list_params.ColumnListParams,
                ),
            ),
            cast_to=ColumnListResponse,
        )

    def delete(
        self,
        column_id: int,
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
            f"/projects/columns/{column_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def move(
        self,
        column_id: int,
        *,
        position: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          position: The position of the column in a project. Can be one of: `first`, `last`, or
              `after:<column_id>` to place after the specified column.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/projects/columns/{column_id}/moves",
            body=maybe_transform({"position": position}, column_move_params.ColumnMoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class AsyncColumnsResource(AsyncAPIResource):
    @cached_property
    def cards(self) -> AsyncCardsResource:
        return AsyncCardsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncColumnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncColumnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColumnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncColumnsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectColumn:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          name: Name of the project column

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/projects/{project_id}/columns",
            body=await async_maybe_transform({"name": name}, column_create_params.ColumnCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProjectColumn,
        )

    async def retrieve(
        self,
        column_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectColumn:
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
            f"/projects/columns/{column_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProjectColumn,
        )

    async def update(
        self,
        column_id: int,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectColumn:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          name: Name of the project column

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/projects/columns/{column_id}",
            body=await async_maybe_transform({"name": name}, column_update_params.ColumnUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProjectColumn,
        )

    async def list(
        self,
        project_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ColumnListResponse:
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
            f"/projects/{project_id}/columns",
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
                    column_list_params.ColumnListParams,
                ),
            ),
            cast_to=ColumnListResponse,
        )

    async def delete(
        self,
        column_id: int,
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
            f"/projects/columns/{column_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def move(
        self,
        column_id: int,
        *,
        position: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        > [!WARNING] > **Closing down notice:** Projects (classic) is being deprecated
        > in favor of the new Projects experience. See the
        > [changelog](https://github.blog/changelog/2024-05-23-sunset-notice-projects-classic/)
        > for more information.

        Args:
          position: The position of the column in a project. Can be one of: `first`, `last`, or
              `after:<column_id>` to place after the specified column.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/projects/columns/{column_id}/moves",
            body=await async_maybe_transform({"position": position}, column_move_params.ColumnMoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )


class ColumnsResourceWithRawResponse:
    def __init__(self, columns: ColumnsResource) -> None:
        self._columns = columns

        self.create = to_raw_response_wrapper(
            columns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            columns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            columns.update,
        )
        self.list = to_raw_response_wrapper(
            columns.list,
        )
        self.delete = to_raw_response_wrapper(
            columns.delete,
        )
        self.move = to_raw_response_wrapper(
            columns.move,
        )

    @cached_property
    def cards(self) -> CardsResourceWithRawResponse:
        return CardsResourceWithRawResponse(self._columns.cards)


class AsyncColumnsResourceWithRawResponse:
    def __init__(self, columns: AsyncColumnsResource) -> None:
        self._columns = columns

        self.create = async_to_raw_response_wrapper(
            columns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            columns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            columns.update,
        )
        self.list = async_to_raw_response_wrapper(
            columns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            columns.delete,
        )
        self.move = async_to_raw_response_wrapper(
            columns.move,
        )

    @cached_property
    def cards(self) -> AsyncCardsResourceWithRawResponse:
        return AsyncCardsResourceWithRawResponse(self._columns.cards)


class ColumnsResourceWithStreamingResponse:
    def __init__(self, columns: ColumnsResource) -> None:
        self._columns = columns

        self.create = to_streamed_response_wrapper(
            columns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            columns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            columns.update,
        )
        self.list = to_streamed_response_wrapper(
            columns.list,
        )
        self.delete = to_streamed_response_wrapper(
            columns.delete,
        )
        self.move = to_streamed_response_wrapper(
            columns.move,
        )

    @cached_property
    def cards(self) -> CardsResourceWithStreamingResponse:
        return CardsResourceWithStreamingResponse(self._columns.cards)


class AsyncColumnsResourceWithStreamingResponse:
    def __init__(self, columns: AsyncColumnsResource) -> None:
        self._columns = columns

        self.create = async_to_streamed_response_wrapper(
            columns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            columns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            columns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            columns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            columns.delete,
        )
        self.move = async_to_streamed_response_wrapper(
            columns.move,
        )

    @cached_property
    def cards(self) -> AsyncCardsResourceWithStreamingResponse:
        return AsyncCardsResourceWithStreamingResponse(self._columns.cards)
