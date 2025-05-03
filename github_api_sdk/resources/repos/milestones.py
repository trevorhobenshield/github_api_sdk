from __future__ import annotations

from datetime import datetime
from typing import Union

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
from ...types.repos import (
    milestone_create_params,
    milestone_list_labels_params,
    milestone_list_params,
    milestone_update_params,
)
from ...types.repos.milestone import Milestone
from ...types.repos.milestone_list_labels_response import MilestoneListLabelsResponse
from ...types.repos.milestone_list_response import MilestoneListResponse

__all__ = ["MilestonesResource", "AsyncMilestonesResource"]


class MilestonesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MilestonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return MilestonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MilestonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return MilestonesResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        title: str,
        description: str | NotGiven = NOT_GIVEN,
        due_on: str | datetime | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Milestone:
        """
        Creates a milestone.

        Args:
          title: The title of the milestone.

          description: A description of the milestone.

          due_on: The milestone due date. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          state: The state of the milestone. Either `open` or `closed`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/milestones",
            body=maybe_transform(
                {
                    "title": title,
                    "description": description,
                    "due_on": due_on,
                    "state": state,
                },
                milestone_create_params.MilestoneCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Milestone,
        )

    def retrieve(
        self,
        milestone_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Milestone:
        """
        Gets a milestone using the given milestone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/milestones/{milestone_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Milestone,
        )

    def update(
        self,
        milestone_number: int,
        *,
        owner: str,
        repo: str,
        description: str | NotGiven = NOT_GIVEN,
        due_on: str | datetime | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Milestone:
        """
        Update a milestone

        Args:
          description: A description of the milestone.

          due_on: The milestone due date. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          state: The state of the milestone. Either `open` or `closed`.

          title: The title of the milestone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/milestones/{milestone_number}",
            body=maybe_transform(
                {
                    "description": description,
                    "due_on": due_on,
                    "state": state,
                    "title": title,
                },
                milestone_update_params.MilestoneUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Milestone,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["due_on", "completeness"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MilestoneListResponse:
        """Lists milestones for a repository.

        Args:
          direction: The direction of the sort.

        Either `asc` or `desc`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: What to sort results by. Either `due_on` or `completeness`.

          state: The state of the milestone. Either `open`, `closed`, or `all`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/milestones",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    milestone_list_params.MilestoneListParams,
                ),
            ),
            cast_to=MilestoneListResponse,
        )

    def delete(
        self,
        milestone_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a milestone using the given milestone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/milestones/{milestone_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_labels(
        self,
        milestone_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MilestoneListLabelsResponse:
        """
        Lists labels for issues in a milestone.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/milestones/{milestone_number}/labels",
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
                    milestone_list_labels_params.MilestoneListLabelsParams,
                ),
            ),
            cast_to=MilestoneListLabelsResponse,
        )


class AsyncMilestonesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMilestonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMilestonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMilestonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncMilestonesResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        title: str,
        description: str | NotGiven = NOT_GIVEN,
        due_on: str | datetime | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Milestone:
        """
        Creates a milestone.

        Args:
          title: The title of the milestone.

          description: A description of the milestone.

          due_on: The milestone due date. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          state: The state of the milestone. Either `open` or `closed`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/milestones",
            body=await async_maybe_transform(
                {
                    "title": title,
                    "description": description,
                    "due_on": due_on,
                    "state": state,
                },
                milestone_create_params.MilestoneCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Milestone,
        )

    async def retrieve(
        self,
        milestone_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Milestone:
        """
        Gets a milestone using the given milestone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/milestones/{milestone_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Milestone,
        )

    async def update(
        self,
        milestone_number: int,
        *,
        owner: str,
        repo: str,
        description: str | NotGiven = NOT_GIVEN,
        due_on: str | datetime | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Milestone:
        """
        Update a milestone

        Args:
          description: A description of the milestone.

          due_on: The milestone due date. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          state: The state of the milestone. Either `open` or `closed`.

          title: The title of the milestone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/milestones/{milestone_number}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "due_on": due_on,
                    "state": state,
                    "title": title,
                },
                milestone_update_params.MilestoneUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Milestone,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["due_on", "completeness"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MilestoneListResponse:
        """Lists milestones for a repository.

        Args:
          direction: The direction of the sort.

        Either `asc` or `desc`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: What to sort results by. Either `due_on` or `completeness`.

          state: The state of the milestone. Either `open`, `closed`, or `all`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/milestones",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    milestone_list_params.MilestoneListParams,
                ),
            ),
            cast_to=MilestoneListResponse,
        )

    async def delete(
        self,
        milestone_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a milestone using the given milestone number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/milestones/{milestone_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_labels(
        self,
        milestone_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MilestoneListLabelsResponse:
        """
        Lists labels for issues in a milestone.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/milestones/{milestone_number}/labels",
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
                    milestone_list_labels_params.MilestoneListLabelsParams,
                ),
            ),
            cast_to=MilestoneListLabelsResponse,
        )


class MilestonesResourceWithRawResponse:
    def __init__(self, milestones: MilestonesResource) -> None:
        self._milestones = milestones

        self.create = to_raw_response_wrapper(
            milestones.create,
        )
        self.retrieve = to_raw_response_wrapper(
            milestones.retrieve,
        )
        self.update = to_raw_response_wrapper(
            milestones.update,
        )
        self.list = to_raw_response_wrapper(
            milestones.list,
        )
        self.delete = to_raw_response_wrapper(
            milestones.delete,
        )
        self.list_labels = to_raw_response_wrapper(
            milestones.list_labels,
        )


class AsyncMilestonesResourceWithRawResponse:
    def __init__(self, milestones: AsyncMilestonesResource) -> None:
        self._milestones = milestones

        self.create = async_to_raw_response_wrapper(
            milestones.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            milestones.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            milestones.update,
        )
        self.list = async_to_raw_response_wrapper(
            milestones.list,
        )
        self.delete = async_to_raw_response_wrapper(
            milestones.delete,
        )
        self.list_labels = async_to_raw_response_wrapper(
            milestones.list_labels,
        )


class MilestonesResourceWithStreamingResponse:
    def __init__(self, milestones: MilestonesResource) -> None:
        self._milestones = milestones

        self.create = to_streamed_response_wrapper(
            milestones.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            milestones.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            milestones.update,
        )
        self.list = to_streamed_response_wrapper(
            milestones.list,
        )
        self.delete = to_streamed_response_wrapper(
            milestones.delete,
        )
        self.list_labels = to_streamed_response_wrapper(
            milestones.list_labels,
        )


class AsyncMilestonesResourceWithStreamingResponse:
    def __init__(self, milestones: AsyncMilestonesResource) -> None:
        self._milestones = milestones

        self.create = async_to_streamed_response_wrapper(
            milestones.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            milestones.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            milestones.update,
        )
        self.list = async_to_streamed_response_wrapper(
            milestones.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            milestones.delete,
        )
        self.list_labels = async_to_streamed_response_wrapper(
            milestones.list_labels,
        )
